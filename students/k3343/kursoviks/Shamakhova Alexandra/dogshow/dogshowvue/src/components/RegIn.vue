<template>
  <main>
    <v-col cols="8" class="my-1 mx-auto">
      <h2>Регистрация участника</h2>
    </v-col>
    <v-col cols="8" class="mx-auto">
      <form>
        <v-text-field v-model="reg_username" label="Логин" required></v-text-field>
        <v-text-field v-model="reg_surname" label="Фамилия" required></v-text-field>
        <v-text-field v-model="reg_name" label="Имя" required></v-text-field>
        <v-text-field v-model="reg_patronym" label="Отчество" required></v-text-field>
        <v-text-field v-model="reg_passport" label="Паспорт" required></v-text-field>
        <v-text-field
          v-model="reg_password"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="show1 ? 'text' : 'password'"
          name="input-10-1"
          label="Пароль"
          @click:append="show1 = !show1"
          required>
        </v-text-field>
        <v-btn class="light-green darken-4" @click="newUser">Зарегестрироваться</v-btn>
        <v-btn class="mr-4" :to="'/login'" color="teal lighten-1" dark>Есть аккаунт?</v-btn>
      </form>
    </v-col>
  </main>
</template>

<script>
export default {
  name: 'RegHuman',
  data () {
    return {
      reg_username: '',
      reg_surname: '',
      reg_name: '',
      reg_patronym: '',
      reg_passport: '',
      reg_password: '',
      client_user: ''
    }
  },
  props: ['show1'],
  methods: {
    newUser () {
      let userdata = {
        username: this.reg_username,
        password: this.reg_password
      }

      this.axios
        .post(`http://127.0.0.1:8000/api/auth/users/`, userdata)
        .then(response => { this.newClient(response.data) })
        .catch(err => { console.error(err) })
    },
    newClient (data) {
      this.client_user = data.id
      let clientdata = {
        user: this.client_user,
        human_surname: this.reg_surname,
        human_name: this.reg_name,
        human_patronym: this.reg_patronym,
        human_passport: this.reg_passport
      }

      this.axios
        .post(`http://127.0.0.1:8000/api/human/new`, clientdata)
        .then(response => { this.clearForm(response.data) })
        .catch(err => { console.error(err) })
    },
    clearForm () {
      this.reg_username = ''
      this.reg_surname = ''
      this.reg_name = ''
      this.reg_patronym = ''
      this.reg_passport = ''
      this.reg_password = ''
      this.client_user = ''
      this.$router.push('/login')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h2 {
  font-weight: normal;
}
</style>
