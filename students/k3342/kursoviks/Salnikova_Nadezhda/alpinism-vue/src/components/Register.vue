<template>
    <div>
        <h1>Please, enter the following information</h1>
        Username and password should consist of more than 8 characters.
        <br/>
        <br/>
        <input v-model="username" type="text" placeholder="Username"/> <br/>
        <p></p>
        <input v-model="password" type="password" placeholder="Password"/> <br/>
        <p></p>
        <input v-model="password2" type="password" placeholder="Password Again"/> <br/>
        <p></p>
        <input v-model="email" type="email" placeholder="E-mail"/>
        <p>*optional</p>
        <br/>
        <br/>
        <mu-container class="button-wrapper">
            <mu-button color="#2c3e50" textColor="white" @click="passwordCheck">Sign Up</mu-button>
        </mu-container>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Register",
        data() {
            return {
                username: '',
                password: '',
                email: '',
                password2: ''
            }
        },
        methods: {
            passwordCheck() {
                if (this.password === this.password2) {
                    this.signUp()
                } else {
                    alert('Passwords do not match')
                }
            },
            signUp() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/users/create/",
                    type: "POST",
                    data: {
                        username: this.username,
                        password: this.password
                    },
                    success: (response) => {
                        this.signIn()
                    },
                    error: (response) => {
                        alert('Something is wrong')
                        console.log(response)
                    }
                })
            },
            signIn() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login/",
                    type: "POST",
                    data: {
                        username: this.username,
                        password: this.password
                    },
                    success: (response) => {
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "main_page"})
                    }
                })
            }
        }
    }
</script>

<style scoped>
    body {
        background-color: #ffffff;
    }

    h1 {
        margin-top: 80px;
        font-size: 200%;
        line-height: 100px;
        color: #000000;
        font-family: 'Questrial', sans-serif;
        text-align: center;
    }

    p {
        margin-left: -100px;
        font-size: 80%;
        color: #000000;
        font-family: 'Questrial', sans-serif;
    }
</style>
