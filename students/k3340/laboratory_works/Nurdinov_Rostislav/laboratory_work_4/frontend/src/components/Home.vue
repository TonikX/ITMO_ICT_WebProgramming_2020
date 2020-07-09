<template>
  <mu-container>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
  </mu-container>
</template>


<script>
  import Navbar from '../components/Navbar';
  export default {
      name: "Home",
    components: {
        Navbar,
    }

  }
</script>
<!--<script>-->
<!--  export default {-->
<!--    name: "Home",-->
<!--    components: {-->
<!--    },-->
<!--    computed: {-->
<!--      auth() {-->
<!--        if (sessionStorage.getItem("auth_token")) {-->
<!--          return true-->
<!--        }-->
<!--      }-->
<!--    },-->
<!--    methods: {-->
<!--      goLogin() {-->
<!--        this.$router.push({name: "login"})-->
<!--      },-->
<!--      logout() {-->
<!--        sessionStorage.removeItem("auth_token")-->
<!--        document.location.href = "http://localhost:8080/login";-->
<!--      },-->
<!--    }-->
<!--  }-->
<!--</script>-->

<!--<style scoped>-->
<!--</style>-->