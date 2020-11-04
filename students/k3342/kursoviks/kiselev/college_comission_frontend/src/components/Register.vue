<template>
  <main class="container mx-auto">
    <h1 class="headline">Регистрация для подачи заявления</h1>
    <section>
      <v-col cols="5" class="mx-auto">
        <v-form>
          <v-text-field v-model="username" label="Имя пользователя"></v-text-field>
          <v-text-field v-model="password" type="password" label="Пароль"></v-text-field>
          <v-text-field v-model="fullname" label="ФИО"></v-text-field>
          <v-text-field v-model="email" type="email" label="Email"></v-text-field>
          <v-text-field v-model="exam_common" type="number" label="Баллы по общим ЕГЭ"></v-text-field>
          <v-text-field v-model="exam_profile" type="number" label="Баллы по профильным ЕГЭ"></v-text-field>
          <v-text-field v-model="certificate_average" type="number" label="Средний балл аттестата"></v-text-field>
          <v-text-field v-model="certificate" type="number" label="Номер аттестата"></v-text-field>
          <v-text-field v-model="passport" type="number" label="Номер паспорта"></v-text-field>
          <v-select :items="class_types" v-model="class_type" label="Класс"></v-select>
          <v-select v-model="privelege" :items='priveleges' label="Льготы"></v-select>
          <v-btn color="blue accent-2" dark @click="register">
            <v-icon>mdi-send</v-icon>Регистрация
          </v-btn>
        </v-form>
      </v-col>
      </v-form>
    </section>
  </main>
</template>
<script>
export default {
  name: 'Register',
  data() {
    return {
      username: '',
      password: '',
      passport: '',
      fullname: '',
      email: '',
      exam_common: '',
      exam_profile: '',
      certificate_average: '',
      certificate: '',
      class_type: null,
      class_types: [
        { value: null, text: 'Выберите класс', disabled: true },
        { value: '1', text: '9' },
        { value: '2', text: '11' }
      ],
      privelege: null,
      priveleges: [
        { value: null, text: 'Выберите льготы', disabled: true },
        { value: '1', text: 'Нет льгот' },
        { value: '2', text: 'Инвалид' },
        { value: '3', text: 'Сирота' }
      ]
    }
  },
  methods: {
    register() {
      let user = {
        username: this.username,
        email: this.email,
        password: this.password
      }

      this.axios
        .post('http://127.0.0.1:8000/api/auth/users/', user)
        .then(response => {
          console.log(response)
          this.addEnrollee(response.data.id)
        })
    },
    addEnrollee(user) {
      let enrollee = {
        class_type: this.class_type,
        privelege_type: this.privelege,
        fullname: this.fullname,
        exam_common: this.exam_common,
        exam_profile: this.exam_profile,
        certificate_average: this.certificate_average,
        certificate: this.certificate,
        passport: this.passport,
        user: user
      }

      this.axios
        .post('http://127.0.0.1:8000/api/enrollee/new', enrollee)
        .then(response => {
          console.log(response)
          localStorage.setItem('enrollee', response.data.id)
          this.$router.push('/auth')
        })
    }
  },
  mounted() {
    if (localStorage.getItem('username') && localStorage.getItem('token')) {
      this.$router.push('/')
      return
    }
  }
}

</script>
