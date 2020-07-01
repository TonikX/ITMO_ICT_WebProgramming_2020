<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>Пожалуйста, заполните следующие поля</h1>
                <h3>Поля должны содержать не менее 8 символов.</h3>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <br/>
                <br/>
                <mu-text-field v-model="username" placeholder="Username"></mu-text-field><br/>
            </mu-col>
        </mu-row >
        <mu-row align="center">
            <mu-col>
                <mu-text-field v-model="password" label="Password" :action-icon="visibility ? 'visibility_off' : 'visibility'" :action-click="() => (visibility = !visibility)" :type="visibility ? 'text' : 'password'"></mu-text-field><br/>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <mu-text-field v-model="password2" label="Password again" :action-icon="visibility ? 'visibility_off' : 'visibility'" :action-click="() => (visibility = !visibility)" :type="visibility ? 'text' : 'password'"></mu-text-field><br/>
            </mu-col>
        </mu-row>
        <mu-container class="button-wrapper">
            <mu-row>
                <mu-col>
            <mu-button color="secondary" @click="passwordCheck">Зарегистрироваться</mu-button>
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
                        alert("Вы успешно зарегистрировались")
                        this.$router.push({name: "Вход"})
                    },
                    error: (response) => {
                            if (response.status === 400) {
                                alert("Проверьте корректность введенных данных")
                            }
                        }
                })
            },
        }
    }
</script>

<style scoped>

</style>