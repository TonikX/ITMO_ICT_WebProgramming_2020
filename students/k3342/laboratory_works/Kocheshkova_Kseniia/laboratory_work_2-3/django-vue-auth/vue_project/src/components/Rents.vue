<template>
  <main>
    <section class="content">
      <h2>Total rents: {{ rents.length }}</h2>
          <v-card class="my-2 mx-2" width=550 color="brown" dark v-for="rent in rents" :key="rent.id">
            <v-card-title class="headline"> Event: <i>{{ rent.event_name }}</i> </v-card-title>
            <v-card-subtitle class="title"> {{ rent.type_event }}</v-card-subtitle>
            <v-card-subtitle> Hall: {{ rent.hall }}</v-card-subtitle>
            <v-card-subtitle>Start time: {{ rent.data_time }}</v-card-subtitle>
            <v-card-subtitle>Approximate duration (in hours): {{ rent.time_period }}</v-card-subtitle>
            <v-card-subtitle>Max people: {{ rent.max_people }}</v-card-subtitle>
            <v-card-subtitle>Organised by: {{ rent.librarian }}</v-card-subtitle>
          </v-card>
      <v-btn href="/rents/add">New rent</v-btn>
    </section>
  </main>
</template>
<script>
  export default {
    name: 'Rents',
    data () {
      return {
          rents: []
      }
    },
    mounted() {
      this.axios
      .get(`http://192.168.99.100:8000/api/rents`)
      .then(response => { this.showRents(response.data) })
      .catch(err => { console.error(err) })
    },
    methods: {
      showRents(data) {
        this.rents = []
        for (let i = 0; i < data.length; i++) {
          let rent = {}
          rent.event_name = data[i].event_name
          rent.type_event = data[i].type_event
          rent.hall = data[i].hall
          rent.data_time = data[i].data_time
          rent.time_period = data[i].time_period
          rent.max_people = data[i].max_people
          rent. library = data[i]. library
          console.log(rent)
          this.rents.push(rent)
        }
      },
    }
  }
</script>
<style></style>
