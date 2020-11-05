<template>
  <main>
    <section class="content">
      <h2>Halls list: {{ halls.length }}</h2>
      <v-container fluid>
        <v-row>
          <v-card class="my-1 mx-1"  width=400 color="brown" dark v-for="hall in halls" :key="hall.id">
            <v-card-title class="headline"> Name: {{ hall.hall_name }} </v-card-title>
            <v-card-subtitle> Max people: {{ hall.max_visitor }} </v-card-subtitle>
            <v-card-subtitle> Start work at {{ hall.start_time_working }} and finish at {{ hall.finish_time_working }} </v-card-subtitle>
            <v-card-subtitle> Weekend: {{ hall.weekend }} </v-card-subtitle>
          </v-card>
        </v-row>
      </v-container>
    </section>
  </main>
</template>
<script>
  export default {
    name: 'Halls',
    data () {
      return {
          halls: []
      }
    },
    mounted() {
      this.axios
      .get(`http://192.168.99.100:8000/api/halls`)
      .then(response => { this.showHalls(response.data) })
      .catch(err => { console.error(err) })
    },
    methods: {
      showHalls(data) {
        this.halls = []
        for (let i = 0; i < data.length; i++) {
          let hall = {}
          hall.hall_name = data[i].hall_name
          hall.max_visitor = data[i].max_visitor
          hall.start_time_working = data[i].start_time_working
          hall.finish_time_working = data[i].finish_time_working
          hall.weekend = data[i].weekend
          console.log(hall)
          this.halls.push(hall)
        }
      },
    }
  }
</script>
<style></style>
