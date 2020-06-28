<template>
  <main>
    <div class="d-flex flex-column">
      <div class="filter d-flex flex-row">
        <div class="m-auto">
          <b-form inline>
            <div class="m-1">
              <label for="arrival">Отправление</label>
              <b-form-input id="arrival" v-model="arrival"></b-form-input>
            </div>
            <div class="m-1">
              <label for="departure">Прибытие</label>
              <b-form-input id="departure" v-model="departure"></b-form-input>
            </div>
            <div class="m-1">
              <label for="tickets">Количество билетов</label>
              <b-form-input id="tickets" type="number" v-model="tickets"></b-form-input>
            </div>
            <div class="m-1">
              <label for="price">Цена</label>
              <b-form-input type="number" id="price" v-model="price"></b-form-input>
            </div>
            <div class="m-1">
              <b-form-checkbox type="checkbox" id="transit" v-model="transit">Транзитные посадки</b-form-checkbox>
            </div>
            <div class="m-1 mt-4">
              <b-button variant="info" @click="filterFlights()">Найти</b-button>
              <b-button variant="warning" @click="clear()">Сброс</b-button>
            </div>
          </b-form>
        </div>
      </div>
      <div class="content container mt-5">
        <h2 class="mb-5" v-if="flights.length > 0">Найдено {{ flights.length }} полётов</h2>
        <h2 class="mb-5" v-if="flights.length === 0">Ничего не найдено :(</h2>
        <flight v-for="flight in flights" :key="flight.id" :arrival="flight.arrival" :departure="flight.departure" :price="flight.price" :tickets="flight.tickets" :transit="flight.is_transit" :distance="flight.distance" :flightID="flight.id"></flight>
      </div>
    </div>
  </main>
</template>
<script>
import Flight from './Flight'
export default {
  name: 'Airport',
  data() {
    return {
      arrival: '',
      flights: [],
      tickets: '',
      price: '',
      departure: '',
      date: '',
      transit: false
    }
  },
  mounted() {
    this.axios
      .get(`http://${window.location.hostname}:8000/api/flights/`)
      .then(response => { console.log(response);
        this.showFlights(response.data) })
      .catch(err => { console.error(err) })
  },
  methods: {
    showFlights(data) {

      this.flights = []

      for (let i = 0; i < data.length; i++) {
        let flight = {}
        flight.id = data[i].id
        flight.tickets = data[i].saled_tickets_amount
        flight.distance = data[i].distance
        flight.arrival = data[i].arrival_point
        flight.departure = data[i].departure_point
        flight.is_transit = data[i].is_transit
        flight.price = data[i].price

        this.flights.push(flight)
      }

    },
    filterFlights() {
      let transit = this.transit === true ? '1' : '0'
      this.axios
        .get(`http://${window.location.hostname}:8000/api/flights/?arrival=${this.arrival}&departure=${this.departure}&tickets=${this.tickets}&price=${this.price}&is_transit=${transit}`)
        .then(response => { console.log(response);
          this.showFlights(response.data) })
        .catch(err => { console.error(err) })
    },
    clear() {
      this.arrival = ''
      this.tickets = ''
      this.price = ''
      this.departure = ''
      this.date = ''
      this.transit = false

      this.axios
        .get(`http://${window.location.hostname}:8000/api/flights/`)
        .then(response => { console.log(response);
          this.showFlights(response.data) })
        .catch(err => { console.error(err) })
    }

  },
  components: {
    Flight
  }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
