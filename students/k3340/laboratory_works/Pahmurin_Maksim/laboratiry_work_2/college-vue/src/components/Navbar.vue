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
      <mu-list-item button @click="record">
        <mu-list-item-content>
          <mu-list-item-title>Журнал</mu-list-item-title>
        </mu-list-item-content>
      </mu-list-item>
      <mu-list-item button>
        <mu-list-item-content>
          <mu-list-item-title>Студенты</mu-list-item-title>
        </mu-list-item-content>
      </mu-list-item>
      <mu-list-item button>
        <mu-list-item-content>
          <mu-list-item-title>Преподаватели</mu-list-item-title>
        </mu-list-item-content>
      </mu-list-item>
    </mu-list>
  </mu-menu>

      Расписание
      <mu-button flat slot="right" v-if="!auth" @click="goLogin">Вход</mu-button>
      <mu-button flat slot="right" v-else @click="logout">Выход</mu-button>
    </mu-appbar>
</mu-container>
</template>

<script>
    export default {
        name: "navbar",
      methods: {
      goLogin() {
        this.$router.push({name: "login"})
      },
      logout() {
        sessionStorage.removeItem("auth_token")
        window.location = "/"
      },
      shedule() {
        window.location = "/"
      },
    }
    }
</script>

<style scoped>

</style>
