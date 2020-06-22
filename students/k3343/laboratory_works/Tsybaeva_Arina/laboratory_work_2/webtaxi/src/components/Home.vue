<template>
<div>
  <main class="pa-2">
    <section>
      <h3 align="left">Наши молодые активисты: </h3>
      <v-simple-table dense>
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-center">Фамилия</th>
                  <th class="text-center">Возраст</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in clients">
                  <td class="text-center">{{ item.name }}</td>
                  <td class="text-center">{{ item.age }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
    </section>
    <section>
      <h3 align="left">Количество заказов в зависимости от дня недели: </h3>
        <v-simple-table dense>
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-center">День недели</th>
                  <th class="text-center">Процентная занятость</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in visuals">
                  <td class="text-center">{{ item.week_day }}</td>
                  <td class="text-center">{{ item.percent }} %</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
    </section>
    <section>
      <h3 align="left">Топ-3 самых сдаваемых категорий мусора:</h3>
        <v-simple-table dense>
            <template v-slot:default>
              <tbody>
                <tr v-for="item in trash">
                  <td class="text-left">{{ item.category }}</td>
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
  name: 'Home',
  data() {
    return {
      clients : [],
      visuals: [],
      trash: []
    }
  },
        async created() {
        await this.fetchClients();
        await this.fetchOrders();
        await this.fetchTrash()
        },
  methods: {
              async fetchClients() {
            const response = await fetch('http://127.0.0.1:8000/client/?age_max=40');
            this.clients = await response.json()
          },
                  async fetchOrders() {
            const response = await fetch('http://127.0.0.1:8000/week/');
            this.visuals = await response.json()
          },
             async fetchTrash() {
            const response = await fetch('http://127.0.0.1:8000/top/');
            this.trash = await response.json()
          },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h3{
    padding: 10px;
  }
</style>
