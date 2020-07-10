<template>
  <main>
    <section>
      <v-col cols="8" class="mx-auto">
        <h1 class="headline">Отель "Белорусская"</h1>
        <p>Устраиваясь на работу сегодня - Вы становитесь частью дружелюбной интернациональной команды!</p>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="mx-auto">
        <h2 class="headline">Анкета для служащего</h2>
        <v-form>
          <p>Данные для входа</p>
          <v-text-field label="Имя пользователя" v-model="username"></v-text-field>
          <v-text-field type="password" label="Пароль" v-model="password"></v-text-field>
          <p>Ваши данные для анкеты</p>
          <v-text-field label="Фамилия" v-model="surname"></v-text-field>
          <v-text-field label="Имя" v-model="name"></v-text-field>
          <v-text-field label="Отчество" v-model="middle_name"></v-text-field>
          <v-text-field label="Паспорт" v-model="passport"></v-text-field>
          <v-text-field type="date" v-model="birthdate" label="Дата рождения"></v-text-field>
          <v-text-field type="number" label="Стаж работы" v-model="work_experience"></v-text-field>
          <v-btn color="primary" @click="submit">Отправить заявку</v-btn>
          <v-btn color="red" dark @click="reset">Сбросить</v-btn>
        </v-form>
      </v-col>
    </section>
    <section>
      <v-dialog v-model="success" max-width="400">
        <v-card>
          <v-card-title class="headline">Ваша анкета принята!</v-card-title>
          <v-card-text>
            Наш оператор свяжется с Вами в течение пяти минут и уточнит все вопросы.
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="teal" dark @click="success = false">
              Хорошо
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </section>
  </main>
</template>
<script>
export default {
  name: 'NewServant',
  data () {
    return {
      surname: '',
      name: '',
      middle_name: '',
      birthdate: '',
      passport: '',
      success: false,
      username: '',
      password: '',
      work_experience: ''
    }
  },
  methods: {
    submit () {
      this.axios
        .post('http://127.0.0.1:8000/api/auth/users/', { username: this.username, password: this.password })
        .then(response => { this.addServant(response.data.id) })
        .catch(err => { console.error(err) })
    },
    addServant (userId) {
      this.axios
        .post('http://127.0.0.1:8000/api/employee/add/', { name: this.name, surname: this.surname, middle_name: this.middle_name, user: userId, birthdate: this.birthdate, passport: this.passport, position: '3', work_experience: this.work_experience })
        .then(response => { this.success = true; this.reset() })
        .catch(err => { console.error(err) })
    },
    reset () {
      this.surname = ''
      this.name = ''
      this.middle_name = ''
      this.birthdate = ''
      this.passport = ''
      this.username = ''
      this.password = ''
      this.work_experience = ''
    }
  },
  mounted () {
    if (localStorage.getItem('token')) {
      this.$router.push('/')
    }
  }
}

</script>
<style></style>
