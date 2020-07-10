import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '@/components/MainPage'
import Enrollee from '@/components/Enrollee'
import Top from '@/components/Top'
import Specialization from '@/components/Specialization'

Vue.use(Router)

export default new Router({
  routes: [
  	{
      path: '/',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/enrollee/top',
      name: 'Top',
      component: Top
    },
    {
   	  path: '/enrollee/:id',
   	  name: 'Enrollee',
   	  component: Enrollee,
   	  props: true
    },
    {
   	  path: '/specialization/:id',
   	  name: 'Specialization',
   	  component: Specialization,
   	  props: true
    }
  ]
})
