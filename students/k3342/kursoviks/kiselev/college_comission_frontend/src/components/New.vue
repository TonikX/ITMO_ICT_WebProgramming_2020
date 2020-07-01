<template>
  <main>
    <h1 class="headline">Подача заявления</h1>
    <v-col cols="5" class="mx-auto">
      <v-form>
        <v-select :items="specs" v-model="spec" label="Специальность"></v-select>
        <v-btn color="blue accent-2" dark @click="sendApplication">
          <v-icon>mdi-send</v-icon>Отправить заявление
        </v-btn>
      </v-form>
    </v-col>
    <v-dialog v-model="successSending" max-width="400">
      <v-card>
        <v-card-title class="headline">Ваше заявление принято в обработку</v-card-title>
        <v-card-text>
          Мы напишем вам, когда результат будет известен.
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="indigo lighten-2" text @click="successSending = false">
            Ок
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </main>
</template>
<script>
export default {
  name: 'New',
  data() {
    return {
      date: '',
      specs: [
        { value: null, text: 'Выберите специальность', disabled: true }
      ],
      spec: null,
      successSending: false
    }
  },
  created() {
    let date = new Date()
    let currDate = {
      y: `${date.getFullYear()}`,
      m: `${date.getMonth()}`.length > 1 ? `${date.getMonth() + 1}` : `0${date.getMonth() + 1}`,
      d: `${date.getDate()}`.length > 1 ? `${date.getDate()}` : `0${date.getDate()}`
    }

    let today = `${currDate.y}-${currDate.m}-${currDate.d}`

    this.date = today
  },
  mounted() {
    if (!localStorage.getItem('username') && !localStorage.getItem('token')) {
      this.$router.push('/auth')
      return
    }

    this.axios
      .get('http://127.0.0.1:8000/api/specializations/all')
      .then(response => { this.showSpecs(response.data) })
  },
  methods: {
    showSpecs(data) {
      for (let i = 0; i < data.length; i++) {
        let spec = {
          value: data[i].id,
          text: `${data[i].name}, Проходной балл: ${data[i].minimal_point}`
        }

        this.specs.push(spec)
      }
    },
    sendApplication() {
      let enrollee = localStorage.getItem('enrollee')

      let application = {
        application_date: this.date,
        state: '1',
        enrollee: enrollee,
        secretary: 1,
        spec: this.spec
      }

      this.axios
        .post('http://127.0.0.1:8000/api/applications/new', application)
        .then(response => {
          console.log(response);
          this.successSending = true;
          this.clear()
        })
    },
    clear() {
      this.spec = null
    }
  }
}

</script>
<style></style>
