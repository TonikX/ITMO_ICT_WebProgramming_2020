<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      Сайт клиники на Vue.js
      <mu-button flat slot="right" v-if="!auth" @click="goLogin">Вход</mu-button>
      <mu-button  flat slot="right" v-else @click="logout">Выход</mu-button>
    </mu-appbar>
    </mu-container>
</template>

<script>
    export default {
        name: "Home",
        computed: {
          auth() {
            if(sessionStorage.getItem("auth_token")){
              return true
            }
          }

        },
        methods: {
          goLogin() {
            this.$router.push({name: "login"})
          },
          logout(){
            sessionStorage.removeItem("auth_token")
            window.location = "/"
          }
        }
    }
</script>

<style scoped>

</style>
