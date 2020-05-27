<template>
    <div>
        <h2>Subjects</h2>
        <mu-container>
            <mu-button color="#4db6ac" @click="returnHome">Home</mu-button>
            <mu-button color="#4db6ac" v-if="!auth" @click="goLogin">Log in</mu-button><br v-if="!auth"><br v-if="!auth">
            <mu-button color="#4db6ac" v-if="auth" @click="logout">Log out</mu-button><br v-if="auth"><br v-if="auth">
            <mu-paper>
                <p v-for='s in subjects' v-bind:key="s.name">
                    Subject: {{ s.name }}<br>
                    Type: {{ s.sub_type }}<br>
                </p>
            </mu-paper>
        </mu-container>
    </div>
</template>

<script>
/* eslint-disable */

import $ from 'jquery'

export default {
    name: 'Subject',
    data() {
        return {
            subjects: '',
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
        this.loadSubject()
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
        loadSubject() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/subjects/",
                type: "GET",
                success: (response) => {
                    this.subjects = response.data.data
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
    },
    p {
        font-size: 16px; font-weight: 400;
    }
</style>
