<template>
  <main>
    <v-col cols="12">
      <v-form v-model="valid">
        <v-container>
          <v-row>
            <v-col cols="12" md="4">
              <v-text-field v-model="from_point" label="Откуда"></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="to_point" label="Куда"></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="price" label="Цена билета"></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="4">
              <v-text-field v-model="plane_model" label="Модель самолёта"></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="tickets_left" label="Количество оставшихся билетов"></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-checkbox v-model="is_transit" label="Нет транзитных точек" required></v-checkbox>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-btn class="mr-4" @click="submit">
                <v-icon>mdi-filter</v-icon>Отфильтровать
              </v-btn>
              <v-btn @click="clear">
                <v-icon>mdi-autorenew</v-icon>Очистить
              </v-btn>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </v-col>
    <v-col cols="12">
      <h4 v-if="cards.length === 0">Извините, по вашему запросу ничего не найдено...</h4>
      <v-card class="my-2" color="#385F73" dark v-for="card in cards" :key="card.id">
        <v-card-title class="headline">{{ card.title }}</v-card-title>
        <br />
        <v-card-subtitle>Осталось {{ card.tickets_left }} билетов<span v-if="card.isTransit"> | Есть пересадки</span></v-card-subtitle>
        {{ card.price }} руб./билет
        <v-card-actions>
          <v-btn text @click="buyTicket(card.id)">Купить</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
    <v-dialog
      v-model="success"
      max-width="290"
    >
      <v-card>
        <v-card-title class="headline">Спасибо!</v-card-title>

        <v-card-text>
          Билет появится в Вашем <router-link to="/cabinet">кабинете</router-link>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
            @click="success = false"
          >
            Ок
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </main>
</template>
<script>
export default {
  name: 'Flights',
  data () {
    return {
      valid: false,
      flightsData: '',
      cards: [],
      from_point: '',
      to_point: '',
      price: 0,
      plane_model: '',
      tickets_left: 0,
      is_transit: false,
      url: 'http://127.0.0.1:8000/api/flights',
      success: false
    }
  },
  mounted () {
    this.axios
      .get(this.url)
      .then(response => { this.flightsData = response; this.updateCards() })
      .catch(error => { console.error(error) })
  },
  methods: {
    updateCards () {
      let data = this.flightsData.data

      this.cards = []

      let flights = data.flights
      let transitPoints = data.transit_points
      let tickets = data.tickets

      for (let flight of flights) {
        let id = flight.id
        let title = `${flight.plane.company.name}: ${flight.route.from_point} - ${flight.route.to_point} | Plane: ${flight.plane.model}`
        let filteredTickets = this.getTickets(tickets, id)
        let routeId = flight.route.id
        let isTransit = this.isTransit(transitPoints, routeId)

        let card = {}
        card.id = id
        card.title = title
        card.tickets_left = filteredTickets.amount
        card.price = filteredTickets.price
        card.isTransit = isTransit

        this.cards.push(card)

        this.url = 'http://127.0.0.1:8000/api/flights'
      }
    },
    getTickets (tickets, flightId) {
      let result

      for (let ticket of tickets) {
        if (ticket.flight.id === flightId && ticket.state === 'Left') {
          result = ticket
        }
      }

      return result
    },
    isTransit (transitPoints, routeId) {
      for (let point of transitPoints) {
        if (point.route.id === routeId) {
          return true
        }
      }
      return false
    },
    submit () {
      let isTransit = 'yes'
      if (this.is_transit) {
        isTransit = 'no'
      }

      let price = 9999999
      let ticketsLeft = 9999999

      if (this.price > 0) {
        price = this.price
      }

      if (this.tickets_left > 0) {
        ticketsLeft = this.tickets_left
      }

      this.url = `http://127.0.0.1:8000/api/flights?from_point=${this.from_point}&to_point=${this.to_point}&price=${price}&plane_model=${this.plane_model}&tickets_left=${ticketsLeft}&is_transit=${isTransit}`

      this.axios
        .get(this.url)
        .then(response => { this.flightsData = response; this.updateCards() })
        .catch(error => { console.error(error) })
    },
    clear () {
      this.from_point = ''
      this.to_point = ''
      this.price = 0
      this.plane_model = ''
      this.tickets_left = 0
      this.is_transit = false

      this.url = 'http://127.0.0.1:8000/api/flights'
    },
    buyTicket (flightID) {
      if (!localStorage.getItem('username') && !localStorage.getItem('token')) {
        this.$router.push('/login')
        return
      }

      let userID = localStorage.getItem('id')

      this.axios
        .post('http://127.0.0.1:8000/api/user/ticket/', { 'user': userID, 'flight': flightID })
        .then(response => { console.log(response); this.success = true })
        .catch(err => { console.error(err) })
    }
  }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

</style>
