import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../../../vue-airport/src/views/Login";
import SignUp from "../views/SignUp";
import AirCarrier_single from "../views/AirCarrier_single";
import Route from "../views/Route";
import Employee from "../views/Employee";
import Flight from "../views/Flight";
import Queries from "../views/Queries";
import Report from "../views/Report";
import CrewCommander from "../views/CrewCommander";
import SecondPilot from "../views/SecondPilot";
import Navigator from "../views/Navigator";
import Steward from "../views/Steward";

import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';

Vue.use(MuseUI);
Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Главная страница',
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
        path: '/aircarrier',
        name: 'Авиаперевозчик',
        component: AirCarrier_single,
        props: true
    },
    {
        path: '/route',
        name: 'Маршруты',
        component: Route,
        props: true
    },
    {
        path: '/crewcommander/:id',
        name: 'Командир экипажа',
        component: CrewCommander,
        props: true
    },
    {
        path: '/secondpilot/:id',
        name: 'Второй пилот',
        component: SecondPilot,
        props: true
    },
    {
        path: '/navigator/:id',
        name: 'Штурман',
        component: Navigator,
        props: true
    },
    {
        path: '/steward/:id',
        name: 'Бортпроводник',
        component: Steward,
        props: true
    },
    {
        path: '/employee',
        name: 'Сотрудники',
        component: Employee,
        props: true
    },
    {
        path: '/flight',
        name: 'Рейсы',
        component: Flight,
        props: true
    },
    {
        path: '/queries',
        name: 'Запросы',
        component: Queries,
        props: true
    },
    {
        path: '/report',
        name: 'Отчет',
        component: Report,
        props: true
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    }
]

const router = new VueRouter({
    routes
})

export default router
