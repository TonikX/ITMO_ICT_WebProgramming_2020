import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '@/components/MainPage'
import Enrollee from '@/components/Enrollee'
import Top from '@/components/Top'
import Specialization from '@/components/Specialization'
import SignIn from '@/components/SignIn'
import SignUp from '@/components/SignUp'
import Application from '@/components/Application'
import Cabinet from '@/components/Cabinet'

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
      path: '/signin',
      name: 'SignIn',
      component: SignIn
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUp
    },
    {
      path: '/application/new',
      name: 'Application',
      component: Application
    },
    {
      path: '/cabinet',
      name: 'Cabinet',
      component: Cabinet
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
