import Vue from 'vue'
import Router from 'vue-router'
import Shows from '../components/Shows'
import LogIn from '../components/LogIn'
import RegIn from '../components/RegIn'
import OrgIn from '../components/OrgIn'
import OrgCab from '../components/OrgCab'
import PartCab from '../components/PartCab'
import AddDog from '../components/AddDog'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Shows',
      component: Shows
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogIn
    },
    {
      path: '/regin',
      name: 'RegIn',
      component: RegIn,
      props: true
    },
    {
      path: '/orgin',
      name: 'OrgIn',
      component: OrgIn
    },
    {
      path: '/orgcab',
      name: 'OrgCab',
      component: OrgCab
    },
    {
      path: '/partcab',
      name: 'PartCab',
      component: PartCab
    },
    {
      path: '/adddog',
      name: 'AddDog',
      component: AddDog
    }
  ]
})
