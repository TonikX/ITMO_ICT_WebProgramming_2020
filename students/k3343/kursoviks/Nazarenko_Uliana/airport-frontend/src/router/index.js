import Vue from 'vue'
import Router from 'vue-router'
import Airport from '@/components/Airport'
import Challenger from '@/components/Challenger'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Cabinet from '@/components/Cabinet'
import MyTickets from '@/components/MyTickets'
import FlightDetail from '@/components/FlightDetail'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Airport',
      component: Airport
    },
    {
      path: '/challenger',
      name: 'Challenger',
      component: Challenger
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/cabinet',
      name: 'Cabinet',
      component: Cabinet
    },
    {
      path: '/tickets',
      name: 'MyTickets',
      component: MyTickets
    },
    {
      path: '/detail/:id',
      name: 'FlightDetail',
      component: FlightDetail,
      props: true
    }
  ]
})
