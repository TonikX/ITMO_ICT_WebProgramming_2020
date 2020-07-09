<template>
  <mu-container>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
  <mu-dialog title="Добавление абитуриента" width="560" scrollable :open.sync="isOpenAddForm">
        <mu-form :model="form" class="mu-demo-form" label-position="top" label-width="100">
          <mu-form-item prop="surname" label="Фамилия">
            <mu-text-field v-model="form.surname"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="name" label="Имя">
            <mu-text-field v-model="form.name"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="secon_dname" label="Отчество">
            <mu-text-field v-model="form.second_name"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="email" label="Email">
            <mu-text-field v-model="form.email"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="number" label="Номер телефона">
            <mu-text-field v-model="form.number"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="Фирма" label="Фирма">
            <mu-text-field v-model="form.firm"></mu-text-field>
          </mu-form-item>
        </mu-form>
        <mu-button slot="actions" flat color="primary" @click="CloseAddForm">Закрыть</mu-button>
        <mu-button v-if="isUpdateForm" slot="actions" flat color="success" @click="updateEmployer(last_id)">Обновить</mu-button>
        <mu-button v-else="isCreateForm" slot="actions" flat color="success" @click="createEmployer">Добавить</mu-button>
      </mu-dialog>
  <mu-paper :z-depth="1">
    <mu-data-table stripe :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="list">
      <template slot-scope="scope">
        <td class="is-center"><button v-on:click="goTo(scope.row.id)">{{ scope.row.surname }}</button></td>
        <td class="is-center">{{ scope.row.name }}</td>
        <td class="is-center">{{ scope.row.second_name }}</td>
        <td class="is-center">{{ scope.row.email }}</td>
        <td class="is-center">{{ scope.row.number }}</td>
        <td class="is-center">{{ scope.row.firm }}</td>
        <td class="is-center"><button v-on:click="deleteEmployer(scope.row.id)">Удалить</button></td>
        <td class="is-center"><button v-on:click="openUpdateForm(scope.row.id)">Обновить</button></td>
      </template>
    </mu-data-table>
  </mu-paper>
  <mu-container v-show="true">
    <h2>Добавить соискателя</h2>
       <mu-form class="mu-demo-form" >
         <mu-button style="margin-bottom: 20px;" @click="openCreateForm">Создать</mu-button>
       </mu-form>
  </mu-container>
</mu-container>
</template>

<script>
import Navbar from '../components/Navbar';
import $ from "jquery";
export default {
  comments:{
    Navbar,
  },
  name: "Employer",
    data: function () {
        return {
            last_id: '',
            sort: {
                name: '',
                order: 'asc'
            },
            columns: [
                {title: 'Фамилия', width: 150, name: 'surname', align: 'center'},
                {title: 'Имя', name: 'name', width: 126, align: 'center', sortable: true},
                {title: 'Отчество', name: 'second_name', width: 150, align: 'center', sortable: true},
                {title: 'Email', name: 'email', width: 150, align: 'center', sortable: true},
                {title: 'Телефон', name: 'number', width: 135, align: 'center', sortable: true},
                {title: 'Фирма зарплата', name: 'firm', width: 135, align: 'center', sortable: true},
                {title: '', name: 'del', width: 125, align: 'center', sortable: true},
                {title: '', name: 'update', width: 125, align: 'center', sortable: true}
            ],
            isModalVisible: true,
            isCreateForm: true,
            isUpdateForm: true,
            isOpenAddForm: false,
            list: '',
            form: {
                surname: '',
                name: '',
                second_name: '',
                email: '',
                number: '',
                firm: ''
            }
        }
    },
  components:{
    Navbar,
  },
  created() {
    this.loadListEmployer();
  },

  methods: {
    handleSortChange({name, order}) {
      this.list = this.list.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
    },
    async loadListEmployer() {
            this.list = await fetch(
                `${this.$store.getters.getServerUrl}/employer/list/`
            ).then(response => response.json())
    },
    goTo(id) {
      this.$router.push({name: 'employerSingle', params: {id: id}});
    },
    async openUpdateForm(id) {
            this.isCreateForm = false;
            this.isUpdateForm = true;
            this.isOpenAddForm = true;
            this.last_id = id;
            this.form = await fetch(
                `${this.$store.getters.getServerUrl}/employer/detail/` + id, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + sessionStorage.getItem("access"),
                    },
                }
            ).then(response => response.json());
        },
      async openCreateForm() {
          this.isUpdateForm = false;
          this.isCreateForm = true;
          this.isOpenAddForm = true;
          this.last_id = '';
      },
     async updateEmployer(id) {
      console.log(id);
      const response = await fetch('http://127.0.0.1:8000/api/v1/employer/detail/' + id, {
        method: "PUT",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + sessionStorage.getItem("access"),
        },
        body: JSON.stringify(this.form)
      });

      if (response.status === 200) {
        alert("Пользователь обновлен!");
      }
    },
    async deleteEmployer(id) {
        const response = await fetch('http://127.0.0.1:8000/api/v1/employer/detail/' + id, {
            method: "DELETE",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + sessionStorage.getItem("access"),
            },
            body: JSON.stringify(this.form)
        });

        if (response.status === 200) {
            alert("Пользователь удален!");
        }
    },
    CloseAddForm() {
      this.form = {
          surname: '',
          name: '',
          second_name: '',
          email: '',
          number: '',
          firm: ''
        };
      this.isOpenAddForm = false;
    },
    async createEmployer() {
      this.isCreateForm = true;
      const response = await fetch('http://127.0.0.1:8000/api/v1/employer/create/', {
        method: "POST",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + sessionStorage.getItem("access"),
        },
        body: JSON.stringify(this.form)
      });
      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
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