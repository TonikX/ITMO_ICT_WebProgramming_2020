import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Books from '@/components/books/Books'
import Readers from '@/components/readers/Readers'
import Halls from "../components/halls/Halls";

Vue.use(Router)

export default new Router({
    routes: [{
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
        path: '/books',
        name: 'books',
        component: Books
        },
        {
        path: '/readers',
        name: 'readers',
        component: Readers
        },
        {
        path: '/halls',
        name: 'halls',
        component: Halls
        },
    ]
})
