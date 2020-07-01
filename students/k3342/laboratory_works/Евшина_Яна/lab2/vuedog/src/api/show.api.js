import axios from "../axios";
import { authHeader } from "../axios";

export const showApi = {
  getShows,
  getShowRings,
  getRingGrades,
};

function getShows() {
  const requestOptions = {
    url: "/api/shows/",
    method: "GET",
    headers: {
      ...authHeader(),
      "Content-Type": "application/json"
    }
  };

  return axios(requestOptions);
}

function getShowRings(showId) {
  const requestOptions = {
    url: `/api/shows/${showId}/rings/`,
    method: "GET",
    headers: {
      ...authHeader(),
      "Content-Type": "application/json"
    }
  };

  return axios(requestOptions);
}

function getRingGrades(showId, ringId) {
  const requestOptions = {
    url: `/api/shows/${showId}/rings/${ringId}/grades/`,
    method: "GET",
    headers: {
      ...authHeader(),
      "Content-Type": "application/json"
    }
  };

  return axios(requestOptions);
}