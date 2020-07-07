import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../views/Login";
import SignUp from "../views/SignUp";
import Book from "../views/Book";
import BookSingle from "../views/BookSingle";
import Reader from "../views/Reader";
import ReadingRoom from "../views/ReadingRoom";
import ReaderSingle from "../views/ReaderSingle";
import TakingBook from "../views/TakingBook";
import Queries from "../views/Queries";

import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';

Vue.use(MuseUI)
Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'Вход',
        component: Login
    },
    {
        path: '/signup',
        name: 'Регистрация',
        component: SignUp
    },
    {
        path: '/book',
        name: 'Книги',
        component: Book,
        props: true
    },
    {
        path: '/book_single/:id',
        name: 'Книга',
        component: BookSingle,
        props: true
    },
    {
        path: '/reader',
        name: 'Читатели',
        component: Reader,
        props: true
    },
    {
        path: '/reader_single/:id',
        name: 'Читатель',
        component: ReaderSingle,
        props: true
    },
    {
        path: '/reading_room',
        name: 'Читальные залы',
        component: ReadingRoom,
        props: true
    },
    {
        path: '/taking_book',
        name: 'Учет книг',
        component: TakingBook,
        props: true
    },
    {
        path: '/queries',
        name: 'Запросы',
        component: Queries,
        props: true
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
    routes
})

export default router
