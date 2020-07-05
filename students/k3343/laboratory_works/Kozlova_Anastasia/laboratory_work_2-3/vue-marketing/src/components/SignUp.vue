<template>
  <main>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h1>Регистрация</h1>
        <p class="my-1">Уже зарегистрированы? <router-link to="/auth">Вход</router-link></p>
      </v-col>
      <v-col cols="4" class="mx-auto">
        <form>
          <v-text-field v-model="username" label="Логин" required></v-text-field>
          <v-text-field v-model="password" label="Пароль" type="password" required></v-text-field>
          <v-text-field v-model="patronymic" label="ФИО" required></v-text-field>
          <v-text-field v-model="phone" label="Телефон" type="tel" required></v-text-field>
          <v-text-field v-model="email" label="Почта" type="email" required></v-text-field>
          <v-text-field v-model="company_name" label="Название компании" required></v-text-field>
          <v-text-field v-model="company_sphere" label="Сфера, в которой работает компания" required></v-text-field>
          <v-select v-model="company_type" :items="company_types" label="ИП/ООО" required></v-select>
          <v-btn dark class="teal" @click="signUp">Зарегистрировать аккаунт</v-btn>
        </form>
      </v-col>
    </section>
  </main>
</template>
<script>
export default {
  name: 'SignUp',
  data () {
    return {
      username: '',
      email: '',
      password: '',
      phone: '',
      company_type: '',
      company_name: '',
      company_sphere: '',
      user_id: '',
      patronymic: '',
      company_id: '',
      company_types: [
        { value: 1, text: 'ИП' },
        { value: 2, text: 'ООО' }
      ]
    }
  },
  methods: {
    signUp () {
      let user = {
        username: this.username,
        email: this.email,
        password: this.password
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/auth/users/`, user)
        .then(response => { this.addCompany(response.data) })
        .catch(err => { console.error(err) })
    },
    addCompany (data) {
      this.user_id = data.id

      let company = {
        company_type: this.company_type,
        name: this.company_name,
        sphere: this.company_sphere
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/company/new`, company)
        .then(response => { this.addClient(response.data) })
        .catch(err => { console.error(err) })
    },
    addClient (data) {
      this.company_id = data.id

      let client = {
        user: this.user_id,
        phone: this.phone,
        company: this.company_id,
        patronymic: this.patronymic
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/client/new`, client)
        .then(response => { this.clear() })
        .catch(err => { console.error(err) })
    },
    clear () {
      this.username = ''
      this.email = ''
      this.reg_first_name = ''
      this.reg_last_name = ''
      this.password = ''
      this.phone = ''
      this.company_type = ''
      this.company_name = ''
      this.user_id = ''
      this.company_id = ''
      this.patronymic = ''

      this.$router.push('/auth')
    }
  }
}
</script>
<style scoped>
</style>
