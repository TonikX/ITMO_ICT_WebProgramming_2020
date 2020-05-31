<template>
  <v-app id="app">
    <v-navigation-drawer v-model="drawer" color="indigo" dark app>
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
    </v-navigation-drawer>
    <v-app-bar color="indigo" dense dark app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="headline">
      <v-icon>mdi-white-balance-sunny</v-icon> ЛУЧ
      </v-toolbar-title>
    </v-app-bar>
    <v-content>
      <v-container fluid>
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
        { title: 'Главная', icon: 'mdi-charity', link: '/' },
        { title: 'Личный кабинет', icon: 'mdi-account-key', link: '/cabinet' },
        { title: 'Кабинет админа', icon: 'mdi-account-lock', link: '/admin' }
      ],
      drawer: false
    }
  }
}
</script>
<style scoped>
</style>
