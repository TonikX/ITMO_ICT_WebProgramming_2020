import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import MainPage from "@/components/MainPage"
import Groups from '@/components/Groups'
import Alpinists from '@/components/Alpinists'
import Mountains from '@/components/Mountains'
import Clubs from '@/components/Clubs'
import Countries from "@/components/Countries"
import Ascents from "@/components/Ascents"
import Emergencies from "@/components/Emergencies"
import Successes from "@/components/Successes"
import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';
import Register from "@/components/Register";
import Request1 from "../components/Request1";


Vue.use(MuseUI);
Vue.use(Router);

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
            path: '/home',
            name: 'main_page',
            component: MainPage
        },
        {
            path: '/groups',
            name: 'groups',
            component: Groups
        },
        {
            path: '/alpinists',
            name: 'alpinists',
            component: Alpinists
        },
        {
            path: '/mountains',
            name: 'mountains',
            component: Mountains
        },
        {
            path: '/clubs',
            name: 'clubs',
            component: Clubs
        },
        {
            path: '/countries',
            name: 'countries',
            component: Countries
        },
        {
            path: '/ascents',
            name: 'ascents',
            component: Ascents
        },
        {
            path: '/emergencies',
            name: 'emergencies',
            component: Emergencies
        },
        {
            path: '/successes',
            name: 'successes',
            component: Successes
        },
        {
            path: '/signup',
            name: 'register',
            component: Register
        },
        {
            path: '/request1',
            name: 'request1',
            component: Request1
        }
    ]
})
