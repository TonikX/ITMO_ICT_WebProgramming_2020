import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Patient from '@/components/Patient'
import Doctor from '@/components/Doctor'
import Appointment from '@/components/Appointment'
import Queries from '@/components/Queries'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/patients',
      name: 'patient',
      component: Patient
    },
    {
      path: '/doctors',
      name: 'doctor',
      component: Doctor
    },
    {
      path: '/apps',
      name: 'apps',
      component: Appointment
    },
    {
      path: '/queries',
      name: 'queries',
      component: Queries
    }
  ]
})
