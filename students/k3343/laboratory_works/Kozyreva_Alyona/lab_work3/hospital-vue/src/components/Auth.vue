<template>
  <main>
    <v-col cols="4" class="mx-auto">
      <form>
        <v-text-field v-model="username" label="Логин" required></v-text-field>
        <v-text-field type="password" v-model="password" label="Пароль" required></v-text-field>
        <v-btn class="mr-4" @click="submit" color="teal" dark>Вход</v-btn>
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
  created () {
    if (sessionStorage.getItem('token') !== null) {
      this.$router.push('/doctor')
    }
  },
  methods: {
    submit () {
      if (this.username && this.password) {
        this.axios
          .post(`http://${window.location.hostname}:8000/api/auth/token`, { 'username': this.username, 'password': this.password })
          .then(response => { this.setLogin(response.data.token) })
          .catch(err => { console.error(err) })
      }
    },
    setLogin (token) {
      sessionStorage.setItem('token', token)
      sessionStorage.setItem('user', this.username)
      this.$router.push('/doctor')
    }
  }
}

</script>
<style></style>
