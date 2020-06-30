<template>
  <v-card color="teal" class="my-3" dark>
    <div class="d-flex flex-no-wrap justify-space-between">
      <div>
        <v-card-title class="headline" v-text="patient"></v-card-title>
        <v-card-subtitle v-text="doctor"></v-card-subtitle>
        <p class="mx-4" v-if="price">Стоимость: {{ price }}</p>
        <p class="mx-4" v-if="date">Дата приёма: {{ date }}</p>
        <p v-if="paidStatus" class="mx-4">Дата оплаты: {{ paidDate }}</p>
      </div>
    </div>
    <v-card-actions v-if="link || (!paidStatus && isPatient)">
      <v-btn text v-if="link" :to="link">Подробнее</v-btn>
      <v-btn text v-if="!paidStatus && isPatient && price" @click="pay(paymentId)">Оплатить</v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
export default {
  name: 'AppointmentInfo',
  props: {
    patient: String,
    doctor: String,
    price: String,
    link: String,
    date: String,
    isPaid: Boolean,
    isPatient: Boolean,
    payDate: String,
    appId: Number,
    paymentId: Number
  },
  data () {
    return {
      paidStatus: this.isPaid,
      paidDate: this.payDate
    }
  },
  methods: {
    pay (paymentId) {
      let date = new Date()
      let currDate = {
        y: `${date.getFullYear()}`,
        m: `${date.getMonth()}`.length > 1 ? `${date.getMonth() + 1}` : `0${date.getMonth() + 1}`,
        d: `${date.getDate()}`.length > 1 ? `${date.getDate()}` : `0${date.getDate()}`
      }

      let today = `${currDate.y}-${currDate.m}-${currDate.d}`

      let payData = {
        amount: this.price,
        payment_date: today,
        is_paid: true
      }

      this.axios
        .patch(`http://${window.location.hostname}:8000/api/payments/${paymentId}`, payData)
        .then(response => { console.log(response); this.paidStatus = true; this.paidDate = today })
        .catch(err => { console.error(err) })
    }
  }
}

</script>
<style>
</style>
