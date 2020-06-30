<template>
  <main>
    <div class="d-flex flex-column">
      <div class="filter container d-flex flex-row">
        <div class="m-auto">
          <b-form inline>
            <div class="m-1">
              <label for="specialization">Специальность</label>
              <b-form-select id="specialization" v-model="specialization" :options="specializations" :value="null"></b-form-select>
            </div>
            <div class="m-1">
              <label for="educationForm">Форма</label>
              <b-form-select id="educationForm" v-model="educationForm" :options="[{text: 'Все', value: 'null'}, { text: 'Контракт', value: '1' }, { text: 'Бюджет', value: '2' }]" :value="null"></b-form-select>
            </div>
            <div class="m-1 mt-4">
              <b-button variant="primary" @click="filterEnrollee()">Найти</b-button>
              <b-button variant="primary" @click="clear()">Очистить</b-button>
            </div>
          </b-form>
        </div>
      </div>
      <div class="content container mt-5">
        <h2 class="mb-5">Общий конкурс</h2>
        <enrollee-card class="mb-2" v-for="e in enrollees" :key="e.id" :id="e.id" :name="e.name" :specialization="e.specialization" :date="e.date" :educationForm="e.educationForm" :state="e.state" :secretary="e.secretary" :specId="e.specId"></enrollee-card>
      </div>
    </div>
  </main>
</template>
<script>
import EnrolleeCard from './EnrolleeCard'

export default {
  name: 'Top',
  data() {
    return {
      enrollees: [],
      enrolleesData: [],
      specData: [],
      specializations: [{text: 'Полный список', value: 'null'}],
      educationForm: null,
      specialization: null
    }
  },
  components: {
  	EnrolleeCard
  },
  mounted () {
  	this.axios
  	  .get(`http://${window.location.hostname}:8005/api/applications/?exam=1`)
	  .then(response => { this.enrolleesData = response; this.getEnrollee() })
	  .catch(err => { console.error('API', err) })

  	this.axios
	  .get(`http://${window.location.hostname}:8005/api/specializations/`)
	  .then(response => { this.specData = response; this.getSpec() })
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
  		console.log('enrolleesData', enrolleeData)
  	},
  	getSpec () {
  	  let s = this.specData.data

  	  for (let i = 0; i < s.length; i++) {
  	  	let specialization = {}

  	  	specialization.text = s[i].name
  	  	specialization.value = s[i].id

  	  	this.specializations.push(specialization)
  	  }
  	},
  	filterEnrollee () {
  	  let specialization = this.specialization === null ? '' : this.specialization;
  	  let educationForm = this.educationForm === null ? '' : this.educationForm;

  	  let url = `http://${window.location.hostname}:8005/api/applications/?exam=1&specialization=${specialization}&education_form=${educationForm}`

  	  this.axios
  		.get(url)
  		.then(response => { this.enrolleesData = response; this.getEnrollee() })
  		.catch(err => { console.error('API', err) })  		
  	},
  	clear () {
  	  this.specialization = null
  	  this.educationForm = null

  	  this.axios
  	    .get(`http://${window.location.hostname}:8005/api/applications/`)
	    .then(response => { this.enrolleesData = response; this.getEnrollee() })
	    .catch(err => { console.error('API', err) })
  	}
  }
}

</script>
<style scoped>
</style>
