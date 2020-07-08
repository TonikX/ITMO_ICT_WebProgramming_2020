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
<!--    <mu-paper :z-depth="1" v-if="auth">-->
<!--      <mu-data-table width="600" border :columns="columns" :sort.sync="sort" :data="doctors">-->
<!--        <template slot-scope="scope">-->
<!--          <td class="is-center"><mu-text-field v-show=edit v-model="value1"></mu-text-field><br/><p v-show=!edit>{{scope.row.name}}</p></td>-->
<!--          <td class="is-center"><mu-text-field v-show=edit v-model="value2"></mu-text-field><br/><p v-show=!edit>{{scope.row.surname}}</p></td>-->
<!--          <td class="is-center"><mu-text-field v-show=edit v-model="value3"></mu-text-field><br/><p v-show=!edit>{{scope.row.specialty}}</p></td>-->
<!--          <td class="is-center"><mu-text-field v-show=edit v-model="value4"></mu-text-field><br/><p v-show=!edit>{{scope.row.sex}}</p></td>-->

    <!--        </template>-->
    <!--          <td class="is-center"><mu-button v-if="!edit" v-on:click="edit = true" color="info" :name="scope.row.id">Изменить</mu-button><mu-button v-on:click="edit = false" v-if="edit" color="error">Отмена</mu-button></td>-->
    <!--          <td class="is-center"><mu-button v-if="!edit" color="error">Удалить</mu-button><mu-button v-on:click="edit = false" v-if="edit" color="success">Готово</mu-button></td>-->
    <!--      </mu-data-table>-->
<!--    </mu-paper>-->
    <div>
      <div class="flex-table">
        <div>Имя</div>
        <div>Фамилия</div>
        <div>Специальность</div>
        <div>Пол</div>
      </div>
      <div v-for="doctor in doctors" :key="doctor.id" class="flex-table">
        <div>
          <div v-if="tagEditingId == doctor.id">
            <mu-text-field v-model="form.name"></mu-text-field>
          </div>
          <div v-else>
          {{ doctor.name }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == doctor.id">
            <mu-text-field v-model="form.surname"></mu-text-field>
          </div>
          <div v-else>
            {{ doctor.surname }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == doctor.id">
            <mu-text-field v-model="form.specialty"></mu-text-field>
          </div>
          <div v-else>
            {{ doctor.specialty }}
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == doctor.id">
            <mu-text-field v-model="form.sex"></mu-text-field>
          </div>
          <div v-else>
            <div>{{ doctor.sex }}</div>
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == doctor.id">
            <mu-button v-on:click="cancelEditing" color="error">Отмена</mu-button>
          </div>
          <div v-else>
            <mu-button v-on:click="setEditing(doctor)" color="info" >Изменить</mu-button>
          </div>
        </div>
        <div>
          <div v-if="tagEditingId == doctor.id">
            <mu-button @click="sendEdits" color="success">Готово</mu-button>
          </div>
          <div v-else>
            <mu-button v-on:click="deleteRow(doctor)" color="error">Удалить</mu-button>
          </div>
        </div>
      </div>
    </div>
    <mu-paper :z-depth="2" v-if="!add">
      <mu-text-field placeholder="Имя" solo full-width class="demo-divider-form" v-model="addForm.name"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Фамилия" solo full-width class="demo-divider-form" v-model="addForm.surname"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Отчество" solo full-width class="demo-divider-form" v-model="addForm.middle_name"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Специальность" solo full-width class="demo-divider-form" v-model="addForm.specialty"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Образование" solo full-width class="demo-divider-form" v-model="addForm.education"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Пол" solo full-width class="demo-divider-form" v-model="addForm.sex"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Дата рождения" solo full-width class="demo-divider-form" v-model="addForm.bdate"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Начало контракта" solo full-width class="demo-divider-form" v-model="addForm.start_contract"></mu-text-field>
      <mu-divider></mu-divider>
      <mu-text-field placeholder="Конец контракта" solo full-width class="demo-divider-form" v-model="addForm.end_contract"></mu-text-field>
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
    name: "Doctors",
    data() {
      return {
        tagEditingId: "",
        middle_name: '',
        education: '',
        bdate: '',
        start_contract: '',
        end_contract: '',
        form: {
          name: '',
          surname: '',
          specialty: '',
          sex: '',
        },
        addForm: {
          name: '',
          surname: '',
          middle_name: '',
          specialty: '',
          education: '',
          sex: '',
          bdate: '',
          start_contract:'',
          end_contract:''
        },
        value1: '',
        value2: '',
        value3: '',
        value4: '',
        value5: '',
        value6: '',
        value7: '',
        value8: '',
        doctors: "",
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
          url: "http://127.0.0.1:8000/doctor/",
          type: "GET",
          success: (response) => {
            this.doctors = response
            console.log(this.doctors)
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
      setEditing(doctor){
        this.tagEditingId = doctor.id;
        this.middle_name = doctor.middle_name
        this.education = doctor.education
        this.bdate = doctor.bdate
        this.start_contract = doctor.start_contract
        this.end_contract = doctor.end_contract
        this.edit = true;
      },
      cancelEditing(){
        this.tagEditingId = "";
        this.edit = false;
      },
      sendEdits(){
        this.edit = false
        $.ajax({
          url: "http://127.0.0.1:8000/doctor/" + this.tagEditingId + "/",
          type: "PUT",
          data: {
            name: this.form.name,
            surname: this.form.surname,
            middle_name: this.middle_name,
            specialty: this.form.specialty,
            education: this.education,
            sex: this.form.sex,
            bdate: this.bdate,
            start_contract: this.start_contract,
            end_contract: this.end_contract,
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
          url: "http://127.0.0.1:8000/doctor/",
          type: "POST",
          data: {
            name: this.addForm.name,
            surname: this.addForm.surname,
            middle_name: this.addForm.middle_name,
            specialty: this.addForm.specialty,
            education: this.addForm.education,
            sex: this.addForm.sex,
            bdate: this.addForm.bdate,
            start_contract: this.addForm.start_contract,
            end_contract: this.addForm.end_contract,
          },

          success: (response) => {
            console.log(response)
          },
        }),
          this.tagEditingId = "";
        this.edit = false;
      },
      deleteRow(doctor){
        $.ajax({
          url: "http://127.0.0.1:8000/doctor/" + doctor.id + "/",
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
