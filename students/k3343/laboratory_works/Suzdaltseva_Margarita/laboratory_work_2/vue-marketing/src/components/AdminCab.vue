<template>
  <main>
    <v-col cols="8" class="my-1 mx-auto">
      <h2>Страница руководителя</h2>
      <p>Все заявки</p>
    </v-col>
    <v-col cols="8" class="my-1 mx-auto">
      <v-form>
        <v-container>
          <v-row>
            <v-select v-model="req_status" :items="statuses" label="Статус"></v-select>
          </v-row>
          <v-row>
            <v-select v-model="req_service" :items="services" label="Услуга"></v-select>
          </v-row>
          <v-row>
            <v-col cols="6" md="4">
              <v-menu ref="menu" v-model="menu" :close-on-content-click="false" :return-value.sync="date" transition="scale-transition" offset-y min-width="290px">
                <template v-slot:activator="{ on }">
                  <v-text-field v-model="req_after" label="С" readonly v-on="on"></v-text-field>
                </template>
                <v-date-picker v-model="req_after" class="mt-4" @input="menu = false"></v-date-picker>
              </v-menu>
            </v-col>
            <v-col cols="6" md="4">
              <v-menu ref="menu" v-model="menu" :close-on-content-click="false" :return-value.sync="date" transition="scale-transition" offset-y min-width="290px">
                <template v-slot:activator="{ on }">
                  <v-text-field v-model="req_before" label="По" readonly v-on="on"></v-text-field>
                </template>
                <v-date-picker v-model="req_before" class="mt-4" @input="menu = false"></v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
          <v-row>
            <v-select v-model="req_employee" :items="employees" label="Сотрудник"></v-select>
          </v-row>
          <v-row>
            <v-select v-model="req_client" :items="clients" label="Клиент"></v-select>
          </v-row>
          <v-row>
            <v-btn dark class="mr-4 pink accent-3" @click="filterReq">
              <v-icon>mdi-filter</v-icon>Отфильтровать
            </v-btn>
            <v-btn dark class="mr-4 pink accent-4" @click="clearFilter">
              <v-icon>mdi-autorenew</v-icon>Очистить
            </v-btn>
          </v-row>
        </v-container>
      </v-form>
    </v-col>
    <section>
      <v-col cols="8" class="mx-auto">
        <h3>Найдено заявок {{ requestcards.length }} </h3>
        <v-card class="my-2" color="pink darken-3" dark v-for="card in requestcards" :key="card.id">
          <v-card-title class="headline">{{ card.title }} -- {{ card.status }}</v-card-title>
          <v-card-subtitle>{{ card.service.name }}</v-card-subtitle>
          <v-card-text>
            <p>Заказчик {{ card.client.first_name }} {{ card.client.last_name }}</p>
            <p>Исполнитель {{ card.employee.first_name }} {{ card.employee.last_name }}</p>
          </v-card-text>
          <v-card-actions>
            <v-btn text :to='"/details/" + card.id'>Подробнее</v-btn>
            <v-btn light class="pink lighten-5" v-if="card.status === 'in progress'" @click="markCompleted(card.id)">Отметить как завершённую</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </section>
  </main>
</template>
<script>
export default {
  name: 'AdminCab',
  created () {
    if (sessionStorage.getItem('token') === null || sessionStorage.getItem('user') === null) {
      this.$router.push('/auth')
    }
  },
  mounted () {
    this.axios
      .get(`http://${window.location.hostname}:8000/api/gethead?user=${sessionStorage.getItem('user')}`)
      .then(response => { this.getRequests(response.data) })
      .catch(err => { console.error(err) })
  },
  data () {
    return {
      requestcards: [],
      statuses: [
        {
          text: 'in progress',
          value: 0
        },
        {
          text: 'completed',
          value: 1
        }
      ],
      services: [],
      employees: [],
      clients: [],
      req_status: '',
      req_service: '',
      req_after: '',
      req_before: '',
      req_employee: '',
      req_client: ''
    }
  },
  methods: {
    getRequests (data) {
      if (data.length === 0) {
        this.$router.push('/')
      }
      console.log(data)
      this.axios
        .get(`http://${window.location.hostname}:8000/api/request/all`)
        .then(response => { this.getCards(response.data) })
        .catch(err => { console.error(err) })

      this.axios
        .get(`http://${window.location.hostname}:8000/api/service/all`)
        .then(response => { this.getServices(response.data) })
        .catch(err => { console.error(err) })

      this.axios
        .get(`http://${window.location.hostname}:8000/api/employee/all`)
        .then(response => { this.getEmployees(response.data) })
        .catch(err => { console.error(err) })

      this.axios
        .get(`http://${window.location.hostname}:8000/api/client/all`)
        .then(response => { this.getClients(response.data) })
        .catch(err => { console.error(err) })
    },
    getCards (data) {
      this.requestcards = []
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
    },
    filterReq () {
      this.axios
        .get(`http://${window.location.hostname}:8000/api/request/adminfilter?status=${this.req_status}&service=${this.req_service}&after=${this.req_after}&before=${this.req_before}&employee=${this.req_employee}&client=${this.req_client}`)
        .then(response => { this.getCards(response.data) })
        .catch(err => { console.error(err) })
    },
    clearFilter () {
      this.req_status = ''
      this.req_service = ''
      this.req_after = ''
      this.req_before = ''
      this.req_employee = ''
      this.req_client = ''

      this.filterReq()
    },
    getServices (data) {
      for (let i = 0; i < data.length; i++) {
        let service = {}
        service.value = data[i].id
        service.text = data[i].name

        this.services.push(service)
      }
    },
    getEmployees (data) {
      for (let i = 0; i < data.length; i++) {
        let employee = {}
        employee.value = data[i].id
        employee.text = `${data[i].first_name} ${data[i].last_name} (${data[i].user.username})`

        this.employees.push(employee)
      }
    },
    getClients (data) {
      for (let i = 0; i < data.length; i++) {
        let client = {}
        client.value = data[i].id
        client.text = `${data[i].first_name} ${data[i].last_name} (${data[i].user.username})`

        this.clients.push(client)
      }
    },
    markCompleted (id) {
      let data = {
        status: '1'
      }
      this.axios
        .patch(`http://${window.location.hostname}:8000/api/request/${id}`, data)
        .then(response => { console.log(response); this.filterReq() })
        .catch(err => { console.error(err) })
    }
  }
}
</script>
<style scoped>
</style>
