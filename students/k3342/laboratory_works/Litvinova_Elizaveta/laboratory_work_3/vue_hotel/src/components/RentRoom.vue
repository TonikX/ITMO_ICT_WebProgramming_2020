<template>
  <main>
    <section>
      <v-col cols="8" class="mx-auto">
        <h1 class="headline">Отель "Белорусская"</h1>
        <p>Арендуя номер сегодня - вы получаете гарантированно счастливый отпуск и пару улыбок в подарок!</p>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="mx-auto">
        <h2 class="headline">Аренда номера</h2>
        <v-form>
          <v-text-field label="Фамилия" v-model="surname"></v-text-field>
          <v-text-field label="Имя" v-model="name"></v-text-field>
          <v-text-field label="Отчество" v-model="middle_name"></v-text-field>
          <v-text-field label="Город, из которого приезжаете" v-model="city_from"></v-text-field>
          <v-select v-model="room" :items="rooms"></v-select>
          <v-text-field type="date" v-model="arrival_date" label="С"></v-text-field>
          <v-text-field type="date" v-model="departure_date" label="По"></v-text-field>
          <v-btn color="primary" @click="rent">Арендовать</v-btn>
          <v-btn color="red" dark @click="reset">Сбросить</v-btn>
        </v-form>
      </v-col>
    </section>
    <section>
      <v-dialog v-model="success" max-width="400">
        <v-card>
          <v-card-title class="headline">Аренда прошла успешно!</v-card-title>
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
  name: 'RentRoom',
  data () {
    return {
      surname: '',
      name: '',
      middle_name: '',
      room: null,
      rooms: [
        { text: 'Выберите номер', value: null }
      ],
      arrival_date: '',
      departure_date: '',
      success: false,
      city_from: ''
    }
  },
  methods: {
    rent () {
      this.axios
        .post('http://127.0.0.1:8000/api/client/add/', { name: this.name, surname: this.surname, middle_name: this.middle_name, city_from: this.city_from })
        .then(response => { this.addClientRoom(response.data.id) })
        .catch(err => { console.error(err) })
    },
    addClientRoom (clientId) {
      this.axios
        .post('http://127.0.0.1:8000/api/client/room/add/', { client: clientId, room: this.room, arrival_date: this.arrival_date, departure_date: this.departure_date })
        .then(response => { this.updateRoomAccept() })
        .catch(err => { console.error(err) })
    },
    updateRoomAccept () {
      this.axios
        .patch(`http://127.0.0.1:8000/api/room/${this.room}/`, { room_state: '2' })
        .then(response => { console.log(response); this.success = true; this.reset() })
        .catch(err => { console.error(err) })
    },
    reset () {
      this.surname = ''
      this.name = ''
      this.middle_name = ''
      this.room = null
      this.arrival_date = ''
      this.departure_date = ''
      this.city_from = ''
    }
  },
  mounted () {
    this.axios
      .get('http://127.0.0.1:8000/api/rooms/')
      .then(response => {
        let freeRooms = response.data.filter(room => room.room_state === '1')

        freeRooms.forEach((room) => {
          this.rooms.push({ text: `Номер на ${room.room_type} человека, цена: ${room.price}`, value: room.id })
        })
      })
      .catch(err => { console.error(err) })
  }
}

</script>
<style></style>
