import Vue from 'vue';
import Router from 'vue-router';
import Home from '../components/Home';
import Login from '../components/Login';
import Registration from "../components/Registration";
import Vacancy from "../components/Vacancy";
import Jobseeker from "../components/Jobseeker";
import VacancySingle from "../components/VacancySingle";
import JobseekerSingle from "../components/JobseekerSingle";
import ResumeReg from '../components/ResumeReg'
import Employer from "../components/Employer";
import EmployerSingle from "../components/EmploerSingle";
import Application from "../components/Application"


Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/registration',
      name: 'registration',
      component: Registration,
    },
    {
      path: '/vacancy',
      name: 'vacancy',
      component: Vacancy,
      props: true,
    },
    {
      path: '/vacancy/:id',
      name: 'vacancySingle',
      component: VacancySingle,
      props: true,
    },
    {
      path: '/jobseeker',
      name: 'jobseeker',
      component: Jobseeker,
      props: true,
    },
    {
      path: '/jobseeker/:id',
      name: 'jobseekerSingle',
      component: JobseekerSingle,
      props: true,
    },
    {
      path: '/resume_reg/',
      name: 'resumeReg',
      component: ResumeReg,
    },
      {
      path: '/employer',
      name: 'employer',
      component: Employer,
      props: true,
    },
    {
      path: '/employer/:id',
      name: 'employerSingle',
      component: EmployerSingle,
      props: true,
    },
      {
      path: '/application',
      name: 'application',
      component: Application,
    },
  ]
})