<template>
  <main>
    <div class="d-flex flex-column">
      <h1 class="text-center">Кабинет абитуриента</h1>
      <p class="text-center">Здесь вы сможете увидеть все свои заявления</p>
      <div class="content container mt-5">
        <h2 class="mb-5" v-if="enrollees.length > 0">Найдено {{ enrollees.length }} заявлений</h2>
        <h2 class="mb-5" v-if="enrollees.length === 0">Вы ещё не подавали заявлние :(</h2>
        <enrollee-card class="mb-2" v-for="e in enrollees" :key="e.id" :id="e.id" :name="e.name" :specialization="e.specialization" :date="e.date" :educationForm="e.educationForm" :state="e.state" :secretary="e.secretary" :specId="e.specId"></enrollee-card>
      </div>
    </div>
  </main>
</template>
<script>
import EnrolleeCard from './EnrolleeCard'

export default {
  name: 'Cabinet',
  data () {
    return {
      enrollees: [],
      enrolleesData: []
    }
  },
  components: {
    EnrolleeCard
  },
  mounted () {
    if (!sessionStorage.getItem('token')) {
      this.$router.push('/signin')
      return
    }

  	this.axios
  	  .get(`http://${window.location.hostname}:8005/api/applications/?enrollee=${localStorage.getItem('enrollee')}`)
  	  .then(response => { this.enrolleesData = response; this.getEnrollee() })
  	  .catch(err => { console.error('API', err) })
  },
  methods: {
  	getEnrollee () {
  	  this.enrollees = []
  	  let enrolleeData = this.enrolleesData.data;
  	  for (let i = 0; i < enrolleeData.length; i++ ) {
  	  	let enrollee = {}

  	  	enrollee.id = parseInt(enrolleeData[i].id)
  	  	enrollee.name = `${enrolleeData[i].enrollee.last_name} ${enrolleeData[i].enrollee.first_name} ${enrolleeData[i].enrollee.patronymic}`
  	  	enrollee.specialization = enrolleeData[i].specialization.name
  	  	enrollee.specId = parseInt(enrolleeData[i].specialization.id)
  	  	enrollee.date = enrolleeData[i].date
  	  	enrollee.educationForm = enrolleeData[i].education_form
  	  	enrollee.state = enrolleeData[i].state
  	  	enrollee.secretary = `${enrolleeData[i].secretary.last_name} ${enrolleeData[i].secretary.first_name} ${enrolleeData[i].secretary.patronymic}`

  	  	this.enrollees.push(enrollee)
  	  }
  	}
  }
}

</script>
<style scoped>
</style>
