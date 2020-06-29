<template>
  <v-app id="app">
    <v-navigation-drawer v-model="drawer" class="pink darken-4" dark app>
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
    <v-app-bar color="pink darken-4" dense dark app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="headline">
      <v-icon>mdi-palette-advanced</v-icon> LUCH Marketing
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
        { title: 'Главная', icon: 'mdi-palette-swatch', link: '/' },
        { title: 'Личный кабинет', icon: 'mdi-emoticon', link: '/Cabinet' },
        { title: 'Для админа', icon: 'mdi-emoticon-cool', link: '/adminCab' }
      ],
      drawer: false
    }
  }
}
</script>
<style scoped>
</style>
