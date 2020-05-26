<template>
  <main class="pa-2">
    <section>
      <h2 align="center">Добавить заказ на склад</h2>
      <v-text-field label="Номер заказа"  v-model.number="currentOrder.order"></v-text-field><v-btn @click="createOrder" small color="green">Добавить</v-btn>
      <v-btn small color="primary" @click="goStorage()">Вернуться на склад</v-btn>
        <v-simple-table>
          <template v-slot:default>
            <thead>
                <tr>
                  <th class="text-center">Номер заказа</th>
                  <th class="text-center">Категория</th>
                  <th class="text-center">Масса</th>
                  <th class="text-center">Дата</th>
                  <th class="text-center">Водитель</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in orders">
                  <td class="text-center">{{ item.id }}</td>
                  <td class="text-center">{{ item.category }}</td>
                  <td class="text-center">{{ item.mass }} </td>
                  <td class="text-center">{{ item.data }} </td>
                  <td class="text-center">{{ item.driver }} </td>
                </tr>
            </tbody>
          </template>
        </v-simple-table>
    </section>
  </main>
</template>

<script>
    export default {
        name: "addOrder",
      data() {
          return {
            orders: [],
            currentOrder: {},
          }
      },
       async created() {
        await this.fetchOrders();
         let token = localStorage.getItem('auth_token');
        console.log(token);
        this.$axios.get('http://127.0.0.1:8000/orders/?api_token='+token, {headers: {'Authorization' : "Token "+token}})
          .then(response => {this.orders = response.data
            console.log(response);
          })
          .catch((error) => {
            console.log(error)
          })},
      methods: {
            async fetchOrders() {
            const response = await fetch('http://127.0.0.1:8000/orders/');
            this.orders = await response.json()
          },
        goStorage() {
          this.$router.push({name:'Storage'})
        },
          async createOrder(order) {
              const {id} =order
            let token = localStorage.getItem('auth_token');
            const response = await fetch('http://127.0.0.1:8000/add_order/?api_token='+token, {
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization' : "Token "+token
              },
              method: "POST",
              body: JSON.stringify(this.currentOrder)
              });
            if (response.status !== 201) {
              alert(JSON.stringify(await response.json(), null, 2));
            }
            await this.fetchOrders();
          },
    }}
</script>

<style scoped>

</style>
