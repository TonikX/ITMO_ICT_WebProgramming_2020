<template>
  <main>
    <v-col cols="5" class="mx-auto">
      <h1 class="headline mb-5">Login</h1>
      <form>
        <p class="my-2" v-if="err">{{ err }}</p>
        <v-text-field v-model="login" label="Login" required></v-text-field>
        <v-text-field type="password" v-model="password" label="Password" required></v-text-field>
        <v-btn class="mr-4" @click="submit" color="primary" dark>login</v-btn>
        <p class="my-2">No account? <router-link to="/register">Register</router-link></p>
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
      password: '',
      err: ''
    }
  },
  methods: {
    submit () {
      if (this.login && this.password) {
        this.axios
          .post(`http://${window.location.hostname}:8000/api/auth/token/`, { 'username': this.login, 'password': this.password })
          .then(response => { this.loginUser(response.data.token) })
          .catch(err => { console.error(err); this.err = err })
      }
    },
    loginUser (token) {
      sessionStorage.setItem('token', token)
      sessionStorage.setItem('username', this.login)
      this.$router.push('/')
    }
  },
  mounted () {
    if (sessionStorage.getItem('username')) {
      this.$router.push('/')
    }
  }
}

</script>
<style></style>
