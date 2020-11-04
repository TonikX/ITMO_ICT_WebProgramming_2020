<template>
  <v-app id='app'>
    <v-navigation-drawer v-model="drawer" class="light-green darken-4" dark app>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            Меню
          </v-list-item-title>
          <v-list-item-subtitle>
            Добро пожаловать!
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title" link :to="item.link"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      color="light-green darken-4"
      dense
      dark app
    >
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="headline">
        <v-icon>mdi-dog-side</v-icon>
        Yearly Dog Shows
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu
        left
        bottom
      >
      </v-menu>
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
        { title: 'Выставки', icon: 'mdi-view-dashboard', link: '/' },
        { title: 'Участник', icon: 'mdi-account', link: '/login' },
        { title: 'Организатор', icon: 'mdi-account-tie', link: '/orgin' }
      ],
      drawer: false
    }
  }
}
</script>

<style>
#app {

}
</style>
