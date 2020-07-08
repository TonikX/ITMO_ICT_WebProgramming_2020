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
        <div>Доктор</div>
        <div>Дата</div>
        <div>Цена</div>
        <div>Оплачено</div>
      </div>
      <div v-for="transaction in transactions" :key="transaction.id" class="flex-table">
        <div>
          <div v-if="tagEditingId == transaction.id">
            <mu-text-field v-model="form.patients"></mu-text-field>
          </div>
          <div v-else>
            {{ transaction.patients }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == transaction.id">
            <mu-text-field v-model="form.doctor"></mu-text-field>
          </div>
          <div v-else>
            {{ transaction.doctor }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == transaction.id">
            <mu-text-field v-model="form.date"></mu-text-field>
          </div>
          <div v-else>
            {{ transaction.date }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == transaction.id">
            <mu-text-field v-model="form.price"></mu-text-field>
          </div>
          <div v-else>
            <div>{{ transaction.price }}</div>
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == transaction.id">
            <mu-text-field v-model="form.paid"></mu-text-field>
          </div>
          <div v-else>
            <div>{{ transaction.paid }}</div>
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == transaction.id">
            <mu-button v-on:click="cancelEditing" color="error">Отмена</mu-button>
          </div>
          <div v-else>
            <mu-button v-on:click="setEditing(transaction)" color="info" >Изменить</mu-button>
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == transaction.id">
            <mu-button @click="sendEdits" color="success">Готово</mu-button>
          </div>
          <div v-else>
            <mu-button v-on:click="deleteRow(transaction)" color="error">Удалить</mu-button>
          </div>
        </div>
      </div>
    </div>
    <mu-paper :z-depth="2" v-if="!add">
      <mu-row gutter>
        <mu-col>
          <mu-select label="Пациент" v-model="addForm.patients" full-width>
            <mu-option v-for="client in clients" :key="client.id" :label="client.surname" :value="client.id">
            </mu-option>
          </mu-select>
        </mu-col>
      </mu-row>
      <mu-row gutter>
        <mu-col>
          <mu-select label="Доктор" v-model="addForm.doctor" full-width>
            <mu-option v-for="doctor in doctors" :key="doctor.id" :label="doctor.surname" :value="doctor.id">
            </mu-option>
          </mu-select>
        </mu-col>
      </mu-row>
      <mu-text-field placeholder="Дата" solo full-width class="demo-divider-form" v-model="addForm.date"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Цена" solo full-width class="demo-divider-form" v-model="addForm.price"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Оплачено" solo full-width class="demo-divider-form" v-model="addForm.paid"></mu-text-field>
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
    name: "Transactions",
    data() {
      return {
        tagEditingId: "",
        form: {
          patients: '',
          doctor: '',
          date: '',
          price: '',
          paid: '',

        },
        addForm: {
          patients: '',
          doctor: '',
          date: '',
          price: '',
          paid: '',
        },
        value1: '',
        value2: '',
        value3: '',
        value4: '',
        value5: '',
        value6: '',
        value7: '',
        value8: '',
        transactions: "",
        clients: "",
        doctors: "",
        add: true,
        edit: false,
        normal: {
          patients: '',
          value2: '',
          value3: '',
          value4: 'Option 1',
          value5: 'Option 2'
        }
      };
    }, created() {
      this.showTransactions()
      this.showClients()
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
      showTransactions() {
        $.ajax({
          url: "http://127.0.0.1:8000/transaction/",
          type: "GET",
          success: (response) => {
            this.transactions = response
            console.log(this.transactions)
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
      setEditing(transaction){
        this.tagEditingId = transaction.id;
        this.edit = true;
      },
      cancelEditing(){
        this.tagEditingId = "";
        this.edit = false;
      },
      sendEdits(){
        this.edit = false
        $.ajax({
          url: "http://127.0.0.1:8000/transaction/" + this.tagEditingId + "/",
          type: "PUT",
          data: {
            patients: this.form.patients,
            doctor: this.form.doctor,
            date: this.form.date,
            price: this.form.price,
            paid: this.form.paid,
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
          url: "http://127.0.0.1:8000/transaction/",
          type: "POST",
          data: {
            patients: this.addForm.patients,
            doctor: this.addForm.doctor,
            date: this.addForm.date,
            price: this.addForm.price,
            paid: this.addForm.paid,
          },

          success: (response) => {
            console.log(response)
          },
        }),
          this.tagEditingId = "";
        this.edit = false;
      },
      deleteRow(transaction){
        $.ajax({
          url: "http://127.0.0.1:8000/transaction/" + transaction.id + "/",
          type: "DELETE",

          success: (response) => {
            console.log(response)
          },
        })
      },
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
      showDoctors() {
        $.ajax({
          url: "http://127.0.0.1:8000/doctor/",
          type: "GET",
          success: (response) => {
            this.doctors = response
            console.log(this.doctors)
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
