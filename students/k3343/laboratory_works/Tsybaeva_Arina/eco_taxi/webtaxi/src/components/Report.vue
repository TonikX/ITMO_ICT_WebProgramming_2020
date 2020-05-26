<template>
  <div>
    <main class="pa-2">
      <section>
      <h2 align="center">Отчет за текущий месяц</h2>
          <v-simple-table height="100px">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center">Количество забранного мусора (кг)</th>
              <th class="text-center">Количество сданного мусора (кг)</th>
              <th class="text-center">Количество заказов</th>
              <th class="text-center">Доход</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in report">
              <td>{{ item.total_from_client }}</td>
              <td>{{ item.total_to_fabric }}</td>
              <td>{{ item.total_client }}</td>
              <td>{{ item.total_money }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </section>
      <section>
        <h3>Посмотреть активность водителя за определенную дату</h3>
      </section>
       <section>
        <div class="form-inline my-2 my-lg-0">
          <v-text-field label="Введите фамилию и дату через пробел" v-model.number="search_term" ></v-text-field>
          <h1 align="center"><v-btn text small color="success" @click="getOrders()">Найти</v-btn></h1>
          </div>
      </section>
      <section>
        <h2>Заказы:</h2>
        <v-simple-table height="200px">
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-center">Водитель</th>
                <th class="text-center">Дата</th>
                <th class="text-center">Клиент</th>
                <th class="text-center">Стоимость</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in orders">
                <td>{{ item.driver }}</td>
                <td>{{ item.data }}</td>
                <td>{{ item.client}}</td>
                <td>{{ item.cost }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </section>
    </main>
  </div>
</template>
<script>
  import $ from 'jquery'
    export default {
        name: "Report",
      data () {
          return {
            report: [],
            currentDriver: {},
            filters: [],
            orders: [],
            search_term: '',
          };
      },
      async created() {
        await this.fetchReport();
        await this.fetchOrders();
      },
        mounted: function() {
        this.getOrders();
        let token = localStorage.getItem('auth_token');
        console.log(token);
        this.$axios.get('http://127.0.0.1:8000/report/?api_token='+token, {headers: {'Authorization' : "Token "+token}})
          .then(response => {this.report = response.data
            console.log(response);
          })
          .catch((error) => {
            console.log(error)
          })
      },
      methods: {
          async fetchReport() {
            const response = await fetch('http://127.0.0.1:8000/report/');
            this.report = await response.json()
          },
        async fetchOrders() {
            const response = await fetch('http://127.0.0.1:8000/order-list/');
            this.orders = await response.json()
        },

        getOrders() {
            let api_url = 'http://127.0.0.1:8000/order-list/';
            if (this.search_term !== ''|| this.search_term !==null) {
              api_url = `http://127.0.0.1:8000/order-list/?search=${this.search_term}`
            }
            this.loading = true;
            this.$http.get(api_url)
              .then((response)=>{
              this.orders = response.data;
              this.loading = false
          })
          .catch((err) =>{
            this.loading = false;
            console.log(err);
          })
        }
    }}
</script>

<style scoped>
 TD, TH {
   text-align: center; /* Выравниваем текст по центру ячейки */
   }
section{
  padding: 10px;
}
</style>
