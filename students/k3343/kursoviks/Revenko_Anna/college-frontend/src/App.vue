<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand to="/">Приёмная комиссия коледжа</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/enrollee/top">Конкурс</b-nav-item>
          <b-nav-item to="/application/new">Подать заявление</b-nav-item>
          <b-nav-item to="/cabinet">Личный кабинет</b-nav-item>
          <b-nav-item to="/signup">Регистрация</b-nav-item>
          <b-nav-item to="/signin">Вход</b-nav-item>
          <b-nav-item @click="signout()">Выход</b-nav-item>
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
  methods: {
    signout () {
      sessionStorage.clear()
      this.$router.push('/')
    }
  }
}

</script>
<style>
</style>
