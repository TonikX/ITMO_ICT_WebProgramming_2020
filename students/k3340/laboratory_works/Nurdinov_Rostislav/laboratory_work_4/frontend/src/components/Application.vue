<template>
  <mu-container>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
  <mu-paper :z-depth="1">
    <mu-data-table stripe :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="list">
      <template slot-scope="scope">
        <td class="is-center">{{ scope.row.id }}</td>
        <td class="is-center">{{ scope.row.resume }}</td>
        <td class="is-center">{{ scope.row.vacancy }}</td>
        <td class="is-center">{{ scope.row.date_start }}</td>
      </template>
    </mu-data-table>
  </mu-paper>
</mu-container>
</template>

<script>
import Navbar from '../components/Navbar';
export default {
  comments:{
    Navbar,
  },
  name: "Application",
  data() {
    return {
      sort: {
        name: '',
        order: 'asc'
      },
      columns: [
        {title: 'ID', width: 100, name: 'id', align: 'center'},
        {title: 'ID резюме', width: 100, name: 'id_resume', align: 'center'},
        {title: 'ID вакансии', name: 'id_vacancy', width: 100, align: 'center', sortable: true},
        {title: 'Дата заявки', name: 'date_start', width: 150, align: 'center', sortable: true},
      ],
      list: '',
    }
  },
  components:{
    Navbar,
  },
  created() {
    this.loadListApplication();
  },

  methods: {
    handleSortChange({name, order}) {
      this.list = this.list.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
    },
    async loadListApplication() {
            this.list = await fetch(
                `${this.$store.getters.getServerUrl}/application/list/`
            ).then(response => response.json())
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