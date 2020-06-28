<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="primary">
      <b-navbar-brand to="/">Аэропорт</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item v-for="navItem in navItems" :key="navItem.name" :to="navItem.link">{{ navItem.name }}</b-nav-item>
          <b-nav-item v-if="!isLogin" to="/login">Вход</b-nav-item>
          <b-nav-item v-if="!isLogin" to="/register">Регистрация</b-nav-item>
          <b-nav-item v-if="isLogin" to="/cabinet">Личный кабинет</b-nav-item>
          <b-nav-item v-if="isLogin" to="/tickets">Мои билеты</b-nav-item>
          <b-nav-item v-if="isLogin" @click="logout()">Выход</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <div class="container-fluid mt-2 mb-2">
      <router-view />
    </div>
  </div>
</template>
<script>
export default {
  name: 'App',
  data () {
    return {
      navItems: [
        { link: '/challenger', name: 'Отправить резюме' }
      ],
      isLogin: sessionStorage.getItem('isLogin')
    }
  },
  mounted () {
    if (sessionStorage.getItem('token') && sessionStorage.getItem('username')) {
      this.isLogin = true
    }
  },
  methods: {
    logout () {
      sessionStorage.clear()
      this.isLogin = false
    }
  }
}

</script>
<style>
.nav-link {
  color: #fff !important;
}
</style>
