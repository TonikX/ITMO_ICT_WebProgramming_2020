<template>
  <main class="container mx-auto">
    <h1 class="headline">Сайт приёмной комиссии колледжа | Кабинет абитуриента</h1>
    <section class="content">
      <h2>Количество заявлений: {{ applications.length }}</h2>
      <v-card class="my-2 mx-auto" color="primary" dark v-for="card in applications" :key="card.id">
        <v-card-title class="headline">{{ card.name }} | {{ card.class_type }} класс | Статус: {{ card.state }}</v-card-title>
        <v-card-subtitle>Специальность {{ card.spec }} (Проходной балл: {{ card.minimal_point }})</v-card-subtitle>
        <v-card-text>Льготы: {{ card.privelege }}</v-card-text>
        <v-card-text>Дата подачи: {{ card.date }}</v-card-text>
        <v-card-text>Ответственный {{ card.secretary }}</v-card-text>
        <v-card-actions>
          <v-btn v-if="card.state !== 'Принято'" color="teal" @click="accept(card.id)">Принять</v-btn>
          <v-btn v-if="card.state !== 'Не принято'" color="red lighten-2" @click="reject(card.id)">Отклонить</v-btn>
        </v-card-actions>
      </v-card>
    </section>
  </main>
</template>
<script>
export default {
  name: 'Secretary',
  data() {
    return {
      applications: []
    }
  },
  mounted() {
    if (!localStorage.getItem('token')) {
      this.$router.push('/auth')
    }
    this.axios
      .get(`http://127.0.0.1:8000/api/applications/all?secretary=${localStorage.getItem('username')}`)
      .then(response => { this.showApplications(response.data) })
  },
  methods: {
    showApplications(data) {
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
          state = 'Не принято'
        } else if (state === '3') {
          state = 'Принято'
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
    accept(appId) {
      this.axios
        .patch(`http://127.0.0.1:8000/api/applications/${appId}`, { state: '3' })
        .then(response => {
          console.log(response.data)
          this.update()
        })
    },
    reject(appId) {
      this.axios
        .patch(`http://127.0.0.1:8000/api/applications/${appId}`, { state: '2' })
        .then(response => {
          console.log(response.data)
          this.update()
        })
    },
    update() {
      this.axios
        .get(`http://127.0.0.1:8000/api/applications/all?secretary=${localStorage.getItem('username')}`)
        .then(response => { this.showApplications(response.data) })
    }
  }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
