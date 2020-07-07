<template>
  <mu-container>
  <mu-row>
    <h3>Расписание уборок</h3>
    <div v-for="d in days" :key="d">
      <ul>
        <li>День: {{d}}</li>
      </ul>
      <div v-for="cl in cleanings">
      <ul>
        <li v-if="cl.day_of_week===d"> Этаж: {{cl.floor}}</li>
      </ul>
        </div>
    </div>
    </mu-row>

    <mu-row>
      <mu-button round v-if="!show" @click="SOtchets">Показать отчеты</mu-button>
      <mu-button round v-if="show" @click="HOtchets">Скрыть отчеты</mu-button>
    </mu-row>
    <mu-row v-if="show"><h3>Отчеты об уборках</h3></mu-row>
    <mu-row>
    <mu-card v-if="show" v-for="d in days" :key="d">
      <mu-card-header> День: {{d}} </mu-card-header>
      <div class="otchets" v-for="otchet in otchets" :key="otchet.id">
        <mu-col v-if="otchet.day_of_week===d">
          <mu-row>Дата: {{otchet.date}}</mu-row>
          <mu-row>Этаж: {{otchet.floor}}</mu-row>
          <mu-row>Статус: {{otchet.status}}</mu-row>
          <mu-row>Комментарий</mu-row>
          <mu-row>{{otchet.text}}</mu-row>
          <mu-row><br></mu-row>
        </mu-col>
      </div>

    </mu-card>
  </mu-row>


  </mu-container>
</template>

<script>
  import $ from 'jquery'
    export default {
      name: "Timetable",
      props: ['worker'],
      data() {
          return {
            cleanings: '',
            days: ['Пон', 'Вт', 'Ср', 'Чт','Пт', 'Сб', 'Вс'],
            otchets: '',
            show: false,
          }
        },
        created() {
          $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
          });
          this.loadCleanings();
          this.ShowOtchets();
        },
        methods: {
          loadCleanings() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/cleanings/" + this.worker,
              type: "GET",
              success: (response) => {
                console.log(response);
                this.cleanings = response.data.data
              }
            })
          },
          ShowOtchets() {
            $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            $.ajax({
                  url: "http://127.0.0.1:8000/app/hotel/otchets/" + this.worker,
                  type: "GET",
                  success: (response) => {
                    console.log(response);
                    this.otchets = response.data.data;
                  }
                })
          },
          SOtchets() {
            this.show = true
          },
          HOtchets() {
            this.show = false
          },
        }
    }
</script>

<style scoped>

</style>
