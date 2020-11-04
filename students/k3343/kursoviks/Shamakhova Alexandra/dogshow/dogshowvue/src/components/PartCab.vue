<template>
  <main>
    <v-col cols="8" class="my-1 mx-auto">
      <h2>Кабинет участника</h2>
    </v-col>
    <section>
      <v-col cols="8" class="mx-auto">
        <h3>Ваши собаки:</h3>
        <p>Всего собак: {{ requestcards.length }}</p>
        <v-card class="my-2" color="teal lighten-1" dark v-for="card in requestcards" :key="card.id">
          <v-card-title class="headline">{{ card.dog_name }} -- {{ card.dog_breed }}</v-card-title>
          <v-card-subtitle>Клуб: {{ card.dog_club}}</v-card-subtitle>
          <v-card-text>
            <p>Возраст: {{ card.dog_age }}; {{ card.dog_class }}</p>
            <p>№ документа: {{ card.dog_document }}</p>
            <p>Родители: {{ card.dog_mother }} и {{ card.dog_father }}</p>
            <p>Дата прививки: {{card.dog_vaccination}}</p>
          </v-card-text>
        </v-card>
        <v-btn class="mr-4" :to="'/adddog'" color="light-green darken-4" dark>Добавить собаку</v-btn>
      </v-col>
    </section>

  </main>
</template>

<script>
export default {
  name: 'PartCab',
  created () {
    if (sessionStorage.getItem('token') === null || sessionStorage.getItem('user') === null) {
      this.$router.push('/login')
    }
  },
  mounted () {
    this.axios
      .get(`http://127.0.0.1:8000/api/human/all?user=${sessionStorage.getItem('user')}`)
      .then(response => { console.log(response); this.getRequest(response.data) })
      .catch(err => { console.error(err) })

  },
  data () {
    return {
      requestcards: [],
      check: ''
    }
  },
  methods: {
    getRequest (data) {
      this.axios
        .get(`http://127.0.0.1:8000/api/dogs/all?dog_owner=${data[0].id}`)
        .then(response => { console.log(response); this.getRequests(response.data) })
        .catch(err => { console.error(err) })
    },
    getRequests (data) {
      for (let i = 0; i < data.length; i++) {
        let requestcard = {}
        requestcard.id = data[i].id
        requestcard.dog_name = data[i].dog_name
        requestcard.dog_breed = data[i].dog_breed
        requestcard.dog_club = data[i].dog_club
        requestcard.dog_age = data[i].dog_age
        requestcard.dog_class = data[i].dog_class
        requestcard.dog_document = data[i].dog_document
        requestcard.dog_mother = data[i].dog_mother
        requestcard.dog_father = data[i].dog_father
        requestcard.dog_vaccination = data[i].dog_vaccination

        this.requestcards.push(requestcard)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h2, h3 {
  font-weight: normal;
}
</style>
