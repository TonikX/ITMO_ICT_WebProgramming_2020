<template>
  <main>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h2>Детали заявки</h2>
        <div>Подробная информация о выбранной заявке</div>
      </v-col>
      <v-col  cols="12" class="my-1 mx-auto">
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">Номер заявки</th>
                <th class="text-left">Услуга</th>
                <th class="text-left">Клиент</th>
                <th class="text-left">Сотрудник</th>
                <th class="text-left">Краткое описание</th>
                <th class="text-left">Материалы</th>
                <th class="text-left">Дата</th>
                <th class="text-left">Статус</th>
              </tr>
            </thead>
            <tbody>
              <tr>
              <td>{{ request.id }}</td>
              <td>{{ request.service.service_type  }}: {{ request.service.name }}</td>
              <td>{{ request.client.first_name }} {{ request.client.last_name }} ({{ request.client.user.username }}) {{ request.client.company.company_type }} "{{ request.client.company.name }}" Контакты: {{ request.client.user.email }} {{ request.client.phone }}</td>
              <td>{{ request.employee.first_name }} {{ request.employee.last_name }} ({{request.employee.user.username }}) {{ request.employee.position }} Контакты: {{ request.employee.user.email }} {{ request.employee.phone }}</td>
              <td>{{ request.description }}</td>
              <td>{{ request.materials }}</td>
              <td>{{ request.date }}</td>
              <td>{{ request.status }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="mx-auto">
        <h3>Информация об оплате</h3>
        <v-card class="my-2 mx-2">
          <v-card-title>Платёжное поручение № {{ payment }}</v-card-title>
          <v-card-subtitle>на сумму {{ pay_amount }} руб.</v-card-subtitle>
          <v-card-text>
            <div>от {{ pay_requested }}</div>
            <div>{{ pay_status }} {{ pay_paid }}</div>
          </v-card-text>
          <v-card-actions>
            <v-btn v-if="pay_status === 'не оплачено'" dark class="pink accent-3">Оплатить</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="mx-auto">
        <h3>Рекламные продукты ({{ productcards.length }})</h3>
      </v-col>
      <v-col cols="12" class="mx-auto">
        <v-row>
        <v-col cols="6" v-for="card in productcards" :key="card.id">
        <v-card class="my-2 mx-2">
          <v-img height="200px" :src="card.image">
          </v-img>
          <v-card-title class="headline">{{ card.name }}</v-card-title>
          <v-card-subtitle>{{ card.description }}</v-card-subtitle>
        </v-card>
        </v-col>
       </v-row>
      </v-col>
    </section>
  </main>
</template>
<script>
export default {
  name: 'Details',
  created () {
    if (sessionStorage.getItem('token') === null || sessionStorage.getItem('user') === null) {
      this.$router.push('/auth')
    }
  },
  data () {
    return {
      request: {
        id: '',
        service: '',
        client: '',
        employee: '',
        description: '',
        materials: '',
        date: '',
        status: ''
      },
      payment: '',
      pay_amount: '',
      pay_requested: '',
      pay_paid: '',
      pay_status: '',
      productcards: []
    }
  },
  mounted () {
    this.axios
      .get(`http://${window.location.hostname}:8000/api/request/${this.id}`)
      .then(response => { this.getRequest(response.data) })
      .catch(err => { console.error('API', err) })

    this.axios
      .get(`http://${window.location.hostname}:8000/api/product/all?req=${this.id}`)
      .then(response => { this.getProducts(response.data) })
      .catch(err => { console.error('API', err) })

    this.axios
      .get(`http://${window.location.hostname}:8000/api/payment/all?req=${this.id}`)
      .then(response => { this.getPayment(response.data) })
      .catch(err => { console.error('API', err) })
  },
  methods: {
    getRequest (data) {
      let request = {}

      request.id = data.id
      request.service = data.service
      request.client = data.client
      request.employee = data.employee
      request.description = data.description
      request.materials = data.materials
      request.date = new Date(Date.parse(data.date))
      request.status = data.status === '0' ? 'in progress' : 'completed'

      this.request = request
    },
    getProducts (data) {
      for (let i = 0; i < data.length; i++) {
        let productcard = {}
        productcard.id = data[i].id
        productcard.name = data[i].name
        productcard.description = data[i].description
        productcard.image = data[i].image

        this.productcards.push(productcard)
      }
    },
    getPayment (data) {
      let payRequested = new Date(Date.parse(data[0].day_requested))
      let payPaid = data[0].day_paid ? new Date(Date.parse(data[0].day_paid)) : ''
      this.payment = data[0].id
      this.pay_amount = data[0].amount
      this.pay_requested = payRequested
      this.pay_paid = payPaid
      this.pay_status = data[0].status === '0' ? 'не оплачено' : 'оплачено'
    }
  },
  props: ['id']
}
</script>
<style scoped>
</style>
