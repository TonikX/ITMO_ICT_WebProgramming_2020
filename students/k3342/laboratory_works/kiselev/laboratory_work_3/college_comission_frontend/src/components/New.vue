<template>
  <main>
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
        <v-select :items="specs" v-model="spec" label="Специальность"></v-select>
        <v-select v-model="privelege" :items='priveleges' label="Льготы"></v-select>
        <v-btn color="blue accent-2" dark @click="sendApplication">
          <v-icon>mdi-send</v-icon>Отправить заявление
        </v-btn>
      </v-form>
    </v-col>
    <v-dialog v-model="successSending" max-width="400">
      <v-card>
        <v-card-title class="headline">Ваше заявление принято в обработку</v-card-title>
        <v-card-text>
          Мы напишем вам, когда результат будет известен.
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="indigo lighten-2" text @click="successSending = false">
            Ок
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </main>
</template>
<script>
export default {
  name: 'New',
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
      date: '',
      specs: [
        { value: null, text: 'Выберите специальность', disabled: true }
      ],
      spec: null,
      privelege: null,
      priveleges: [
        { value: null, text: 'Выберите льготы', disabled: true },
        { value: '1', text: 'Нет льгот' },
        { value: '2', text: 'Инвалид' },
        { value: '3', text: 'Сирота' }
      ],
      successSending: false
    }
  },
  created() {
    let date = new Date()
    let currDate = {
      y: `${date.getFullYear()}`,
      m: `${date.getMonth()}`.length > 1 ? `${date.getMonth() + 1}` : `0${date.getMonth() + 1}`,
      d: `${date.getDate()}`.length > 1 ? `${date.getDate()}` : `0${date.getDate()}`
    }

    let today = `${currDate.y}-${currDate.m}-${currDate.d}`

    this.date = today
  },
  mounted() {
    this.axios
      .get('http://127.0.0.1:8000/api/specializations/all')
      .then(response => { this.showSpecs(response.data) })
  },
  methods: {
    showSpecs(data) {
      for (let i = 0; i < data.length; i++) {
        let spec = {
          value: data[i].id,
          text: `${data[i].name}, Проходной балл: ${data[i].minimal_point}`
        }

        this.specs.push(spec)
      }
    },
    sendApplication() {
      let user = {
        username: this.username,
        email: this.email,
        password: this.password
      }

      this.axios
        .post('http://127.0.0.1:8000/api/auth/users/', user)
        .then(response => {
          console.log(response);
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
          console.log(response);
          this.addApplication(response.data.id)
        })
    },
    addApplication(enrollee) {
      let application = {
        application_date: this.date,
        state: '1',
        enrollee: enrollee,
        secretary: 1,
        spec: this.spec
      }

      this.axios
        .post('http://127.0.0.1:8000/api/applications/new', application)
        .then(response => {
          console.log(response);
          this.successSending = true;
          this.clear()
        })
    },
    clear() {
      this.username = ''
      this.password = ''
      this.passport = ''
      this.fullname = ''
      this.email = ''
      this.exam_common = ''
      this.exam_profile = ''
      this.certificate_average = ''
      this.certificate = ''
      this.class_type = null
      this.spec = null
      this.privelege = null
    }
  }
}

</script>
<style></style>
