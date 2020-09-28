<template>
  <v-app id="app">
    <v-navigation-drawer v-model="drawer" color="black" dark app>
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
    <v-app-bar color="black" dense dark app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="headline">
        <v-icon>mdi-newspaper</v-icon> Chicken Chicken Chicken: Chicken Chicken
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
        { title: 'Home', icon: 'mdi-laptop', link: '/' },
        { title: 'Workers', icon: 'mdi-hammer', link: '/workers' },
        { title: 'Login', icon: 'mdi-key', link: '/auth' },
        { title: 'Register', icon: 'mdi-pencil', link: '/register' },
        { title: 'Cages', icon: 'mdi-pound-box-outline', link: '/cages' },
        { title: 'Chickens', icon: 'mdi-food-drumstick', link: '/chickens' },
        { title: 'Reports', icon: 'mdi-book', link: '/reports'},
        { title: 'Queries', icon: 'mdi-chart-bar-stacked' },
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
