<template>
  <main>
    <section>
      <v-col cols="8" class="mx-auto">
        <h1 class="headline">Отель "Белорусская"</h1>
        <p>Почувствуйте эту свободу вместе с нами.</p>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="mx-auto">
        <v-card class="mx-auto my-2">
          <v-img src="https://hotel-spb.ru/images/main-photo.jpg" height="600px"></v-img>
          <v-card-title>
            ЛУЧШИЙ ВИД В ГОРОДЕ
          </v-card-title>
          <v-card-subtitle>
            Доступно {{ freeRooms }} номеров
          </v-card-subtitle>
          <v-card-actions>
            <v-btn color="primary" @click="rentRoom" dark>Арендовать номер сейчас</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="mx-auto">
        <v-row>
          <v-col cols="6">
            <v-card class="mx-auto my-2">
              <v-img src="https://static6.depositphotos.com/1000816/563/i/450/depositphotos_5632643-stock-photo-big-group-of-business-isolated.jpg" height="300px"></v-img>
              <v-card-title>
                СТАНЬ ЧАСТЬЮ НАШЕЙ КОМАНДЫ
              </v-card-title>
              <v-card-subtitle>
                Подавай заявку сегодня и завтра уже будешь работать с нами!
              </v-card-subtitle>
              <v-card-actions>
                <v-btn color="teal" @click="newServant" dark>Подать заявку</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
          <v-col cols="6">
            <v-card class="mx-auto my-2">
              <v-img src="https://st3.depositphotos.com/12674628/15819/i/450/depositphotos_158195266-stock-photo-family-spending-time-together.jpg" height="300px"></v-img>
              <v-card-title>
                НОМЕР ДЛЯ ВСЕЕЕЙ СЕМЬИ
              </v-card-title>
              <v-card-subtitle>
                Арендуя сейчас - вы арендуете не номер, а счастливый отпуск
              </v-card-subtitle>
              <v-card-actions>
                <v-btn color="red" @click="rentRoom" dark>Арендовать</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </section>
  </main>
</template>
<script>
export default {
  name: 'Index',
  data () {
    return {
      freeRooms: 0
    }
  },
  methods: {
    rentRoom () {
      this.$router.push('/get_room')
    },
    newServant () {
      this.$router.push('/new_servant')
    }
  },
  mounted () {
    this.axios
      .get('http://127.0.0.1:8000/api/rooms/')
      .then(response => {
        let freeRooms = response.data.filter(room => room.room_state === '1')

        this.freeRooms = freeRooms.length
      })
      .catch(err => { console.error(err) })
  }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
