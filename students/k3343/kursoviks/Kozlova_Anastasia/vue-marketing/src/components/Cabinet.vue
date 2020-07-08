<template>
  <main>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h2>Личный кабинет пользователя</h2>
        <p v-if="this.is_client">Все Ваши рекламные заявки</p>
        <p v-if="!this.is_client">Рекламные заявки, над которыми Вы работаете</p>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="mx-auto">
        <v-row class="mw-100 mx-auto">
          <h3 v-if="!requests.length">Заявок пока нет</h3>
          <h3 v-if="requests.length">Количество заявок {{ requests.length }}</h3>
          <div class="ml-auto">
            <v-btn to="/payments" color="primary accent-2" dark>Финансы</v-btn>
            <v-btn to="/request/new" color="teal" dark>Создать заявку</v-btn>
          </div>
        </v-row>
        <v-card class="my-2" color="indigo" dark v-for="r in requests" :key="r.id">
          <v-card-title class="headline">{{ r.title }}, {{ r.date }} | {{ r.state }}&nbsp;<span v-if="r.isPaid">| Оплачено</span> <span v-if="!r.isPaid">| Не оплачено</span></v-card-title>
          <v-card-subtitle>{{ r.service }}</v-card-subtitle>
          <v-card-text>
            <p>Цель: {{ r.desc }}</p>
            <p>Заказчик: {{ r.client }}</p>
            <p>Исполнитель: {{ r.executor }}</p>
          </v-card-text>
          <v-card-actions v-if="r.state === 'Not complete' || !r.isPaid">
            <v-btn v-if="r.state === 'Not complete'" text @click='tickRequest(r.id)'>Отметить как выполненное</v-btn>
            <v-btn v-if="!r.isPaid" text @click='payRequest(r.id)'>Оплатить</v-btn>
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
    if (sessionStorage.getItem('token') === null || sessionStorage.getItem('username') === null) {
      this.$router.push('/auth')
    }

    if (sessionStorage.getItem('type') === 'Employee') {
      this.is_client = false
    }
  },
  mounted () {
    this.axios
      .get(`http://localhost:8000/api/request/service/all?username=${sessionStorage.getItem('username')}`)
      .then(response => { console.log(response); this.showRequests(response.data) })
      .catch(err => { console.error(err) })
  },
  data () {
    return {
      requests: [],
      is_client: true
    }
  },
  methods: {
    showRequests (data) {
      this.requests = []
      for (let i = 0; i < data.length; i++) {
        let request = {
          title: 'Заявка #' + data[i].request.id,
          id: data[i].request.id,
          service: 'Название услуги: ' + data[i].service.name + ', Цена: ' + data[i].service.price,
          client: data[i].request.client.user.last_name + ' ' + data[i].request.client.user.first_name + ' ' + data[i].request.client.patronymic,
          executor: data[i].request.executor.user.last_name + ' ' + data[i].request.executor.user.first_name + ' ' + data[i].request.executor.patronymic,
          desc: data[i].request.target,
          date: data[i].request.date,
          state: data[i].request.state,
          isPaid: data[i].request.is_paid,
          price: data[i].service.price
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
        .then(response => { console.log(response); this.updateRequests() })
        .catch(err => { console.error(err) })
    },
    updateRequests () {
      this.axios
        .get(`http://localhost:8000/api/request/service/all?username=${sessionStorage.getItem('username')}`)
        .then(response => { console.log(response); this.showRequests(response.data) })
        .catch(err => { console.error(err) })
    },
    payRequest (requestId) {
      let requestData = {
        is_paid: true
      }

      this.axios
        .patch('http://localhost:8000/api/request/' + requestId, requestData)
        .then(response => { console.log(response); this.addPayment(requestId) })
        .catch(err => { console.error(err) })
    },
    addPayment (requestId) {
      let date = new Date()
      let currDate = {
        y: `${date.getFullYear()}`,
        m: `${date.getMonth()}`.length > 1 ? `${date.getMonth() + 1}` : `0${date.getMonth() + 1}`,
        d: `${date.getDate()}`.length > 1 ? `${date.getDate()}` : `0${date.getDate()}`
      }

      let today = `${currDate.y}-${currDate.m}-${currDate.d}`

      let reqData = this.requests.filter(request => request.id === requestId)[0]
      console.log('filtered', reqData)
      console.log(this.requests)

      let payData = {
        billing_date: reqData.date,
        payment_date: today,
        amount: reqData.price,
        target: reqData.price,
        state: 1,
        request: requestId
      }

      this.axios
        .post('http://localhost:8000/api/payments/new', payData)
        .then(response => { console.log(response); this.updateRequests() })
        .catch(err => { console.error(err) })
    }
  }
}

</script>
<style scoped>
.mw-100 {
  max-width: 100%
}
</style>
