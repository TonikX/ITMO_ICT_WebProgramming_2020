import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import Login from '../components/Login'
import ReaderCh from '../components/readers/ReaderChange'
import ReaderForm from '../components/readers/ReaderForm'
import Books from '../components/Books'

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
      path: '/reader_ch',
      name: 'reader_ch',
      component: ReaderCh,
      props: true
    },
    {
      path: '/reader_form',
      name: 'reader_form',
      component: ReaderForm
    },
    {
      path: '/books',
      name: 'books',
      component: Books
    }
  ]
})
