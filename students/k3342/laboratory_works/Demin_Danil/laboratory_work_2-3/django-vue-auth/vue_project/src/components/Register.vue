<template>
  <main>
    <v-col cols="5" class="mx-auto">
      <h1 class="headline mb-5">New Account</h1>
      <form>
        <p class="my-2" v-if="err">{{ err }}</p>
        <v-text-field v-model="login" label="Username" required></v-text-field>
        <v-text-field type="password" v-model="password" label="Password" required></v-text-field>
        <v-btn class="mr-4" @click="submit" color="primary" dark>Register</v-btn>
        <p class="my-2">Got an account? <router-link to="/auth">Login</router-link></p>
      </form>
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
      err: ''
    }
  },
  methods: {
    submit () {
      if (this.login && this.password) {
        this.axios
          .post(`http://${window.location.hostname}:8000/api/auth/users/`, { 'username': this.login, 'password': this.password })
          .then(response => { this.$router.push('/auth') })
          .catch(err => { console.error(err); this.err = err })
      }
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
