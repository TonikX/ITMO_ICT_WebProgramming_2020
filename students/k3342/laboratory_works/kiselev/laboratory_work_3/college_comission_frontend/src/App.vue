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
      </v-list>
    </v-navigation-drawer>
    <v-app-bar color="primary lighten-2" dense dark app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="headline">
        <v-icon>mdi-school</v-icon> Приёмная комиссия
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
        { title: 'Все заявления', icon: 'mdi-account-box-multiple', link: '/' },
        { title: 'Подача заявления', icon: 'mdi-circle-edit-outline', link: '/new' },
        { title: 'Топ абитуриентов', icon: 'mdi-align-vertical-bottom', link: '/top/' }
      ],
      drawer: false
    }
  }
}

</script>
<style>
</style>
