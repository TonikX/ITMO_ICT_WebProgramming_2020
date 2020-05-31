import Vue from 'vue'
import Router from 'vue-router'
import Airport from '@/components/Airport'
import Challenger from '@/components/Challenger'

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
    }
  ]
})
