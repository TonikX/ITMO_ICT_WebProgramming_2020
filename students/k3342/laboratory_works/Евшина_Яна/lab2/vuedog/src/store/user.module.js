import { userAPI } from "../api";

export const user = {
  namespaced: true,
  state: {
    username: "",
    id: undefined,
    dogs: [],
  },
  mutations: {
    setState(state, newState) {
      Object.keys(newState).forEach(field => {
          state[field] = newState[field];
      });
    },
    setDogs(state, newDogs) {
      state.dogs = newDogs;
    },
    logOut(state) {
      localStorage.removeItem('tokens');

      state.username = "";
      state.id = undefined;
    },
  },
  actions: {
    login(context, { username, password }) {
      return userAPI.login(username, password)
          .then(
              response => {
                const tokens = JSON.stringify(response.data);

                localStorage.setItem('tokens', tokens);
              }
          );
    },
    register({ commit }, { username, password, lastName }) {
      return userAPI.register(username, password, lastName)
          .then(response => {
                const { username } = response.data;

                commit('setState', { username });
          });
    },
    getDogs({ commit }) {
        return userAPI.getDogs()
          .then(response => {
                const dogs = response.data;

                commit('setState', { dogs });
          });
    },
    createDog({ commit, state }, payload) {
        return userAPI.createDog(payload)
            .then(response => {
                const newDog = response.data;

                commit('setState', { dogs: [...state.dogs, newDog] })
            })
    },
    getProfileInfo({ commit }) {
      return userAPI.getProfileInfo()
          .then(response => {
            const { id, username } = response.data;

            commit('setState', { id, username });
          });
    },
    makeRegistrationRequest(context, payload) {
        return userAPI.makeRegistrationRequest(payload)
            .then(response => response.data);
    },
  }
};