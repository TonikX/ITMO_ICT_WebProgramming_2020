<template>
  <main>
    <v-col cols="5" class="mx-auto">
      <h1 class="headline">Logged in as: {{ username }}</h1>
    </v-col>
  </main>
</template>
<script>
export default {
  name: 'Home',
  data () {
    return {
      username: ''
    }
  },
  methods: {
  },
  mounted () {
    if (!sessionStorage.getItem('username')) {
      this.$router.push('/auth')
      return
    }

    this.username = sessionStorage.getItem('username')
  }
}
</script>
<style></style>
