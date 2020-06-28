import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Shedule from "../components/Shedule";
import Record from "../components/Record";
import Students from "../components/Students";
import Teachers from "../components/Teachers";
import Group from "../components/Group";
import Registration from "../components/Registration";


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/registration',
      name: 'registration',
      component: Registration
    },
    {
      path: '/shedule',
      name: 'shedule',
      component: Shedule
    },
    {
      path: '/record',
      name: 'record',
      component: Record
    },
     {
      path: '/students',
      name: 'students',
      component: Students
    },
     {
      path: '/teachers',
      name: 'teachers',
      component: Teachers
    },
    {
      path: '/groups',
      name: 'groups',
      component: Group
    },
  ]
})
