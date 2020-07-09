import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import Login from '@/components/Login'
import TeacherAdd from '@/components/TeacherAdd'
import TeacherEdit from '@/components/TeacherEdit'
import TeacherDelete from '@/components/TeacherDelete'
import PupilAdd from '@/components/PupilAdd'
import PupilEdit from '@/components/PupilEdit'
import PupilDelete from '@/components/PupilDelete'
import AssessmentAdd from '@/components/AssessmentAdd'
import AssessmentEdit from '@/components/AssessmentEdit'
import AssessmentDelete from '@/components/AssessmentDelete'
import TimetableAdd from '@/components/TimetableAdd'
import TimetableDelete from '@/components/TimetableDelete'

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
      path: '/assessments_add',
      name: 'assessments_add',
      component: AssessmentAdd
    },
    {
      path: '/assessments_edit',
      name: 'assessments_edit',
      component: AssessmentEdit
    },
    {
      path: '/assessments_delete',
      name: 'assessments_delete',
      component: AssessmentDelete
    },
    {
      path: '/timetable_add',
      name: 'timetable_add',
      component: TimetableAdd
    },
    {
      path: '/timetable_delete',
      name: 'timetable_delete',
      component: TimetableDelete
    }
  ]
})
