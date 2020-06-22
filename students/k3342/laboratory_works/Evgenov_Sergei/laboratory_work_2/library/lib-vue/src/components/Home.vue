<template>
  <div>
    <h2>Сайт библиотеки на Vue.js</h2>
    <button v-if="!auth" @click="goLogin">Вход</button>
    <button v-else @click="logout">Выход</button>

    <reader v-if="auth"></reader>
  </div>
</template>

<script>
import Reader from '../components/Reader'

export default {
  name: 'Home',
  components: {
    Reader
  },
  computed: {
    auth () {
      if (sessionStorage.getItem('auth_token')) {
        return true
      }
    }
  },
  methods: {
    goLogin () {
      this.$router.push({name: 'login'})
    },
    logout () {
      sessionStorage.removeItem('auth_token')
      window.location = '/'
    }
  }
}
</script>

<style scoped>

</style>
