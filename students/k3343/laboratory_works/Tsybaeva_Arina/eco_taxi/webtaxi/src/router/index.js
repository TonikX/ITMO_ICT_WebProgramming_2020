import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import Login from "../components/Login";
import Drivers from "../components/Drivers";
import Report from "../components/Report";
import Storage from "../components/Storage";
import Order from "../components/Order";
import Register from "../components/Register";
import addOrder from "../components/addOrder";
import deleteOrder from "../components/deleteOrder";
import Logout from "../components/Logout";
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
      path: '/drivers',
      name: 'Drivers',
      component: Drivers
    },
    {
      path: '/report',
      name: 'Report',
      component: Report
    },
      {
      path: '/storage',
      name: 'Storage',
      component: Storage
    },
     {
      path: '/order',
      name: 'Order',
      component: Order
    },
     {
      path: '/register',
      name: 'Register',
      component: Register
    },
         {
      path: '/add_order',
      name: 'addOrder',
      component: addOrder
    },
         {
      path: '/delete_order',
      name: 'deleteOrder',
      component: deleteOrder
    },
             {
      path: '/logout',
      name: 'Logout',
      component: Logout
    },
  ]
})
