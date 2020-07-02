<template>
  <section>
    <v-col cols="8" class="mx-auto">
      <h2 class="headline">Управление служащими</h2>
      <p class="my-2" v-if="!workers.length">Пока у вас нет работников.</p>
      <v-simple-table v-if="workers.length">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">Сотрудник</th>
              <th class="text-left">Статус</th>
              <th class="text-left">Действие</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="worker in workers" :key="worker.id">
              <td>{{ worker.name }}</td>
              <td>{{ worker.position }}</td>
              <td>
                <v-btn color="primary" @click="editWorker(worker.id, worker.action)">{{ worker.action }}</v-btn>
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-col>
  </section>
</template>
<script>
export default {
  name: 'AdminChallenger',
  data () {
    return {
      workers: []
    }
  },
  methods: {
    getWorkers () {
      this.workers = []
      this.axios
        .get(`http://127.0.0.1:8000/api/employees/?employee_position=2`)
        .then(response => {
          response.data.forEach((worker) => {
            this.workers.push({ name: `${worker.surname} ${worker.name} ${worker.middle_name}`, id: worker.id, position: 'Служащий', action: 'Уволить' })
          })
        })
        .catch(err => { console.error(err) })
    },
    getChallengers () {
      this.axios
        .get(`http://127.0.0.1:8000/api/employees/?employee_position=3`)
        .then(response => {
          response.data.forEach((worker) => {
            this.workers.push({ name: `${worker.surname} ${worker.name} ${worker.middle_name}`, id: worker.id, position: 'Претендент', action: 'Принять' })
          })
        })
        .catch(err => { console.error(err) })
    },
    editWorker (id, action) {
      let position = '2'
      if (action === 'Уволить') {
        position = '4'
      }
      this.axios
        .patch(`http://127.0.0.1:8000/api/employee/${id}/`, { position: position })
        .then(response => {
          console.log(response)
          this.getWorkers()
          this.getChallengers()
        })
        .catch(err => { console.error(err) })
    }
  },
  mounted () {
    this.getWorkers()
    this.getChallengers()
  }
}

</script>
<style></style>
