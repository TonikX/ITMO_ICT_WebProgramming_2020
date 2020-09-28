<template>
  <main>
    <section class="content">
      <h2>Total chickens: {{ chickens.length }}</h2>
      <v-container fluid>
        <v-row>
          <v-card class="my-2 mx-2" width=250 color="primary" dark v-for="chicken in chickens" :key="chicken.id">
            <v-card-title class="headline"> Breed {{ chicken.breed }} </v-card-title>
            <v-card-subtitle>In cage {{ chicken.cage_id }}</v-card-subtitle>
            <v-card-text>Weighs {{ chicken.weight }} kg, is {{ chicken.age }} years old.</v-card-text>
            <v-card-text>Last month: {{ chicken.productivity }} eggs produced</v-card-text>
          </v-card>
        </v-row>
      </v-container>
      <v-btn href="/chickens/add">New Chicken</v-btn>
    </section>
  </main>
</template>
<script>
  export default {
    name: 'Chickens',
    data () {
      return {
          chickens: []
      }
    },
    mounted() {
      this.axios
      .get(`http://127.0.0.1:8000/api/chickens`)
      .then(response => { this.showChickens(response.data) })
      .catch(err => { console.error(err) })
    },
    methods: {
      showChickens(data) {
        this.chickens = []
        for (let i = 0; i < data.length; i++) {
          let chicken = {}
          chicken.cage_id = data[i].cage_id
          chicken.breed = data[i].breed
          chicken.productivity = data[i].productivity
          chicken.weight = data[i].weight
          chicken.age = data[i].age
          console.log(chicken)
          this.chickens.push(chicken)
        }
      },
    }
  }
</script>
<style></style>
