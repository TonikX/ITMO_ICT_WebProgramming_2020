<template>
  <div id="app">
<mu-container>
        <mu-appbar class="mu-navbar" style="width: 100%;" color="indigo400">
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
                    <mu-list-item button href="/jobseeker">
                        <mu-list-item-title>Соискатели</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/employer">
                        <mu-list-item-title>Работодатели</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/resume_reg">
                        <mu-list-item-title>Создать резюме</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/application">
                        <mu-list-item-title>Заявки</mu-list-item-title>
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
        if (sessionStorage.getItem("access")) {
          return true
        }
      }
    },
    methods: {
      goLogin() {
        this.$router.push({name: "login"})
      },
      logout() {
        sessionStorage.removeItem("access")
        document.location.href = "http://localhost:8080/login";
      },
    }
  }
</script>

<style scoped>
  .mu-navbar {
    width: 100%;
    margin-left: auto;
    margin-right: auto;
  }
</style>