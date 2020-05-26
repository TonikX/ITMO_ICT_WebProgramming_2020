<template>
  <div>
    <h2 align="center">Создать заказ</h2>
    <v-text-field label="Масса мусора" :rules="rules" hide-details="auto"  v-model.number="currentOrder.mass"></v-text-field>
    <v-text-field label="Цена" v-model.number="currentOrder.cost"></v-text-field>
    <v-text-field label="Дата" v-model="currentOrder.data"></v-text-field>
    <v-text-field label="Водитель" v-model="currentOrder.driver"></v-text-field>
    <v-text-field label="Клиент" v-model="currentOrder.client"></v-text-field>
    <v-text-field label="Категория" v-model="currentOrder.category"></v-text-field>
    <h2 align="center"><v-btn rounded color="green" dark @click="createOrder()">Создать</v-btn></h2>
  </div>
</template>

<script>
    export default {
        name: "Order",
      data () {
          return {
            currentOrder: {}
          }
      },
      methods : {
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

    }}}
</script>

<style scoped>
     h2 {padding: 25px;}

</style>
