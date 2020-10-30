import axios from "../axios";
import { authHeader } from "../axios";

export const userAPI = {
  login,
  register,
  refreshAccessToken,
  getProfileInfo,
  getDogs,
  createDog,
  makeRegistrationRequest,
};

function login(username, password) {
  const requestOptions = {
    url: "/api/token/",
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    data: JSON.stringify({ username, password })
  };

  return axios(requestOptions)
      .then(response => {
        return response;
      });
}

function register(username, password, lastName) {
  const requestOption = {
    url: "/api/users/register/",
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    data: JSON.stringify({
      username,
      password,
      last_name: lastName,
    })
  };
  return axios(requestOption)
      .then(response => {
        return response
      });
}

function refreshAccessToken(refreshToken) {
  const requestOptions = {
    url: "/api/token/refresh/",
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    data: JSON.stringify({ refresh: refreshToken })
  };
  return axios(requestOptions)
      .then(response => {
        console.log("Requested new access token.");
        return response;
      });
}

function getProfileInfo() {
  const requestOptions = {
    url: "/api/users/profile-info/",
    method: "GET",
    headers: {
      ...authHeader(),
      "Content-Type": "application/json"
    }
  };
  return axios(requestOptions);
}

function getDogs() {
  const requestOptions = {
    url: "/api/dogs/",
    method: "GET",
    headers: {
      ...authHeader(),
      "Content-Type": "application/json"
    }
  };

  return axios(requestOptions);
}

function createDog(payload) {
  const requestOptions = {
    url: "/api/dogs/",
    method: "POST",
    headers: {
      ...authHeader(),
      "Content-Type": "application/json"
    },
    data: JSON.stringify(payload),
  };

  return axios(requestOptions);
}

function makeRegistrationRequest(payload) {
  const requestOptions = {
    url: "/api/registrations/",
    method: "POST",
    headers: {
      ...authHeader(),
      "Content-Type": "application/json"
    },
    data: JSON.stringify(payload),
  };

  return axios(requestOptions);
}