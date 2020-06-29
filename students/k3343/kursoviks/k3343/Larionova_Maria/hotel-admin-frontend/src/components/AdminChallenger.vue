<template>
  <main>
    <v-col cols="10" class="mx-auto">
      <h1>Кабинет Претендента</h1>
      <div class="my-2">
        <v-col cols="8" class="mx-auto">
          <v-row dense class="my-2">
            <v-card v-for="r in requests" :key="r.id" class="mx-auto my-2">
              <v-card-title>
                Заявка на работу # {{ r.id }} от {{ r.name }}, д. р. {{ r.birthdate }}
              </v-card-title>
              <v-card-subtitle>
                Должность: служащий
              </v-card-subtitle>
              <v-card-text>
                Паспорт: {{ r.passport }}
              </v-card-text>
              <v-card-text>
                Статус: {{ r.isHired }}
              </v-card-text>
              <v-card-text>
                Дата изменения статуса: {{ r.date }}
              </v-card-text>
              <v-card-text>
                Ответственный: {{ r.admin }}
              </v-card-text>
              <v-card-actions v-if="r.isHired === 'Not hired'">
                <v-btn text @click="hire(r.id)">Принять на работу</v-btn>
              </v-card-actions>
            </v-card>
          </v-row>
        </v-col>
      </div>
    </v-col>
  </main>
</template>
<script>
export default {
  name: 'AdminChallenger',
  data () {
    return {
      requests: []
    }
  },
  mounted () {
    if (!sessionStorage.getItem('token')) {
      this.$router.push('/auth')
      return
    }

    this.showAllReqs()
  },
  methods: {
    hire (reqId) {
      this.axios
        .patch(`http://${window.location.hostname}:8000/api/request/update/${reqId}`, { state: '2' })
        .then(response => { console.log(response); this.showAllReqs() })
        .catch(err => { console.error(err) })
    },
    showAllReqs () {
      this.requests = []

      this.axios
        .get(`http://${window.location.hostname}:8000/api/request/all`)
        .then(response => {
          let request = response.data[0]
          console.log('reqdata', request)
          let challenger = request.challenger
          let req = {}
          req.id = request.id
          req.name = challenger.surname + ' ' + challenger.name + ' ' + challenger.middle_name
          req.birthdate = challenger.birthdate
          req.passport = challenger.passport
          req.isHired = request.state
          req.date = request.date
          req.admin = request.administrator.surname

          this.requests.push(req)
        })
        .catch(err => { console.error(err) })
    }
  }
}

</script>
<style></style>
