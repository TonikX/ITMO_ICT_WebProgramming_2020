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
          <mu-list-item button>
            <mu-list-item-content>
              <mu-list-item-title>Преподаватели</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button @click="students">
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

      Список преподавателей
      <mu-button flat slot="right" v-if="!auth" @click="goLogin">Вход</mu-button>
      <mu-button flat slot="right" v-else @click="logout">Выход</mu-button>
    </mu-appbar>
    <mu-paper class="demo-paper" :z-depth="5">
      <table>
        <br/>
        <tr>
          <th>Имя</th>
          <th>Фамилия</th>
          <th>Номер кабинета</th>
          <th>id</th>
          <th></th>
          <th></th>
        </tr>
        <tr v-for="teacher in teachers" :key="teacher.id">
          <td>{{teacher.name}}</td>
          <td>{{teacher.surname}}</td>
          <td>{{teacher.class_number}}</td>
          <td>{{teacher.id}}</td>
          <td>
            <mu-button style="margin-right: 3px; margin-left: 3px;" @click="deleteTeacher(teacher.id)">удалить</mu-button>
          </td>
          <td>
            <mu-button @click="openAlertDialog">Редактировать</mu-button>
          </td>

          <mu-dialog title="Редактировать пользователя" width="600" max-width="80%" :esc-press-close="false"
                     :overlay-close="false" :open.sync="openAlert">
            <mu-form class="mu-demo-form">

        <mu-form-item prop="input">
          <mu-text-field placeholder="Имя" v-model="teacher_update.name"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="input">
          <mu-text-field placeholder="Фамилия" v-model="teacher_update.surname"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="input">
          <mu-text-field placeholder="Номер кабинета" v-model="teacher_update.class_number"></mu-text-field>
        </mu-form-item>

      </mu-form>
            <mu-button slot="actions" flat color="primary" @click="updateTeacher(teacher.id)">Редактировать</mu-button>
            <mu-button slot="actions" flat color="primary" @click="closeAlertDialog">Закрыть</mu-button>
          </mu-dialog>
        </tr>

      </table>
      <mu-button @click="addFilter()">+</mu-button>

      <ul>
        <p v-for="filter in filters" :key="id">
          <input v-model="filter.key">
          <input v-model="filter.value">
          <mu-button @click="dropFilter(filter)">-</mu-button>
        </p>
      </ul>
      <mu-button @click="filterTeachers()">Отфильтровать</mu-button>
      <br/>
      <br/>
      <h1>Добавить учителя</h1>
      <mu-form class="mu-demo-form">

        <mu-form-item prop="input">
          <mu-text-field placeholder="Имя" v-model="one_teacher.name"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="input">
          <mu-text-field placeholder="Фамилия" v-model="one_teacher.surname"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="input">
          <mu-text-field placeholder="Номер кабинета" v-model="one_teacher.class_number"></mu-text-field>
        </mu-form-item>
        <mu-button style="margin-bottom: 20px;" @click="createTeacher">Добавить</mu-button>
      </mu-form>

    </mu-paper>
  </mu-container>
</template>

<script>
  import $ from "jquery";

  export default {
    name: "Teachers",
    data() {
      return {
        teachers: '',
        teacher_update: {name: "", surname: "", class_number: ""},
        one_teacher: {},
        filters: [],
        openAlert: false,
      }
    },
    created() {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
      });
      this.loadTeacher()
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
      loadTeacher() {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/teachers/",
          type: "GET",
          success: (response) => {
            this.teachers = response
            console.log(response)
          }
        })
      },
      async updateTeacher(teacherId) {
        const response = await fetch('http://127.0.0.1:8000/api/v1/teachers/update/8', {
          method: 'PUT',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.teacher_update),
        });
        this.closeAlertDialog()
        await this.loadTeacher();
      },
      async createTeacher() {
        const response = await fetch('http://127.0.0.1:8000/api/v1/teachers/', {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.one_teacher),
        });
        if (response.status !== 201) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.loadTeacher();
      },
      deleteTeacher(teacherId) {
        $.ajax({
          url: 'http://127.0.0.1:8000/api/v1/teachers/delete/'+teacherId,
          type: "DELETE",
          success: (response) => {
            this.teachers = response
            document.location.href = "http://localhost:8080/#/teachers"
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
      students() {
        document.location.href = "http://localhost:8080/#/students";
      },
      record() {
        document.location.href = "http://localhost:8080/#/record";
      },
      addFilter() {
        this.filters.push({id: Math.random()});
      },
      dropFilter(filter) {
        this.filters = this.filters.filter(f => f.id !== filter.id);
      },

      async filterTeachers() {
        const filledFilters = this.filters.filter(({key, value}) => key && value);
        const url = new URL("http://127.0.0.1:8000/api/v1/teachers/");
        filledFilters.forEach(({key, value}) => url.searchParams.append(key, value));
        console.log(url)
        document.location.href = url;
        /*this.reloadTeacher(url)*/
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
