<template>
  <div>
    <input v-model="login" type="text" placeholder="Логин"/>
    <input v-model="password" type="password" placeholder="Пароль"/>
    <button @click="doLogin">Войти</button>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Login',
  data () {
    return {
      login: '',
      password: ''
    }
  },
  methods: {
    doLogin () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/token/login/',
        type: 'POST',
        data: {
          username: this.login,
          password: this.password
        },
        success: (response) => {
          alert('Вы успешно вошли')
          sessionStorage.setItem('auth_token', response.data.attributes.auth_token)
          this.$router.push({name: 'home'})
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Логин или пароль не верен')
          }
          console.log(response)
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
