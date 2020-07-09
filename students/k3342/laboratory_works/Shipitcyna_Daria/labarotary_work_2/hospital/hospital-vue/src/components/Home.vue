<template>
  <mu-container>
      <mu-appbar style="width: 100%;" color="primary">
          Система администрирования клиники
          <mu-button flat slot="right" v-if="!auth" @click="goLogin">Вход</mu-button>
          <mu-button flat slot="right" v-else @click="logout">Выход</mu-button>
          <mu-menu slot="left">
              <mu-button flat>Меню</mu-button>
              <mu-list slot="content">
                  <mu-list-item button @click="goPatient">
                      <mu-list-item-content>
                          <mu-list-item-title>Пациенты</mu-list-item-title>
                      </mu-list-item-content>
                  </mu-list-item>
                  <mu-list-item button @click="goDoctor">
                      <mu-list-item-content>
                          <mu-list-item-title>Врачи</mu-list-item-title>
                      </mu-list-item-content>
                  </mu-list-item>
                   <mu-list-item button @click="goApp">
                      <mu-list-item-content>
                          <mu-list-item-title>Приемы</mu-list-item-title>
                      </mu-list-item-content>
                  </mu-list-item>
                  <mu-list-item button @click="goQueries">
                      <mu-list-item-content>
                          <mu-list-item-title>Запросы</mu-list-item-title>
                      </mu-list-item-content>
                  </mu-list-item>
              </mu-list>
          </mu-menu>
      </mu-appbar>
  </mu-container>

</template>

<script>

    export default {
        name: 'Home',
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
            goPatient() {
                  this.$router.push({name: "patient"})
            },
            goDoctor() {
                  this.$router.push({name: "doctor"})
            },
            goApp() {
                  this.$router.push({name: "apps"})
            },
            goQueries() {
                  this.$router.push({name: "queries"})
            },
            logout() {
                  sessionStorage.removeItem("auth_token")
                  window.location = '/'
            }
        }
    }
</script>

<style scoped>

</style>
