import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { API_URL } from '@/services/config'
const ApiService = {
  init () {
    Vue.use(VueAxios, axios)
    Vue.axios.defaults.baseURL = API_URL
  },
  get (resource, slug='') {
    return Vue.axios
            .get('${resource}\${slug}')
            .catch((error) => { throw new Error('ApiService ${error}' )
            })

  },
}
export default ApiService


