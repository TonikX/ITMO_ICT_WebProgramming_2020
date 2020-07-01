<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      Сайт библиотеки на Vue.js
    </mu-appbar>
    <mu-container>
      <mu-row>
        <mu-col></mu-col>
        <mu-col align-items="center">
          <mu-flex><hr/></mu-flex>
          <mu-flex justify-content="center">
            Логин: <input v-model="login" type="text" placeholder="Логин"/>
          </mu-flex>
          <mu-flex><hr/></mu-flex>
          <mu-flex justify-content="center">
            Пароль: <input v-model="password" type="password" placeholder="Пароль"/>
          </mu-flex>
          <mu-flex><hr/></mu-flex>
          <mu-flex justify-content="center">
            <button @click="doLogin">Войти</button>
          </mu-flex>
        </mu-col>
        <mu-col></mu-col>
      </mu-row>
    </mu-container>
  </mu-container>
</template>

<script>
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
      // eslint-disable-next-line
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
  .flex-wrapper {
    width: 100%;
    height: 56px;
    margin-top: 8px;
  }
</style>
