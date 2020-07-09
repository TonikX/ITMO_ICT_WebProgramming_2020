<template>
  <mu-container>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
    <mu-dialog title="Фильтр" width="560" scrollable :open.sync="isOpenFilterForm">
        <mu-form :model="filters" class="mu-demo-form" label-position="top" label-width="100">
          <mu-select v-model="filters.profession" label="Фильтр по названию">
              <mu-option v-for="prof in listProfession" :key="prof.id" :label="prof.prof"
                         :value="prof.id"></mu-option>
          </mu-select>
          <mu-form-item prop="from_s" label="От">
            <mu-text-field v-model="filters.from_s"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="from_to" label="До">
            <mu-text-field v-model="filters.from_to"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="min_exp" label="Минимальный опыт работы">
            <mu-text-field v-model="filters.min_exp"></mu-text-field>
          </mu-form-item>
        </mu-form>
        <mu-button slot="actions" flat color="primary" @click="closeFilter">Закрыть</mu-button>
        <mu-button slot="actions" flat color="success" @click="loadListVacancy">Отфтльтровать</mu-button>
      </mu-dialog>
  <mu-paper :z-depth="1">
    <mu-data-table stripe :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="list" color="FFFAFE">
      <template slot-scope="scope">
        <td class="is-right"><button v-on:click="goTo(scope.row.id)">{{ scope.row.profession }}</button></td>
        <td class="is-right">{{ scope.row.date_start }}</td>
        <td class="is-right">{{ scope.row.salary }}</td>
        <td class="is-right">{{ scope.row.min_exp }}</td>
        <td class="is-right">{{ scope.row.status }}</td>
      </template>
    </mu-data-table>
  </mu-paper>
    <p></p>
    <mu-container class="button-wrapper">
  <mu-flex justify-content="center" align-items="center">
    <mu-button round color="success" @click="showForm">Фильтр</mu-button>
  </mu-flex>
    </mu-container>
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
      filters:{
        profession: '',
        min_exp: '',
        from_s: '',
        from_to: '',
      },
      list: '',
      isModalVisible: true,
      isOpenFilterForm: false,
      listProfession: [],
    }
  },
  comments:{
    Navbar,
  },
  created() {
    this.loadListVacancy();
    this.loadProfession();
    // this.getToken();
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
            console.log(111);
            this.list = await fetch(
                `${this.$store.getters.getServerUrl}/vacancy/list/?min_exp=${this.filters.min_exp}&profession=${this.filters.profession}&from_s=${this.filters.from_s}&from_to=${this.filters.from_to}`
            ).then(response => response.json());
            this.closeFilter()
    },
    async loadProfession() {
      this.listProfession = await fetch(
                    `http://127.0.0.1:8000/api/v1/profession/list/`
                ).then(response => response.json())
    },
    goTo(id) {
      this.$router.push({name: 'vacancySingle', params: {id: id}})
    },
    showModal() {
        this.isModalVisible = true;
    },
    closeModal() {
        this.isModalVisible = false;
    },
    showForm() {
        this.isOpenFilterForm = true;
    },
    closeFilter() {
        this.isOpenFilterForm = false;
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