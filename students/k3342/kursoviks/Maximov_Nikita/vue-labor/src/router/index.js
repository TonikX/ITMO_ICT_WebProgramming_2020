import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../views/Login";
import SignUp from "../views/SignUp";
import Applicants from "../views/Applicants";
import ApplicantSingle from "../views/ApplicantSingle";
import ApplicantRegistration from "../views/ApplicantRegistration";
import Course from "../views/Course";
import Employer from "../views/Employer";
import EmployerSingle from "../views/EmployerSingle";
import Gratuity from "../views/Gratuity";
import Vacancy from "../views/Vacancy";
import VacancySingle from "../views/VacancySingle";
import Application from "../views/Application";
import ApplicationSingle from "../views/ApplicationSingle";

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
        path: '/applicant',
        name: 'Соискатели',
        component: Applicants,
        props: true
    },
    {
        path: '/applicant/:id',
        name: 'Соискатель',
        component: ApplicantSingle,
        props: true
    },
    {
        path: '/applicant_reg',
        name: 'Регистрация соискателя',
        component: ApplicantRegistration,
        props: true
    },
    {
        path: '/course',
        name: 'Курсы',
        component: Course,
        props: true
    },
    {
        path: '/employer',
        name: 'Работодатели',
        component: Employer,
        props: true
    },
    {
        path: '/employer/:id',
        name: 'Работодатель',
        component: EmployerSingle,
        props: true
    },
    {
        path: '/gratuity',
        name: 'Пособие',
        component: Gratuity,
        props: true
    },
    {
        path: '/vacancy',
        name: 'Вакансии',
        component: Vacancy,
        props: true
    },
    {
        path: '/vacancy/:id',
        name: 'Вакансия',
        component: VacancySingle,
        props: true
    },

]

const router = new VueRouter({
    routes
})

export default router
