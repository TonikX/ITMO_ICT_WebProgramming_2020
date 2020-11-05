<template>
  <main>
    <section class="content">
      <h2>Visitors: {{ visitors.length }}</h2>
      <v-container fluid>
        <v-row>
          <v-card class="my-1 mx-1"  width=350 color="brown" dark v-for="visitor in visitors" :key="visitor.id">
            <v-card-title class="headline"> Library card number: {{ visitor.library_card_number }} </v-card-title>
            <v-card-subtitle class="title"> Full name visitor: {{ visitor.full_name }} </v-card-subtitle>
            <v-card-subtitle> Birth date: {{ visitor.birth_date }} </v-card-subtitle>
            <v-card-subtitle> Passport ID: {{ visitor.passport_ID }} </v-card-subtitle>
            <v-card-subtitle> Adress: {{ visitor.adress }} </v-card-subtitle>
            <v-card-subtitle> Phone number: {{ visitor.phone_number }} </v-card-subtitle>
            <v-card-subtitle> Education: {{ visitor.education }} </v-card-subtitle>
            <v-card-subtitle> Academic degree: {{ visitor.academic_degree }} </v-card-subtitle>
            <v-card-subtitle> Data last registration: {{ visitor.data_last_registration }} </v-card-subtitle>
            <v-card-subtitle> Delete: {{ visitor.failure }} </v-card-subtitle>
          </v-card>
        </v-row>
      </v-container>
    </section>
  </main>
</template>
<script>
  export default {
    name: 'Visitors',
    data () {
      return {
          visitors: []
      }
    },
    mounted() {
      this.axios
      .get(`http://192.168.99.100:8000/api/visitors`)
      .then(response => { this.showVisitors(response.data) })
      .catch(err => { console.error(err) })
    },
    methods: {
      showVisitors(data) {
        this.visitors = []
        for (let i = 0; i < data.length; i++) {
          let visitor = {}
          visitor.library_card_number = data[i].library_card_number
          visitor.full_name = data[i].full_name
          visitor.birth_date = data[i].birth_date
          visitor.passport_ID = data[i].passport_ID
          visitor.adress = data[i].adress
          visitor.phone_number = data[i].phone_number
          visitor.education = data[i].education
          visitor.academic_degree = data[i].academic_degree
          visitor.data_last_registration = data[i].data_last_registration
          visitor.failure = data[i].failure
          console.log(visitor)
          this.visitors.push(visitor)
        }
      },
    }
  }
</script>
<style></style>
