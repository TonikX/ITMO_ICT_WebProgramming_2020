<template>
  <main>
    <v-col cols="6" class="mx-auto">
      <h1 class="text-left">Вход</h1>
      <v-form class="my-5">
        <v-col cols="12" class="mx-auto">
          <v-text-field v-model="login" label="Имя пользователя"></v-text-field>
          <v-text-field v-model="password" type="password" label="Пароль"></v-text-field>
          <v-btn class="mr-4" @click="loginUser">
            <v-icon>mdi-key</v-icon>&nbsp;&nbsp;Войти
          </v-btn>
          <p class="my-5">Ещё нет аккаунта? <router-link to="/register">Регистрация</router-link>
          </p>
        </v-col>
      </v-form>
    </v-col>
  </main>
</template>
<script>
export default {
  name: 'Login',
  data () {
    return {
      login: '',
      password: ''
    }
  },
  methods: {
    loginUser () {
      this.axios
        .post('http://127.0.0.1:8000/api/auth/token/', { username: this.login, password: this.password })
        .then(response => { this.setLogin(response.data.token) })
        .catch(err => { console.error(err) })
    },
    setLogin (token) {
      localStorage.setItem('token', token)
      localStorage.setItem('username', this.login)

      this.axios
        .get(`http://127.0.0.1:8000/api/user/me/?user=${this.login}`)
        .then(response => { localStorage.setItem('id', response.data.user[0].id); this.$router.push('/') })
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
