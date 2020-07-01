<template>
  <main class="container mx-auto">
    <h1 class="headline">Вход</h1>
    <section>
      <v-col cols="5" class="mx-auto">
        <v-form>
          <v-text-field v-model="username" label="Имя пользователя"></v-text-field>
          <v-text-field v-model="password" type="password" label="Пароль"></v-text-field>
          <v-btn color="blue accent-2" dark @click="login">
            <v-icon>mdi-send</v-icon>Войти
          </v-btn>
        </v-form>
      </v-col>
      </v-form>
    </section>
  </main>
</template>
<script>
export default {
  name: 'Auth',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login() {
      let user = {
        username: this.username,
        password: this.password
      }

      this.axios
        .post('http://127.0.0.1:8000/api/auth/token', user)
        .then(response => {
          console.log(response)
          localStorage.setItem('username', this.username)
          localStorage.setItem('token', response.data.token)

          this.axios
            .get(`http://127.0.0.1:8000/api/enrollee/all?username=${this.username}`)
            .then(response => {
              if (!response.data.length) {
                localStorage.setItem('secretary', true)
                this.$router.push('/secretary')
                return
              }
              localStorage.setItem('enrollee', response.data[0].id)
              this.$router.push('/enrollee')
            })
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
