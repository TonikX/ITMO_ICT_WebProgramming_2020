<template>
    <v-row align="start" justify="center">
        <v-col cols="12" sm="8" md="6" lg="5" xl="4">
            <v-card class="elevation-12">
                <v-toolbar color="primary" dark flat>
                    <v-toolbar-title>Авторизация</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                    <v-form v-model="valid">
                        <v-text-field v-model="username"
                                      name="login"
                                      label="Логин"
                                      prepend-icon="person"
                                      required
                                      :rules="rules"/>
                        <v-text-field v-model="password"
                                      name="password"
                                      prepend-icon="lock"
                                      :append-icon="showPassword ? 'visibility' : 'visibility_off'"
                                      :rules="rules"
                                      :type="showPassword ? 'text' : 'password'"
                                      label="Пароль"
                                      required
                                      @click:append="showPassword = !showPassword"/>
                    </v-form>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="accent" :disabled="!valid" @click="login()">Войти</v-btn>
                </v-card-actions>
            </v-card>
        </v-col>
    </v-row>
</template>

<script>
    import {httpClient} from "../api/httpClient"
    import {TokenStorage} from "../api/tokenStorage";
    import router from "../router";

    export default {
        name: "Login",
        data: () => ({
            valid: false,
            showPassword: false,
            username: "",
            password: "",
            rules: [
                v => !!v || 'Это поле обязательно'
            ]
        }),
        methods: {
            login() {
                httpClient.post('/auth', {
                    username: this.username,
                    password: this.password
                })
                    .then((response) => {
                        TokenStorage.storeAccessToken(response.data.access);
                        TokenStorage.storeRefreshToken(response.data.refresh);
                        console.log('response login' + JSON.stringify(response));
                        router.push({name: 'quests'})
                    })
                    .catch((error) => {
                        TokenStorage.clear();
                        console.log('response login error' + JSON.stringify(error))
                    })
            }
        }
    }
</script>
