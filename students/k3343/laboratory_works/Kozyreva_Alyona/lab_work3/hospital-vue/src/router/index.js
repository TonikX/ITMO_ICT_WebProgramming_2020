import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Auth from '@/components/Auth'
import AppointmentNew from '@/components/AppointmentNew'
import Appointments from '@/components/Appointments'
import Appointment from '@/components/Appointment'

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
      path: '/appointments/:id',
      name: 'Appointment',
      component: Appointment,
      props: true
    }
  ]
})
