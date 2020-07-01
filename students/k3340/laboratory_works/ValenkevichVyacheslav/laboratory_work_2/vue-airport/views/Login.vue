<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <br>
                <br>
                <mu-text-field v-model="login" label="Имя пользователя" label-float
                               help-text=""></mu-text-field>
                <br/>
                <mu-text-field v-model="password" label="Пароль" type="password" label-float
                               error-text="Пожалуйста, введите пароль"></mu-text-field>
                <br/>
                <mu-button color="primary" @click="setLogin">Войти</mu-button>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
            <br>
                <a href="#/signup">Регистрация</a>
            </mu-col>
        </mu-row>
    </mu-container>
</template>
<script>
    import $ from 'jquery'

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
                        console.log(response)
                        localStorage.setItem("auth_token", response.auth_token)
                        alert("Спасибо что Вы с нами")
                        this.$router.push({name: "Главная страница"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Логин или пароль не верен")
                        }
                    }
                })
            },
        }
    }
</script>

<style scoped>
</style>