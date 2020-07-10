import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../views/Login";
import SignUp from "../views/SignUp";
import Application from "../views/Application";
import ApplicationSingle from "../views/ApplicationSingle";
import Enrollee from "../views/Enrollee";
import EnrolleSingle from "../views/EnrolleSingle";
import Documents from "../views/Documents";
import Facullty from "../views/Facullty";
import Queries from "../views/Queries";
import Report from "../views/Report";
import Marks from "../views/Marks";
import EgeResults from "../views/EgeResults";

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
        path: '/application',
        name: 'Заявки',
        component: Application,
        props: true
    },
    {
        path: '/application/:id',
        name: 'Заявка',
        component: ApplicationSingle,
        props: true
    },
    {
        path: '/enrollee',
        name: 'Абитуриенты',
        component: Enrollee,
        props: true
    },
    {
        path: '/enrollee/:id',
        name: 'Абитуриент',
        component: EnrolleSingle,
        props: true
    },
    {
        path: '/faculty',
        name: 'Факультеты',
        component: Facullty,
        props: true
    },
    {
        path: '/docs',
        name: 'Документы',
        component: Documents,
        props: true
    },
    {
        path: '/marks',
        name: 'Оценки',
        component: Marks,
        props: true
    },
    {
        path: '/ege_results',
        name: 'Результаты',
        component: EgeResults,
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
        name: 'Отчеты',
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
