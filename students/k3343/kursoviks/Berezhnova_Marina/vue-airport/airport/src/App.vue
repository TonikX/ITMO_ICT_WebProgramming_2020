<template>
  <v-app id="app">
    <v-navigation-drawer v-model="drawer" class="primary" dark app>
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
    <v-app-bar color="primary" dense dark app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="headline">
        <v-icon>mdi-airplane-takeoff</v-icon> Airport
      </v-toolbar-title>
    </v-app-bar>
    <v-content>
      <v-container fluid>
        <router-view />
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
        { title: 'Все рейсы', icon: 'mdi-earth', link: '/' },
        { title: 'Хочу работать', icon: 'mdi-send', link: '/challenger' }
      ],
      drawer: false
    }
  },
  mounted () {
    if (localStorage.getItem('username') && localStorage.getItem('token')) {
      this.items.push({ title: 'Кабинет', icon: 'mdi-pencil', link: '/cabinet' })
      return
    }

    this.items.push({ title: 'Вход', icon: 'mdi-key', link: '/login' })
    this.items.push({ title: 'Регистрация', icon: 'mdi-pencil', link: '/register' })
  }
}

</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
