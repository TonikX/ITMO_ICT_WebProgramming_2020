<template>
  <v-app id="app">
    <v-navigation-drawer v-model="drawer" class="deep-orange" dark app>
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
    <v-app-bar color="deep-orange" dense dark app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="headline">
        <v-icon>mdi-bed</v-icon> Hotel
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
        // { title: 'Арендовать номер', icon: 'mdi-bed', link: '/room' },
        { title: 'Для служащих', icon: 'mdi-briefcase', link: '/worker' },
        { title: 'Для администратора', icon: 'mdi-solar-panel', link: '/admin' },
        { title: 'Моё резюме', icon: 'mdi-file', link: '/challenger' }
        // { title: 'Как устроиться', icon: 'mdi-newspaper-variant', link: '/challenger' }
      ],
      drawer: false
    }
  }
}

</script>
<style>
</style>
