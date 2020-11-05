import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Auth from '@/components/Auth'
import Register from '@/components/Register'
import Librarians from '@/components/Librarians'
import Books from '@/components/Books'
import Ownerships from '@/components/Ownerships'
import Halls from '@/components/Halls'
import Visitors from '@/components/Visitors'
import AddOwnership from "@/components/AddOwnership"
import Rents from '@/components/Rents'
import AddRent from "@/components/AddRent"
import AddBook from "@/components/AddBook"

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/librarians',
      name: 'Librarians',
      component: Librarians
    },
    {
      path: '/visitors',
      name: 'Visitors',
      component: Visitors
    },
    {
      path: '/books',
      name: 'Books',
      component: Books
    },
    {
      path: '/books/add',
      name: 'AddBook',
      component: AddBook
    },
    {
      path: '/halls',
      name: 'Halls',
      component: Halls
    },
    {
      path: '/ownerships',
      name: 'Ownerships',
      component: Ownerships
    },
    {
      path: '/ownerships/add',
      name: 'AddOwnership',
      component: AddOwnership
    },
    {
      path: '/rents',
      name: 'Rents',
      component: Rents
    },
    {
      path: '/rents/add',
      name: 'AddRent',
      component: AddRent
    }
  ]
})
