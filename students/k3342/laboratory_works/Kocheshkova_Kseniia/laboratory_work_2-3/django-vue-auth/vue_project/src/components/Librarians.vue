<template>
  <main>
    <section class="content">
      <h2>Librarians: {{ librarians.length }}</h2>
      <v-container fluid>
        <v-row>
          <v-card class="my-1 mx-1"  width=400 color="brown" dark v-for="librarian in librarians" :key="librarian.id">
            <v-card-title class="headline"> Name: {{ librarian.librarian_name }} </v-card-title>
            <v-card-subtitle class="title"> Passport number: {{ librarian.passport }} </v-card-subtitle>
            <v-card-subtitle> Salary: {{ librarian.salary }} </v-card-subtitle>
          </v-card>
        </v-row>
      </v-container>
    </section>
  </main>
</template>
<script>
  export default {
    name: 'Librarians',
    data () {
      return {
          librarians: []
      }
    },
    mounted() {
      this.axios
      .get(`http://192.168.99.100:8000/api/librarians`)
      .then(response => { this.showLibrarians(response.data) })
      .catch(err => { console.error(err) })
    },
    methods: {
      showLibrarians(data) {
        this.librarians = []
        for (let i = 0; i < data.length; i++) {
          let librarian = {}
          librarian.librarian_name = data[i].librarian_name
          librarian.passport = data[i].passport
          librarian.salary = data[i].salary
          console.log(librarian)
          this.librarians.push(librarian)
        }
      },
    }
  }
</script>
<style></style>
