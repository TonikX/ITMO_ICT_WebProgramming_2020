import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Quests from '../views/Quests.vue'
import QuestDetail from "../views/QuestEdit";
import Teams from "../views/Teams";
import MainNavbar from "../layout/MainNavbar";
import LoginNavbar from "../layout/LoginNavbar";
import Statistic from "../views/Statistic";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        redirect: '/quests'
    },
    {
        path: '/login',
        name: 'login',
        components: { default: Login, header: LoginNavbar }
    },
    {
        path: '/quests',
        name: 'quests',
        components: { default: Quests, header: MainNavbar }
    },
    {
        path: '/quests/:id',
        name: 'editQuest',
        components: { default: QuestDetail, header: MainNavbar }
    },
    {
        path: '/createQuest',
        name: 'createQuest',
        components: { default: QuestDetail, header: MainNavbar }
    },
    {
        path: '/teams',
        name: 'teams',
        components: { default: Teams, header: MainNavbar }
    },
    {
        path: '/quests/:id/statistic',
        name: 'statistic',
        components: { default: Statistic, header: MainNavbar }
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
