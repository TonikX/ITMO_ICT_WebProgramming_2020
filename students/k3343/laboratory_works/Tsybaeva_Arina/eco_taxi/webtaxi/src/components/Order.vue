<template>
  <div>
    <h2 align="center">Создать заказ</h2>
    <v-text-field label="Масса мусора"  v-model.number="currentOrder.mass"></v-text-field>
    <v-text-field label="Цена" v-model.number="currentOrder.cost"></v-text-field>
    <v-text-field label="Дата" v-model="currentOrder.data"></v-text-field>
    <v-select v-model="currentOrder.driver" :items="drivers" label="Водитель"></v-select>
    <v-select v-model="currentOrder.client" :items="clients" label="Клиент"></v-select>
    <v-select v-model="currentOrder.category" :items="categories" label="Категория"></v-select>
    <h2 align="center"><v-btn rounded color="green" dark @click="createOrder()">Создать</v-btn></h2>
  </div>
</template>

<script>
    export default {
        name: "Order",
      data () {
          return {
            currentOrder: {
              driver: '',
              mass: '',
              client : '',
              data: '',
              cost: '',
              category: ''
            },
            driversData: [],
            drivers: [],
            clients: [],
            clientData: [],
            categories: [],
            categoriesData: []
          }
      },
        mounted () {
    this.$axios
      .get('http://127.0.0.1:8000/drivers/')
      .then(response => { this.driversData = response; this.updateDrivers() });
    this.$axios.get('http://127.0.0.1:8000/category/')
          .then(response =>{this.categoriesData = response; this.updateCategories()});
    this.$axios.get('http://127.0.0.1:8000/clients/')
          .then(response => {this.clientData = response; this.updateClients()})
  },
      methods : {
          updateDrivers(){
                  let data = this.driversData.data
             for (let driver of data) {
        this.drivers.push({'text': `${driver.name}`, 'value': `${driver.id}`})
      }

    },
        updateClients() {
                let data = this.clientData.data
             for (let client of data) {
        this.clients.push({'text': `${client.name}`, 'value': `${client.id}`})
      }
        },
        updateCategories(){
            let data = this.categoriesData.data
             for (let category of data) {
               this.categories.push({'text': `${category.name}`, 'value': `${category.id}`})

             }},
        async createOrder() {
            let token = localStorage.getItem('auth_token');
            const response = await fetch('http://127.0.0.1:8000/order/?api_token='+token, {
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization' : "Token "+token
              },
              method: "POST",
              body: JSON.stringify(this.currentOrder)
              });
            alert("Спасибо за заказ!")
            this.$router.push({name: "home"});
            if (response.status !== 201) {
              alert(JSON.stringify(await response.json(), null, 2));
            }


    },
      }}
</script>

<style scoped>
     h2 {padding: 25px;}

</style>
