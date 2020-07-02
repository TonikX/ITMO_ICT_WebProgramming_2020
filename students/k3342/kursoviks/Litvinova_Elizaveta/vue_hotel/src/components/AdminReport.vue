<template>
  <section>
    <v-col cols="8" class="mx-auto">
      <h2 class="headline">Отчёт</h2>
      <p><strong>Актуальная статистика</strong></p>
      <p>Количество занятых номеров: {{ total }}</p>
      <p>Количество занятых номеров на одного человека: {{ one }}</p>
      <p>Количество занятых номеров на двух человек: {{ two }}</p>
      <p>Количество занятых номеров на трёх человек: {{ three }}</p>
      <p>Количество клиентов: {{ clients }}</p>
      <p>Прибыль: {{ sum }}</p>
      <p></p>
      <p><strong>Пересчитать прибыль и количество криентов за период</strong></p>
      <v-text-field type="date" label="С" v-model="start_date"></v-text-field>
      <v-text-field type="date" label="По" v-model="end_date"></v-text-field>
      <v-btn color="primary" dark @click="getData()">Пересчитать</v-btn>
      <v-btn color="red" dark @click="reset()">Сбросить</v-btn>
      <p></p>
      <p><strong>Пересчитать прибыль и количество клиентов из определённого города</strong></p>
      <v-text-field label="Название города" v-model="city_from"></v-text-field>
      <v-btn color="primary" dark @click="reCity()">Вывести</v-btn>
      <v-btn color="red" dark @click="resetCity()">Сбросить</v-btn>
    </v-col>
  </section>
</template>
<script>
export default {
  name: 'AdminReport',
  data () {
    return {
      total: 0,
      one: 0,
      two: 0,
      three: 0,
      start_date: '',
      end_date: '',
      clients: 0,
      city_from: '',
      sum: 0
    }
  },
  methods: {
    getData () {
      this.axios
        .get(`http://127.0.0.1:8000/api/client/rooms/?date1=${this.start_date}&date2=${this.end_date}`)
        .then(response => {
          this.sum = 0
          this.total = response.data.length
          this.one = response.data.filter(room => room.room.room_type === '1').length
          this.two = response.data.filter(room => room.room.room_type === '2').length
          this.three = response.data.filter(room => room.room.room_type === '3').length
          this.clients = parseInt(this.one) + 2 * parseInt(this.two) + 3 * parseInt(this.three)
          response.data.forEach(r => { this.sum += parseInt(r.room.price) })
        })
        .catch(err => { console.error(err) })
    },
    reset () {
      this.end_date = ''
      this.start_date = ''
      this.getData()
    },
    reCity () {
      this.axios
        .get(`http://127.0.0.1:8000/api/client/rooms/?from_city=${this.city_from}`)
        .then(response => {
          this.sum = 0
          this.total = response.data.length
          this.one = response.data.filter(room => room.room.room_type === '1').length
          this.two = response.data.filter(room => room.room.room_type === '2').length
          this.three = response.data.filter(room => room.room.room_type === '3').length
          this.clients = parseInt(this.one) + 2 * parseInt(this.two) + 3 * parseInt(this.three)
          response.data.forEach(r => { this.sum += parseInt(r.room.price) })
        })
        .catch(err => { console.error(err) })
    },
    resetCity () {
      this.city_from = ''
      this.getData()
    }
  },
  mounted () {
    this.getData()
  }
}

</script>
<style></style>
