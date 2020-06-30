<template>
  <main>
    <section>
      <v-col cols="10" class="my-2 mx-auto">
        <h1>Клиника "Hospital"</h1>
        <br>
        <h2>Приём номер {{ id }}</h2>
        <br>
        <p>Здравствуйте! Вам следует зафиксировать информацию о приёме в форме <u>(все поля обязательны к заполнению)</u>:</p>
      </v-col>
    </section>
    <section>
      <v-form>
        <v-col cols="5" class="mx-auto">
          <v-text-field type="number" v-model="price" label="Стоимость"></v-text-field>
          <v-text-field v-model="diagnosis" label="Диагноз"></v-text-field>
          <v-text-field v-model="recomendations" label="Рекомендации"></v-text-field>
          <v-btn color="indigo lighten-2" @click="submit" dark>
            <v-icon>mdi-send-circle</v-icon>Отправить
          </v-btn>
        </v-col>
      </v-form>
    </section>
    <v-dialog v-model="success" max-width="350">
      <v-card>
        <v-card-title class="headline">Успешно!</v-card-title>
        <v-card-text>
          Данные зафиксированы в базе!
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
  name: 'Appointment',
  props: ['id'],
  data () {
    return {
      diagnosis: '',
      recomendations: '',
      price: '',
      success: false,
      patient: '',
      currDate: ''
    }
  },
  methods: {
    submit () {
      let patientCard = {
        patient: this.patient,
        date: this.currDate,
        diagnosis: this.diagnosis,
        recomendations: this.recomendations
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/patients/cards/add/`, patientCard)
        .then(response => { console.log(response.data); this.createPayment() })
        .catch(err => { console.error(err) })
    },
    createPayment () {
      let payment = {
        appointment: this.id,
        payment_date: this.currDate,
        amount: this.price,
        is_paid: false
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/payments/add/`, payment)
        .then(response => { console.log(response.data); this.clear(); this.success = true })
    },
    clear () {
      this.diagnosis = ''
      this.recomendations = ''
      this.price = ''
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

    this.currDate = today

    this.axios
      .get(`http://${window.location.hostname}:8000/api/appointments/${this.id}`)
      .then(response => { this.patient = response.data.patient })
      .catch(err => { console.error(err) })
  }
}

</script>
<style></style>
