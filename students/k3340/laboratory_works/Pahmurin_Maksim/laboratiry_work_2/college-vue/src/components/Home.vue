<template>

  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      <mu-menu slot="left">
    <mu-button flat>Меню</mu-button>
    <mu-list slot="content">
      <mu-list-item button @click="shedule">
        <mu-list-item-content>
          <mu-list-item-title>Расписание</mu-list-item-title>
        </mu-list-item-content>
      </mu-list-item>
      <mu-list-item button @click="teachers">
        <mu-list-item-content>
          <mu-list-item-title>Преподаватели</mu-list-item-title>
        </mu-list-item-content>
      </mu-list-item>
      <mu-list-item button @click="students">
        <mu-list-item-content>
          <mu-list-item-title>Студенты</mu-list-item-title>
        </mu-list-item-content>
      </mu-list-item>

       <mu-list-item button @click="record">
        <mu-list-item-content>
          <mu-list-item-title>Журнал</mu-list-item-title>
        </mu-list-item-content>
      </mu-list-item>
    </mu-list>
  </mu-menu>

      Расписание
      <mu-button flat slot="right" v-if="!auth" @click="goLogin">Вход</mu-button>
      <mu-button flat slot="right" v-else @click="logout">Выход</mu-button>
    </mu-appbar>
    <mu-paper class="demo-paper" :z-depth="5">

    <mu-row>
      <room v-if="auth"></room>
    </mu-row>

    </mu-paper>
  </mu-container>
</template>

<script>
  import Room from '@/components/Room.vue'
  import Record from "./Record";

  export default {
    name: "Home",
    components: {
      Record,
      Room
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
        document.location.href = "http://localhost:8080/#/login";
      },
      shedule() {
        document.location.href = "http://localhost:8080/#/";
      },
      record() {
        document.location.href = "http://localhost:8080/#/record";
      },
      students() {
        document.location.href = "http://localhost:8080/#/students";
      },
      teachers() {
        document.location.href = "http://localhost:8080/#/teachers";
      },
    }
  }
</script>

<style scoped>

</style>
