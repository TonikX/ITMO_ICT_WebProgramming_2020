<template>
  <v-app id="app">
    <v-navigation-drawer v-model="drawer" class="teal" dark app>
      <v-list>
        <v-list-item v-for="item in items" :key="item.title" link :to="item.link">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item @click="logout">
          <v-list-item-icon>
            <v-icon>mdi-location-exit</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Выход</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar color="teal" dense dark app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="headline">
        <v-icon>mdi-hospital-building</v-icon> Hospital
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
        { title: 'Главная', icon: 'mdi-leaf-maple', link: '/' },
        { title: 'Моя медкарта', icon: 'mdi-book-open', link: '/cabinet' },
        { title: 'Запись на приём', icon: 'mdi-circle-edit-outline', link: '/patient/new' },
        { title: 'Ведение приёма', icon: 'mdi-book-open-outline', link: '/doctor/' }
      ],
      drawer: false
    }
  },
  methods: {
    logout () {
      sessionStorage.clear()
      this.$router.push('/')
    }
  }
}

</script>
<style>
</style>
