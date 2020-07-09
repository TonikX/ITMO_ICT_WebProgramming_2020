import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Teachers from '../views/Teachers.vue'
import Teacher_single from '../views/Teacher_single.vue'
import Pupils from '../views/Pupils.vue'
import Pupil_single from '../views/Pupil_single.vue'
import Cabinets from '../views/Cabinets.vue'
import Subjects from '../views/Subjects.vue'
import Klasses from '../views/Klasses.vue'
import Klass_timetable from "../views/Klass_timetable";
import Klass_pupils from "../views/Klass_pupils";
import Login from '../views/Login'
import Timetable from "../views/Timetable";
import Delete_Pupil from "../views/Delete_Pupil";
import Regis from "../views/Regis";
import Queries from "../views/Queries";
import KlassReport from "../views/KlassReport";

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
        path: '/regis',
        name: 'Регистрация',
        component: Regis
    },
    {
        path: '/teacher',
        name: 'Учителя',
        component: Teachers,
        props: true
    },
    {
        path: '/teacher/:id',
        name: 'Досье учителя',
        component: Teacher_single,
        props: true
    },
    {
        path: '/klass/:id',
        name: 'Ученики',
        component: Pupils,
        props: true
    },
    {
        path: '/pupils',
        name: 'Ученики',
        component: Pupils,
        props: true
    },
    {
        path: '/pupil/delete',
        name: 'Удаление ученика',
        component: Delete_Pupil,
    },
    {
        path: '/pupil/:id',
        name: 'Досье ученика',
        component: Pupil_single,
        props: true
    },
    {
        path: '/cabinets',
        name: 'Кабинеты',
        component: Cabinets,
    },
    {
        path: '/subjects',
        name: 'Дисциплины',
        component: Subjects,
    },
    {
        path: '/klass',
        name: 'Классы',
        component: Klasses,
        props: true
    },
    {
        path: '/klass/:id/timetable',
        name: 'Расписание класса',
        component: Klass_timetable,
        props: true
    },
    {
        path: '/klass/:id/pupils',
        name: 'Ученики класса',
        component: Klass_pupils,
        props: true
    },
    {
        path: '/klass/:id/timetable',
        name: 'Расписание',
        component: Timetable,
        props: true
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/queries',
        name: 'Запросы',
        component: Queries
    },
    {
        path: '/klass_report',
        name: 'Отчет по классу',
        component: KlassReport
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
    mode: 'history',
    routes
})

export default router
