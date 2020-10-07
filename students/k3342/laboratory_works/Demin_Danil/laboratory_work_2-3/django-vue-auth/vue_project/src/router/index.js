import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Auth from '@/components/Auth'
import Register from '@/components/Register'
import Workers from '@/components/Workers'
import Cages from '@/components/Cages'
import Chickens from '@/components/Chickens'
import AddChicken from "@/components/AddChicken"
import Reports from '@/components/Reports'
import AddReport from "@/components/AddReport"

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
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
      path: '/workers',
      name: 'Workers',
      component: Workers
    },
    {
      path: '/cages',
      name: 'Cages',
      component: Cages
    },
    {
      path: '/chickens',
      name: 'Chickens',
      component: Chickens
    },
    {
      path: '/chickens/add',
      name: 'AddChicken',
      component: AddChicken
    },
    {
      path: '/reports',
      name: 'Reports',
      component: Reports
    },
    {
      path: '/reports/add',
      name: 'AddReport',
      component: AddReport
    }
  ]
})
