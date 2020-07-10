<template>
  <main>
    <v-col cols="6" class="mx-auto">
      <h1 class="text-left">Регистрация</h1>
      <v-form class="my-5">
        <v-col cols="12" class="mx-auto">
          <v-text-field v-model="login" label="Имя пользователя"></v-text-field>
          <v-text-field v-model="email" label="Адрес электронной почты"></v-text-field>
          <v-text-field v-model="password" type="password" label="Пароль"></v-text-field>
          <v-btn class="mr-4" @click="registerUser">
            <v-icon>mdi-key</v-icon>&nbsp;&nbsp;Зарегистрироваться
          </v-btn>
          <p class="my-5">Уже есть аккаунт? <router-link to="/login">Вход</router-link>
          </p>
        </v-col>
      </v-form>
    </v-col>
  </main>
</template>
<script>
export default {
  name: 'Register',
  data () {
    return {
      login: '',
      password: '',
      email: ''
    }
  },
  methods: {
    registerUser () {
      this.axios
        .post('http://127.0.0.1:8000/api/auth/users/', { username: this.login, password: this.password, email: this.email })
        .then(response => { this.$router.push('/login') })
        .catch(err => { console.error(err) })
    }
  },
  mounted () {
    if (localStorage.getItem('token') && localStorage.getItem('username')) {
      this.$router.push('/')
    }
  }
}

</script>
<style></style>
