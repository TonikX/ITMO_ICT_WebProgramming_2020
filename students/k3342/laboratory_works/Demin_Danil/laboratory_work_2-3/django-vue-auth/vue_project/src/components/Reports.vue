<template>
  <main>
    <section class="content">
      <h2>Total reports: {{ reports.length }}</h2>
      <v-container fluid>
        <v-row>
          <v-card class="my-2 mx-2" width=250 color="primary" dark v-for="report in reports" :key="report.id">
            <v-card-subtitle>In cage {{ report.cage_id }}</v-card-subtitle>
            <v-card-text>{{ report.content }}</v-card-text>
            <v-card-text>Submitted by: {{ report.worker }}</v-card-text>
          </v-card>
        </v-row>
      </v-container>
      <v-btn href="/reports/add">New Report</v-btn>
    </section>
  </main>
</template>
<script>
  export default {
    name: 'Reports',
    data () {
      return {
          reports: []
      }
    },
    mounted() {
      this.axios
      .get(`http://127.0.0.1:8000/api/reports`)
      .then(response => { this.showReports(response.data) })
      .catch(err => { console.error(err) })
    },
    methods: {
      showReports(data) {
        this.reports = []
        for (let i = 0; i < data.length; i++) {
          let report = {}
          report.cage_id = data[i].cage_id
          report.chicken = data[i].chicken
          report.content = data[i].content
          report.worker = data[i].worker
          console.log(report)
          this.reports.push(report)
        }
      },
    }
  }
</script>
<style></style>
