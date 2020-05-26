// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import vuetify from './plugins/vuetify'
import vueResource from 'vue-resource'
import axios from 'axios'
import Vuex from 'vuex'
Vue.prototype.$axios = axios

Vue.config.productionTip = false
Vue.use(vueResource);
axios.defaults.baseURL ='http://127.0.0.1:8000/';
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  vuetify
})
