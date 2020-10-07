<template>
  <main>
    <section class="content">
      <h2>Workers: {{ workers.length }}</h2>
      <v-card class="my-2 mx-2" color="primary" dark v-for="worker in workers" :key="worker.id">
        <v-card-title class="headline"> Passport number: {{ worker.passport }} </v-card-title>
        <v-card-subtitle>Salary: {{ worker.salary }} </v-card-subtitle>
      </v-card>
    </section>
  </main>
</template>
<script>
  export default {
    name: 'Workers',
    data () {
      return {
          workers: []
      }
    },
    mounted() {
      this.axios
      .get(`http://127.0.0.1:8000/api/workers`)
      .then(response => { this.showWorkers(response.data) })
      .catch(err => { console.error(err) })
    },
    methods: {
      showWorkers(data) {
        this.workers = []
        for (let i = 0; i < data.length; i++) {
          let worker = {}
          worker.passport = data[i].passport
          worker.salary = data[i].salary
          console.log(worker)
          this.workers.push(worker)
        }
      },
    }
  }
</script>
<style></style>
