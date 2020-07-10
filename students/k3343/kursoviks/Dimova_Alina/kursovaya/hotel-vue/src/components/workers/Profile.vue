<template>
  <mu-container>
  <mu-appbar style="width: 100%;" color="primary">
        Кабинет работника
    <mu-button flat @click="addOtch">Добавление отчета</mu-button>
    <mu-button flat @click="Logout">Выход</mu-button>
  </mu-appbar>
  <mu-row>
    <h3></h3>
  </mu-row>
  <mu-row>
    <h3> Расписание уборок </h3>
    <Timetable v-bind:worker="worker_id"></Timetable>
  </mu-row>
  </mu-container>
</template>

<script>
  import $ from 'jquery'
  import Timetable from "../rooms/Timetable";
  export default {
    name: "Profile",
    data() {
      return {
        worker_id: ''
      }
    },
    components: {Timetable},
    methods: {
        goTT() {

        },
        addOtch() {
          this.$router.push({name: "Otchet"})
        },
        Logout() {

        }
      }
    }
</script>

<style scoped>

</style>
