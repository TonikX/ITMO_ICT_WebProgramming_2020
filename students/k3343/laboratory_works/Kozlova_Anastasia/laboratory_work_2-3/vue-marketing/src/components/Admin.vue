<template>
  <main>
    <v-col cols="8" class="my-1 mx-auto">
      <h1>Админ-панель</h1>
      <p>Цифры и заявки.</p>
    </v-col>
    <v-col cols="8" class="my-1 mx-auto">
      <v-form>
        <v-container>
          <v-row>
            <v-select v-model="state" :items="states" label="Статус"></v-select>
            <v-select class="ml-5" v-model="service" :items="services" label="Услуга"></v-select>
            <v-text-field class="ml-5" v-model="from_date" type="date" label="От"></v-text-field>
            <v-text-field class="ml-5" v-model="to_date" type="date" label="До"></v-text-field>
          </v-row>
          <v-row>
            <v-select v-model="executor" :items="executors" label="Сотрудник"></v-select>
            <v-select class="ml-5" v-model="client" :items="clients" label="Клиент"></v-select>
          </v-row>
          <v-row>
            <v-btn dark color="teal" @click="filter">
              Отфильтровать
            </v-btn>
            <v-btn dark class="ml-5" color="deep-orange accent-4" @click="clear">
              Сбросить
            </v-btn>
          </v-row>
        </v-container>
      </v-form>
    </v-col>
    <section>
      <v-col cols="8" class="mx-auto">
        <h2 v-if="!requests.length">Ничего не найдено</h2>
        <h2 v-if="requests.length">Количество заявок {{ requests.length }}</h2>
        <v-card class="my-2" color="indigo" dark v-for="r in requests" :key="r.id">
          <v-card-title class="headline">{{ r.title }}, {{ r.date }} | {{ r.state }}</v-card-title>
          <v-card-subtitle>{{ r.service }}</v-card-subtitle>
          <v-card-text>
            <p>Цель: {{ r.desc }}</p>
            <p>Заказчик: {{ r.client }}</p>
            <p>Исполнитель: {{ r.executor }}</p>
          </v-card-text>
          <v-card-actions v-if="r.state === 'Not complete'">
            <v-btn text @click='tickRequest(r.id)'>Отметить как выполненное</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </section>
  </main>
</template>
<script>
export default {
  name: 'Admin',
  created () {
    if (sessionStorage.getItem('token') === null || sessionStorage.getItem('username') === null) {
      this.$router.push('/auth')
    }
  },
  mounted () {
    this.getRequests()
  },
  data () {
    return {
      requests: [],
      states: [
        {
          text: 'Not Completed',
          value: 2
        },
        {
          text: 'Completed',
          value: 1
        }
      ],
      services: [],
      executors: [],
      clients: [],
      state: '',
      service: '',
      to_date: '',
      from_date: '',
      executor: '',
      client: ''
    }
  },
  methods: {
    getRequests () {
      this.axios
        .get('http://localhost:8000/api/request/service/all')
        .then(response => { this.showRequests(response.data) })
        .catch(err => { console.error(err) })

      this.axios
        .get('http://localhost:8000/api/services/all')
        .then(response => { this.getServices(response.data) })
        .catch(err => { console.error(err) })

      this.axios
        .get(`http://localhost:8000/api/is/employee`)
        .then(response => { this.getexecutors(response.data) })
        .catch(err => { console.error(err) })

      this.axios
        .get(`http://localhost:8000/api/client/all`)
        .then(response => { this.getClients(response.data) })
        .catch(err => { console.error(err) })
    },
    filter () {
      this.requests = []

      this.axios
        .get(`http://localhost:8000/api/request/service/all?state=${this.state}&service=${this.service}&from_date=${this.from_date}&to_date=${this.to_date}&employee=${this.executor}&client=${this.client}`)
        .then(response => { this.showRequests(response.data) })
        .catch(err => { console.error(err) })
    },
    clear () {
      this.state = ''
      this.service = ''
      this.to_date = ''
      this.from_date = ''
      this.executor = ''
      this.client = ''

      this.filter()
    },
    getServices (data) {
      for (let i = 0; i < data.length; i++) {
        let service = {
          value: data[i].id,
          text: data[i].name
        }

        this.services.push(service)
      }
    },
    getexecutors (data) {
      for (let i = 0; i < data.length; i++) {
        let executor = {}
        executor.value = data[i].id
        executor.text = `${data[i].user.last_name} ${data[i].user.first_name} ${data[i].patronymic}`

        this.executors.push(executor)
      }
    },
    getClients (data) {
      for (let i = 0; i < data.length; i++) {
        let client = {}
        client.value = data[i].id
        client.text = `${data[i].user.last_name} ${data[i].user.first_name} ${data[i].patronymic}`

        this.clients.push(client)
      }
    },
    showRequests (data) {
      for (let i = 0; i < data.length; i++) {
        let request = {
          title: 'Заявка #' + data[i].id,
          id: data[i].id,
          service: 'Название услуги: ' + data[i].service.name + ' Цена: ' + data[i].service.price,
          client: data[i].request.client.user.last_name + ' ' + data[i].request.client.user.first_name + ' ' + data[i].request.client.patronymic,
          executor: data[i].request.executor.user.last_name + ' ' + data[i].request.executor.user.first_name + ' ' + data[i].request.executor.patronymic,
          desc: data[i].request.target,
          date: data[i].request.date,
          state: data[i].request.state
        }

        this.requests.push(request)
      }
    },
    tickRequest (requestId) {
      let requestData = {
        state: '1'
      }

      this.axios
        .patch('http://localhost:8000/api/request/' + requestId, requestData)
        .then(response => { console.log(response) })
        .catch(err => { console.error(err) })
    }
  }
}
</script>
<style scoped>
</style>
