<template>
  <div id="app">
<mu-container>
        <mu-appbar style="width: 100%;" color="indigo400">
            <mu-menu slot="left">
                <mu-button flat> Меню
                </mu-button>
                <mu-list slot="content">
                    <mu-list-item button href="/">
                        <mu-list-item-title>Главная страница</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/vacancy">
                        <mu-list-item-title>Вакансии</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/klass">
                        <mu-list-item-title>Классы</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/pupils">
                        <mu-list-item-title>Ученики школы</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/subjects">
                        <mu-list-item-title>Дисциплины</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/cabinets">
                        <mu-list-item-title>Кабинеты</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/query">
                        <mu-list-item-title>Запросы</mu-list-item-title>
                    </mu-list-item>
                </mu-list>
            </mu-menu>
            <mu-row align="center">
            <mu-col span="11">
                    <h4>Биржа труда</h4>
                </mu-col>
            </mu-row>
            <mu-button flat slot="right" v-if="!auth" @click="goLogin">LOGIN</mu-button>
            <mu-button flat slot="right" v-else @click="logout">LOGOUT</mu-button>
        </mu-appbar>
    </mu-container>
    <router-view/>
  </div>
</template>

<script>
  export default {
    name: "Navbar",
    components: {
    },
    computed: {
      auth() {
        if (sessionStorage.getItem("auth_token")) {
          return true
        }
      }
    },
    methods: {
      goLogin() {
        this.$router.push({name: "login"})
      },
      logout() {
        sessionStorage.removeItem("auth_token")
        document.location.href = "http://localhost:8080/login";
      },
    }
  }
</script>

<style scoped>
</style>