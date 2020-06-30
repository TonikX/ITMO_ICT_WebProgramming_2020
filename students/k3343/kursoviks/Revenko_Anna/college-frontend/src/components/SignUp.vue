<template>
  <main>
    <div class="content container mt-5">
      <div class="d-flex flex-column m-auto">
        <h1 class="text-center">Регистрация абитуриента</h1>
        <p class="mb-2 mt-2 w-100 text-center">Если вы уже зарегистрированы, то можете войти <router-link to="/signin">тут</router-link>.</p>
      </div>
      <div class="d-flex flex-row">
        <div class="m-auto w-75">
          <b-form>
            <p class="m-1 font-weight-bold">Данные для входа</p>
            <div class="m-1">
              <label for="username">Имя пользователя</label>
              <b-form-input id="username" v-model="username" placeholder="Имя пользователя"></b-form-input>
            </div>
            <div class="m-1">
              <label for="password">Пароль</label>
              <b-form-input id="password" v-model="password" type="password" placeholder="Пароль"></b-form-input>
            </div>
            <p class="m-1 font-weight-bold">Информация о Вас</p>
            <div class="m-1">
              <label for="last_name">Фамилия</label>
              <b-form-input id="last_name" v-model="last_name" placeholder="Фамилия"></b-form-input>
            </div>
            <div class="m-1">
              <label for="first_name">Имя</label>
              <b-form-input id="first_name" v-model="first_name" placeholder="Имя"></b-form-input>
            </div>
            <div class="m-1">
              <label for="patronymic">Отчество</label>
              <b-form-input id="patronymic" v-model="patronymic" placeholder="Отчество"></b-form-input>
            </div>
            <div class="m-1">
              <label for="schoolClass">Класс</label>
              <b-form-select id="schoolClass" v-model="schoolClass" :options="schoolClasses" :value="null"></b-form-select>
            </div>
            <div class="m-1">
              <label for="privelege">Льготы</label>
              <b-form-select id="privelege" v-model="privelege" :options="priveleges" :value="null"></b-form-select>
            </div>
            <p class="m-1 font-weight-bold">Ваши документы</p>
            <div class="m-1">
              <label for="certificate">Аттестат</label>
              <b-form-input id="certificate" v-model="certificate" placeholder="Аттестат"></b-form-input>
            </div>
            <div class="m-1">
              <label for="passport">Паспорт</label>
              <b-form-input id="passport" v-model="passport" placeholder="Паспорт"></b-form-input>
            </div>
            <p class="m-1 font-weight-bold">Балл по экзаменам</p>
            <div class="m-1">
              <label for="profile_exam">Профильные</label>
              <b-form-input id="profile_exam" v-model="profile_exam" placeholder="Профильные"></b-form-input>
            </div>
            <div class="m-1">
              <label for="common_exam">Общие</label>
              <b-form-input id="common_exam" v-model="common_exam" placeholder="Общие"></b-form-input>
            </div>
            <p class="m-1 font-weight-bold">Средний балл аттестата</p>
            <div class="m-1">
              <label for="certificate_avg">Средний балл аттестата</label>
              <b-form-input id="certificate_avg" v-model="certificate_avg" placeholder="Средний балл аттестата"></b-form-input>
            </div>
            <div class="m-1 mt-4">
              <b-button variant="primary" @click="signup()">Регистрация</b-button>
            </div>
          </b-form>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  name: 'SignUp',
  data () {
    return {
      username: '',
      password: '',
      last_name: '',
      first_name: '',
      patronymic: '',
      schoolClass: null,
      schoolClasses: [{ text: 'Выберите класс', value: null, disabled: true }, { text: '9', value: '1' }, { text: '11', value: '2' }],
      privelege: null,
      priveleges: [{ text: 'Выберите льготы', value: null, disabled: true }, { text: 'Нет льгот', value: '1' }, { text: 'Инвалид', value: '2' }, { text: 'Сирота', value: '3' }],
      certificate: '',
      passport: '',
      profile_exam: '',
      common_exam: '',
      certificate_avg: '',
      user: '',
      doc: '',
      cert: '',
      exam: ''
    }
  },
  methods: {
    signup () {
      this.axios
        .post(`http://${window.location.hostname}:8005/api/auth/users/`, { username: this.username, password: this.password })
        .then(response => { console.log(response); this.user = response.data.id; this.addDocuments() })
        .catch(err => { console.error(err) })
    },
    addDocuments () {
      this.axios
        .post(`http://${window.location.hostname}:8005/api/add/doc/`, { passport_num: this.passport, certificate_num: this.certificate })
        .then(response => { this.doc = response.data.id; this.addCertificate() })
        .catch(err => { console.error(err) })
    },
    addCertificate () {
      this.axios
        .post(`http://${window.location.hostname}:8005/api/add/cert/`, { avg_mark: this.certificate_avg })
        .then(response => { this.cert = response.data.id; this.addExam() })
        .catch(err => { console.error(err) })
    },
    addExam () {
      this.axios
        .post(`http://${window.location.hostname}:8005/api/add/exam/`, { profile_points: this.profile_exam, common_points: this.common_exam })
        .then(response => { this.exam = response.data.id; this.addEnrollee() })
        .catch(err => { console.error(err) })
    },
    addEnrollee () {
      let enrollee = {
        school_class: this.schoolClass,
        privelege: this.privelege,
        first_name: this.first_name,
        last_name: this.last_name,
        patronymic: this.patronymic,
        documents: this.doc,
        exams: this.exam,
        certificate_avg: this.cert,
        user: this.user
      }

      this.axios
        .post(`http://${window.location.hostname}:8005/api/add/enrollee/`, enrollee)
        .then(response => { console.log(response); localStorage.setItem('enrollee', response.data.id); this.$router.push('/signin') })
        .catch(err => { console.error(err) })
    }
  },
  mounted () {
    if (sessionStorage.getItem('token')) {
      this.$router.push('/application/new')
      return
    }
  }
}
</script>
