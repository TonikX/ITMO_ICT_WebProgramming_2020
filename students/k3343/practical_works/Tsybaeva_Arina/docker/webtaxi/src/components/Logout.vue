<template>
  <main class="pa-2">
    <div>
      <h1 align="center">Вы вышли из системы!</h1>
      <section>
        <h2 align="center"><v-btn @click="logIn()" color="success">Войти</v-btn> </h2>
      </section>
    </div>
  </main>
</template>

<script>
    export default {
        name: "Logout",
      mounted() {
        let token = localStorage.getItem('auth_token');
        console.log(token);
        this.$axios.get("http://127.0.0.1:8000/logout?api_token="+token, {headers: {'Authorization' : "Token "+token}})
      },
      methods: {
          logIn() {
            this.$router.push({name:'login'})
          }
      }
    }
</script>

<style scoped>
 h2,h1 { padding: 10px;}
section{
  padding: 10px;
}
</style>
