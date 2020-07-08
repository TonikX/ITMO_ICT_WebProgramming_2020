import Vue from 'vue'
import { showApi } from "../api";

export const show = {
    namespaced: true,
    state: {
        list: [],
        rings: {},
        grades: {},
    },
    mutations: {
        setShows(state, newShows) {
            return state.list = newShows;
        },
        setRings(state, { showId, newRings }) {
            Vue.set(state.rings, showId, newRings)
        },
        setGrades(state, { showId, ringId, newGrades }) {
            if (!state.grades[showId]) {
                Vue.set(state.grades, showId, {});
            }

            const show = state.grades[showId];

            Vue.set(show, ringId, newGrades);
        }
    },
    actions: {
        getShows({ commit }) {
            return showApi
                .getShows()
                .then(response => {
                    const shows = response.data;

                    commit('setShows', shows);
                });
        },
        getShowRings({ commit }, showId) {
            return showApi
                .getShowRings(showId)
                .then(response => {
                    const rings = response.data;

                    commit('setRings', { showId, newRings: rings });
                })
        },
        getRingGrades({ commit }, { showId, ringId }) {
            return showApi
                .getRingGrades(showId, ringId)
                .then(response => {
                    const grades = response.data;

                    commit('setGrades', { showId, ringId, newGrades: grades });
                })
        }
    },
};