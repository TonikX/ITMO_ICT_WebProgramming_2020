<template>
  <v-app id="app">
    <v-navigation-drawer v-model="drawer" color="brown" dark app>
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
      <template v-slot:append>
        <div class="pa-2">
          <v-btn block @click="logout">Logout</v-btn>
        </div>
      </template>
    </v-navigation-drawer>
    <v-app-bar color="red" dense dark app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="headline">
        <v-icon>mdi-content_paste</v-icon> Library <i>Self-Saving System</i>
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
        { title: 'Home', icon: 'mdi-redo', link: '/' },
        { title: 'Librarian', icon: 'mdi-face', link: '/librarians' },
        { title: 'Book', icon: 'mdi-book', link: '/books' },
        { title: 'Visitor', icon: 'mdi-pencil', link: '/visitors'},
        { title: 'Login', icon: 'mdi-lock', link: '/auth' },
        { title: 'Register', icon: 'mdi-fingerprint', link: '/register' },
      ],
      drawer: true
    }
  },
  methods: {
    logout () {
      sessionStorage.clear()
      this.$router.push('/auth')
    }
  }
}
</script>
<style>
</style>
