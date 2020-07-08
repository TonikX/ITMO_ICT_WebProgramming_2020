<template>
  <main>
    <v-col cols="4" class="mx-auto">
      <form>
        <v-text-field v-model="username" label="Логин" required></v-text-field>
        <v-text-field type="password" v-model="password" label="Пароль" required></v-text-field>
        <v-btn class="mr-4" @click="login" color="indigo" dark>Вход</v-btn>
        <v-btn dark class="mr-4" to='/signup' color="teal">Зарегистрироваться</v-btn>
      </form>
    </v-col>
  </main>
</template>
<script>
export default {
  name: 'Auth',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login () {
      if (this.username && this.password) {
        this.axios
          .post(`http://${window.location.hostname}:8000/api/auth/token`, { 'username': this.username, 'password': this.password })
          .then(response => { this.setLogin(response.data.token) })
          .catch(err => { console.error(err) })
      }
    },
    setLogin (token) {
      sessionStorage.setItem('token', token)
      sessionStorage.setItem('username', this.username)

      this.axios
        .get(`http://${window.location.hostname}:8000/api/is/client?username=${this.username}`)
        .then(response => { this.isClient(response.data) })
    },
    isClient (data) {
      if (data.length > 0) {
        sessionStorage.setItem('type', 'Client')
      } else {
        sessionStorage.setItem('type', 'Employee')
      }

      this.goToCabinet()
    },
    goToCabinet () {
      this.$router.push('/cabinet')
    }
  }
}

</script>
<style></style>
