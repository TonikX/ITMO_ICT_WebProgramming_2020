<template>
  <mu-container>

    <mu-appbar style="width: 100%;"  color="indigo400" align="center">

      Выполните вход

    </mu-appbar>
 <mu-paper class="demo-paper" :z-depth="5">
    <mu-form class="mu-demo-form">
      <mu-form-item prop="username">
        <mu-text-field style="margin-top: 20px;" v-model="username" type="text" placeholder="Логин"></mu-text-field>
      </mu-form-item>
      <mu-form-item prop="username">
        <mu-text-field v-model="password" type="password" placeholder="Пароль"></mu-text-field>
      </mu-form-item>
      <mu-form-item prop="username">
        <mu-text-field  type="password" placeholder="Повторите пароль"></mu-text-field>
      </mu-form-item>
      <mu-button style="margin-bottom: 20px;" @click="setReg">Регистрация</mu-button>
    </mu-form>
   </mu-paper>
  </mu-container>
</template>
<script>
  import $ from 'jquery'
  export default {
    name: "Registration",
    data() {
      return {
        username: '',
        password: '',
      }
    },
    methods: {
      setReg() {
        $.ajax({
          url: "http://127.0.0.1:8000/register",
          type: "POST",
          data: {
            username: this.username,
            password: this.password
          },
          success: (response) => {
                this.$router.push({name: "ResumeReg"})
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