import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import Login from '@/components/Login'

import Teacher from '@/components/Teacher'
import TeacherAdd from '@/components/TeacherAdd'
import TeacherEdit from '@/components/TeacherEdit'
import TeacherDelete from '@/components/TeacherDelete'

import Pupil from '@/components/Pupil'
import PupilAdd from '@/components/PupilAdd'
import PupilEdit from '@/components/PupilEdit'
import PupilDelete from '@/components/PupilDelete'

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
      path: '/teachers_add',
      name: 'teachers_add',
      component: TeacherAdd
    },
    {
      path: '/teachers_edit',
      name: 'teachers_edit',
      component: TeacherEdit
    },
    {
      path: '/teachers_delete',
      name: 'teachers_delete',
      component: TeacherDelete
    },
    {
      path: '/pupils',
      name: 'pupils',
      component: Pupil
    },
    {
      path: '/pupils_add',
      name: 'pupils_add',
      component: PupilAdd
    },
    {
      path: '/pupils_edit',
      name: 'pupils_edit',
      component: PupilEdit
    },
    {
      path: '/pupils_delete',
      name: 'pupils_delete',
      component: PupilDelete
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
