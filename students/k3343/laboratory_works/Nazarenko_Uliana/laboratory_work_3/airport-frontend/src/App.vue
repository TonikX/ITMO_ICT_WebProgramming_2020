<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="primary">
      <b-navbar-brand to="/">Аэропорт</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/challenger">Отправить резюме</b-nav-item>
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
.nav-link {
  color: #fff !important;
}
</style>
