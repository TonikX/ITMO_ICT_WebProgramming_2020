<template>
  <main>
    <section>
      <v-col cols="10" class="my-2 mx-auto">
        <h1>Клиника "Hospital"</h1>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="mx-auto my-2">
        <p>Чтобы вести приём выберите один из предложенных приёмов на сегодняшнюю дату:</p>
        <appointment-info v-for="a in appointments" :patient="a.patient" :key="a.id" :link="'/appointments/' + a.id"></appointment-info>
      </v-col>
    </section>
  </main>
</template>
<script>
import AppointmentInfo from './AppointmentInfo'
export default {
  name: 'Appointments',
  components: { AppointmentInfo },
  data () {
    return {
      appointments: []
    }
  },
  created () {
    if (sessionStorage.getItem('token') === null) {
      this.$router.push('/auth')
    }
    if (localStorage.getItem('patient')) {
      this.$router.push('/cabinet')
    }
  },
  mounted () {
    let date = new Date()
    let currDate = {
      y: `${date.getFullYear()}`,
      m: `${date.getMonth()}`.length > 1 ? `${date.getMonth() + 1}` : `0${date.getMonth() + 1}`,
      d: `${date.getDate()}`.length > 1 ? `${date.getDate()}` : `0${date.getDate()}`
    }

    let today = `${currDate.y}-${currDate.m}-${currDate.d}`
    let doctor = sessionStorage.getItem('user')

    this.axios
      .get(`http://${window.location.hostname}:8000/api/appointments/?date=${today}&doctor=${doctor}`)
      .then(response => { this.showAppointments(response.data) })
      .catch(err => { console.error(err) })
  },
  methods: {
    showAppointments (resp) {
      for (let i = 0; i < resp.length; i++) {
        let appointment = {
          id: resp[i].id,
          patient: resp[i].patient.fullname
        }

        this.appointments.push(appointment)
      }
    }
  }
}

</script>
<style></style>
