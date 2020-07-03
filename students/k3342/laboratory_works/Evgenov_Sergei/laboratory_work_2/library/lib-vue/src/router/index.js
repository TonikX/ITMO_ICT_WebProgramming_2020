import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import Login from '../components/Login'
import ReaderCh from '../components/readers/ReaderCh'

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
    }
  ]
})
