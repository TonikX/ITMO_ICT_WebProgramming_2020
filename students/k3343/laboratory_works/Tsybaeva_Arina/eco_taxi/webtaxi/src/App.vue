<template>
  <v-app id="app">
    <v-navigation-drawer v-model="drawer" class="green" dark app>
      <v-list>
        <v-list-item v-for="item in items" :key="item.title" link :to="item.link">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
          <div class="pa-2">
            <v-btn block color="green lighten-2" @click="goLogin()">Login</v-btn>
          </div>
          <div class="pa-2">
            <v-btn block color="green lighten-2" @click="goLogout()">Logout</v-btn>
          </div>
          <div class="pa-2">
            <v-btn block color="green lighten-2" @click="goRegister()">Register</v-btn>
          </div>
    </v-navigation-drawer>
    <v-app-bar color="green" dense dark app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="headline">
        <v-icon>mdi-tree</v-icon> Эко Такси
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu left bottom>
        <v-list>
        </v-list>
      </v-menu>
    </v-app-bar>
    <!-- Sizes your content based upon application components -->
    <v-content>
      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>
<script>
export default {
  name: 'App',
  data () {
    return {
      items: [
        { title: 'Главная', icon: 'mdi-earth', link: '/' },
        { title: 'Сделать заказ', icon: 'mdi-account-box', link: '/order' },
        { title: 'Наши водители', icon: 'mdi-car', link: '/drivers' },
        { title: 'Склад', icon: 'mdi-home-city-outline', link: '/storage' },
        { title: 'Отчет', icon: 'mdi-file', link: '/report' }
      ],
      drawer: false
    }
  },
  methods:{
      goLogin() {
      this.$router.push({name:"login"})
    },
    goRegister() {
        this.$router.push({name:'Register'})
    },
    goLogout() {
        this.$router.push({name:'Logout'})
    }
}}
</script>
<style>
#app {
  color: #2c3e50;
}
</style>
