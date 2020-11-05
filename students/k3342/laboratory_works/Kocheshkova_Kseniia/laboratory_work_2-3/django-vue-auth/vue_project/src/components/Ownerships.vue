<template>
  <main>
    <section class="content">
      <h2>Total ownerships: {{ ownerships.length }}</h2>
      <v-container fluid>
        <v-row>
          <v-card class="my-2 mx-2" width=250 color="primary" dark v-for="ownership in ownerships" :key="ownership.id">
            <v-card-title class="headline"> Book {{ ownership.book }} </v-card-title>
            <v-card-text>Person {{ ownership.visitor }}</v-card-text>
            <v-card-text>Was issued by {{ ownership.librarian }}</v-card-text>
            <v-card-text>Start of owning {{ ownership.start_of_owning }} ans finish is {{ ownership.finish_of_owning }}.</v-card-text>
            <v-card-text>Was returning: {{ ownership.returning }} </v-card-text>
          </v-card>
        </v-row>
      </v-container>
      <v-btn href="/ownerships/add">New ownership</v-btn>
    </section>
  </main>
</template>
<script>
  export default {
    name: 'Ownerships',
    data () {
      return {
          ownerships: []
      }
    },
    mounted() {
      this.axios
      .get(`http://127.0.0.1:8000/api/ownerships`)
      .then(response => { this.showOwnerships(response.data) })
      .catch(err => { console.error(err) })
    },
    methods: {
      showOwnerships(data) {
        this.ownerships = []
        for (let i = 0; i < data.length; i++) {
          let ownership = {}
          ownership.visitor = data[i].visitor
          ownership.book = data[i].book
          ownership.librarian = data[i].librarian
          ownership.start_of_owning = data[i].start_of_owning
          ownership.finish_of_owning = data[i].finish_of_owning
          ownership.returning = data[i].returning
          console.log(ownership)
          this.ownerships.push(ownership)
        }
      },
    }
  }
</script>
<style></style>
