import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '@/components/MainPage'
import New from '@/components/New'
import Top from '@/components/Top'
import Auth from '@/components/Auth'
import Register from '@/components/Register'
import Secretary from '@/components/Secretary'
import Enrollee from '@/components/Enrollee'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/new',
      name: 'New',
      component: New
    },
    {
      path: '/top',
      name: 'Top',
      component: Top
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/enrollee',
      name: 'Enrollee',
      component: Enrollee
    },
    {
      path: '/secretary',
      name: 'Secretary',
      component: Secretary
    }
  ]
})
