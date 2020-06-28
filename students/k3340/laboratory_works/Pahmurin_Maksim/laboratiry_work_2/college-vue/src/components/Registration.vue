<template xmlns="http://www.w3.org/1999/html">
  <mu-container>

    <mu-appbar style="width: 100%;"  color="primary">

      Твоя любимая шарага

    </mu-appbar>
 <mu-paper class="demo-paper" :z-depth="5">
    <mu-form class="mu-demo-form">
      <mu-form-item prop="username">
        <mu-text-field style="margin-top: 20px;" v-model="login" type="text" placeholder="Логин"></mu-text-field>
      </mu-form-item>
      <mu-form-item prop="username">
        <mu-text-field v-model="password" type="password" placeholder="Пароль"></mu-text-field>
      </mu-form-item>
      <mu-form-item prop="username">
        <mu-text-field  type="password" placeholder="Повторите пароль"></mu-text-field>
      </mu-form-item>
      <mu-button style="margin-bottom: 20px;" @click="setLogin">Регистрация</mu-button>
    </mu-form>
   </mu-paper>
  </mu-container>
</template>
<script>

  import $ from 'jquery'

  export default {
    name: "Login",
    data() {
      return {
        login: '',
        password: '',
      }
    },
    methods: {
      setLogin() {
        $.ajax({
          url: "http://127.0.0.1:8000/auth/users/",
          type: "POST",
          data: {
            username: this.login,
            password: this.password
          },
          success: (response) => {
            this.$router.push({name: "login"})

          },
          error: (response) => {
            if (response.status === 400) {
              alert("Логин или пароль не введен")
            }
          }
        })
      },
    }
  }
</script>

<style scoped>

  .mu-demo-form {
    width: 100%;
    max-width: 460px;
   margin-left: auto;
    margin-right: auto;

  }



</style>
