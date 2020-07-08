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
        <div>Пациент</div>
        <div>Заболевание</div>
        <div>Дата посещения</div>
        <div>Диагноз</div>
        <div>Рекомендации</div>
      </div>
      <div v-for="record in records" :key="record.id" class="flex-table">
        <div>
          <div v-if="tagEditingId == record.id">
            <mu-text-field v-model="form.patient"></mu-text-field>
          </div>
          <div v-else>
            {{ record.patient }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == record.id">
            <mu-text-field v-model="form.diseases"></mu-text-field>
          </div>
          <div v-else>
            {{ record.diseases }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == record.id">
            <mu-text-field v-model="form.date_of_acceptance"></mu-text-field>
          </div>
          <div v-else>
            {{ record.date_of_acceptance }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == record.id">
            <mu-text-field v-model="form.diagnosis"></mu-text-field>
          </div>
          <div v-else>
            <div>{{ record.diagnosis }}</div>
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == record.id">
            <mu-text-field v-model="form.recommendations_for_treatment"></mu-text-field>
          </div>
          <div v-else>
            <div>{{ record.recommendations_for_treatment }}</div>
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == record.id">
            <mu-button v-on:click="cancelEditing" color="error">Отмена</mu-button>
          </div>
          <div v-else>
            <mu-button v-on:click="setEditing(record)" color="info" >Изменить</mu-button>
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == record.id">
            <mu-button @click="sendEdits" color="success">Готово</mu-button>
          </div>
          <div v-else>
            <mu-button v-on:click="deleteRow(record)" color="error">Удалить</mu-button>
          </div>
        </div>
      </div>
    </div>
    <mu-paper :z-depth="2" v-if="!add">
      <mu-text-field placeholder="Пациент" solo full-width class="demo-divider-form" v-model="addForm.patient"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Заболевание" solo full-width class="demo-divider-form" v-model="addForm.diseases"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Дата посещения" solo full-width class="demo-divider-form" v-model="addForm.date_of_acceptance"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Диагноз" solo full-width class="demo-divider-form" v-model="addForm.diagnosis"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Рекомендации" solo full-width class="demo-divider-form" v-model="addForm.recommendations_for_treatment"></mu-text-field>
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
    name: "Records",
    data() {
      return {
        tagEditingId: "",
        form: {
          patient: '',
          diseases: '',
          date_of_acceptance: '',
          diagnosis: '',
          recommendations_for_treatment: '',
        },
        addForm: {
          patient: '',
          diseases: '',
          date_of_acceptance: '',
          diagnosis: '',
          recommendations_for_treatment: '',
        },
        value1: '',
        value2: '',
        value3: '',
        value4: '',
        value5: '',
        value6: '',
        value7: '',
        value8: '',
        records: "",
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
          url: "http://127.0.0.1:8000/record/",
          type: "GET",
          success: (response) => {
            this.records = response
            console.log(this.records)
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
      setEditing(record){
        this.tagEditingId = record.id;
        this.edit = true;
      },
      cancelEditing(){
        this.tagEditingId = "";
        this.edit = false;
      },
      sendEdits(){
        this.edit = false
        $.ajax({
          url: "http://127.0.0.1:8000/record/" + this.tagEditingId + "/",
          type: "PUT",
          data: {
            patient: this.form.patient,
            diseases: this.form.diseases,
            date_of_acceptance: this.form.date_of_acceptance,
            diagnosis: this.form.diagnosis,
            recommendations_for_treatment: this.form.recommendations_for_treatment,
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
          url: "http://127.0.0.1:8000/record/",
          type: "POST",
          data: {
            patient: this.addForm.patient,
            diseases: this.addForm.diseases,
            date_of_acceptance: this.addForm.date_of_acceptance,
            diagnosis: this.addForm.diagnosis,
            recommendations_for_treatment: this.addForm.recommendations_for_treatment,
          },

          success: (response) => {
            console.log(response)
          },
        }),
          this.tagEditingId = "";
          this.edit = false;
      },
      deleteRow(record){
        $.ajax({
          url: "http://127.0.0.1:8000/record/" + record.id + "/",
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
    grid-template-columns: repeat(auto-fill, 14%);
    padding: 10px;
    border-bottom: 1px #000000 solid;
  }


</style>
