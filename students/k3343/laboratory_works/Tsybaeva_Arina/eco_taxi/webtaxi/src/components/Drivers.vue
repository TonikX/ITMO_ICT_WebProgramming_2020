<template>
  <div>
    <section>
      <h2 align="center">Наши водители</h2>
      <v-simple-table>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center">Фамилия</th>
              <th class="text-center">Возраст</th>
              <th class="text-center"> </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in drivers">
              <td>{{ item.name }}</td>
              <td>{{ item.age }}</td>
              <td> <v-btn text small color="error" @click="removeDriver(item)">Уволить</v-btn></td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </section>
        <div>
          <h2 align="center">Добавить водителя</h2>
          <v-text-field label="Фамилия" :rules="rules" hide-details="auto"  v-model="currentDriver.name"></v-text-field>
          <v-text-field label="Возраст" v-model.number="currentDriver.age"></v-text-field>
          <v-text-field label="Email" v-model="currentDriver.email"></v-text-field>
          <v-text-field label="Телефон" v-model="currentDriver.telephone"></v-text-field>
          <v-text-field label="Модель и марка машины" v-model="currentDriver.car_model"></v-text-field>
          <v-text-field label="Номер машины" v-model="currentDriver.car_number"></v-text-field>
          <h2 align="center"><v-btn rounded color="green" dark @click="createDriver()">Добавить</v-btn></h2>
        </div>
  </div>
</template>

<script>
    export default {
        name: "Drivers",
      data () {
          return {
            drivers: [],
            currentDriver: {},
          };
      },
      async created() {
        await this.fetchDrivers();
      },
      methods: {
          async fetchDrivers() {
            const response = await fetch('http://127.0.0.1:8000/drivers/');
            this.drivers = await response.json()
          },
          async createDriver() {
            let token = localStorage.getItem('auth_token');
            const response = await fetch('http://127.0.0.1:8000/new-driver/?api_token='+token, {
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization' : "Token "+token
              },
              method: "POST",
              body: JSON.stringify(this.currentDriver)
              });
            if (response.status !== 201) {
              alert(JSON.stringify(await response.json(), null, 2));
            }
            await this.fetchDrivers();
          },
        async removeDriver(driver) {
            let token = localStorage.getItem('auth_token');
            const { id } = driver;
            const response = await fetch(`http://127.0.0.1:8000/delete-driver/${id}?api_token=`+token, {
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
            await this.fetchDrivers();
        }
      }
    }
</script>

<style scoped>
   table {
    width: 300px; /* Ширина таблицы */
    border: 1px solid green; /* Рамка вокруг таблицы */
    margin: auto; /* Выравниваем таблицу по центру окна  */
   }
   td {
    text-align: center; /* Выравниваем текст по центру ячейки */
   }

    h2 {padding: 25px;}
input {
border: 1px solid #f7f7f7;
padding: 0.75rem 1.25rem;
}
</style>
