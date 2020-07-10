import Vue from 'vue'
import Router from 'vue-router'
import Main from "../components/Main";
import Start from "../components/startPage"

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Start',
      component: Start
    },
      {
          path: '/main',
          name:'Main',
          component: Main
      }
  ]
})


