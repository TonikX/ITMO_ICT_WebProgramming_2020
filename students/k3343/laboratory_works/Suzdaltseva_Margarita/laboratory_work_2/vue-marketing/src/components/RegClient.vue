<template>
  <main>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h2>Регистрация клиента</h2>
      </v-col>
      <v-col cols="8" class="mx-auto">
        <form>
          <v-text-field v-model="reg_username" label="Логин" required></v-text-field>
          <v-text-field v-model="reg_email" label="Почта" required></v-text-field>
          <v-text-field v-model="reg_first_name" label="Имя" required></v-text-field>
          <v-text-field v-model="reg_last_name" label="Фамилия" required></v-text-field>
          <v-text-field v-model="reg_compname" label="Название компании" required></v-text-field>
          <v-select v-model="reg_comptype" :items="types" label="Тип организации" required></v-select>
          <v-text-field
            v-model="reg_password"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            label="Пароль"
            @click:append="show1 = !show1"
            required>
          </v-text-field>
          <v-text-field v-model="reg_phone" label="Телефон" required></v-text-field>
          <v-btn dark class="mr-4 pink accent-3" @click="newUser">Зарегистрироваться!</v-btn>
        </form>
      </v-col>
    </section>
  </main>
</template>
<script>
export default {
  name: 'RegClient',
  data () {
    return {
      reg_username: '',
      reg_email: '',
      reg_first_name: '',
      reg_last_name: '',
      reg_password: '',
      reg_phone: '',
      reg_comptype: '',
      reg_compname: '',
      client_user: '',
      client_company: '',
      types: [
        {value: 1, text: 'ИП'},
        {value: 2, text: 'ОАО'},
        {value: 3, text: 'ООО'},
        {value: 4, text: 'ЗАО'},
        {value: 5, text: 'ПТ'},
        {value: 6, text: 'ТНВ'},
        {value: 7, text: 'ГКП'}
      ]
    }
  },
  props: ['show1'],
  methods: {
    newUser () {
      let userdata = {
        username: this.reg_username,
        email: this.reg_email,
        password: this.reg_password
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/auth/users/`, userdata)
        .then(response => { this.newCompany(response.data) })
        .catch(err => { console.error(err) })
    },
    newCompany (data) {
      this.client_user = data.id
      let compdata = {
        company_type: this.reg_comptype,
        name: this.reg_compname
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/company/new`, compdata)
        .then(response => { this.newClient(response.data) })
        .catch(err => { console.error(err) })
    },
    newClient (data) {
      this.client_company = data.id
      let clientdata = {
        user: this.client_user,
        phone: this.reg_phone,
        company: this.client_company,
        first_name: this.reg_first_name,
        last_name: this.reg_last_name
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/client/new`, clientdata)
        .then(response => { this.clearForm() })
        .catch(err => { console.error(err) })
    },
    clearForm () {
      this.reg_username = ''
      this.reg_email = ''
      this.reg_first_name = ''
      this.reg_last_name = ''
      this.reg_password = ''
      this.reg_phone = ''
      this.reg_comptype = ''
      this.reg_compname = ''
      this.client_user = ''
      this.client_company = ''

      this.$router.push('/auth')
    }
  }
}
</script>
<style scoped>
</style>
