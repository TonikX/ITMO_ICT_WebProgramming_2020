<template>
  <mu-container>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
  <mu-paper :z-depth="1">
    <mu-data-table stripe :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="list">
      <template slot-scope="scope">
        <td><button v-on:click="goTo(scope.row.id)">{{ scope.row.profession }}</button></td>
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
export default {

  name: "Vacancy",
  components:{
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
        {title: 'Дата публикации', name: 'date_start', width: 150, align: 'center', sortable: true},
        {title: 'Зарплата', name: 'salary', width: 110, align: 'center', sortable: true},
        {title: 'Опыт работы', name: 'min_exp', width: 105, align: 'center', sortable: true},
        {title: 'Статус', name: 'status', width: 100, align: 'center', sortable: true},
      ],
      list: '',
    }
  },
  comments:{
    Navbar,
  },
  created() {
    this.loadListVacancy();
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
    async loadListVacancy() {
            this.list = await fetch(
                `${this.$store.getters.getServerUrl}/vacancy/list/`
            ).then(response => response.json())
    },
    goTo(id) {
      this.$router.push({name: 'vacancySingle', params: {id: id}})
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