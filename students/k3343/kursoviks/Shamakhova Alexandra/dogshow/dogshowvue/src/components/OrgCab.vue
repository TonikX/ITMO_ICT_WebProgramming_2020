<template>
  <main>
    <v-col cols="8" class="my-1 mx-auto">
      <h2>Кабинет организатора</h2>
    </v-col>
    <section>
      <v-col cols="8" class="mx-auto">
        <v-card v-for="rec in recs" :key="rec.id">
          <v-checkbox
            v-model="rec.record_medical"
            :label="`Медосмотр: ${rec.record_medical.toString()}`"
          ></v-checkbox>
          <v-checkbox
            v-model="rec.record_pay"
            :label="`Оплата счёта: ${rec.record_pay.toString()}`"
          ></v-checkbox>
          <v-checkbox
            v-model="rec.record_confirmation"
            :label="`Подтверждение: ${rec.record_confirmation.toString()}`"
          ></v-checkbox>
        </v-card>
      </v-col>
    </section>

  </main>
</template>

<script>
export default {
  name: 'OrgCab',
  created () {
    if (sessionStorage.getItem('token') === null || sessionStorage.getItem('user') === null) {
      this.$router.push('/orgin')
    }
  },
  data () {
    return {
      recs: []
    }
  },
  mounted () {
    this.axios
      .get(`http://127.0.0.1:8000/api/shows/all`)
      .then(response => { this.records = response; this.updateRecs() })
      .catch(err => { console.error(err) })
  },
  methods: {
    updateRecs () {
      for (let i = 0; i < this.records.data.length; i++) {
        let rec = {}
        rec.record_medical = this.records.data[i].record_medical
        rec.record_pay = this.records.data[i].record_pay
        rec.record_confirmation = this.records.data[i].record_confirmation
        this.recs.push(rec)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h2, h3 {
  font-weight: normal;
}
</style>
