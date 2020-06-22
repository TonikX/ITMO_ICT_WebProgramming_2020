import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Quests from '../views/Quests.vue'
import QuestDetail from "../views/QuestDetail";
import Teams from "../views/Teams";
import MainNavbar from "../layout/MainNavbar";
import LoginNavbar from "../layout/LoginNavbar";

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
        name: 'questDetail',
        components: { default: QuestDetail, header: MainNavbar }
    },
    {
        path: '/teams',
        name: 'teams',
        components: { default: Teams, header: MainNavbar }
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
