<template>
  <main>
    <section class="content">
      <h2>Cages: {{ cages.length }}</h2>
      <v-container fluid>
        <v-row>
          <v-card class="my-2 mx-2" width=250 color="primary" dark v-for="cage in cages" :key="cage.id">
            <v-card-title class="headline"> Assigned worker: {{ cage.worker }} </v-card-title>
            <v-card-subtitle>Building: {{ cage.building }} </v-card-subtitle>
            <v-card-text>Cage number {{ cage.number }}, in row {{ cage.row }}</v-card-text>
          </v-card>
        </v-row>
      </v-container>
    </section>
  </main>
</template>
<script>
  export default {
    name: 'Cages',
    data () {
      return {
          cages: []
      }
    },
    mounted() {
      this.axios
      .get(`http://127.0.0.1:8000/api/cages`)
      .then(response => { this.showCages(response.data) })
      .catch(err => { console.error(err) })
    },
    methods: {
      showCages(data) {
        this.cages = []
        for (let i = 0; i < data.length; i++) {
          let cage = {}
          cage.worker = data[i].worker
          cage.building = data[i].building
          cage.row = data[i].row
          cage.number = data[i].number
          console.log(cage)
          this.cages.push(cage)
        }
      },
    }
  }
</script>
<style></style>
