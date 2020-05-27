<template>
    <div>
        <h2>Pupils</h2>
        <mu-button v-if="auth" color="#4db6ac" @click="">Update</mu-button>
        <mu-button v-if="auth" color="#4db6ac" @click="">Add</mu-button>
        <mu-button v-if="auth" color="#4db6ac" @click="">Delete</mu-button><br><br>
        <mu-container>
            <mu-button color="#4db6ac" @click="returnHome">Home</mu-button>
            <mu-button color="#4db6ac" v-if="!auth" @click="goLogin">Log in</mu-button><br v-if="!auth"><br v-if="!auth">
            <mu-button color="#4db6ac" v-if="auth" @click="logout">Log out</mu-button><br v-if="auth"><br v-if="auth">
            <mu-paper>
                <p v-for='pupil in pupils' v-bind:key='pupil.id'>
                    Pupil: {{ pupil.name }}<br>
                    Gender: {{ pupil.gender }}<br>
                    Class: {{ pupil.study_class.name }}<br>
                </p>
            </mu-paper>
        </mu-container>
    </div>
</template>

<script>
/* eslint-disable */

import $ from 'jquery'

export default {
    name: 'Pupil',
    data() {
        return {
            pupils: '',
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
        this.loadPupil()
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
        loadPupil() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/pupils/",
                type: "GET",
                success: (response) => {
                    this.pupils = response.data.data
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
