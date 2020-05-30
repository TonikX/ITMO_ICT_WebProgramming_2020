import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import WorkerCabinet from '@/components/WorkerCabinet'
import AdminCabinet from '@/components/AdminCabinet'
import AuthForm from '@/components/AuthForm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/worker',
      name: 'WorkerCabinet',
      component: WorkerCabinet
    },
    {
      path: '/admin',
      name: 'AdminCabinet',
      component: AdminCabinet
    },
    {
      path: '/auth',
      name: 'AuthForm',
      component: AuthForm
    }
  ]
})
