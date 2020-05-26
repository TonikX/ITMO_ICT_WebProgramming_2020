<template>
<div>

<input v-model="login.username" type="text" placeholder="Логин"/>
  <input v-model="login.password" type="password" placeholder="Пароль"/>
  <button @click="setLogin()">Войти</button>

</div>
</template>

<script>
export default {
  name: 'Login',
  data(){
    return{
      login: {
        username: '',
        password: '',
      }
    }
  },
  methods:{

    setLogin() {
      this.$axios.post("http://127.0.0.1:8000/auth/token/login", this.login )
      .then(response =>{
        console.log(response.data.auth_token)
          let auth_token = response.data.auth_token;
          localStorage.setItem('auth_token', auth_token);
          alert("Спасибо, что с нами!");
        this.$router.push({name: "home"})})
    }
}}
</script>


<style scoped>

</style>
