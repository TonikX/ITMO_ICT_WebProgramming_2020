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
        <div>Имя</div>
        <div>Фамилия</div>
        <div>Номер телефона</div>
      </div>
      <div v-for="client in clients" :key="client.id" class="flex-table">
        <div>
          <div v-if="tagEditingId == client.id">
            <mu-text-field v-model="form.name"></mu-text-field>
          </div>
          <div v-else>
            {{ client.name }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == client.id">
            <mu-text-field v-model="form.surname"></mu-text-field>
          </div>
          <div v-else>
            {{ client.surname }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == client.id">
            <mu-text-field v-model="form.phone"></mu-text-field>
          </div>
          <div v-else>
            {{ client.phone }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == client.id">
            <mu-button v-on:click="cancelEditing" color="error">Отмена</mu-button>
          </div>
          <div v-else>
            <mu-button v-on:click="setEditing(client)" color="info" >Изменить</mu-button>
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == client.id">
            <mu-button @click="sendEdits" color="success">Готово</mu-button>
          </div>
          <div v-else>
            <mu-button v-on:click="deleteRow(client)" color="error">Удалить</mu-button>
          </div>
        </div>
      </div>
    </div>
    <mu-paper :z-depth="2" v-if="!add">
      <mu-text-field placeholder="Имя" solo full-width class="demo-divider-form" v-model="addForm.name"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Фамилия" solo full-width class="demo-divider-form" v-model="addForm.surname"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Номер телефона" solo full-width class="demo-divider-form" v-model="addForm.phone"></mu-text-field>
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
        name: "Patients",
      data() {
        return {
          tagEditingId: "",
          form: {
            name: '',
            surname: '',
            phone: '',
          },
          addForm: {
            name: '',
            surname: '',
            phone: '',
          },
          value1: '',
          value2: '',
          value3: '',
          value4: '',
          value5: '',
          value6: '',
          value7: '',
          value8: '',
          clients: "",
          add: true,
          edit: false,
        };
      },
        computed: {
          auth() {
            if(sessionStorage.getItem("auth_token")){
              return true
            }
          },
        },
        created() {
          this.showClients()
          $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
          })
        },
        methods: {
          showClients() {
            $.ajax({
              url: "http://127.0.0.1:8000/client/",
              type: "GET",
              success: (response) => {
                this.clients = response
                console.log(this.clients)
              },
            })
          },
          setEditing(client){
            this.tagEditingId = client.id;
            this.edit = true;
          },
          cancelEditing(){
            this.tagEditingId = "";
            this.edit = false;
          },
          sendEdits(){
            this.edit = false
            $.ajax({
              url: "http://127.0.0.1:8000/client/" + this.tagEditingId + "/",
              type: "PUT",
              data: {
                name: this.form.name,
                surname: this.form.surname,
                phone: this.form.phone,
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
              url: "http://127.0.0.1:8000/client/",
              type: "POST",
              data: {
                name: this.addForm.name,
                surname: this.addForm.surname,
                phone: this.addForm.phone,
              },

              success: (response) => {
                console.log(response)
              },
            }),
              this.tagEditingId = "";
            this.edit = false;
          },
          deleteRow(client){
            $.ajax({
              url: "http://127.0.0.1:8000/client/" + client.id + "/",
              type: "DELETE",

              success: (response) => {
                console.log(response)
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
        }
    }
</script>

<style scoped>
  .demo-divider-form {
    padding: 0 16px;
  }
  .flex-table{
    display: grid;
    grid-template-columns: repeat(auto-fill, 20%);
    padding: 10px;
    border-bottom: 1px #000000 solid;
  }
</style>
