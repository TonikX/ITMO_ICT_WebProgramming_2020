<template>
  <main>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h2>Финансы пользователя</h2>
        <p>Все фин. операции по заявкам</p>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="mx-auto">
        <v-row class="mw-100 mx-auto">
          <h3 v-if="!requests.length">Операций пока нет</h3>
          <h3 v-if="requests.length">Количество операций {{ requests.length }}</h3>
          <div class="ml-auto">
            <v-btn to="/cabinet" color="primary accent-2" dark>Заявки</v-btn>
          </div>
        </v-row>
        <v-card class="my-2" color="indigo" dark v-for="r in requests" :key="r.id">
          <v-card-title class="headline">{{ r.title }}, {{ r.date }}&nbsp;<span v-if="r.isPaid">| Оплачено</span> <span v-if="!r.isPaid">| Не оплачено</span></v-card-title>
          <v-card-subtitle>{{ r.service }}</v-card-subtitle>
          <v-card-text>
            <p>Цель: {{ r.desc }}</p>
          </v-card-text>
          <v-card-text>
            <p>Дата выставления счёта: {{ r.billDate }}</p>
          </v-card-text>
          <v-card-text>
            <p>Дата оплаты: {{ r.payDate }}</p>
          </v-card-text>
        </v-card>
      </v-col>
    </section>
  </main>
</template>
<script>
export default {
  name: 'Payments',
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
      .get(`http://localhost:8000/api/payments/all?username=${sessionStorage.getItem('username')}`)
      .then(response => { console.log(response); this.showPayments(response.data) })
      .catch(err => { console.error(err) })
  },
  data () {
    return {
      requests: [],
      is_client: true
    }
  },
  methods: {
    showPayments (data) {
      this.requests = []
      for (let i = 0; i < data.length; i++) {
        let request = {
          title: 'Операция #' + data[i].request.id,
          reqId: data[i].request.id,
          service: 'Продукт: ' + data[i].request.product.name + ', Цена: ' + data[i].amount,
          desc: data[i].request.target,
          date: data[i].request.date,
          isPaid: data[i].request.is_paid,
          id: data[i].id,
          billDate: data[i].billing_date,
          payDate: data[i].payment_date
        }

        this.requests.push(request)
      }
    }
  }
}

</script>
<style scoped>
.mw-100 {
  max-width: 100%
}
</style>
