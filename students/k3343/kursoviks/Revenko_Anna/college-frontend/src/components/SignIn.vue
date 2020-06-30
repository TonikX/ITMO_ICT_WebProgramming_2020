<template>
  <main>
    <div class="content container mt-5">
  	  <h1 class="text-center">Вход абитуриента</h1>
      <div class="d-flex flex-row">
        <div class="m-auto">
          <b-form>
            <div class="m-1">
              <label for="username">Имя пользователя</label>
              <b-form-input id="username" v-model="username" placeholder="Имя пользователя"></b-form-input>
            </div>
            <div class="m-1">
              <label for="password">Пароль</label>
              <b-form-input id="password" v-model="password" type="password" placeholder="Пароль"></b-form-input>
            </div>
            <div class="m-1 mt-4">
              <b-button variant="primary" @click="signin()">Вход</b-button>
            </div>
          </b-form>
          <p class="mb-2 mt-2">Если вы ещё не зарегистрированы, то сделайте это <router-link to="/signup">тут</router-link>.</p>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  name: 'SignIn',
  data () {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    signin () {
      this.axios
        .post(`http://${window.location.hostname}:8005/api/auth/token`, { username: this.username, password: this.password })
        .then(response => { console.log(response); sessionStorage.setItem('token', response.data.token); sessionStorage.setItem('username', this.username); this.$router.push('/application/new') })
        .catch(err => { console.error(err) })
    }
  },
  mounted () {
    if (sessionStorage.getItem('token')) {
      this.$router.push('/application/new')
      return
    }
  }
}
</script>