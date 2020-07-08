import Vue from "vue";
import Vuex from "vuex";

import { user } from "./user.module";
import { show } from "./show.module";
import { club } from "./club.module";

Vue.config.devtools = process.env.NODE_ENV === 'development'

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    show,
    club,
  }
});