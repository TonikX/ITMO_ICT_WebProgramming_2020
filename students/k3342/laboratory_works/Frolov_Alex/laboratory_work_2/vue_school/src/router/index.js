import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Teachers from '../views/Teachers.vue'
import Teacher_single from '../views/Teacher_single.vue'
import Childrens from '../views/Childrens.vue'
import Children_single from '../views/Children_single.vue'
import Rooms from '../views/Rooms.vue'
import Subjects from '../views/Subjects.vue'
import Nclasses from '../views/Nclasses.vue'
import Nclass_timetable from "../views/Nclass_timetable.vue"
import Nclass_childrens from "../views/Nclass_childrens.vue"
import Login from '../views/Login.vue'
import Timetable from "../views/Timetable.vue"
import Delete_children from "../views/Delete_children.vue";
import Registration from "../views/Registration.vue";

import 'typeface-roboto'

Vue.use(VueRouter)

  const routes = [
  {
        path: '/',
        name: 'Главная страница',
        component: Home
    },
    {
        path: '/registration',
        name: 'Регистрация',
        component: Registration
    },
    {
        path: '/teacher',
        name: 'Учителя',
        component: Teachers,
        props: true
    },
    {
        path: '/teacher/:id',
        name: 'Досье учителя',
        component: Teacher_single,
        props: true
    },
        {
        path: '/nclass/:id',
        name: 'Классы',
        component: Childrens,
        props: true
    },
    {
        path: '/children',
        name: 'Ученики',
        component: Childrens,
        props: true
    },
    {
        path: '/children/delete',
        name: 'Удаление ученика',
        component: Delete_children,
    },
    {
        path: '/children/:id',
        name: 'Досье ученика',
        component: Children_single,
        props: true
    },
    {
        path: '/rooms',
        name: 'Кабинеты',
        component: Rooms,
    },
    {
        path: '/subjects',
        name: 'Дисциплины',
        component: Subjects,
    },
    {
        path: '/nclass',
        name: 'Классы',
        component: Nclasses,
        props: true
    },
    {
        path: '/nclass/:id/timetable',
        name: 'Расписание класса',
        component: Nclass_timetable,
        props: true
    },
    {
        path: '/nclass/:id/childrens',
        name: 'Ученики класса',
        component: Nclass_childrens,
        props: true
    },
    {
        path: '/nclass/:id/timetable',
        name: 'Расписание класса',
        component: Timetable,
        props: true
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
