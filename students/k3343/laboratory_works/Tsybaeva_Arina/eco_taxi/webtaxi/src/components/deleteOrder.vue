<template>
<main class="pa-3">
  <h1><v-btn small color="primary" @click="goStorage()">Вернуться на склад</v-btn></h1>
    <h2 aligh="left">Списать заказ со склада</h2>
    <h3>Выберите заказ, который хотите списать:</h3>
  <section>
      <v-simple-table>
          <template v-slot:default>
            <thead>
                <tr>
                  <th class="text-center">Номер заказа</th>
                  <th> </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in orders">
                  <td class="text-center">{{ item.order }}</td>
                  <td><v-btn text small @click="removeOrder(item)" color="error">Списать</v-btn></td>
                </tr>
            </tbody>
          </template>
        </v-simple-table>
  </section>

</main>
</template>

<script>
    export default {
        name: "deleteOrder",
      data() {
          return {
            orders: [],
            currentOrder: {}
          }},
            async created() {
        await this.fetchOrders();
      },
      mounted() {
          let token = localStorage.getItem('auth_token');
        console.log(token);
        this.$axios.get('http://127.0.0.1:8000/total_storage/?api_token='+token, {headers: {'Authorization' : "Token "+token}})
          .then(response => {this.orders = response.data;
            console.log(response);
          })
          .catch((error) => {
            console.log(error)
          })
      },
      methods: {
          goStorage() {
            this.$router.push({name:'Storage'})
          },
          async removeOrder(order){
            let token = localStorage.getItem('auth_token');
            const { id } = order;
            const response = await fetch(`http://127.0.0.1:8000/delete-order/${id}?api_token=`+token, {
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization' : "Token "+token
              },
              method: "DELETE",
              });
            if (response.status !== 204) {
              alert(JSON.stringify(await response.json(), null, 2));
            }
            await this.fetchOrders();
        },
        async fetchOrders() {
            const response = await fetch('http://127.0.0.1:8000/total_storage/');
            this.orders = await response.json()
          },
          }
    }
</script>

<style scoped>
h1{
  text-align: right;
}
  h2{
    text-align: center;
    padding: 10px;
  }
</style>
