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

      Список студентов
      <mu-button flat slot="right" v-if="!auth" @click="goLogin">Вход</mu-button>
      <mu-button flat slot="right" v-else @click="logout">Выход</mu-button>
    </mu-appbar>
    <mu-paper class="demo-paper" :z-depth="5">

      <!--<div class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="text" placeholder="Search"  v-model="search_term" aria-label="Search">
            <button class="btn btn-outline-success my-2 my-sm-0">Search</button>
          </div>
-->
      <table>
        <br/>
        <tr>
          <th>Имя</th>
          <th>Фамилия</th>
          <th>Номер группы</th>
          <th>id</th>
          <th></th>
          <th></th>
        </tr>
        <tr v-for="student in students">
          <td>{{student.name}}</td>
          <td>{{student.surname}}</td>
          <td>{{student.group.group}}</td>
          <td>{{student.id}}</td>
          <td><mu-button style="margin-right: 3px; margin-left: 3px;" @click="DeleteStudents(student.id)" >удалить</mu-button></td>
           <td>
            <mu-button @click="openAlertDialog">Редактировать</mu-button>
          </td>
          <mu-dialog title="Редактировать пользователя" width="600" max-width="80%" :esc-press-close="false"
                     :overlay-close="false" :open.sync="openAlert">
            <mu-form class="mu-demo-form">

        <mu-form-item prop="input">
          <mu-text-field placeholder="Имя" v-model="student_update.name"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="input">
          <mu-text-field placeholder="Фамилия" v-model="student_update.surname"></mu-text-field>
        </mu-form-item>
         <mu-select v-model="student_update.group" label="Номер группы" style="width: 200px" >
      <mu-option v-for="group in groups" :value=group.id :label="group.group">{{group.group}} </mu-option>
      </mu-select>

      </mu-form>
            <mu-button slot="actions" flat color="primary" @click="updateStudent(student.id)">Редактировать</mu-button>
            <mu-button slot="actions" flat color="primary" @click="closeAlertDialog">Закрыть</mu-button>
          </mu-dialog>
        </tr>

      </table>
       <h2>Добавить студента</h2>
       <mu-form class="mu-demo-form" >

        <mu-form-item prop="input" >
          <mu-text-field placeholder = "Имя" v-model="one_student.name"></mu-text-field>
        </mu-form-item>
         <mu-form-item prop="input" >
          <mu-text-field placeholder = "Фамилия" v-model="one_student.surname"></mu-text-field>
        </mu-form-item>

      <mu-select v-model="one_student.group" label="Номер группы" style="width: 200px" >
      <mu-option v-for="group in groups" :value=group.id :label="group.group">{{group.group}} </mu-option>
      </mu-select>
         <mu-button style="margin-bottom: 20px;" @click="createStudents">Добавить</mu-button>
       </mu-form>

      <h2>Добавить группу</h2>
       <mu-form class="mu-demo-form" >

        <mu-form-item prop="input" >
          <mu-text-field placeholder = "Название группы" v-model="one_group.group"></mu-text-field>
        </mu-form-item>
         <mu-button style="margin-bottom: 20px;" @click="createGroup">Создать</mu-button>
       </mu-form>
    </mu-paper>
  </mu-container>
</template>

<script>
  import $ from 'jquery'

  export default {
    name: "Students",
    data() {
      return {
       /* search_term: '',*/
        groups: '',
        students: '',
        one_student:  {group: "", name: "", surname: ""},
        student_update: {group: "", name: "", surname: ""},
        openAlert: false,
        one_group: {},
      }
    },
    created() {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
      });
      this.loadStudents()
      this.loadGroup()
    },
    computed: {
      auth() {
        if (sessionStorage.getItem("auth_token")) {
          return true
        }
      }
    },
    methods: {
       openAlertDialog () {
      this.openAlert = true;
    },
    closeAlertDialog () {
      this.openAlert = false;
    },
      async updateStudent(studentId) {
        const response = await fetch('http://127.0.0.1:8000/api/v1/student/update/6', {
          method: 'PUT',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.teacher_update),
        });
        this.closeAlertDialog()
        await this.loadStudents();
      },
      DeleteStudents(studentId) {
        $.ajax({
          url: 'http://127.0.0.1:8000/api/v1/students/delete/'+studentId,
          type: "DELETE",
          success: (response) => {
            this.students = response
            document.location.href = "http://localhost:8080/#/students"
          }
        })
      },
      loadGroup(){
          $.ajax({
          url: "http://127.0.0.1:8000/api/v1/groups/",
          type: "GET",
          success: (response) => {
            this.groups = response
            console.log(response)
          }
        })
      },
      loadStudents() {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/students/",
          type: "GET",
          success: (response) => {
            this.students = response
            console.log(response)
          }
        })
      },
      async createStudents(){
        const response = await fetch('http://127.0.0.1:8000/api/v1/students/', {
          method: 'POST',
          headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
    },
    body: JSON.stringify(this.one_student),
        });
        if (response.status !== 201){
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.loadStudents();
      },
      async createGroup(){
        const response = await fetch('http://127.0.0.1:8000/api/v1/groups/', {
          method: 'POST',
          headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
    },
    body: JSON.stringify(this.one_group),
        });
        if (response.status !== 201){
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.loadStudents();
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

  td:first-child {
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
