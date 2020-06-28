<template>
<mu-container>
  <table>
    <tr>
      <th>Предмет</th>
      <th>Преподаватель</th>
      <th>Номер кабинета</th>
      <th>Номер группы</th>
      <th>Дата и время</th>
      <th>id</th>
      <th></th>
    </tr>
    <tr v-for="room in rooms">
      <td>{{room.subject.name}}</td>
      <td>{{room.teacher.name}} {{room.teacher.surname}}</td>
      <td>{{room.teacher.class_number}}</td>
      <td>{{room.group.group}}</td>
      <td>{{room.time}}</td>
      <td v-model="id_room">{{room.id}}</td>
      <td><mu-button style="margin-right: 3px; margin-left: 3px;" @click="deleteRoom(room.id)" >удалить</mu-button></td>
    </tr>
  </table>
    <h2>Добавить поле в расписание</h2>
       <mu-form class="mu-demo-form" >

        <mu-form-item prop="input" >
          <mu-text-field placeholder = "Дата и время" v-model="one_room.time"></mu-text-field>
        </mu-form-item>
        <mu-select v-model="one_room.group" label="Номер группы" style="width: 200px">
      <mu-option v-for="group in groups" :value=group.id :label=group.group>{{group.group}} </mu-option>
      </mu-select>
         <mu-select v-model="one_room.teacher" label="Преподаватель" style="width: 200px">
      <mu-option v-for="teacher in teachers" :value=teacher.id :label=teacher.surname>{{teacher.surname}} </mu-option>
      </mu-select>
         <mu-select v-model="one_room.subject" label="Предмет" style="width: 200px">
      <mu-option v-for="subject in subjects" :value=subject.id :label=subject.name>{{subject.name}} </mu-option>
      </mu-select>


         <mu-button style="margin-bottom: 20px;" @click="createRoom">Добавить</mu-button>
       </mu-form>
</mu-container>
</template>

<script>
  import $ from 'jquery'

  export default {
    name: "Room",
    data() {
      return {
        id_room:"",
        rooms: '',
        one_room: {group: "", subject: "", teacher: "", time: ""},

      }
    },
    created() {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
      });
      this.loadRoom()
      this.loadSubject()
      this.loadGroup()
      this.loadTeacher()
    },
    methods: {

      // Загружаю список учеников
      loadRoom() {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/shedule/",
          type: "GET",
          success: (response) => {
            this.rooms = response
          }
        })
      },
      loadSubject(){
          $.ajax({
          url: "http://127.0.0.1:8000/api/v1/subjects/",
          type: "GET",
          success: (response) => {
            this.subjects = response
            console.log(response)
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
      loadTeacher(){
          $.ajax({
          url: "http://127.0.0.1:8000/api/v1/teachers/",
          type: "GET",
          success: (response) => {
            this.teachers = response
            console.log(response)
          }
        })
      },
      async createRoom(){
        const response = await fetch('http://127.0.0.1:8000/api/v1/shedule/', {
          method: 'POST',
          headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
    },
    body: JSON.stringify(this.one_room),
        });
        if (response.status !== 201){
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.loadRoom();
      },
      deleteRoom(roomId) {
        $.ajax({
          url: 'http://127.0.0.1:8000/api/v1/shedule/delete/'+roomId,
          type: "DELETE",
          success: (response) => {
            this.rooms = response
            window.location = "/"
          }
        })
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

  th, td:first-child {
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

  th:first-child, td:first-child {
    text-align: left;
  }
  .mu-demo-form {
    width: 100%;
    max-width: 200px;
    margin: auto;
  }
</style>
