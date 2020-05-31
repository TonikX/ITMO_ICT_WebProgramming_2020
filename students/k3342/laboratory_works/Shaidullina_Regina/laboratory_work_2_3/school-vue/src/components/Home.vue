<template>
    <div>
        <mu-container class="button-wrapper">
            <mu-button v-if="!auth" color="#5c6bc0" textColor="white" @click="goLogin">Log in</mu-button>
            <mu-button v-if="auth" color="#5c6bc0" textColor="white" @click="logout">Log out</mu-button>
        </mu-container>
        <h1>School administration</h1>
        <mu-container v-if="auth">
            <mu-tabs :value.sync="active1" inverse color="#5c6bc0" textColor="white" indicator-color="#5c6bc0" center>
                <mu-tab>Timetable</mu-tab>
                <mu-tab>Teachers</mu-tab>
                <mu-tab>Pupils</mu-tab>
                <mu-tab>Assessments</mu-tab>
                <mu-tab>Classes</mu-tab>
                <mu-tab>Subjects</mu-tab>
                <mu-tab>Rooms</mu-tab>
            </mu-tabs>
            <div class="demo-text" v-if="active1 === 0">
                <br><p>To edit information, choose the option below.</p>
                <timetable></timetable>
            </div>
            <div class="demo-text" v-if="active1 === 1">
                <br><p>To edit information, choose the option below.</p>
                <teacher></teacher>
            </div>
            <div class="demo-text" v-if="active1 === 2">
                <br><p>To edit information, choose the option below.</p>
                <pupil></pupil>
            </div>
            <div class="demo-text" v-if="active1 === 3">
                <br><p>To edit information, choose the option below.</p>
                <assessment></assessment>
            </div>
            <div class="demo-text" v-if="active1 === 4">
                <br><p>Information about classes.</p>
                <class></class>
            </div>
            <div class="demo-text" v-if="active1 === 5">
                <br><p>Information about subjects.</p>
                <subject></subject>
            </div>
            <div class="demo-text" v-if="active1 === 6">
                <br><p>Information about study rooms.</p>
                <room></room>
            </div>
            <div class="demo-text" v-if="active1 === -1">
                <!-- <br><br><img width="350" src="https://cdn.shopify.com/s/files/1/2562/6932/articles/teacher-tired-humor-teacher-memes-funny_1200x679_crop_top.jpg?v=1518395627"> -->
                <br><br><img width="350" src="https://edu.tatar.ru/2018/img/girl.png">
            </div>
        </mu-container>
        <mu-container v-if="!auth">
            <!-- <br><img width="350" src="https://cdn.shopify.com/s/files/1/2562/6932/articles/teacher-tired-humor-teacher-memes-funny_1200x679_crop_top.jpg?v=1518395627"> -->
            <br><br><img width="350" src="https://edu.tatar.ru/2018/img/girl.png">
        </mu-container>
    </div>
</template>

<script>
/* eslint-disable */

import Timetable from '@/components/Timetable.vue'
import Teacher from '@/components/Teacher'
import Pupil from '@/components/Pupil'
import Class from '@/components/Class'
import Subject from '@/components/Subject'
import Room from '@/components/Room'
import Assessment from '@/components/Assessment'

export default {
    name: 'Home',
    components: {
        Timetable, 
        Teacher, 
        Pupil, 
        Class, 
        Subject, 
        Room, 
        Assessment
    },
    data () {
        return {
            active1: -1
        };
    },
    computed: {
        auth() {
            if (sessionStorage.getItem("auth_token")) {
                return true
            }
        }
    },
    methods: {
        goLogin() {
            this.$router.push({name: "login"})
        },
        logout() {
            sessionStorage.removeItem("auth_token")
            window.location = '/'
        }
    }
}
</script>

<style scoped>
    h1 {
        font-size: 60px; 
        font-weight: 300;
        text-align: center;
        color: #1a237e;
    },
    .button-wrapper {
        text-align: right;
        .mu-button{
            margin: 8px;
        }
    },
    .button-wrapper2 {
        text-align: center;
        .mu-button{
            margin: 8px;
        }
    }
</style>
