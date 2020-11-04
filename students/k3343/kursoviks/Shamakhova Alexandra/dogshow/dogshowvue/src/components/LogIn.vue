<template>
  <main>
    <v-col cols="8" class="my-1 mx-auto">
      <h2>Авторизация участника</h2>
    </v-col>
    <v-col cols="8" class="mx-auto">
      <form>
        <v-text-field v-model="login" label="Логин" required></v-text-field>
        <v-text-field type="password" v-model="password" label="Пароль" required></v-text-field>
        <v-btn class="mr-4" @click="submit" color="light-green darken-4" dark>Вход</v-btn>
        <v-btn class="mr-4" :to="'/regin'" color="teal lighten-1" dark>Нет аккаунта?</v-btn>
      </form>
    </v-col>
  </main>
</template>

<script>
export default {
  name: 'LogIn',
  data () {
    return {
      login: '',
      password: ''
    }
  },
  methods: {
    submit () {
      if (this.login && this.password) {
        this.axios
          .get(`http://127.0.0.1:8000/api/auth/`, { 'username': this.login, 'password': this.password })
          .then(response => { this.loginUser(response.data.token) })
          .catch(err => { console.error(err) })
      }
    },
    loginUser (token) {
      sessionStorage.setItem('token', token)
      sessionStorage.setItem('user', this.login)
      this.$router.push('/partcab')
    }
  }
}
</script>

<style scoped>
h2 {
  font-weight: normal;
}
</style>
