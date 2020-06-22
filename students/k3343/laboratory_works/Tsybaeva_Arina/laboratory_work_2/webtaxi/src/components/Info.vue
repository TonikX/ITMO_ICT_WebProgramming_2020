<template>
    <div>
          <h2 align="center">Добавьте информацию о себе</h2>
          <v-text-field label="Фамилия" :rules="rules" hide-details="auto"  v-model="currentClient.name"></v-text-field>
          <v-text-field label="Возраст" v-model.number="currentClient.age"></v-text-field>
          <v-text-field label="Email" v-model="currentClient.email"></v-text-field>
          <v-text-field label="Телефон" v-model="currentClient.telephone"></v-text-field>
          <v-text-field label="Адрес" v-model="currentClient.address"></v-text-field>
          <h2 align="center"><v-btn rounded color="green" dark @click="createClient()">Добавить</v-btn></h2>
        </div>
</template>

<script>
    export default {
        name: "Info",
      data () {
          return {
            currentClient: {}
          }
      },
      methods : {
        async createClient() {
            const response = await fetch('http://127.0.0.1:8000/add_client/', {
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              },
              method: "POST",
              body: JSON.stringify(this.currentClient)
              });
          this.$router.push({name: 'login'})
            if (response.status !== 201) {
              alert(JSON.stringify(await response.json(), null, 2));
            }

    }}}
</script>

<style scoped>

</style>
