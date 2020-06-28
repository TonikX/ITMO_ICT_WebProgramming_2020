import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import JobSeekerDetail from '../views/JobSeekerDetail.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/jobseeker/:id',
    name: 'Jobseeker',
    component: JobSeekerDetail,
    props: true,
  },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;
