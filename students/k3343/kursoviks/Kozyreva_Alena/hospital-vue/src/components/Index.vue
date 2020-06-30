<template>
  <main>
    <section>
      <v-col cols="10" class="my-2 mx-auto">
        <h1>Клиника "Hospital"</h1>
      </v-col>
    </section>
    <section>
      <v-col cols="10" class="my-2 mx-auto">
        <h2>Найти пациента</h2>
        <v-form>
          <v-row>
            <v-col cols="4">
              <v-select v-model="doctor" :items="doctors" label="Лечащий врач"></v-select>
            </v-col>
            <v-col cols="4">
              <v-text-field type="date" v-model="date" label="Дата приёма"></v-text-field>
            </v-col>
            <v-col cols="4">
              <v-text-field type="number" v-model="price" label="Стоимость приёма"></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="4">
              <v-text-field type="date" v-model="birthdate" label="Дата рождения пациента"></v-text-field>
            </v-col>
            <v-col cols="4">
              <v-checkbox v-model="is_paid" label="Была ли оплата?"></v-checkbox>
            </v-col>
            <v-col cols="4" class="my-auto">
              <v-checkbox v-model="is_sum" label="Вывести суммарную стоимость"></v-checkbox>
              <v-btn color="indigo lighten-2" @click="submit" dark>
                <v-icon>mdi-filter</v-icon>Отфильтровать
              </v-btn>
              <v-btn color="red lighten-2" @click="reset" dark>
                <v-icon>mdi-delete</v-icon>Сбросить
              </v-btn>
            </v-col>
          </v-row>
        </v-form>
      </v-col>
    </section>
    <section>
      <v-col cols="10" class="mx-auto">
        <h3 v-if="appointments.length > 0">Найдено {{ appointments.length }} приёмов</h3>
        <h3 v-if="!appointments.length">К сожалению, нам не удалось ничего найти</h3>
        <h5 v-if="is_sum">Суммарная стоимость {{ sum }} рублей</h5>
        <appointment-info v-for="a in appointments" :key="a.id" :doctor="a.doctor" :patient="a.patient" :price="a.price"></appointment-info>
      </v-col>
    </section>
  </main>
</template>
<script>
import AppointmentInfo from './AppointmentInfo'

export default {
  name: 'Index',
  data () {
    return {
      doctor: '',
      doctors: [],
      date: '',
      price: '',
      birthdate: '',
      is_paid: false,
      is_sum: false,
      sum: 0,
      appointments: []
    }
  },
  methods: {
    submit () {
      let isPaid = this.is_paid ? '1' : ''
      this.axios
        .get(`http://${window.location.hostname}:8000/api/payments/?doctor=${this.doctor}&date=${this.date}&price=${this.price}&patient_birthdate=${this.birthdate}&is_paid=${isPaid}`)
        .then(response => { this.showAppointments(response.data) })
        .catch(err => { console.error(err) })
    },
    reset () {
      this.doctor = ''
      this.date = ''
      this.price = ''
      this.birthdate = ''
      this.is_paid = false
      this.is_sum = false
    },
    showAppointments (resp) {
      this.appointments = []
      this.sum = 0

      for (let i = 0; i < resp.length; i++) {
        let appointment = {
          id: resp[i].appointment.id,
          patient: resp[i].appointment.patient.fullname,
          doctor: resp[i].appointment.doctor.fullname,
          price: `${resp[i].amount}`
        }

        this.sum += resp[i].amount

        this.appointments.push(appointment)
      }
    },
    addDoctors (resp) {
      for (let i = 0; i < resp.length; i++) {
        let doctor = {
          text: `${resp[i].fullname}, ${resp[i].specialization}`,
          value: resp[i].id
        }

        this.doctors.push(doctor)
      }
    }
  },
  mounted () {
    this.axios
      .get(`http://${window.location.hostname}:8000/api/payments/`)
      .then(response => { this.showAppointments(response.data) })
      .catch(err => { console.error(err) })

    this.axios
      .get(`http://${window.location.hostname}:8000/api/doctors/`)
      .then(response => { this.addDoctors(response.data) })
      .catch(err => { console.error(err) })
  },
  components: {
    AppointmentInfo
  }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
