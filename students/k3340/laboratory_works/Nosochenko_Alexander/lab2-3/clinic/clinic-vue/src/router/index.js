import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import MainPage from "../components/Doctors";
import Requests from "../components/Requests";
import Doctors from "../components/Doctors";
import Patients from "../components/Patients";
import Records from "../components/Records";
import Cabinets from "../components/Cabinets";
import Transactions from "../components/Transactions";
import Reception from "../components/Reception";
import Reviews from "../components/Reviews";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login/',
      name: 'login',
      component: Login
    },
    {
      path: '/doctors/',
      name: 'doctors',
      component: Doctors
    },
    {
      path: '/requests/',
      name: 'requests',
      component: Requests
    },
    {
      path: '/patients/',
      name: 'patients',
      component: Patients
    },
    {
      path: '/medicalrecord/',
      name: 'records',
      component: Records
    },
    {
      path: '/cabinet/',
      name: 'cabinet',
      component: Cabinets
    },
    {
      path: '/transactions/',
      name: 'transactions',
      component: Transactions
    },
    {
      path: '/reception/',
      name: 'reception',
      component: Reception
    },
    {
      path: '/reviews/',
      name: 'reviews',
      component: Reviews
    }
  ]
})
