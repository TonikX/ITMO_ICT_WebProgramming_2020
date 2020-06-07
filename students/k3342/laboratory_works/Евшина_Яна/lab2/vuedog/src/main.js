import Vue from 'vue'
import MuseUI from 'muse-ui';
import App from './App.vue'
import router from './router';
import store from './store';

import 'muse-ui/dist/muse-ui.css';

Vue.config.productionTip = false
Vue.config.devtools = process.env.NODE_ENV === 'development'

Vue.use(MuseUI);

const app = new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')

window.__VUE_DEVTOOLS_GLOBAL_HOOK__.Vue = app.constructor
