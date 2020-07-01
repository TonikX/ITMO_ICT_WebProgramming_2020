import { clubApi } from "../api";

export const club = {
    namespaced: true,
    state: {
        list: [],
    },
    mutations: {
        setClubs(state, newClubs) {
            return state.list = newClubs;
        },
    },
    actions: {
        getClubs({ commit }) {
            return clubApi
                .getClubs()
                .then(response => {
                    const clubs = response.data;

                    commit('setClubs', clubs);
                });
        }
    },
};