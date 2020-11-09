// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';
import { theme } from 'muse-ui'
import { carbon, createTheme } from 'muse-ui-carbon-theme';
import MenuIcon from 'vue-material-design-icons/Menu.vue';
import 'vue-material-design-icons/styles.css'


theme.add('carbon', carbon)
  .addCreateTheme(createTheme)
  .use('carbon');

import { Plugin } from 'vue-responsive-video-background-player'
import VideoBg from 'vue-videobg'

Vue.component('video-bg', VideoBg)
Vue.component('menu-icon', MenuIcon);
Vue.use(Plugin);
Vue.use(MuseUI);
Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})


