<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <br/>
                <br/>
                <mu-text-field v-model="username" label="Имя пользователя"></mu-text-field><br/>
            </mu-col>
        </mu-row >
        <mu-row align="center">
            <mu-col>
                <mu-text-field v-model="password" label="Пароль, не менее 8 символов" :action-icon="visibility ? 'visibility_off' : 'visibility'" :action-click="() => (visibility = !visibility)" :type="visibility ? 'text' : 'password'"></mu-text-field><br/>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <mu-text-field v-model="password2" label="Повторите ввод пароля" :action-icon="visibility ? 'visibility_off' : 'visibility'" :action-click="() => (visibility = !visibility)" :type="visibility ? 'text' : 'password'"></mu-text-field><br/>
            </mu-col>
        </mu-row>
        <mu-container class="button-wrapper">
            <mu-row>
                <mu-col>
            <mu-button color="primary" @click="passwordCheck">Зарегистрироваться</mu-button>
                </mu-col>
            </mu-row>
        </mu-container>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Signup",
        data() {
            return {
                username: '',
                password: '',
                password2: '',
                visibility: false,
            }
        },
        methods: {
            passwordCheck() {
                if (this.password === this.password2) {
                    this.signUp()
                } else {
                    alert('Пароли не совпадают')
                }
            },
            signUp() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/users/",
                    type: "POST",
                    data: {
                        username: this.username,
                        password: this.password
                    },
                    success: (response) => {
                        alert("Регистрация прошла успешно")
                        this.$router.push({name: "Вход"})
                    },
                    error: (response) => {
                            if (response.status === 400) {
                                alert("Некорректное имя пользователя и/или пароль")
                            }
                        }
                })
            },
        }
    }
</script>

<style scoped>

</style>