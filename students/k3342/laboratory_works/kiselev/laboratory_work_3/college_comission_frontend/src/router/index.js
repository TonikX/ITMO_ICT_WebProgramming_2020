import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '@/components/MainPage'
import New from '@/components/New'
import Top from '@/components/Top'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/new',
      name: 'New',
      component: New
    },
    {
      path: '/top',
      name: 'Top',
      component: Top
    }
  ]
})
