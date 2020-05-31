<template>
  <main>
    <section>
      <v-col cols="10" class="my-2 mx-auto">
        <h1>Клиника "Hospital"</h1>
        <br>
        <p>Здравствуйте! Если Вы хотите записаться на приём к врачу, то заполните форму <u>(все поля обязательны к заполнению)</u>:</p>
      </v-col>
    </section>
    <section>
      <v-form>
        <v-col cols="5" class="mx-auto">
          <v-text-field v-model="fullname" label="ФИО"></v-text-field>
          <v-text-field type="tel" v-model="phone_number" label="Номер телефона"></v-text-field>
          <v-text-field type="date" v-model="birthdate" label="Дата рождения"></v-text-field>
          <v-text-field type="date" v-model="date" label="Дата приёма"></v-text-field>
          <v-select v-model="doctor" :items="doctors" label="Выберите врача"></v-select>
          <v-btn color="indigo lighten-2" @click="submit" dark>
            <v-icon>mdi-send-circle</v-icon>Отправить
          </v-btn>
        </v-col>
      </v-form>
    </section>
    <v-dialog v-model="success" max-width="350">
      <v-card>
        <v-card-title class="headline">Спасибо за заявку!</v-card-title>
        <v-card-text>
          Мы свяжемся с Вами в течение 5 минут!
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="indigo lighten-2" text @click="success = false">
            Ок
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </main>
</template>
<script>
export default {
  name: 'AppointmentNew',
  data () {
    return {
      doctor: '',
      doctors: [],
      fullname: '',
      phone_number: '',
      birthdate: '',
      date: '',
      success: false
    }
  },
  methods: {
    submit () {
      let patient = {
        fullname: this.fullname,
        birthdate: this.birthdate,
        phone_number: this.phone_number
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/patients/add/`, patient)
        .then(response => { this.addAppointment(response.data) })
        .catch(err => { console.error(err) })
    },
    clear () {
      this.doctor = ''
      this.fullname = ''
      this.phone_number = ''
      this.birthdate = ''
      this.date = ''
    },
    addAppointment (resp) {
      let patientId = resp.id

      let appointment = {
        patient: patientId,
        doctor: this.doctor,
        date: this.date
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/appointments/add/`, appointment)
        .then(response => { console.log(response); this.clear(); this.success = true })
        .catch(err => { console.error(err) })
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
      .get(`http://${window.location.hostname}:8000/api/doctors/`)
      .then(response => { this.addDoctors(response.data) })
      .catch(err => { console.error(err) })
  }
}

</script>
<style></style>
