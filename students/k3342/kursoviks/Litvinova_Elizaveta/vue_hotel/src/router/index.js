import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import RentRoom from '@/components/RentRoom'
import Servant from '@/components/Servant'
import NewServant from '@/components/NewServant'
import Admin from '@/components/Admin'
import AdminServant from '@/components/AdminServant'
import AdminReport from '@/components/AdminReport'
import AdminChallenger from '@/components/AdminChallenger'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/get_room',
      name: 'RentRoom',
      component: RentRoom
    },
    {
      path: '/servant',
      name: 'Servant',
      component: Servant
    },
    {
      path: '/admin',
      name: 'Admin',
      component: Admin
    },
    {
      path: '/new_servant',
      name: 'NewServant',
      component: NewServant
    },
    {
      path: '/admin/report',
      name: 'AdminReport',
      component: AdminReport
    },
    {
      path: '/admin/servant',
      name: 'AdminServant',
      component: AdminServant
    },
    {
      path: '/admin/challenger',
      name: 'AdminChallenger',
      component: AdminChallenger
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
    }
  ]
})
