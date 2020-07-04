import axios from 'axios'
import {TokenStorage} from './tokenStorage'
import Promise from 'es6-promise'
import router from "../router";

const BASE_URL = `https://${window.location.hostname}/api/`;
const REFRESH_TOKEN_ROUTE = '/token/refresh';

let httpClientInstance = axios.create({
    baseURL: BASE_URL,
});

httpClientInstance.interceptors.request.use(
    (config) => {
        if (TokenStorage.isAuthenticated()) {
            config.headers = {
                'Authorization': 'Bearer ' + TokenStorage.getAccessToken()
            }
        }
        return config
    },
    (error) => {
        return Promise.reject(error)
    }
);

httpClientInstance.interceptors.response.use(
    (response) => {
        return response
    },
    (error) => {
        const originalRequest = error.config;
        if (error.response.status === 401 && !error.config.url.endsWith(REFRESH_TOKEN_ROUTE)) {
            console.log("refresh " + TokenStorage.getRefreshToken());
            return httpClientInstance.post(REFRESH_TOKEN_ROUTE, {refresh: TokenStorage.getRefreshToken()})
                .then((response) => {
                    console.log("Access token was successfully updated");
                    TokenStorage.storeAccessToken(response.data.access);
                    return httpClient(originalRequest)
                })
                .catch((error) => {
                    if (error.response.status === 401) {
                        console.log("Unable to refresh token. Logout");
                        TokenStorage.clear();
                        router.push({name: "login"});
                    }
                })
        }
        return Promise.reject(error)
    }
);

export const httpClient = httpClientInstance;
