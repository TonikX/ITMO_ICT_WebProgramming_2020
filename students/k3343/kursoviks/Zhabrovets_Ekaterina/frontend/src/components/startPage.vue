<template>
    <div>
        <!--        <video-background class="video-container" src="../assets/video-grey.mp4" style="max-height: 400px; height: 100vh;"/>-->
        <!--    <div>-->
        <!--        <link rel="stylesheet" href="../../static/style.css">-->
        <link rel="stylesheet" href="../assets/style.css">
        <video-bg :sources="['../static/Abstract.mp4']">
            <mu-container style="margin-top: 200px; align-content: center">
                <h1>Курсовая работа по введению в web-программирование:</h1>
                <h1><i>"Танцевальные мастер-классы Санкт-Петербурга"</i></h1>
                <mu-row gutter style="margin-top: 20px;">
                    <mu-col>
                        <mu-button color="primary" full-width @click="openLogin">Войти
                            <mu-icon value="done_all"></mu-icon>
                        </mu-button>
                    </mu-col>
                    <mu-col>
                        <mu-button color="secondary" full-width @click="openSignUp">Зарегистрироваться
                            <mu-icon value="add"/>
                        </mu-button>
                    </mu-col>
                </mu-row>
                <mu-container>
                    <mu-dialog title="Вход" width="400" max-width="80%" :open.sync="open_login">
                        <mu-container>
                            <mu-paper>
                                <mu-form>
                                    <mu-form-item label="Логин" prop="username">
                                        <mu-text-field prop="username" v-model="login"></mu-text-field>
                                    </mu-form-item>
                                    <mu-form-item label="Пароль" prop="password" :rules="passwordRules">
                                        <mu-text-field type="password" v-model="password"
                                                       prop="password"></mu-text-field>
                                    </mu-form-item>
                                    <mu-form-item>
                                        <mu-button color="primary" @click="setLogin(login, password)">Войти</mu-button>
                                    </mu-form-item>
                                </mu-form>
                            </mu-paper>
                        </mu-container>
                    </mu-dialog>
                    <mu-dialog title="Регистрация" width="500" max-width="80%" :open.sync="open_signup">
                        <mu-container>
                            <mu-paper>
                                <mu-stepper :active-step="vactiveStep" orientation="vertical">
                                    <mu-step>
                                        <mu-step-label>
                                            Придумайте логин
                                        </mu-step-label>
                                        <mu-step-content>
                                            <p>
                                                <mu-form>
                                                    <mu-form-item label="Логин" prop="name_user">
                                                        <mu-text-field prop="name_user"
                                                                       v-model="name_user"></mu-text-field>
                                                    </mu-form-item>
                                                </mu-form>
                                            </p>
                                            <mu-button v-if="name_user!==''" class="demo-step-button"
                                                       @click="vhandleNext" color="primary">
                                                Далее
                                            </mu-button>
                                        </mu-step-content>
                                    </mu-step>
                                    <mu-step>
                                        <mu-step-label>
                                            Придумайте пароль
                                        </mu-step-label>
                                        <mu-step-content>
                                            <p>
                                                <mu-form>
                                                    <mu-form-item label="Пароль" prop="password_user">
                                                        <mu-text-field type="password" prop="password_user"
                                                                       v-model="password_user"></mu-text-field>
                                                    </mu-form-item>
                                                    <mu-form-item label="Повторите пароль" prop="password_user_check">
                                                        <mu-text-field type="password" prop="password_user_check"
                                                                       v-model="password_user_check"></mu-text-field>
                                                    </mu-form-item>
                                                </mu-form>
                                            </p>
                                            <mu-button
                                                v-if="password_user === password_user_check & password_user!=='' & password_user_check!==''"
                                                class="demo-step-button" @click="vhandleNext" color="primary">
                                                Далее
                                            </mu-button>
                                            <mu-button flat class="demo-step-button" @click="vhandlePrev">Назад
                                            </mu-button>
                                        </mu-step-content>
                                    </mu-step>
                                    <mu-step>
                                        <mu-step-label>
                                            А теперь давайте познакомимся
                                        </mu-step-label>
                                        <mu-step-content>
                                            <p>
                                                <mu-form>
                                                    <mu-form-item label="Фамилия - Имя" prop="full_name">
                                                        <mu-text-field prop="full_name"
                                                                       v-model="full_name"></mu-text-field>
                                                    </mu-form-item>
                                                </mu-form>
                                            </p>
                                            <mu-button class="demo-step-button" @click="vhandleNext" color="primary">
                                                Далее
                                            </mu-button>
                                            <mu-button flat class="demo-step-button" @click="vhandlePrev">Назад
                                            </mu-button>
                                        </mu-step-content>
                                    </mu-step>
                                </mu-stepper>
                                <p v-if="vfinished">
                                    <mu-button class="demo-step-button" color="primary" @click="createUser">
                                        Завершить процесс регистрации
                                    </mu-button>
                                    <mu-button flat class="demo-step-button" @click="vhandlePrev">Назад
                                    </mu-button>
                                </p>
                            </mu-paper>
                        </mu-container>
                    </mu-dialog>
                </mu-container>
                <!--        <mu-container>-->
                <!--    <mu-paper style="margin-top: 200px">-->
                <!--        <h1>Танцевальные мастер-классы Санкт-Петербурга</h1>-->
                <!--        <mu-form>-->
                <!--            <mu-form-item label="username" prop="username">-->
                <!--                <mu-text-field prop="username" v-model="login"></mu-text-field>-->
                <!--            </mu-form-item>-->
                <!--            <mu-form-item label="password" prop="password" :rules="passwordRules">-->
                <!--                <mu-text-field type="password" v-model="password" prop="password"></mu-text-field>-->
                <!--            </mu-form-item>-->
                <!--            <mu-form-item>-->
                <!--                <mu-button color="primary" @click="setLogin">submit</mu-button>-->
                <!--            </mu-form-item>-->
                <!--        </mu-form>-->
                <!--    </mu-paper>-->
                <!--    </mu-container>-->


            </mu-container>
        </video-bg>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "startPage",
        data() {
            return {
                login: '',
                password: '',
                open_login: false,
                open_signup: false,
                vactiveStep: 0,
                name_user: '',
                password_user: '',
                password_user_check: '',
                full_name: '',

            }
        },
        computed: {
            vfinished() {
                return this.vactiveStep > 2;
            }
        },
        methods: {
            setLogin(log, pass) {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login/",
                    type: "POST",
                    data: {
                        username: log,
                        password: pass,
                    },
                    success: (response) => {
                        alert("Вход выполнен")
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "Main"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Ошибка авторизации")
                        }
                    }

                })
            },
            openLogin() {
                this.open_login = true
            },
            openSignUp() {
                this.open_signup = true
            },
            vhandleNext() {
                this.vactiveStep++;
            },
            vhandlePrev() {
                this.vactiveStep--;
            },
            vreset() {
                this.vactiveStep = 0;
            },
            setSignIn() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/users/",
                    type: "POST",
                    data: {
                        username: this.name_user,
                        password: this.password_user,
                    },
                    success: (response) => {
                        alert("Регистрация завершена")
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Ошибка регистрации")
                        }
                    }
                })
            },
            addName() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/profile_new/",
                    type: "POST",
                    data: {
                        full_name: this.full_name,
                    },
                    success: (response) => {
                        alert("Имя добавлено")
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Ошибка добавления имени")
                        }
                    }
                })
            },
            async createUser() {
                this.setSignIn();
                setTimeout(this.addName,1000);
                setTimeout(()=>this.setLogin(this.name_user, this.password_user), 3000);
            }

        }
    }
</script>

<style scoped>

</style>
