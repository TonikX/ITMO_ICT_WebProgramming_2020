<template>
    <mu-container>
        <h2>Assessments</h2>
        <mu-button v-if="auth" color="#4db6ac" @click="">Update</mu-button>
        <mu-button v-if="auth" color="#4db6ac" @click="">Add</mu-button>
        <mu-button v-if="auth" color="#4db6ac" @click="">Delete</mu-button><br><br>
        <mu-container>
            <mu-button color="#4db6ac" @click="returnHome">Home</mu-button>
            <mu-button v-if="!auth" color="#4db6ac" @click="goLogin">Log in</mu-button><br v-if="!auth"><br v-if="!auth">
            <mu-button v-if="auth" color="#4db6ac" @click="logout">Log out</mu-button><br v-if="auth"><br v-if="auth">
        </mu-container>
        <mu-paper>
            <mu-data-table border :columns="columns" :data="assessment" :min-col-width="200">
                <template slot-scope="scope">
                    <td class="is-left">{{ scope.row.term }}</td>
                    <td class="is-left">{{ scope.row.pupil.name }}</td>
                    <td class="is-left">{{ scope.row.subject.name }}</td>
                    <td class="is-left">{{ scope.row.grade }}</td>
                </template>
            </mu-data-table>
        </mu-paper>
    </mu-container>
</template>

<script>
/* eslint-disable */

import $ from 'jquery'

export default {
    name: 'Assessment',
    data() {
        return {
            assessment: '',
            columns: [
                { title: 'Term', name: 'term', align: 'center' },
                { title: 'Pupil', name: 'pupil', width: '370', align: 'center' },
                { title: 'Subject', name: 'subject', align: 'center' },
                { title: 'Grade', name: 'grade', align: 'center' },
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
        this.loadAss()
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
        loadAss() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/assessments/",
                type: "GET",
                success: (response) => {
                    this.assessment = response.data.data
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
