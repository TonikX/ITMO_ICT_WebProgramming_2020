<template>
  <main class="grey lighten-5 pa-2">
    <!-- {{ shows }} {{ shows.data }} {{ showids }} {{ records.data }} -->
    <section>
      <h1 class="display-1">Ежегодные собачьи выставки</h1>
      <v-col cols="8" class="mx-auto">
        <v-card max-width="400" class="showcard teal lighten-1 ma-3" dark v-for="card in cards" :key="card.id">
          <v-card-title>{{ card.show_presentment }}</v-card-title>
        </v-card>
      </v-col>
    </section>
    <section>
      <h1 class="display-1">Наши спонсоры</h1>
      <v-col cols="8" class="mx-auto">
        <v-card max-width="400" class="showcard cyan ma-3" dark v-for="fund in funds" :key="fund.id">
          <v-card-title>{{ fund.funder_name }}</v-card-title>
        </v-card>
      </v-col>
    </section>
    <section>
      <h1 class="display-1">Наши эксперты</h1>
      <v-col cols="8" class="mx-auto">
        <v-card max-width="400" class="showcard lime darken-1 ma-3" dark v-for="exp in exps" :key="exp.id">
          <v-card-title>{{ exp.expert_name }} {{exp.expert_surname}}</v-card-title>
          <v-card-subtitle>{{exp.expert_club}}</v-card-subtitle>
        </v-card>
      </v-col>
    </section>
    <section>
      <h1 class="display-1">Наши лучшие участники</h1>
      <v-col cols="8" class="mx-auto">
        <v-card max-width="400" class="showcard yellow darken-3 ma-3" dark v-for="action in actions" :key="action.id">
          <v-card-title>{{ action.dog_name }}</v-card-title>
          <v-card-subtitle>{{ action.dog_breed }}</v-card-subtitle>
          <v-card-text>{{ action.show_presentment }} Результат: {{ action.act }}</v-card-text>
        </v-card>
      </v-col>
    </section>
  </main>
</template>

<script>
export default {
  name: 'Shows',
  data () {
    return {
      cards: [],
      shows: null,
      funds: [],
      exps: [],
      actions: []
    }
  },
  components: {

  },
  mounted () {
    this.axios
      .get(`http://127.0.0.1:8000/api/shows/all`)
      .then(response => { this.shows = response; this.updateStats() })
      .catch(error => { console.error('An API error: ', error) })

    this.axios
      .get(`http://127.0.0.1:8000/api/funders/all`)
      .then(response => { this.funders = response; this.updateFunders() })
      .catch(error => { console.error('An API error: ', error) })

    this.axios
      .get(`http://127.0.0.1:8000/api/experts/all`)
      .then(response => { this.experts = response; this.updateExperts() })
      .catch(error => { console.error('An API error: ', error) })

    this.axios
      .get(`http://127.0.0.1:8000/api/acts/all`)
      .then(response => { this.acts = response; this.updateActs() })
      .catch(error => { console.error('An API error: ', error) })
  },
  methods: {
    updateStats () {
      for (let i = 0; i < this.shows.data.length; i++) {
        let card = {}
        card.show_presentment = this.shows.data[i].show_presentment
        this.cards.push(card)
      }
    },
    updateFunders () {
      for (let i = 0; i < this.funders.data.length; i++) {
        let fund = {}
        fund.funder_name = this.funders.data[i].funder_name
        this.funds.push(fund)
      }
    },
    updateExperts () {
      for (let i = 0; i < this.experts.data.length; i++) {
        let exp = {}
        exp.expert_name = this.experts.data[i].expert_name
        exp.expert_surname = this.experts.data[i].expert_surname
        exp.expert_club = this.experts.data[i].expert_club
        this.exps.push(exp)
      }
    },
    updateActs () {
      let data = this.acts.data
      for (let i = 0; i < this.acts.data.length; i++) {
        let action = {}
        action.dog_name = data[i].act_dog.dog_name
        action.dog_breed = data[i].act_dog.dog_breed
        action.show_presentment = data[i].act_show.show_presentment
        action.act = parseInt(data[i].act_1) + parseInt(data[i].act_2) + parseInt(data[i].act_3)
        this.actions.push(action)
      }
      this.actions = this.actions.sort(function (b, a) {
        return a.act - b.act
      })
      this.actions = this.actions.slice(0, 3)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal
}
</style>
