import Vue from 'vue'
import Router from 'vue-router'
import AllClimbings from '@/components/AllClimbings'
import Climbers from "@/components/Climbers";
import Mountains from "@/components/Mountains";
import Groups from "@/components/Groups";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'AllClimbings',
      component: AllClimbings
    },
    {
      path: '/climbers',
      name: 'Climbers',
      component: Climbers
    },
    {
      path: '/groups',
      name: 'Groups',
      component: Groups
    },
    {
      path: '/mountains',
      name: 'Mountains',
      component: Mountains
    }
  ]
})
