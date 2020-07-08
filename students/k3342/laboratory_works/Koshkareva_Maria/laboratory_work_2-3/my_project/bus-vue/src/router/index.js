import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Drivers from '@/components/Drivers'
import Queries from '@/components/Queries'
import Report from '@/components/Report'
import BusMals from '@/components/BusMals'
import SchedReport from '@/components/SchedReport'
import Schedule from '@/components/Buses/Schedule'

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
                  path: '/schedule',
                  name: 'schedule',
                  component: Schedule
            },
            {
                  path: '/drivers',
                  name: 'drivers',
                  component: Drivers
            },
            {
                  path: '/queries',
                  name: 'queries',
                  component: Queries
            },
            {
                  path: '/report',
                  name: 'report',
                  component: Report
            },
            {
                  path: '/malfunctions',
                  name: 'busmals',
                  component: BusMals
            },
            {
                  path: '/sched_reports',
                  name: 'schedreport',
                  component: SchedReport
            }
      ]
})
