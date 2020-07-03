<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <br>
                <br>
                <mu-text-field v-model="login" label="UserName" label-float
                               help-text="A character with a username of 6-12 length"></mu-text-field>
                <br/>
                <mu-text-field v-model="password" label="Password" type="password" label-float
                               error-text="Please enter password"></mu-text-field>
                <br/>
                <mu-button color="primary" @click="setLogin">Войти</mu-button>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
            <br>
                <p> Нет логина и пароля? Тогда Вам необходимо <a href="/regis">зарегистрироваться</a></p>
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