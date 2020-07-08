<template>
  <mu-container>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
    <mu-appbar style="width: 100%;" color="#8B4513">
      <mu-menu slot="left" v-if="auth">
        <mu-button flat icon>
          <mu-icon value="menu"></mu-icon>
        </mu-button>
        <mu-list slot="content">
          <mu-list-item button>
            <mu-list-item-content>
              <mu-list-item-title>Читатели</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button @click="goBooks()">
            <mu-list-item-content>
              <mu-list-item-title>Книги</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
        </mu-list>
      </mu-menu>
      Сайт библиотеки на Vue.js
      <mu-button v-if="!auth" @click="goLogin" flat slot="right">Вход</mu-button>
      <mu-button v-else @click="logout" flat slot="right">Выход</mu-button>
    </mu-appbar>
    <reader v-if="auth" class="reader-class"></reader>
  </mu-container>
</template>

<script>
import Reader from '../components/readers/Reader'
// eslint-disable-next-line
// import Reader_books from '../components/readers/Reader_books'

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
    },
    goBooks () {
      this.$router.push({'name': 'books'})
    }
  }
}
</script>

<style scoped>
  .reader-class {
    margin-bottom: 10px;
  }
</style>
