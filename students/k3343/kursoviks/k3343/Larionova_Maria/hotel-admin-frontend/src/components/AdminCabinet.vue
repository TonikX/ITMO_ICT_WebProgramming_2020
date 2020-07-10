<template>
  <main>
    <v-col cols="10" class="mx-auto">
      <h1>Кабинет администратора</h1>
    </v-col>
    <section>
      <v-col cols="10" class="mx-auto">
        <h2 class="my-2">Статистика</h2>
        <v-btn color="teal" class="my-5" dark to="/edit_challenger">Всё заявки на работу</v-btn>
        <p><strong>Свободных номеров на 1 персону:</strong> {{ onePerson }}</p>
        <p><strong>Свободных номеров на 2 персоны:</strong> {{ twoPersons }}</p>
        <p><strong>Свободных номеров на 3 персоны:</strong> {{ threePersons }}</p>
        <p><strong>Актуальный доход с занятых номеров:</strong> {{ money }}</p>
      </v-col>
    </section>
    <section>
      <v-col cols="10" class="mx-auto">
        <h2>Расписание смен служащих</h2>
        <div class="my-2">
          <v-col cols="5" class="mx-auto my-1">
            <v-simple-table>
              <template v-slot:default>
                <thead>
                  <tr>
                    <th class="text-left">Дата</th>
                    <th class="text-left">Этаж</th>
                    <th class="text-left">Служащий</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="item in floors" :key="item.name">
                    <td>{{ item.date }}</td>
                    <td>{{ item.floor }}</td>
                    <td>{{  item.worker }}</td>
                  </tr>
                </tbody>
              </template>
            </v-simple-table>
          </v-col>
        </div>
      </v-col>
    </section>
  </main>
</template>
<script>
export default {
  name: 'AdminCabinet',
  created () {
    if (sessionStorage.getItem('token') === null || sessionStorage.getItem('worker') === null) {
      this.$router.push('/auth')
    }
  },
  mounted () {
    this.axios
      .get(`http://${window.location.hostname}:8000/api/room/all`)
      .then(response => { this.updateRooms(response.data) })
      .catch(err => { console.error(err) })

    this.axios
      .get(`http://${window.location.hostname}:8000/api/cleaning/all`)
      .then(response => { this.updateWorkers(response.data) })
  },
  methods: {
    updateRooms (data) {
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

      data.map((room) => {
        if (room.room_state === '2') {
          this.money += room.price
        }
      })
    },
    updateWorkers (data) {
      data.map((worker) => {
        let floor = {}
        floor.date = worker.date
        floor.floor = worker.floor.number
        floor.worker = `${worker.employee.surname} ${worker.employee.name} ${worker.employee.middle_name}`

        this.floors.push(floor)
      })
    }
  },
  data () {
    return {
      onePerson: 0,
      twoPersons: 0,
      threePersons: 0,
      money: 0,
      floors: []
    }
  }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
