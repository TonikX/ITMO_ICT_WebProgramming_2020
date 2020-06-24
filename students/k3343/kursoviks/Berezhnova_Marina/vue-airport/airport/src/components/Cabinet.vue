<template>
  <main>
    <v-col cols="6" class="mx-auto">
      <h1 class="text-left">Кабинет пользователя</h1>
      <h2 class="text-left">Ваши билеты:</h2>
    </v-col>
    <v-col cols="6" class="mx-auto">
      <h4 v-if="tickets.length === 0">Вы ещё не покупали билетов...</h4>
      <v-card class="my-2" color="#385F73" dark v-for="ticket in tickets" :key="ticket.id">
        <v-card-title class="headline">{{ ticket.flight }}</v-card-title>
        <br />
      </v-card>
    </v-col>
  </main>
</template>
<script>
export default {
  name: 'Cabinet',
  data () {
    return {
      tickets: []
    }
  },
  methods: {
    showTickets () {
      this.axios
        .get(`http://127.0.0.1:8000/api/user/ticket/?user=${localStorage.getItem('username')}`)
        .then(response => { this.updateTickets(response.data.user_ticket) })
        .catch(err => { console.error(err) })
    },
    updateTickets (data) {
      for (let i = 0; i < data.length; i++) {
        let ticket = {
          id: data[i].id,
          flight: `${data[i].flight.plane.company.name}: ${data[i].flight.route.from_point} - ${data[i].flight.route.to_point},
          ${data[i].flight.route.distance} км, ${data[i].flight.date}`
        }

        this.tickets.push(ticket)
      }
    }
  },
  mounted () {
    if (!localStorage.getItem('username') && !localStorage.getItem('token')) {
      this.$router.push('/login')
      return
    }
    this.showTickets()
  }
}

</script>
<style></style>
