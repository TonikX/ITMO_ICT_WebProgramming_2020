<template>
  <main>
    <v-col cols="10" class="mx-auto">
      <h1>Кабинет Претендента</h1>
      <div class="my-2">
        <v-col cols="8" class="mx-auto">
          <v-row dense class="my-2">
            <v-card class="mx-auto my-2">
              <v-card-title>
                Заявка на работу # {{ id }} от {{ name }}, д. р. {{ birthdate }}
              </v-card-title>
              <v-card-subtitle>
                Должность: служащий
              </v-card-subtitle>
              <v-card-text>
                Паспорт: {{ passport }}
              </v-card-text>
              <v-card-text>
                Статус: {{ isHired }}
              </v-card-text>
              <v-card-text>
                Дата изменения статуса: {{ date }}
              </v-card-text>
              <v-card-text>
                Ответственный: {{ admin }}
              </v-card-text>
            </v-card>
          </v-row>
        </v-col>
      </div>
    </v-col>
  </main>
</template>
<script>
export default {
  name: 'ChallengerCabinet',
  data () {
    return {
      id: '',
      name: '',
      birthdate: '',
      passport: '',
      isHired: '',
      date: '',
      admin: ''
    }
  },
  mounted () {
    if (!sessionStorage.getItem('token')) {
      this.$router.push('/auth')
      return
    }

    this.axios
      .get(`http://${window.location.hostname}:8000/api/request/all?username=${sessionStorage.getItem('worker')}`)
      .then(response => {
        let request = response.data[0]
        console.log('reqdata', request)
        let challenger = request.challenger

        this.id = request.id
        this.name = challenger.surname + ' ' + challenger.name + ' ' + challenger.middle_name
        this.birthdate = challenger.birthdate
        this.passport = challenger.passport
        this.isHired = request.state
        this.date = request.date
        this.admin = request.administrator.surname
      })
      .catch(err => { console.error(err) })
  }
}

</script>
<style></style>
