import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Cabinet from '@/components/Cabinet'
import AdminCab from '@/components/AdminCab'
import Details from '@/components/Details'
import ReqForm from '@/components/ReqForm'
import RegClient from '@/components/RegClient'
import Auth from '@/components/Auth'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/Cabinet',
      name: 'Cabinet',
      component: Cabinet
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/adminCab',
      name: 'AdminCab',
      component: AdminCab
    },
    {
      path: '/details/:id',
      name: 'Details',
      component: Details,
      props: true
    },
    {
      path: '/newReq',
      name: 'ReqForm',
      component: ReqForm
    },
    {
      path: '/newClient',
      name: 'RegClient',
      component: RegClient,
      props: true
    }
  ]
})
