<template>
  <main>
    <v-col class="mx-auto">
      <form>
        <v-text-field v-model="login" label="Логин" required></v-text-field>
        <v-text-field type="password" v-model="password" label="Пароль" required></v-text-field>
        <v-btn class="mr-4" @click="submit" color="pink accent-3" dark>Вход</v-btn>
        <v-btn dark class="mr-4" :to="'/newClient'" color="pink accent-4">Зарегистрироваться</v-btn>
      </form>
    </v-col>
  </main>
</template>
<script>
export default {
  name: 'Auth',
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
          .post(`http://${window.location.hostname}:8000/api/auth/token`, { 'username': this.login, 'password': this.password })
          .then(response => { this.loginUser(response.data.token) })
          .catch(err => { console.error(err) })
      }
    },
    loginUser (token) {
      sessionStorage.setItem('token', token)
      sessionStorage.setItem('user', this.login)
      this.$router.push('/Cabinet')
    }
  }
}

</script>
<style></style>
