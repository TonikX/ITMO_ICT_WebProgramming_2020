<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand to="/">Приёмная комиссия коледжа</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/enrollee/top">Конкурс</b-nav-item>
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
  name: 'App'
}

</script>
<style>
</style>
