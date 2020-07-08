<template>
  <main>
    <h2 class="text-center mt-2 mb-2">Вход</h2>
    <div class="d-flex flex-column">
      <div class="filter d-flex flex-row w-50 mr-auto ml-auto">
        <div class="m-auto w-100">
          <b-form>
            <div class="m-1">
              <label for="username">Имя пользователя</label>
              <b-form-input id="username" v-model="username"></b-form-input>
            </div>
            <div class="m-1">
              <label for="password">Пароль</label>
              <b-form-input id="password" type="password" v-model="password"></b-form-input>
            </div>
            <b-button class="m-1" variant="info" @click="login()">Вход</b-button>
          </b-form>
          <p class="m-1 mt-2">
            Ещё не зарегистрированы? <router-link to="/register">Регистрация</router-link>
          </p>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
  export default {
    name: 'Login',
    data () {
      return {
        username: '',
        password: ''
      }
    },
    mounted () {
      if (sessionStorage.getItem('username') && sessionStorage.getItem('token')) {
        this.$router.push('/cabinet')
      }
    },
    methods: {
      login () {
        this.axios
          .post(`http://${window.location.hostname}:8000/api/auth/token/`, { username: this.username, password: this.password })
          .then(response => {
            this.setUserInfo(response.data.token, this.username)
          })
      },
      setUserInfo (token, username) {
        this.axios
          .get(`http://${window.location.hostname}:8000/api/get_user_info/?username=${username}`)
          .then(response => {
            sessionStorage.setItem('username', username)
            sessionStorage.setItem('token', token)
            sessionStorage.setItem('user_id', response.data[0].id)
            sessionStorage.setItem('isLogin', true)
            this.$router.push('/cabinet')
          })
      }
    }
  }
</script>
<style></style>
