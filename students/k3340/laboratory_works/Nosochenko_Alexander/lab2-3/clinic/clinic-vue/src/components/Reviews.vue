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
        <div>Информация о посещении</div>
        <div>Комментарий</div>
      </div>
      <div v-for="revieew in reviews" :key="revieew.id" class="flex-table">
        <div>
          <div v-if="tagEditingId == revieew.id">
            <mu-text-field v-model="form.reception"></mu-text-field>
          </div>
          <div v-else>
            {{ revieew.reception.doctor }} {{ revieew.reception.patients }} {{ revieew.reception.date }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == revieew.id">
            <mu-text-field v-model="form.review"></mu-text-field>
          </div>
          <div v-else>
            {{ revieew.review }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == revieew.id">
            <mu-button v-on:click="cancelEditing" color="error">Отмена</mu-button>
          </div>
          <div v-else>
            <mu-button v-on:click="setEditing(revieew)" color="info" >Изменить</mu-button>
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == revieew.id">
            <mu-button @click="sendEdits" color="success">Готово</mu-button>
          </div>
          <div v-else>
            <mu-button v-on:click="deleteRow(revieew)" color="error">Удалить</mu-button>
          </div>
        </div>
      </div>
    </div>
    <mu-paper :z-depth="2" v-if="!add">
      <mu-row gutter>
        <mu-col>
          <mu-select label="Информация" v-model="addForm.reception" full-width>
            <mu-option v-for="reception in receptions" :key="reception.id" :label="reception.doctor + ' ' + reception.patients + ' ' + reception.date" :value="reception.id">
            </mu-option>
          </mu-select>
        </mu-col>
      </mu-row>
      <mu-text-field placeholder="Комментарий" solo full-width class="demo-divider-form" v-model="addForm.review"></mu-text-field>
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
    name: "Reviews",
    data() {
      return {
        tagEditingId: "",
        form: {
          reception: '',
          review: '',

        },
        addForm: {
          reception: '',
          review: '',
        },
        value1: '',
        value2: '',
        value3: '',
        value4: '',
        value5: '',
        value6: '',
        value7: '',
        value8: '',
        reviews: "",
        clients: "",
        doctors: "",
        receptions: "",
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
      this.showReviews()
      this.showReceptions()
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
      showReviews() {
        $.ajax({
          url: "http://127.0.0.1:8000/reviews/",
          type: "GET",
          success: (response) => {
            this.reviews = response
            console.log(this.reviews)
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
      setEditing(reception){
        this.tagEditingId = reception.id;
        this.edit = true;
      },
      cancelEditing(){
        this.tagEditingId = "";
        this.edit = false;
      },
      sendEdits(){
        this.edit = false
        $.ajax({
          url: "http://127.0.0.1:8000/reviews/" + this.tagEditingId + "/",
          type: "PUT",
          data: {
            reception: this.form.reception,
            review: this.form.review,
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
          url: "http://127.0.0.1:8000/reviews/",
          type: "POST",
          data: {
            reception: this.addForm.reception,
            review: this.addForm.review,
          },

          success: (response) => {
            console.log(response)
          },
        }),
          this.tagEditingId = "";
        this.edit = false;
      },
      deleteRow(review){
        $.ajax({
          url: "http://127.0.0.1:8000/reviews/" + review.id + "/",
          type: "DELETE",

          success: (response) => {
            console.log(response)
          },
        })
      },
      showReceptions() {
        $.ajax({
          url: "http://127.0.0.1:8000/reception/",
          type: "GET",
          success: (response) => {
            this.receptions = response
            console.log(this.receptions)
          },
        })
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
    grid-template-columns: repeat(auto-fill, 25%);
    padding: 10px;
    border-bottom: 1px #000000 solid;
  }


</style>
