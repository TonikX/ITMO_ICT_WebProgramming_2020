import axios from "axios";
import store from "./store";
import router from "./router";
import { userAPI } from "./api";

export function authHeader() {
  let tokens = JSON.parse(localStorage.getItem("tokens"));

  if (tokens && tokens.access) {
    return { "Authorization": `Bearer ${tokens.access}` };
  } else {
    return {};
  }
}

function updateToken(refreshToken) {
  return new Promise((resolve, reject) => {
    userAPI.refreshAccessToken(refreshToken)
        .then(response => {
          const { access } = response.data;
          return resolve(access);
        })
        .catch(error => {
          return reject(error);
        });
  })
}

axios.interceptors.response.use(null, error => {
  // Trying to refresh existing access token and retry sending
  // query which was interrupted with 401 error.
  // Force log out if refresh token is also expired.
  if (error.response.status == 401 && error.config && !error.config.url.endsWith("/api/token/refresh/")) {
    const tokens = JSON.parse(localStorage.getItem('tokens'));

    if (tokens && tokens.refresh) {
      return updateToken(tokens.refresh)
          .then(accessToken => {
            tokens.access = accessToken;
            localStorage.setItem('tokens', JSON.stringify(tokens));
            Object.assign(error.config.headers, authHeader());

            return axios.request(error.config);
          })
          .catch(error => {
            if (error.response.status == 401) {
              store.commit("user/logOut");
              router.push("/login");
              return;
            }

            return Promise.reject(error);
          })
    }
  }

  return Promise.reject(error);
});

axios.defaults.baseURL = "http://localhost:8000";

export default axios;