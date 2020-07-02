<template>
  <main>
    <section>
      <v-col cols="8" class="mx-auto">
        <h1 class="headline">Отель "Белорусская"</h1>
        <p>На этой странице вы можете войти в кабинет служащего или в админ-панель!</p>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="mx-auto">
        <h2 class="headline">Вход в аккаунт</h2>
        <v-form>
          <v-text-field label="Имя пользователя" v-model="username"></v-text-field>
          <v-text-field type="password" label="Пароль" v-model="password"></v-text-field>
          <v-btn color="primary" @click="login">Войти</v-btn>
        </v-form>
      </v-col>
    </section>
  </main>
</template>
<script>
export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login () {
      this.axios
        .post('http://127.0.0.1:8000/api/auth/token/', { username: this.username, password: this.password })
        .then(response => { localStorage.setItem('token', response.data.token); localStorage.setItem('username', this.username); this.who(this.username) })
        .catch(err => { console.error(err) })
    },
    who (username) {
      this.axios
        .get(`http://127.0.0.1:8000/api/employees/?username=${username}`)
        .then(response => {
          let position = response.data[0].position

          if (position === '2') {
            localStorage.setItem('servant', username)
            this.$router.push('/servant')
          } else if (position === '1') {
            localStorage.setItem('admin', username)
            this.$router.push('/admin')
          } else if (position === '3') {
            localStorage.setItem('challenger', username)
            this.$router.push('/servant')
          }
        })
    }
  }
}

</script>
