<template>
  <main>
    <div class="container">
      <h1>Мои билеты</h1>
      <p>Здесь Вы можете увидеть все свои билеты.</p>
    </div>
    <div class="container">
      <h2 v-if="tickets.length">Найдено {{ tickets.length }} билетов</h2>
      <h2 v-if="!tickets.length">К сожалению, билетов пока нет, но Вы можете их купить!</h2>
      <p>Общие затраты: {{ ticketsSum }} руб.</p>
      <b-card class="mt-2 mb-2" v-for="ticket in tickets" :key="ticket.id">
        <b-card-title>
          {{ ticket.arrival }} - {{ ticket.departure }}
        </b-card-title>
        <b-card-sub-title>Цена: {{ ticket.price }} рублей</b-card-sub-title>
        <b-card-text>
          Расстояние: {{ ticket.distance }} км
        </b-card-text>
        <b-card-text>
          Есть ли транзитные посадки: <span v-if="ticket.transit">Да</span><span v-if="!ticket.transit">Нет</span>
        </b-card-text>
      </b-card>
    </div>
  </main>
</template>
<script>
export default {
  name: 'MyTickets',
  data () {
    return {
      tickets: [],
      ticketsSum: 0
    }
  },
  mounted () {
    if (!sessionStorage.getItem('token')) {
      this.$router.push('/login')
      return
    }

    this.axios
      .get(`http://${window.location.hostname}:8000/api/tickets/list/?username=${sessionStorage.getItem('username')}`)
      .then(response => {
        for (let i = 0; i < response.data.length; i++) {
          let ticket = {}

          ticket.id = response.data[i].id
          ticket.flight = response.data[i].flight.id
          ticket.arrival = response.data[i].flight.arrival_point
          ticket.departure = response.data[i].flight.departure_point
          ticket.price = response.data[i].flight.price
          ticket.distance = response.data[i].flight.distance
          ticket.transit = response.data[i].flight.transit

          this.tickets.push(ticket)

          this.ticketsSum += ticket.price
        }
      })
      .catch(err => { console.error(err) })
  }
}

</script>
<style></style>
