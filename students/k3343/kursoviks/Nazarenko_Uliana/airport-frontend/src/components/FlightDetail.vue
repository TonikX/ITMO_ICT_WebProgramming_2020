<template>
  <div class="container">
    <b-card>
      <b-card-title>
        {{ company }}, {{ arrival }} - {{ departure }}
      </b-card-title>
      <b-card-sub-title>Цена: {{ price }} рублей</b-card-sub-title>
      <b-card-text>
        Расстояние: {{ distance }} км
      </b-card-text>
      <b-card-text>
        Количество оставшихся билетов: {{ tickets }}
      </b-card-text>
      <b-card-text>
        Самолёт: {{ plane }}
      </b-card-text>
      <b-card-text>
        Отправка: {{ arrival_date }}
      </b-card-text>
      <b-card-text>
      	Прибытие: {{ departure_date }}
      </b-card-text>
      <b-card-text>
        Есть ли транзитные посадки: <span v-if="transit">Да</span><span v-if="!transit">Нет</span>
      </b-card-text>
      <b-btn variant="primary" dark @click="buyTicket(id)">Купить билет</b-btn>
      <b-alert class="mt-3" v-model="success" variant="info">Билет куплен и он появится во вкладке "Мои билеты"!</b-alert>
    </b-card>
  </div>
</template>
<script>
export default {
  name: 'FlightDetail',
  props: ['id'],
  data () {
    return {
      company: '',
      arrival: '',
      departure: '',
      price: '',
      distance: '',
      tickets: '',
      transit: false,
      success: false,
      plane: '',
      arrival_date: '',
      departure_date: ''
    }
  },
  mounted () {
    this.axios
      .get(`http://${window.location.hostname}:8000/api/flights/arrival/?flight=${this.id}`)
      .then(response => {
        this.company = response.data[0].company.name
        this.arrival = response.data[0].flight.arrival_point
        this.departure = response.data[0].flight.departure_point
        this.distance = response.data[0].flight.distance
        this.tickets = response.data[0].flight.saled_tickets_amount
        this.price = response.data[0].flight.price
        this.transit = response.data[0].flight.is_transit
        this.plane = response.data[0].plane.plane_model
        this.arrival_date = response.data[0].arrival_date
        this.departure_date = response.data[0].departure_date
      })
  },
  methods: {
    buyTicket (flightID) {
      if (sessionStorage.getItem('token')) {
        this.axios
          .post(`http://${window.location.hostname}:8000/api/tickets/`, { user: sessionStorage.getItem('user_id'), flight: flightID })
          .then(response => { console.log(response); this.updateTicketAmount(flightID) })
          .catch(err => { console.error(err) })
      }
    },
    updateTicketAmount (flightID) {
      this.axios
        .patch(`http://${window.location.hostname}:8000/api/flights/tickets/${flightID}`, { saled_tickets_amount: this.tickets - 1 })
        .then(response => {
          console.log(response)
          this.tickets -= 1
          this.success = true
          setTimeout(() => this.success = false, 2500)
        })
        .catch(err => { console.error(err) })
    }
  },
}

</script>
<style></style>
