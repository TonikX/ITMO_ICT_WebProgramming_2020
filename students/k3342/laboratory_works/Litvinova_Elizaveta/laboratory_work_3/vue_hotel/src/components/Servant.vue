<template>
  <main>
    <section>
      <v-col cols="8" class="mx-auto">
        <v-col cols="12">
          <v-row>
            <h1 class="headline">Отель "Белорусская"</h1>
            <v-btn color="red" @click="logout" dark class="ml-auto">Выход</v-btn>
          </v-row>
        </v-col>
        <p>На этой странице Вы можете узнать своё рабочее расписание</p>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="mx-auto">
        <h2 class="headline">Рабочее расписание</h2>
        <p class="my-2" v-if="!workdays.length">Пока у вас нет рабочих смен.</p>
        <v-simple-table v-if="workdays.length">
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-right">Этаж</th>
                <th class="text-left">Дата</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="workday in workdays" :key="workday.id">
                <td class="text-right">{{ workday.floor }}</td>
                <td>{{ workday.date }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
    </section>
  </main>
</template>
<script>
export default {
  name: 'NewServant',
  data () {
    return {
      workdays: []
    }
  },
  methods: {
    getWorkdays () {
      this.axios
        .get(`http://127.0.0.1:8000/api/cleanings/?servant=${localStorage.getItem('servant')}`)
        .then(response => {
          response.data.map((workday) => {
            this.workdays.push({ date: workday.date, floor: workday.floor.number, id: workday.id })
          })
        })
        .catch(err => { console.error(err) })
    },
    logout () {
      localStorage.clear()
      this.$router.push('/')
    }
  },
  mounted () {
    if (!localStorage.getItem('token')) {
      this.$router.push('/login')
    }
    this.getWorkdays()
  }
}

</script>
<style></style>
