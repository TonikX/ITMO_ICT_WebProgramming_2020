<template>

  <mu-container>

    <mu-appbar style="width: 100%;"  color="indigo400" align="center">

      Биржа труда

    </mu-appbar>
 <mu-paper class="demo-paper" :z-depth="5">
    <mu-form class="mu-demo-form">
      <mu-form-item prop="username">
        <mu-text-field style="margin-top: 20px;" v-model="username" type="text" placeholder="Логин"></mu-text-field>
      </mu-form-item>
      <mu-form-item prop="username">
        <mu-text-field v-model="password" type="password" placeholder="Пароль"></mu-text-field>
      </mu-form-item>
      <mu-button style="margin-bottom: 20px;" @click="setLogin">Войти</mu-button>
      <mu-button style="margin-bottom: 20px;" @click="reg">Регистрация</mu-button>
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
        username: '',
        password: '',
      }
    },
    methods: {
      setLogin() {
        $.ajax({
          url: "http://127.0.0.1:8000/auth",
          type: "POST",
          data: {
            username: this.username,
            password: this.password
          },
          success: (response) => {
            sessionStorage.setItem("access", response.access);
            this.$router.push({name: "home"})
          },
          error: (response) => {
            if (response.status === 400) {
              alert("Логин или пароль не верен")
            }
          }
        })
      },
      reg() {
        document.location.href = "http://localhost:8080/registration";
      }
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