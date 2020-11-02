<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="deepPurpleA100">
            <h2 @click="goHome()">Библиотека</h2>
        </mu-appbar>
        <mu-row>
            <mu-form ref="form" class="mu-demo-form" label-position="left">
                <mu-form-item label="Логин" prop="username">
                  <mu-text-field v-model="login" prop="username"></mu-text-field>
                </mu-form-item>
                <mu-form-item label="Пароль" prop="password">
                    <mu-text-field type="password" v-model="password" prop="password"></mu-text-field>
                </mu-form-item>
                <mu-button @click="setLogin" style="margin-right: 400px;" >Войти</mu-button>
            </mu-form>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
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
                        alert("Спасибо что Вы с нами")
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Логин или пароль не верен")
                        }
                    }
                })
            },
            goHome() {
                this.$router.push({name: 'home'})
            },
        }
    }
</script>

<style scoped>
    .mu-demo-form {
        margin-top: 40px;
        width: 100%;
        max-width: 350px;
        margin-left: 40px;
    }
</style>
