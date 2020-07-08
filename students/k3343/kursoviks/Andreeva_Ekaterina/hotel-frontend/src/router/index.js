import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../views/Login";
import SignUp from "../views/SignUp";
import Cleaning from "../views/Cleaning";
import Resident from "../views/Resident";
import ResidentSingle from "../views/ResidentSingle";
import Room from "../views/Room";
import Servant from "../views/Servant";
import ServantSingle from "../views/ServantSingle";
import Queries from "../views/Queries";

import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';

Vue.use(MuseUI);
Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'Вход',
        component: Login
    },
    {
        path: '/signup',
        name: 'Регистрация',
        component: SignUp
    },
    {
        path: '/cleaning',
        name: 'Уборка',
        component: Cleaning,
        props: true
    },
    {
        path: '/resident',
        name: 'Проживающие',
        component: Resident,
        props: true
    },
    {
        path: '/resident/:id',
        name: 'Проживающий',
        component: ResidentSingle,
        props: true
    },
    {
        path: '/servant',
        name: 'Служащие',
        component: Servant,
        props: true
    },
    {
        path: '/servant/:id',
        name: 'Служащий',
        component: ServantSingle,
        props: true
    },
    {
        path: '/room',
        name: 'Номера',
        component: Room,
        props: true
    },
    {
        path: '/queries',
        name: 'Запросы',
        component: Queries,
        props: true
    },
]

const router = new VueRouter({
    routes
})

export default router
