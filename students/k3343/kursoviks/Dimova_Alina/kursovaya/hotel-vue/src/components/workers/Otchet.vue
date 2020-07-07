<template>
<mu-container>
  <div class="form">
      <mu-form :model="form">
        <mu-form-item label="Дата уборки">
          <label>
            <input type="date" v-model="form.date"></input>
          </label>
        </mu-form-item>

        <mu-form-item label="День недели">
          <mu-select v-model="form.day">
              <mu-option label="Понедельник" value="Пон"></mu-option>
              <mu-option label="Вторник" value="Вт"></mu-option>
              <mu-option label="Среда" value="Ср"></mu-option>
              <mu-option label="Четверг" value="Чт"></mu-option>
              <mu-option label="Пятница" value="Пт"></mu-option>
              <mu-option label="Суббота" value="Сб"></mu-option>
              <mu-option label="Воскресенье" value="Вс"></mu-option>
          </mu-select>
        </mu-form-item>
        <mu-form-item label="Этаж">
          <mu-select v-model="form.floor">
            <mu-option v-for="fl in floors" :key="fl.id" :label="fl.floor_num"
                  :value="fl.id">
            </mu-option>
          </mu-select>
        </mu-form-item>
        <mu-form-item label="Проведена без проблем?">
          <mu-select v-model="form.status">
              <mu-option label="Да" value="Ок"></mu-option>
              <mu-option label="Есть проблемы" value="Пр"></mu-option>
          </mu-select>
        </mu-form-item>
        <mu-form-item label="Комментарий">
          <label>
             <mu-text-field v-model="form.text"></mu-text-field>
          </label>
        </mu-form-item>
        <hr>
       <mu-button class="btn-send" round @click="Add"> Подтвердить добавление</mu-button>
      </mu-form>
    </div>
</mu-container>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Otchet",
        props: ['worker'],
        data() {
          return {
            floors: '',
            form: {
              date: '',
              day: '',
              floor: '',
              status: '',
              text: '',
            }
          }
        },
        created() {
          $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
          });
          this.loadFloors();
        },
        methods: {
          loadFloors() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/floors/",
              type: "GET",
              success: (response) => {
                console.log(response);
                this.floors = response.data.data
              }
            })
          },
          Add() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/otchets/1",
              type: "POST",
              data: {
                worker: this.worker,
                date: this.form.date,
                day_of_week: this.form.day,
                floor: this.form.floor,
                status: this.form.status,
                text: this.form.text
              },
              success: (response) => {
                alert("Отчет добавлен успешно");
                this.$router.push({name: 'W_login'})
              },
              error: (response) => {
                alert("Ошибка при добавлении отчета");
              }
            })
          }
        }
    }
</script>

<style scoped>

</style>
