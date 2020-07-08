<template>
  <main class="container">
    <b-form @submit="submit">
      <b-form-group id="input-group-2" label="Имя:" label-for="input-2">
        <b-form-input id="input-2" v-model="first_name" required></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-2" label="Фамилия:" label-for="input-2">
        <b-form-input id="input-2" v-model="last_name" required></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-2" label="Отчество:" label-for="input-2">
        <b-form-input id="input-2" v-model="patronymic" required></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-2" label="Стаж работы:" label-for="input-2">
        <b-form-input id="input-2" v-model="work_experience" required></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-2" label="Возраст:" label-for="input-2">
        <b-form-input id="input-2" v-model="age" required></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-2" label="Образование:" label-for="input-2">
        <b-form-input id="input-2" v-model="education" required></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-2" label="Паспорт:" label-for="input-2">
        <b-form-input id="input-2" v-model="passport" required></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-3" label="Компания:" label-for="input-3">
        <b-form-select id="input-3" v-model="company" :options="companies" required></b-form-select>
      </b-form-group>
      <b-form-group id="input-group-3" label="Позиция:" label-for="input-3">
        <b-form-select id="input-3" v-model="position" :options="positions" required></b-form-select>
      </b-form-group>
      <b-button type="submit" v-b-modal.modal-1 variant="primary">Отправить</b-button>
      <b-button @click="reset" variant="danger">Сбросить</b-button>
    </b-form>
    <b-modal id="modal-1" title="Спасибо!">
      <p class="my-4">Мы рассмотрим Вашу заявку и свяжемся с Вами.</p>
    </b-modal>
  </main>
</template>
<script>
export default {
  name: 'Challenger',
  data() {
    return {
      first_name: '',
      last_name: '',
      patronymic: '',
      work_experience: '',
      age: '',
      education: '',
      passport: '',
      company: null,
      companies: [{ 'text': 'Выберите компанию', 'value': null, 'disabled': true }],
      position: null,
      positions: [
        { 'text': 'Выберите должность', 'value': null, 'disabled': true },
        { 'text': 'Капитан', 'value': 1 },
        { 'text': 'Второй пилот', 'value': 2 },
        { 'text': 'Штурман', 'value': 3 },
        { 'text': 'Стюард', 'value': 4 },
        { 'text': 'Стюардесса', 'value': 5 }
      ],
      modal: false
    }
  },
  methods: {
    submit() {
      window.event.preventDefault()
      let data = {
        'first_name': this.first_name,
        'last_name': this.last_name,
        'patronymic': this.patronymic,
        'work_experience': this.work_experience,
        'age': this.age,
        'education': this.education,
        'passport': this.passport,
        'company': this.company,
        'position': this.position
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/challengers/`, data)
        .then(response => { console.log(response); this.reset(); this.modal = true })
        .catch(err => { console.error(err) })
    },
    reset() {
      this.first_name = ''
      this.last_name = ''
      this.patronymic = ''
      this.work_experience = ''
      this.age = ''
      this.education = ''
      this.passport = ''
      this.company = null
      this.position = null
    },
    showCompanies(companies) {
      for (let i = 0; i < companies.length; i++) {
        let company = {}
        company.value = companies[i].id
        company.text = companies[i].name

        this.companies.push(company)
      }
    }
  },
  mounted() {
    this.axios
      .get(`http://${window.location.hostname}:8000/api/companies/`)
      .then(response => {
        console.log(response); this.showCompanies(response.data)
      })
      .catch(err => { console.error(err) })

  }
}

</script>
<style></style>
