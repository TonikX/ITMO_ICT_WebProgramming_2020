<template>
  <main>
    <h2 class="text-center mt-2 mb-2">Регистрация</h2>
    <div class="d-flex flex-column">
      <div class="filter d-flex flex-row w-50 mr-auto ml-auto">
        <div class="m-auto w-100">
          <b-form>
            <div class="m-1">
              <label for="username">Имя пользователя</label>
              <b-form-input id="username" v-model="username"></b-form-input>
            </div>
            <div class="m-1">
              <label for="email">Email</label>
              <b-form-input id="email" type="email" v-model="email"></b-form-input>
            </div>
            <div class="m-1">
              <label for="password">Пароль</label>
              <b-form-input id="password" type="password" v-model="password"></b-form-input>
            </div>
            <b-button class="m-1" variant="info" @click="register()">Регистрация</b-button>
          </b-form>
          <p class="m-1 mt-2">
            Уже зарегистрированы? <router-link to="/login">Вход</router-link>
          </p>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
  export default {
    name: 'Register',
    data () {
      return {
        username: '',
        password: '',
        email: ''
      }
    },
    mounted () {
      if (sessionStorage.getItem('username') && sessionStorage.getItem('token')) {
        this.$router.push('/cabinet')
      }
    },
    methods: {
      register () {
        this.axios
          .post(`http://${window.location.hostname}:8000/api/auth/users/`, { username: this.username, password: this.password, email: this.email })
          .then(response => {
            console.log(response.data)
            this.$router.push('/login')
          })
      }
    }
  }
</script>
<style></style>
