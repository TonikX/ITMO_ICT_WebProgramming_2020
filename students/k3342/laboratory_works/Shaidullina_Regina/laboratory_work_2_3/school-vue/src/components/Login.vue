<template>
    <div>
        <h2>Log in</h2>
        <mu-container>
            <mu-text-field v-model="login" label="Username" type="text" label-float></mu-text-field><br>
            <mu-text-field v-model="password" label="Password" type="password" label-float error-text="Please enter password"></mu-text-field><br>
        </mu-container>
        <br>
        <mu-container>
            <mu-button color="#4db6ac" @click="returnHome">Home</mu-button>
            <mu-button color="#4db6ac" @click="setLogin">Log in</mu-button>
        </mu-container>
    </div>
</template>

<script>
/* eslint-disable */

import $ from 'jquery'

export default {
    name: 'Login',
    data() {
        return {
            login: "",
            password: ""
        }
    },
    methods: {
        setLogin() {
            $.ajax({
                url: "http://127.0.0.1:8000/auth/token/create/",
                type: "POST",
                data: {
                    username: this.login,
                    password: this.password
                },
                success: (response) => {
                    //alert("Logged in successfully.")
                    sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                    this.$router.push({name: "home"})
                },
                error: (response) => {
                    if (response.status === 400) {
                        alert("Login or password are incorrect.")
                    }
                }
            })
        },
        returnHome() {
            window.location = '/'
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
