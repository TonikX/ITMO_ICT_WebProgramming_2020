<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      <mu-menu slot="left">
        <mu-button flat>Меню</mu-button>
        <mu-list slot="content">
          <mu-list-item button @click="shedule">
            <mu-list-item-content>
              <mu-list-item-title>Расписание</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button @click="teachers">
            <mu-list-item-content>
              <mu-list-item-title>Преподаватели</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button @click="gostudents">
            <mu-list-item-content>
              <mu-list-item-title>Студенты</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button @click="record">
            <mu-list-item-content>
              <mu-list-item-title>Журнал</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
        </mu-list>
      </mu-menu>

      Журнал
      <mu-button flat slot="right" v-if="!auth" @click="goLogin">Вход</mu-button>
      <mu-button flat slot="right" v-else @click="logout">Выход</mu-button>
    </mu-appbar>
    <mu-paper class="demo-paper" :z-depth="5">
      <br/>
      <table>
        <tr>
          <th>Предмет</th>
          <th>Студент</th>
          <th>Оценка</th>
          <th></th>
        </tr>
        <tr v-for="record in records">
          <td>{{record.subject.name}}</td>
          <td>{{record.student.surname}} {{record.student.name}}</td>
          <td>{{record.rating}}</td>
          <td>
            <mu-button style="margin-right: 3px; margin-left: 3px;" @click="deleteRecord">удалить</mu-button>
          </td>
        </tr>

      </table>
      <h2>Добавить оценку</h2>
      <mu-form class="mu-demo-form">
        <mu-select v-model="one_record.student" label="Студент" style="width: 200px">
          <mu-option v-for="student in students" :value=student.id :label=student.surname+student.name> {{student.surname}} {{student.name}}</mu-option>
        </mu-select>
        <mu-select v-model="one_record.subject" label="Предмет" style="width: 200px">
          <mu-option v-for="subject in subjects" :value=subject.id :label=subject.name> {{subject.name}}</mu-option>
        </mu-select>
        <mu-form-item prop="input">
          <mu-text-field placeholder="Оценка" v-model="one_record.rating"></mu-text-field>
        </mu-form-item>

        <mu-button style="margin-bottom: 20px;" @click="createRecord">Добавить</mu-button>
      </mu-form>
    </mu-paper>
  </mu-container>
</template>

<script>
  import $ from 'jquery'

  export default {
    name: "Records",
    data() {
      return {
        records: '',
        one_record: {},
      }
    },
    created() {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
      });
      this.loadRecord()
      this.loadStudent()
      this.loadSubject()
    },
    computed: {
      auth() {
        if (sessionStorage.getItem("auth_token")) {
          return true
        }
      }
    },
    methods: {
      loadRecord() {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/record/",
          type: "GET",
          success: (response) => {
            this.records = response
            console.log(response)
          }
        })
      },
      loadStudent() {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/students/",
          type: "GET",
          success: (response) => {
            this.students = response
            console.log(response)
          }
        })
      },
      loadSubject() {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/subjects/",
          type: "GET",
          success: (response) => {
            this.subjects = response
            console.log(response)
          }
        })
      },
      async createRecord() {
        const response = await fetch('http://127.0.0.1:8000/api/v1/record/', {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.one_record),
        });
        if (response.status !== 201) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.loadRecord();
      },
      deleteRecord() {
        $.ajax({
          url: 'http://127.0.0.1:8000/api/v1/record/delete/2',
          type: "DELETE",
          success: (response) => {
            this.rooms = response
          }
        })
      },
      goLogin() {
        this.$router.push({name: "login"})
      },
      logout() {
        sessionStorage.removeItem("auth_token")
        window.location = "/"
      },
      shedule() {
        document.location.href = "http://localhost:8080/#/";
      },
      record() {
        document.location.href = "http://localhost:8080/#/record";
      },
      gostudents() {
        document.location.href = "http://localhost:8080/#/students";
      },
      teachers() {
        document.location.href = "http://localhost:8080/#/teachers";
      },
    }
  }
</script>

<style scoped>
  table {
    margin: auto;
    margin-top: 30px;
    margin-bottom: 30px;
    font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-size: 14px;
    border-collapse: collapse;
    text-align: center;
  }

  th {
    background: #AFCDE7;
    color: white;
    padding: 10px 20px;
  }

  th, td {
    border-style: solid;
    border-width: 0 1px 1px 0;
    border-color: white;
  }

  td {
    background: #D8E6F3;
  }

  th:first-child {
    text-align: left;
    font-weight: bold;
  }

  .mu-demo-form {
    width: 100%;
    max-width: 200px;
    margin: auto;
  }
</style>
