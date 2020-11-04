<template>
  <v-app id="app">
    <v-navigation-drawer v-model="drawer" color="primary lighten-2" dark app>
      <v-list>
        <v-list-item v-for="item in items" :key="item.title" link :to="item.link">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item v-if="!isLogin" to="/auth">
          <v-list-item-icon>
            <v-icon>mdi-key</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Вход</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item v-if="!isLogin" to="/register">
          <v-list-item-icon>
            <v-icon>mdi-pencil</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Регистрация</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item v-if="!isSecretary && isLogin" to="/enrollee">
          <v-list-item-icon>
            <v-icon>mdi-pencil</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Кабинет абитуриента</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item v-if="isSecretary && isLogin" to="/secretary">
          <v-list-item-icon>
            <v-icon>mdi-pencil</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Кабинет секретаря</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item v-if="isLogin" @click="logout">
          <v-list-item-icon>
            <v-icon>mdi-exit-run</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Выход</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar color="primary lighten-2" dense dark app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="headline">
        <v-icon>mdi-school</v-icon> Приёмная комиссия
      </v-toolbar-title>
    </v-app-bar>
    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>
<script>
export default {
  name: 'App',
  data () {
    return {
      items: [
        { title: 'Все заявления', icon: 'mdi-account-box-multiple', link: '/' },
        { title: 'Подача заявления', icon: 'mdi-circle-edit-outline', link: '/new' },
        { title: 'Топ абитуриентов', icon: 'mdi-align-vertical-bottom', link: '/top' }
      ],
      drawer: false
    }
  },
  methods: {
    logout () {
      localStorage.removeItem('token')
      localStorage.removeItem('username')
      localStorage.removeItem('secretary')
      localStorage.removeItem('enrollee')
      this.$router.push('/')
    }
  },
  computed: {
    isLogin () {
      return localStorage.getItem('token')
    },
    isSecretary () {
      return localStorage.getItem('secretary')
    }
  }
}

</script>
<style>
</style>
