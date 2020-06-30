import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Auth from '@/components/Auth'
import Register from '@/components/Register'

import AppointmentNew from '@/components/AppointmentNew'
import Appointments from '@/components/Appointments'
import Appointment from '@/components/Appointment'
import Cabinet from '@/components/Cabinet'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/patient/new',
      name: 'AppointmentNew',
      component: AppointmentNew
    },
    {
      path: '/doctor',
      name: 'Appointments',
      component: Appointments
    },
    {
      path: '/cabinet',
      name: 'Cabinet',
      component: Cabinet
    },
    {
      path: '/appointments/:id',
      name: 'Appointment',
      component: Appointment,
      props: true
    }
  ]
})
