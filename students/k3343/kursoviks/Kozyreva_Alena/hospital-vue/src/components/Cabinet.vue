<template>
  <main>
    <section>
      <v-col cols="10" class="my-2 mx-auto">
        <h1>Клиника "Hospital"</h1>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="mx-auto my-2">
        <p>Ваша медицинская карта:</p>
        <v-card color="primary accent-2" class="my-3" dark>
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="headline">Медицинская карта</v-card-title>
              <v-card-subtitle>Дата последнего приёма: {{ card.date }}</v-card-subtitle>
              <p class="mx-4">Диагноз: {{ card.diagnosis }}</p>
              <p class="mx-4">Рекомендации: {{ card.recomendations }}</p>
            </div>
          </div>
        </v-card>
        <p>Список всех ваших приёмов:</p>
        <appointment-info v-for="a in appointments" :paymentId="a.payment_id" :appId="a.id" :isPaid="a.isPaid" :payDate="a.payDate" :date="a.date" :doctor="a.doctor" :price="a.price" :patient="a.patient" :isPatient="a.isPatient" :key="a.id"></appointment-info>
      </v-col>
    </section>
  </main>
</template>
<script>
import AppointmentInfo from './AppointmentInfo'
export default {
  name: 'Cabinet',
  components: { AppointmentInfo },
  data () {
    return {
      appointments: [],
      card: {
        date: '',
        diagnosis: '',
        recomendations: ''
      }
    }
  },
  created () {
    if (sessionStorage.getItem('token') === null) {
      this.$router.push('/auth')
    }
  },
  mounted () {
    this.axios
      .get(`http://${window.location.hostname}:8000/api/patients/cards?patient=${localStorage.getItem('patient')}`)
      .then(response => { this.showPatientCard(response.data[response.data.length - 1]) })
      .catch(err => { console.error(err) })

    this.axios
      .get(`http://${window.location.hostname}:8000/api/appointments/?patient=${localStorage.getItem('patient')}`)
      .then(response => { this.showAppointments(response.data) })
      .catch(err => { console.error(err) })
  },
  methods: {
    showAppointments (resp) {
      for (let i = 0; i < resp.length; i++) {
        let appointment = {
          id: resp[i].id,
          patient: resp[i].patient.fullname,
          price: resp[i].price,
          doctor: resp[i].doctor.fullname,
          date: resp[i].date,
          isPatient: true,
          isPaid: false
        }

        this.axios
          .get(`http://${window.location.hostname}:8000/api/payments/?appointment=${resp[i].id}`)
          .then(response => {
            console.log('resp is', response)
            if (response.data.length) {
              if (response.data[0].is_paid) {
                appointment.isPaid = true
                appointment.payDate = response.data[0].payment_date
              }
              appointment.price = `${response.data[0].amount}`
              appointment.payment_id = response.data[0].id
            }
            this.appointments.push(appointment)
          })
          .catch(err => { console.error(err) })
      }
    },
    showPatientCard (resp) {
      this.card.date = resp.date
      this.card.diagnosis = resp.diagnosis
      this.card.recomendations = resp.recomendations
    }
  }
}

</script>
<style></style>
