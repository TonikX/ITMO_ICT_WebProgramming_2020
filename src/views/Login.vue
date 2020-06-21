<template>
    <v-row align="start" justify="center">
        <v-col cols="12" sm="8" md="6" lg="5" xl="4">
            <v-card class="elevation-12">
                <v-toolbar color="primary" dark flat>
                    <v-toolbar-title>Авторизация</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                    <v-form v-model="valid">
                        <v-text-field v-model="login"
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
                    <v-btn color="accent" :disabled="!valid">Войти</v-btn>
                </v-card-actions>
            </v-card>
        </v-col>
    </v-row>
</template>

<script>
    export default {
        valid: false,
        name: "Login",
        data: () => ({
            showPassword: false,
            login: "",
            password: "",
            rules: [
                v => !!v || 'Это поле обязательно'
            ]
        }),
    }
</script>
