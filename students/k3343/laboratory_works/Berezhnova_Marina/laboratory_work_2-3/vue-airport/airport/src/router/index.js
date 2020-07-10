import Vue from 'vue'
import Router from 'vue-router'
import Flights from '@/components/Flights'
import Challenger from '@/components/Challenger'

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
    }
  ]
})
