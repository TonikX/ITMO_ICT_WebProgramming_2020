import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Teacher from '@/components/Teacher'
import Pupil from '@/components/Pupil'
import Class from '@/components/Class'
import Subject from '@/components/Subject'
import Room from '@/components/Room'
import Assessment from '@/components/Assessment'
import Timetable from '@/components/Timetable'

import 'typeface-roboto'

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
      path: '/teachers',
      name: 'teachers',
      component: Teacher
    },
    {
      path: '/pupils',
      name: 'pupils',
      component: Pupil
    },
    {
      path: '/classes',
      name: 'classes',
      component: Class
    },
    {
      path: '/subjects',
      name: 'subjects',
      component: Subject
    },
    {
      path: '/rooms',
      name: 'rooms',
      component: Room
    },
    {
      path: '/assessments',
      name: 'assessments',
      component: Assessment
    },
    {
      path: '/timetable',
      name: 'timetable',
      component: Timetable
    }
  ]
})
