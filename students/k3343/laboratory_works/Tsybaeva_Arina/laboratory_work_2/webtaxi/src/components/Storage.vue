
<template>
  <div>
    <main class="pa-5">
      <section>
      <h2 align="center">Склад</h2>
        <h1 align="center"><v-btn @click="addOrder()">Принять заказ</v-btn>   <v-btn color="error" @click="deleteOrder()">Списать заказ</v-btn></h1>
      </section>
      <section>
        <h3>Хранится на складе:</h3>
      <v-simple-table dense>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center">Категория</th>
              <th class="text-center">Килограммы</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in storage">
              <td>{{ item.category }}</td>
              <td>{{ item.amount }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
      </section>
      <section>
      <h5>Справка: </h5>
          <v-simple-table dense :height="300" >
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center">Наименование</th>
              <th class="text-center">Название категории</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in category">
              <td>{{ item.id }}</td>
              <td>{{ item.name }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
      </section>
    </main>
  </div>
</template>

<script>
    export default {
        name: "Storage",
       data () {
          return {
            storage: [],
            category: [],
          };
      },
      async created() {
        await this.fetchReport();
        await this.fetchCategory()
      },
      mounted() {
          let token = localStorage.getItem('auth_token');
        console.log(token);
        this.$axios.get('http://127.0.0.1:8000/storage/?api_token='+token, {headers: {'Authorization' : "Token "+token}})
          .then(response => {this.storage = response.data
            console.log(response);
          })
          .catch((error) => {
            console.log(error)
          })
      },
      methods: {
          async fetchReport() {
            const response = await fetch('http://127.0.0.1:8000/storage/');
            this.storage = await response.json()
          },
         async fetchCategory() {
            const response = await fetch('http://127.0.0.1:8000/category/');
            this.category = await response.json()
          },
            addOrder() {
        this.$router.push({name:'addOrder'})
    },
        deleteOrder() {
         this.$router.push({name:'deleteOrder'})
        }
    }
    }
</script>

<style scoped>
 h2,h5 { padding: 10px;}
section{
  padding: 10px;
}
 TD, TH {
   text-align: center; /* Выравниваем текст по центру ячейки */
   }
</style>
