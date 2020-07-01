<template>
  <main>
    <v-col cols="8" class="my-1 mx-auto">
      <h2>Личный кабинет пользователя</h2>
      <p>Все Ваши заявки</p>
      <v-btn :to='"/newReq"' dark class="mr-4 pink accent-3">Оставить новую заявку</v-btn>
    </v-col>
    <section>
      <v-col cols="8" class="mx-auto">
        <h3>Найдено заявок {{ requestcards.length }}</h3>
        <v-card class="my-2" color="pink darken-3" dark v-for="card in requestcards" :key="card.id">
          <v-card-title class="headline">{{ card.title }} -- {{ card.status }}</v-card-title>
          <v-card-subtitle>{{ card.service.name }}</v-card-subtitle>
          <v-card-text>
            <p>Заказчик {{ card.client.first_name }} {{ card.client.last_name }}</p>
            <p>Исполнитель {{ card.employee.first_name }} {{ card.employee.last_name }}</p>
          </v-card-text>
          <v-card-actions>
            <v-btn text :to='"/details/" + card.id'>Подробнее</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </section>
  </main>
</template>
<script>
export default {
  name: 'Cabinet',
  created () {
    if (sessionStorage.getItem('token') === null || sessionStorage.getItem('user') === null) {
      this.$router.push('/auth')
    }
  },
  mounted () {
    this.axios
      .get(`http://${window.location.hostname}:8000/api/request/all?user=${sessionStorage.getItem('user')}`)
      .then(response => { console.log(response); this.getRequests(response.data) })
      .catch(err => { console.error(err) })
  },
  data () {
    return {
      requestcards: []
    }
  },
  methods: {
    getRequests (data) {
      for (let i = 0; i < data.length; i++) {
        let requestcard = {}
        requestcard.title = `Заявка № ${data[i].id}`
        requestcard.id = data[i].id
        requestcard.service = data[i].service
        requestcard.client = data[i].client
        requestcard.employee = data[i].employee
        requestcard.description = data[i].description
        requestcard.materials = data[i].materials
        requestcard.date = data[i].date
        requestcard.status = data[i].status === '0' ? 'in progress' : 'completed'

        this.requestcards.push(requestcard)
      }
    }
  }
}
</script>
<style scoped>
</style>
