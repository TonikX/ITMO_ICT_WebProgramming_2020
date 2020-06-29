<template>
  <main>
    <v-col cols="10" class="mx-auto">
      <h1>Кабинет служащего</h1>
      <div class="my-2">
        <v-col cols="5" class="mx-auto my-1">
          <v-simple-table>
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-left">Дата</th>
                  <th class="text-left">Этаж</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in floors" :key="item.name">
                  <td>{{ item.date }}</td>
                  <td>{{ item.floor }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-col>
      </div>
    </v-col>
  </main>
</template>
<script>
export default {
  name: 'WorkerCabinet',
  created () {
    if (sessionStorage.getItem('token') === null || sessionStorage.getItem('worker') === null) {
      this.$router.push('/auth')
    }
  },
  mounted () {
    this.axios
      .get(`http://${window.location.hostname}:8000/api/cleaning/all?worker=${sessionStorage.getItem('worker')}`)
      .then(response => { this.updateFloors(response.data) })
      .catch(err => { console.error(err) })
  },
  data () {
    return {
      floors: []
    }
  },
  methods: {
    updateFloors (data) {
      data.map((cleaning) => {
        let floor = {}
        floor.date = cleaning.date
        floor.floor = cleaning.floor.number

        this.floors.push(floor)
      })
    }
  }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
