import Vue from 'vue'
import Router from 'vue-router'
import Flights from '@/components/Flights'
import Challenger from '@/components/Challenger'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Cabinet from '@/components/Cabinet'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Flights',
      component: Flights
    },
    {
      path: '/challenger',
      name: 'Challenger',
      component: Challenger
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/cabinet',
      name: 'Cabinet',
      component: Cabinet
    }
  ]
})
