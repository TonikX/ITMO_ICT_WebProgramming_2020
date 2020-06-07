import axios from "../axios";
import { authHeader } from "../axios";

export const clubApi = {
  getClubs,
};

function getClubs() {
  const requestOptions = {
    url: "/api/clubs/",
    method: "GET",
    headers: {
      ...authHeader(),
      "Content-Type": "application/json"
    }
  };

  return axios(requestOptions);
}