<template>
  <main class="container mx-auto">
    <h1 class="headline">Сайт приёмной комиссии колледжа</h1>
    <section class="filter">
      <v-form>
        <v-row>
          <v-col cols="4">
            <v-text-field type="date" v-model="from_date" label="От"></v-text-field>
          </v-col>
          <v-col cols="4">
            <v-text-field type="date" v-model="to_date" label="До"></v-text-field>
          </v-col>
          <v-col cols="4">
            <v-select :items='class_types' v-model="class_type" label="Класс"></v-select>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="4">
            <v-select v-model="spec" :items='specs' label="Специальность"></v-select>
          </v-col>
          <v-col cols="4">
            <v-select v-model="privelege" :items='priveleges' label="Льготы"></v-select>
          </v-col>
          <v-col cols="4">
            <v-select :items='states' v-model="state" label="Статус заявления"></v-select>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="4">
            <v-text-field type="number" v-model="minimal_point" label="Проходной балл"></v-text-field>
          </v-col>
          <v-col cols="4" class="my-auto">
            <v-btn class="mx-auto" style="width:100%" color="teal" @click="submit" dark>
              <v-icon>mdi-filter</v-icon>Фильтр
            </v-btn>
          </v-col>
          <v-col cols="4" class="my-auto">
            <v-btn @click="clear" style="width:100%" color="red lighten-2" dark>
              <v-icon>mdi-autorenew</v-icon>Сбросить
            </v-btn>
          </v-col>
        </v-row>
      </v-form>
    </section>
    <section class="content">
      <h2>Количество заявлений: {{ applications.length }}</h2>
      <v-card class="my-2 mx-auto" color="primary" dark v-for="card in applications" :key="card.id">
        <v-card-title class="headline">{{ card.name }} | {{ card.class_type }} класс | Статус: {{ card.state }}</v-card-title>
        <v-card-subtitle>Специальность {{ card.spec }} (Проходной балл: {{ card.minimal_point }})</v-card-subtitle>
        <v-card-text>Льготы: {{ card.privelege }}</v-card-text>
        <v-card-text>Дата подачи: {{ card.date }}</v-card-text>
        <v-card-text>Ответственный {{ card.secretary }}</v-card-text>
      </v-card>
    </section>
  </main>
</template>
<script>
export default {
  name: 'MainPage',
  data() {
    return {
      from_date: '',
      to_date: '',
      class_types: [
        { value: null, text: 'Выберите класс', disabled: true },
        { value: '1', text: '9' },
        { value: '2', text: '11' }
      ],
      class_type: null,
      specs: [
        { value: null, text: 'Выберите специальность', disabled: true }
      ],
      spec: null,
      priveleges: [
        { value: null, text: 'Выберите льготы', disabled: true },
        { value: '1', text: 'Нет льгот' },
        { value: '2', text: 'Инвалид' },
        { value: '3', text: 'Сирота' }
      ],
      privelege: null,
      states: [
        { value: null, text: 'Выберите статус', disabled: true },
        { value: '1', text: 'В процессе' },
        { value: '2', text: 'Принято' },
        { value: '3', text: 'Не принято' }
      ],
      state: null,
      minimal_point: '',
      applications: []
    }
  },
  mounted () {
    this.axios
      .get('http://127.0.0.1:8000/api/applications/all')
      .then(response => { this.showApplications(response.data) })

    this.axios
      .get('http://127.0.0.1:8000/api/specializations/all')
      .then(response => { this.showSpecs(response.data) })
  },
  methods: {
    showApplications (data) {
      this.applications = []

      for (let i = 0; i < data.length; i++) {
        let privelege = data[i].enrollee.privelege_type
        
        if (privelege === '1') {
          privelege = 'Нет льгот'
        } else if (privelege === '2') {
          privelege = 'Сирота'
        } else if (privelege === '3') {
          privelege = 'Инвалид'
        }

        let class_type = data[i].enrollee.class_type
        
        if (class_type === '1') {
          class_type = '9'
        } else if (class_type === '2') {
          class_type = '11'
        }

        let state = data[i].state

        if (state === '1') {
          state = 'В процессе'
        } else if (state === '2') {
          state = 'Принято'
        } else if (state === '3') {
          state = 'Не принято'
        }

        let application = {
          id: data[i].id,
          name: data[i].enrollee.fullname,
          minimal_point: data[i].spec.minimal_point,
          privelege: privelege,
          spec: data[i].spec.name,
          class_type: class_type,
          date: data[i].application_date,
          secretary: data[i].secretary.fullname,
          state: state
        }

        this.applications.push(application)
      }
    },
    submit () {
      let class_type = ''
      if (this.class_type) {
        class_type = this.class_type
      }
      let spec = ''
      if (this.spec) {
        spec = this.spec
      }
      let privelege = ''
      if (this.privelege) {
        privelege = this.privelege
      }
      let state = ''
      if (this.state) {
        state = this.state
      }
      this.axios
        .get(`http://127.0.0.1:8000/api/applications/all?from_date=${this.from_date}&to_date=${this.to_date}&class=${class_type}&spec=${spec}&privelege=${privelege}&state=${state}&min=${this.minimal_point}`)
        .then(response => { this.showApplications(response.data) })
    },
    clear () {
      this.from_date = ''
      this.to_date = ''
      this.class_type = null
      this.spec = null
      this.privelege = null
      this.state = null
      this.minimal_point = ''

      this.axios
      .get('http://127.0.0.1:8000/api/applications/all')
      .then(response => { this.showApplications(response.data) })
    },
    showSpecs (data) {
      for (let i = 0; i < data.length; i++) {
        let spec = {
          value: data[i].id,
          text: data[i].name
        }

        this.specs.push(spec)
      }
    }
  }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
