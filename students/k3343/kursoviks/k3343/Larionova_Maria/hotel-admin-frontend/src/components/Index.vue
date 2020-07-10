<template>
  <main>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h1>Добро пожаловать в отель "Hotel"</h1>
        <p></p>
        <p>У нас Вы проведёте своё время абсолютно незабываемо!</p>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h2>Свободные номера</h2>
        <p>Любой номер под Ваши нужды</p>
      </v-col>
      <v-col cols="8" class="mx-auto">
        <v-row dense class="my-2">
          <v-card class="mx-auto my-2" max-width="350">
            <v-img src="https://images.unsplash.com/photo-1576675784201-0e142b423952?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1352&q=80" height="200px"></v-img>
            <v-card-title>
              Уютный номер для одного
            </v-card-title>
            <v-card-subtitle>
              Доступно: {{ onePerson }}
            </v-card-subtitle>
          </v-card>
          <v-card class="mx-auto my-2" max-width="350">
            <v-img src="https://images.unsplash.com/photo-1568495248636-6432b97bd949?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1267&q=80" height="200px"></v-img>
            <v-card-title>
              Комфорт для двоих
            </v-card-title>
            <v-card-subtitle>
              Доступно: {{ twoPersons }}
            </v-card-subtitle>
          </v-card>
          <v-card class="mx-auto my-2" max-width="350">
            <v-img src="https://images.unsplash.com/photo-1507038772120-7fff76f79d79?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1267&q=80" height="200px"></v-img>
            <v-card-title>
              Мама, папа, я! (Номер на 3)
            </v-card-title>
            <v-card-subtitle>
              Доступно: {{ threePersons }}
            </v-card-subtitle>
          </v-card>
        </v-row>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h2>Прайс</h2>
        <p>Отель "Hotel" - стабильно низкие цены</p>
      </v-col>
      <v-col cols="5" class="mx-auto my-1">
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">Тип номера</th>
                <th class="text-left">Стоимость</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in rooms" :key="item.name">
                <td>{{ item.name }}</td>
                <td>{{ item.price }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
      <p></p>
    </section>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h2>Арендовать номер</h2>
        <p>Просто заполните форму и мы с Вами свяжемся</p>
      </v-col>
      <v-col cols="5" class="mx-auto">
        <form>
          <v-text-field v-model="room_last_name" label="Фамилия" required></v-text-field>
          <v-text-field v-model="room_first_name" label="Имя" required></v-text-field>
          <v-text-field v-model="room_middle_name" label="Отчество" required></v-text-field>
          <v-text-field v-model="room_passport" label="Паспорт" required></v-text-field>
          <v-text-field v-model="room_from" label="Откуда к нам приезжаете?" required></v-text-field>
          <v-text-field v-model="room_date" label="Когда приедете? (ГГГГ-ММ-ДД)" required></v-text-field>
          <v-select v-model="room" :items="freeRooms" label="Номер" required></v-select>
          <v-btn class="mr-4" color="deep-orange" dark @click="submitRoom">Отправить</v-btn>
          <v-btn @click="clearRoom" color="indigo" dark >Очистить</v-btn>
        </form>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h2>Как устроиться служащим?</h2>
        <p>Всё просто! Заполните анкету:</p>
      </v-col>
      <v-col cols="5" class="mx-auto">
        <form>
          <v-text-field v-model="last_name" label="Фамилия" required></v-text-field>
          <v-text-field v-model="first_name" label="Имя" required></v-text-field>
          <v-text-field v-model="middle_name" label="Отчество" required></v-text-field>
          <v-text-field v-model="passport" label="Паспорт" required></v-text-field>
          <v-text-field type="email" v-model="email" label="Email" required></v-text-field>
          <v-text-field v-model="birthdate" label="Дата рождения (ГГГГ-ММ-ДД)" required></v-text-field>
          <v-text-field v-model="username" label="Имя пользователя" required></v-text-field>
          <v-text-field v-model="password" type="password" label="Пароль" required></v-text-field>
          <v-btn class="mr-4" @click="submitChallenger" color="deep-orange" dark >Отправить</v-btn>
          <v-btn @click="clearChallenger" color="indigo" dark >Очистить</v-btn>
        </form>
      </v-col>
    </section>
    <v-dialog
      v-model="success"
      max-width="350"
    >
      <v-card>
        <v-card-title class="headline">Спасибо!</v-card-title>

        <v-card-text>
          Мы свяжемся с Вами в ближайшее время!
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
            @click="success = false"
          >
            Ок
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </main>
</template>
<script>
export default {
  name: 'Index',
  data () {
    return {
      rooms: [{
        name: '1 персона',
        price: 600
      },
      {
        name: '2 персоны',
        price: 800
      },
      {
        name: '3 персоны',
        price: 1200
      }
      ],
      room_last_name: '',
      room_first_name: '',
      room_middle_name: '',
      room_passport: '',
      room_from: '',
      room_date: '',
      room: '',
      last_name: '',
      first_name: '',
      middle_name: '',
      passport: '',
      email: '',
      birthdate: '',
      freeRooms: [],
      success: false,
      onePerson: 0,
      twoPersons: 0,
      threePersons: 0,
      username: '',
      password: ''
    }
  },
  methods: {
    submitRoom () {
      let data = {
        'name': this.room_first_name,
        'surname': this.room_last_name,
        'middle_name': this.room_middle_name,
        'city_from': this.room_from
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/client/new`, data)
        .then(response => { console.log(response); this.submitClient(response.data.id) })
        .catch(err => { console.error(err) })
    },
    submitClient (clientId) {
      console.log('date is', this.room_date)

      let data = {
        'date': this.room_date,
        'room': this.room,
        'client': clientId
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/client/room/new`, data)
        .then(response => { console.log(response) })
        .catch(err => { console.error(err) })

      this.axios
        .patch(`http://${window.location.hostname}:8000/api/room/${this.room}`, { 'room_state': '2' })
        .then(response => { console.log(response); this.clearRoom(); this.success = true })
        .catch(err => { console.error(err) })
    },
    updateRooms (data) {
      let freeRooms = []

      data.filter((room) => {
        if (room.room_state === '1' && room.room_type !== undefined) {
          freeRooms.push({ 'text': `${room.room_type}, price: ${room.price}`, 'value': `${room.id}` })
        }
      })

      data.map((room) => {
        if (room.room_state === '1' && room.room_type === '1 person') {
          this.onePerson += 1
        }
        if (room.room_state === '1' && room.room_type === '2 persons') {
          this.twoPersons += 1
        }
        if (room.room_state === '1' && room.room_type === '3 persons') {
          this.threePersons += 1
        }
      })

      this.freeRooms = freeRooms.length > 0 ? freeRooms : [{ 'text': 'Комнат нет', 'value': null, 'disabled': true }]
    },
    clearRoom () {
      this.room_last_name = ''
      this.room_first_name = ''
      this.room_middle_name = ''
      this.room_passport = ''
      this.room_from = ''
      this.room_date = ''
      this.room = ''

      this.axios
        .get(`http://${window.location.hostname}:8000/api/room/all`)
        .then(response => { this.updateRooms(response.data) })
        .catch(err => { console.error(err) })
    },
    submitChallenger () {
      let data = {
        username: this.username,
        password: this.password
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/auth/users/`, data)
        .then(response => { console.log(response); this.addChallenger(response.data.id) })
    },
    addChallenger (userId) {
      let data = {
        name: this.last_name,
        surname: this.first_name,
        middle_name: this.middle_name,
        passport: this.passport,
        email: this.email,
        birthdate: this.birthdate,
        user: userId
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/challenger/new`, data)
        .then(response => { console.log(response); this.addRequest(response.data.id) })
        .catch(err => { console.error(err) })
    },
    addRequest (challengerId) {
      let date = new Date()
      let currDate = {
        y: `${date.getFullYear()}`,
        m: `${date.getMonth()}`.length > 1 ? `${date.getMonth() + 1}` : `0${date.getMonth() + 1}`,
        d: `${date.getDate()}`.length > 1 ? `${date.getDate()}` : `0${date.getDate()}`
      }

      let today = `${currDate.y}-${currDate.m}-${currDate.d}`

      let data = {
        challenger: challengerId,
        date: today,
        state: 1
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/request/new`, data)
        .then(response => { console.log(response); this.clearChallenger(); this.success = true })
        .catch(err => { console.error(err) })
    },
    clearChallenger () {
      this.last_name = ''
      this.first_name = ''
      this.middle_name = ''
      this.passport = ''
      this.email = ''
      this.birthdate = ''
      this.username = ''
      this.password = ''
    }
  },
  mounted () {
    this.axios
      .get(`http://${window.location.hostname}:8000/api/room/all`)
      .then(response => { this.updateRooms(response.data) })
      .catch(err => { console.error(err) })
  }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
