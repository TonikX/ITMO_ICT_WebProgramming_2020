import Vue from 'vue'
import VueRouter from 'vue-router'
import Quests from '../views/Quests.vue'
import QuestDetail from "../views/QuestDetail";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        redirect: '/quests'
    },
    {
        path: '/quests',
        name: 'Quests',
        component: Quests
    },
    {
        path: '/quests/:id',
        name: 'QuestDetail',
        component: QuestDetail
    },
    {
        path: '/teams',
        name: 'Teams',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/Teams.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
