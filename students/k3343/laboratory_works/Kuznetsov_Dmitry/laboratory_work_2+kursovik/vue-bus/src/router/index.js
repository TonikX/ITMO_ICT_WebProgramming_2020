import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SignUp from "../views/SignUp";
import Login from "../views/Login";
import Bus from "../views/Bus";
import BusSingle from "../views/BusSingle";
import Driver from "../views/Driver";
import DriverSingle from "../views/DriverSingle";
import Schedule from "../views/Schedule";
import Route from "../views/Route";
import Query from "../views/Query";

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
        path: 'login',
        name: 'Вход',
        component: Login
    },
    {
        path: '/signup',
        name: 'Регистрация',
        component: SignUp
    },
    {
        path: '/bus',
        name: 'Автобусы',
        component: Bus,
        props: true
    },
    {
        path: '/bus/:id',
        name: 'Автобус',
        component: BusSingle,
        props: true
    },
    {
        path: '/driver',
        name: 'Водители',
        component: Driver,
        props: true
    },
    {
        path: '/driver/:id',
        name: 'Водитель',
        component: DriverSingle,
        props: true
    },
    {
        path: '/schedule',
        name: 'График работы водителей',
        component: Schedule,
        props: true
    },
    {
        path: '/route',
        name: 'Маршруты',
        component: Route,
        props: true
    },
    {
        path: '/query',
        name: 'Запросы',
        component: Query,
        props: true
    },
]

const router = new VueRouter({
    routes
})

export default router
