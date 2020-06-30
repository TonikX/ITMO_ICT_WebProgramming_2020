<template>
  <main>
    <v-col cols="4" class="mx-auto">
      <h2 class="mb-4">Регистрация пациента</h2>
      <p>Здравствуйте! Если Вы хотите записаться на приём к врачу, то заполните форму регистрации <u>(все поля обязательны к заполнению)</u>:</p>
      <form>
        <v-text-field v-model="username" label="Логин" required></v-text-field>
        <v-text-field type="password" v-model="password" label="Пароль" required></v-text-field>
        <v-text-field v-model="fullname" label="ФИО"></v-text-field>
        <v-text-field type="tel" v-model="phone_number" label="Номер телефона"></v-text-field>
        <v-text-field type="date" v-model="birthdate" label="Дата рождения"></v-text-field>
        <v-btn class="mr-4" @click="submit" color="teal" dark>Регистрация</v-btn>
        <p class="my-5">Уже зарегистрированы? Тогда <router-link to="/auth">войдите</router-link></p>
      </form>
    </v-col>
  </main>
</template>
<script>
export default {
  name: 'Register',
  data () {
    return {
      username: '',
      password: '',
      fullname: '',
      birthdate: '',
      phone_number: ''
    }
  },
  created () {
    if (sessionStorage.getItem('token') !== null) {
      this.$router.push('/doctor')
    }
  },
  methods: {
    submit () {
      if (this.username && this.password) {
        this.axios
          .post(`http://${window.location.hostname}:8000/api/auth/users/`, { 'username': this.username, 'password': this.password })
          .then(response => { this.addPatient(response.data.id) })
          .catch(err => { console.error(err) })
      }
    },
    addPatient (userId) {
      let patient = {
        fullname: this.fullname,
        birthdate: this.birthdate,
        phone_number: this.phone_number,
        user: userId
      }

      let date = new Date()
      let currDate = {
        y: `${date.getFullYear()}`,
        m: `${date.getMonth()}`.length > 1 ? `${date.getMonth() + 1}` : `0${date.getMonth() + 1}`,
        d: `${date.getDate()}`.length > 1 ? `${date.getDate()}` : `0${date.getDate()}`
      }

      let today = `${currDate.y}-${currDate.m}-${currDate.d}`

      this.axios
        .post(`http://${window.location.hostname}:8000/api/patients/add/`, patient)
        .then(response => {
          localStorage.setItem('patient', response.data.id)
          this.axios
            .post(`http://${window.location.hostname}:8000/api/patients/cards/add/`, { date: today, patient: response.data.id })
            .then(response => {
              console.log(response)
              this.$router.push('/auth')
            })
            .catch(err => { console.error(err) })
        })
        .catch(err => { console.error(err) })
    }
  }
}

</script>
<style></style>
