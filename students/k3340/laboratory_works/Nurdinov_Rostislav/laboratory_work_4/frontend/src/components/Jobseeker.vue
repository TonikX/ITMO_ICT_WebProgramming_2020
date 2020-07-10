<template>
  <mu-container>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
  <mu-paper :z-depth="1">
    <mu-data-table stripe :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="list">
      <template slot-scope="scope">
        <td><button v-on:click="goTo(scope.row.id)">{{ scope.row.surname }}</button></td>
        <td class="is-right">{{ scope.row.name }}</td>
        <td class="is-right">{{ scope.row.second_name }}</td>
        <td class="is-right">{{ scope.row.date_birth }}</td>
        <td class="is-right">{{ scope.row.status_work }}</td>
        <td class="is-right">{{ scope.row.last_salary }}</td>
      </template>
    </mu-data-table>
  </mu-paper>
</mu-container>
</template>

<script>
import Navbar from '../components/Navbar';
import $ from "jquery";
export default {
  comments:{
    Navbar,
  },
  name: "Jobseeker",
  data() {
    return {
      sort: {
        name: '',
        order: 'asc'
      },
      columns: [
        {title: 'Фамилия', width: 200, name: 'surname', align: 'center'},
        {title: 'Имя', name: 'name', width: 126, align: 'center', sortable: true},
        {title: 'Отчество', name: 'second_name', width: 150, align: 'center', sortable: true},
        {title: 'Дата рождения', name: 'date_birth', width: 126, align: 'center', sortable: true},
        {title: 'Статус', name: 'status_work', width: 126, align: 'center', sortable: true},
        {title: 'Последняя зарплата', name: 'last_salary', width: 126, align: 'center', sortable: true},
      ],
      list: '',
      form: {
        surname: '',
        name: '',
        second_name: '',
        date_birth: '',
        address: '',
        status: false,
        status_work: ''
      }
    }
  },
  components:{
    Navbar,
  },
  created() {
    this.loadListJobseeker();
  },

  methods: {
    handleSortChange({name, order}) {
      this.list = this.list.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
    },
    async loadListJobseeker() {
            this.list = await fetch(
                `${this.$store.getters.getServerUrl}/jobseeker/list/`
            ).then(response => response.json())
    },
    goTo(id) {
      this.$router.push({name: 'jobseekerSingle', params: {id: id}});
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