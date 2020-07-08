<template>
  <b-card>
    <b-card-title>
      {{ arrival }} - {{ departure }}
    </b-card-title>
    <b-card-sub-title>Цена: {{ price }} рублей</b-card-sub-title>
    <b-card-text>
      Расстояние: {{ distance }} км
    </b-card-text>
    <b-card-text>
      Количество оставшихся билетов: {{ ticketsAmount }}
    </b-card-text>
    <b-card-text>
      Есть ли транзитные посадки: <span v-if="transit">Да</span><span v-if="!transit">Нет</span>
    </b-card-text>
    <b-btn variant="primary" dark @click="buyTicket(flightID)">Купить билет</b-btn>
    <b-btn variant="info" dark @click="showDetail(flightID)">Подробнее</b-btn>
    <b-alert class="mt-3" v-model="success" variant="info">Билет куплен и он появится во вкладке "Мои билеты"!</b-alert>
  </b-card>
</template>
<script>
export default {
  name: 'Flight',
  props: {
    flightID: Number,
    arrival: String,
    departure: String,
    price: Number,
    tickets: Number,
    transit: Boolean,
    distance: Number
  },
  data () {
    return {
      ticketsAmount: this.tickets,
      success: false
    }
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
          this.ticketsAmount = this.ticketsAmount - 1
          this.success = true
          setTimeout(() => this.success = false, 2500)
        })
        .catch(err => { console.error(err) })
    },
    showDetail (flightID) {
      this.$router.push(`/detail/${flightID}`)
    }
  }
}

</script>
<style></style>
