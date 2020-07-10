<template>
  <section>
    <v-col cols="8" class="mx-auto">
      <v-col cols="12">
        <v-row>
          <h2 class="headline">Рабочее расписание</h2>
          <v-btn color="primary" class="ml-auto" @click="addWorkday = true">Добавить смену</v-btn>
        </v-row>
      </v-col>
      <p class="my-2" v-if="!workdays.length">Пока у вас нет рабочих смен.</p>
      <v-simple-table v-if="workdays.length">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-right">Этаж</th>
              <th class="text-left">Дата</th>
              <th class="text-left">Сотрудник</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="workday in workdays" :key="workday.id">
              <td class="text-right">{{ workday.floor }}</td>
              <td>{{ workday.date }}</td>
              <td>{{ workday.servant }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-col>
    <v-dialog v-model="addWorkday" max-width="600">
      <v-card>
        <v-card-title class="headline">Добавить смену</v-card-title>
        <v-card-text>
          Выберите работника и дату, чтобы добавить смену:
        </v-card-text>
        <v-col cols="8" class="mx-auto">
          <v-text-field v-model="workdate" type="date" label="Дата"></v-text-field>
          <v-select v-model="worker" :items="workers"></v-select>
          <v-select v-model="floor" :items="floors"></v-select>
        </v-col>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="teal" dark @click="addWorkdate">
            Добавить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </section>
</template>
<script>
export default {
  name: 'AdminServant',
  data () {
    return {
      workdays: [],
      addWorkday: false,
      workdate: '',
      worker: null,
      workers: [{ text: 'Выберите сотрудника', value: null }],
      floor: null,
      floors: [{ text: 'Выберите этаж', value: null }]
    }
  },
  methods: {
    getWorkdays () {
      this.workdays = []

      this.axios
        .get(`http://127.0.0.1:8000/api/cleanings/`)
        .then(response => {
          response.data.map((workday) => {
            this.workdays.push({ date: workday.date, floor: workday.floor.number, servant: `${workday.employee.surname} ${workday.employee.name} ${workday.employee.middle_name}`, id: workday.id })
          })
        })
        .catch(err => { console.error(err) })
    },
    addWorkdate () {
      this.axios
        .post('http://127.0.0.1:8000/api/cleaning/add/', { employee: this.worker, floor: this.floor, date: this.workdate })
        .then(response => { console.log(response); this.addWorkday = false; this.getWorkdays(); this.reset() })
    },
    getWorkers () {
      this.axios
        .get(`http://127.0.0.1:8000/api/employees/?employee_position=2`)
        .then(response => {
          response.data.forEach((worker) => {
            this.workers.push({ text: `${worker.surname} ${worker.name} ${worker.middle_name}`, value: worker.id })
          })
        })
        .catch(err => { console.error(err) })
    },
    getFloors () {
      this.axios
        .get('http://127.0.0.1:8000/api/floors/')
        .then(response => {
          response.data.forEach((floor) => {
            this.floors.push({ text: `Этаж №${floor.number}`, value: floor.id })
          })
        })
        .catch(err => { console.error(err) })
    },
    reset () {
      this.worker = null
      this.floor = null
      this.workdate = ''
    }
  },
  mounted () {
    this.getWorkdays()
    this.getWorkers()
    this.getFloors()
  }
}

</script>
<style></style>
