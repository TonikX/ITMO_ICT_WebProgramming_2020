<template>
  <v-app id="app">
    <v-navigation-drawer v-model="drawer" color="teal darken-3" dark app>
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
    <v-app-bar color="teal darken-1" dense dark app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="headline">
        <v-icon>mdi-bed-outline</v-icon> Отель "Белорусская"
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
        { title: 'Главная', icon: 'mdi-human-male-boy', link: '/' },
        { title: 'Арендовать номер', icon: 'mdi-cash-100', link: '/get_room' },
        { title: 'Для служащих', icon: 'mdi-briefcase', link: '/servant' },
        { title: 'Админка', icon: 'mdi-solar-panel', link: '/admin' },
        { title: 'Работать', icon: 'mdi-bullseye', link: '/new_servant' }
      ],
      drawer: false
    }
  }
}
</script>
<style>
</style>
