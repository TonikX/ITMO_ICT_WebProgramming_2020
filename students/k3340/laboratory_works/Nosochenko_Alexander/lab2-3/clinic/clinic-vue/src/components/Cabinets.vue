<template>
  <mu-container>
    <mu-appbar flat style="width: 100%;" color="primary">
      <mu-button href=#/doctors flat slot="left">Доктора</mu-button>
      <mu-button href=#/patients flat slot="left">Пациенты</mu-button>
      <mu-button href=#/medicalrecord flat slot="left">Мед. Карты</mu-button>
      <mu-button href=#/cabinet flat slot="left">Кабинеты</mu-button>
      <mu-button href=#/transactions flat slot="left">Оплата</mu-button>
      <mu-button href=#/reception flat slot="left">Запись</mu-button>
      <mu-button href=#/reviews flat slot="left">Отзывы</mu-button>
      <mu-button flat slot="right" v-if="!auth" @click="goLogin">Вход</mu-button>
      <mu-button flat slot="right" v-else @click="logout">Выход</mu-button>
    </mu-appbar>
    <div>
      <div class="flex-table">
        <div>Ответственный</div>
        <div>Номер кабинета</div>
        <div>Время работы</div>
        <div>Номер телефона</div>
      </div>
      <div v-for="cabinet in cabinets" :key="cabinet.id" class="flex-table">
        <div>
          <div v-if="tagEditingId == cabinet.id">
            <mu-text-field v-model="form.responsible"></mu-text-field>
          </div>
          <div v-else>
            {{ cabinet.responsible }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == cabinet.id">
            <mu-text-field v-model="form.cabinet_number"></mu-text-field>
          </div>
          <div v-else>
            {{ cabinet.cabinet_number }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == cabinet.id">
            <mu-text-field v-model="form.operating_time"></mu-text-field>
          </div>
          <div v-else>
            {{ cabinet.operating_time }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == cabinet.id">
            <mu-text-field v-model="form.telephone"></mu-text-field>
          </div>
          <div v-else>
            <div>{{ cabinet.telephone }}</div>
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == cabinet.id">
            <mu-button v-on:click="cancelEditing" color="error">Отмена</mu-button>
          </div>
          <div v-else>
            <mu-button v-on:click="setEditing(cabinet)" color="info" >Изменить</mu-button>
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == cabinet.id">
            <mu-button @click="sendEdits" color="success">Готово</mu-button>
          </div>
          <div v-else>
            <mu-button v-on:click="deleteRow(cabinet)" color="error">Удалить</mu-button>
          </div>
        </div>
      </div>
    </div>
    <mu-paper :z-depth="2" v-if="!add">
      <mu-text-field placeholder="Ответственный" solo full-width class="demo-divider-form" v-model="addForm.responsible"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Номер кабинета" solo full-width class="demo-divider-form" v-model="addForm.cabinet_number"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Время работы" solo full-width class="demo-divider-form" v-model="addForm.operating_time"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Номер телефона" solo full-width class="demo-divider-form" v-model="addForm.telephone"></mu-text-field>
      <mu-divider></mu-divider>
    </mu-paper>
    <mu-button v-on:click="add = true" v-if="!add" full-width>Отмена</mu-button>
    <mu-divider></mu-divider>
    <mu-button v-on:click="addUser" full-width color="success" v-if="!add">Отправить</mu-button>
    <mu-flex justify-content="center" align-items="center">
      <mu-button v-if="add & auth" v-on:click="add = false" full-width color="primary">Добавить</mu-button>
    </mu-flex>
  </mu-container>
</template>

<script>
  import $ from "jquery";

  export default {
    name: "Cabinets",
    data() {
      return {
        tagEditingId: "",
        form: {
          responsible: '',
          cabinet_number: '',
          operating_time: '',
          telephone: '',
        },
        addForm: {
          responsible: '',
          cabinet_number: '',
          operating_time: '',
          telephone: '',
        },
        value1: '',
        value2: '',
        value3: '',
        value4: '',
        value5: '',
        value6: '',
        value7: '',
        value8: '',
        cabinets: "",
        add: true,
        edit: false,
      };
    }, created() {
      this.showDoctors()
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
      })
    },
    computed: {
      auth() {
        if(sessionStorage.getItem("auth_token")){
          return true
        }
      },

    },
    methods: {
      showDoctors() {
        $.ajax({
          url: "http://127.0.0.1:8000/cabinet/",
          type: "GET",
          success: (response) => {
            this.cabinets = response
            console.log(this.cabinets)
          },


        })
      },
      goLogin() {
        this.$router.push({name: "login"})
      },
      logout(){
        sessionStorage.removeItem("auth_token")
        window.location = "/"
      },
      setEditing(cabinet){
        this.tagEditingId = cabinet.id;
        this.edit = true;
      },
      cancelEditing(){
        this.tagEditingId = "";
        this.edit = false;
      },
      sendEdits(){
        this.edit = false
        $.ajax({
          url: "http://127.0.0.1:8000/cabinet/" + this.tagEditingId + "/",
          type: "PUT",
          data: {
            responsible: this.form.responsible,
            cabinet_number: this.form.cabinet_number,
            operating_time: this.form.operating_time,
            telephone: this.form.telephone,
          },

          success: (response) => {
            console.log(response)
          },
        }),
          this.tagEditingId = "";
        this.edit = false;
      },
      addUser(){
        $.ajax({
          url: "http://127.0.0.1:8000/cabinet/",
          type: "POST",
          data: {
            responsible: this.addForm.responsible,
            cabinet_number: this.addForm.cabinet_number,
            operating_time: this.addForm.operating_time,
            telephone: this.addForm.telephone,
          },

          success: (response) => {
            console.log(response)
          },
        }),
          this.tagEditingId = "";
        this.edit = false;
      },
      deleteRow(cabinet){
        $.ajax({
          url: "http://127.0.0.1:8000/cabinet/" + cabinet.id + "/",
          type: "DELETE",

          success: (response) => {
            console.log(response)
          },
        })
      }
    }
  }
</script>

<style scoped>
  .demo-divider-form {
    padding: 0 16px;
  }
  .flex-table{
    display: grid;
    grid-template-columns: repeat(auto-fill, 16.5%);
    padding: 10px;
    border-bottom: 1px #000000 solid;
  }


</style>
