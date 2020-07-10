<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
        Кабинет работника {{ full_name }}
    <mu-button flat v-if="auth" @click="Logout">Выход</mu-button>
  </mu-appbar>
      <div v-if="!auth" class="login">
        <h2> Войдите в свой аккаунт </h2>
        <mu-text-field v-model="username" label="Логин"></mu-text-field>
        <mu-text-field v-model="password" type="password" label="Пароль"></mu-text-field>
        <mu-button @click="isWorker">Войти</mu-button>
      </div>
    <div v-if="auth">
      <mu-row><p></p></mu-row>
      <Timetable v-if="worker_id" v-bind:worker="worker_id"> </Timetable>
      <hr>
      <mu-button flat v-if="auth&!showOtch" @click="addOtch">Добавление отчета</mu-button>
      <Otchet v-if="showOtch" v-bind:worker="worker_id"> </Otchet>
    </div>
  </mu-container>
</template>

<script>
  import $ from 'jquery'
  import Timetable from "../rooms/Timetable";
  import Otchet from "./Otchet";
  export default {
    name: "W_login",
    data() {
      return {
        show: true,
        auth: false,
        worker_id: '',
        workers: '',
        username: '',
        password: '',
        full_name: '',
        wrks: '',
        showOtch: false,
      }
    },
    components: {Timetable, Otchet},
    methods: {
      setLogin() {
          $.ajax({
              url: "http://127.0.0.1:8000/auth/token/login/",
              type: "POST",
              data: {
                  username: this.username,
                  password: this.password
              },
              success: (response) => {
                    sessionStorage.setItem("auth_token", response.data.attributes.auth_token);
                    this.auth = true;
                    alert("Вы вошли");
                    this.showTT();
              },
              error: (response) => {
                  if (response.status === 400) {
                      alert("Логин или пароль не верен")
                  }
              }
          })
      },
      Logout() {
              sessionStorage.removeItem('auth_token');
              window.location = '/'
            },
      isWorker() {
        $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/users/1",
              type: "GET",
                success: (response) => {
                console.log(response);
                this.workers = response.data.data;
                for (let i = 0; i < this.workers.length; i++) {
                  if (this.workers[i].username === this.username) {
                    this.full_name = this.workers[i].full_name;
                    this.setLogin();
                    return true
                  }
                }
                alert('Вы не являетесь уборщиком');
                sessionStorage.removeItem('auth_token');
                this.$router.push({name: "Home"});
                return false
              }
            })
      },
      showTT() {
        $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
          });
        $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/workers/",
              type: "GET",
              success: (response) => {
                console.log(response);
                this.wrks = response.data;
                for (let i = 0; i < this.wrks.length; i++) {
                  if (this.wrks[i].attributes.full_name === this.full_name) {
                    this.worker_id = this.wrks[i].id;
                    return true
                  }
                }
              }
            })
            },
      addOtch() {
          this.showOtch = true
        },
      },
  }
</script>

<style scoped>

</style>
