<template>
    <mu-container>
        <h2>Timetable</h2>
        <mu-button v-if="auth" color="#4db6ac" @click="">Update</mu-button>
        <mu-button v-if="auth" color="#4db6ac" @click="">Add</mu-button>
        <mu-button v-if="auth" color="#4db6ac" @click="">Delete</mu-button><br><br>
        <mu-container>
            <mu-button color="#4db6ac" @click="returnHome">Home</mu-button>
            <mu-button v-if="!auth" color="#4db6ac" @click="goLogin">Log in</mu-button><br v-if="!auth"><br v-if="!auth">
            <mu-button v-if="auth" color="#4db6ac" @click="logout">Log out</mu-button><br v-if="auth"><br v-if="auth">
        </mu-container>
        <mu-paper>
            <mu-data-table border :columns="columns" :data="timetable">
                <template slot-scope="scope">
                    <td class="is-left">{{ scope.row.study_class.name }}</td>
                    <td class="is-left">{{ scope.row.day_of_week }}</td>
                    <td class="is-left">{{ scope.row.lesson_num }}</td>
                    <td class="is-left">{{ scope.row.subject.name }}</td>
                    <td class="is-left">{{ scope.row.room.number }}</td>
                    <td class="is-left">{{ scope.row.teacher.name }}</td>
                </template>
            </mu-data-table>
        </mu-paper>
    </mu-container>
</template>

<script>
/* eslint-disable */

import $ from 'jquery'

export default {
    name: 'Timetable',
    data() {
        return {
            timetable: '',
            columns: [
                { title: 'Class', name: 'class', align: 'center' },
                { title: 'Day of Week', name: 'day', align: 'center' },
                { title: 'Lesson number', name: 'lesson_num', align: 'center' },
                { title: 'Subject', name: 'subject', align: 'center' },
                { title: 'Room', name: 'room', align: 'center' },
                { title: 'Teacher', name: 'teacher', width: '250', align: 'center' }
            ]
        }
    },
    computed: {
        auth() {
            if (sessionStorage.getItem("auth_token")) {
                return true
            }
        }
    },
    created() {
        $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.loadTimetable()
    },
    methods: {
        goLogin() {
            this.$router.push({name: "login"})
        },
        logout() {
            sessionStorage.removeItem("auth_token")
            window.location = '/'
        },
        returnHome() {
            window.location = '/'
        },
        loadTimetable() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/timetable/",
                type: "GET",
                success: (response) => {
                    this.timetable = response.data.data
                }
            })
        }
    }
}
</script>

<style scoped>
    h2 {
        font-size: 48px; 
        font-weight: 400;
        text-align: center;
        color: #004d40;
    }
</style>
