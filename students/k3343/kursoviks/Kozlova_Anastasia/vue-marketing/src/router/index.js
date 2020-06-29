import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Cabinet from '@/components/Cabinet'
import Admin from '@/components/Admin'
import NewRequest from '@/components/NewRequest'
import SignUp from '@/components/SignUp'
import Auth from '@/components/Auth'
import Payments from '@/components/Payments'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/cabinet',
      name: 'Cabinet',
      component: Cabinet
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/admin',
      name: 'Admin',
      component: Admin
    },
    {
      path: '/request/new',
      name: 'NewRequest',
      component: NewRequest
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUp,
      props: true
    },
    {
      path: '/payments',
      name: 'Payments',
      component: Payments
    }
  ]
})
