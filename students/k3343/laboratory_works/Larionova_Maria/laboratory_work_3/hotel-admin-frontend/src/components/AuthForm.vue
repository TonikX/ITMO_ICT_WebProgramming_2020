<template>
  <main>
    <v-col cols="5" class="mx-auto">
      <form>
        <v-text-field v-model="login" label="Логин" required></v-text-field>
        <v-text-field type="password" v-model="password" label="Пароль" required></v-text-field>
        <v-btn class="mr-4" @click="submit" color="deep-orange" dark>Вход</v-btn>
      </form>
    </v-col>
  </main>
</template>
<script>
export default {
  name: 'AuthForm',
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
      sessionStorage.setItem('worker', this.login)
      this.$router.push('/worker')
    }
  }
}

</script>
<style></style>
