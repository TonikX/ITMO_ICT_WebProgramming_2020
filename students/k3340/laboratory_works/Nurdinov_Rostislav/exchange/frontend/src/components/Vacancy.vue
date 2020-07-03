<template>
  <mu-container>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
  <mu-paper :z-depth="1">
    <mu-data-table stripe :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="list">
      <template slot-scope="scope">
        <td><button v-on:click="clickRow(scope.row.id)">{{ scope.row.profession }}</button></td>
        <td class="is-right">{{ scope.row.date_start }}</td>
        <td class="is-right">{{ scope.row.salary }}</td>
        <td class="is-right">{{ scope.row.min_exp }}</td>
        <td class="is-right">{{ scope.row.status }}</td>
      </template>
    </mu-data-table>
  </mu-paper>
</mu-container>
</template>

<script>
import Navbar from '../components/Navbar';
import $ from "jquery";
export default {

  name: "Vacancy",
  components: {
    Navbar,
  },
  data() {
    return {
      sort: {
        name: '',
        order: 'asc'
      },
      columns: [
        {title: 'Профессия', width: 200, name: 'profession'},
        {title: 'Дата публикации', name: 'date_start', width: 126, align: 'center', sortable: true},
        {title: 'Зарплата', name: 'salary', width: 126, align: 'center', sortable: true},
        {title: 'Опыт работы', name: 'min_exp', width: 126, align: 'center', sortable: true},
        {title: 'Статус', name: 'status', width: 126, align: 'center', sortable: true},
      ],
      list: '',
    }
  },
  comments:{
    Navbar,
  },
  created() {
    this.loadVacancy();
  },
  // computed: {
  //   auth() {
  //     if (sessionStorage.getItem("auth_token")) {
  //       return true
  //     }
  //   }
  // },
  methods: {
    handleSortChange({name, order}) {
      this.list = this.list.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
    },
    loadVacancy() {
    $.ajax({
      url: "http://127.0.0.1:8000/api/v1/vacancy/list/",
      type: "GET",
      success: (response) => {
        this.list = response;
        console.log(this.list);
      },
    })
  },
    clickRow(message) {
        document.location.href = "http://localhost:8080/vacancy/detail/" + String(message);
      },
  }
};
</script>

<style>
  table {
    margin: auto;
    font-size: 14px;
    border-collapse: collapse;
    text-align: center;
  }

</style>