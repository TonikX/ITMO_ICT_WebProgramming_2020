<template>
    <div>
        <input v-model="login" type="text" placeholder="login"/>
        <input v-model="password" type="password" placeholder="password"/>
        </br>
        </br>
        <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
            <mu-button color="grey" textColor="white" @click="setLogin">Login</mu-button>
        </mu-container>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: ''
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login/",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "main_page"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                        alert('Login or password is incorrect')
                    }}
                })

            }
        }
    }
</script>

<style scoped>
    .demo-divider-form {
        font-size: 90%;
        padding: 0 16px;
    }

</style>
