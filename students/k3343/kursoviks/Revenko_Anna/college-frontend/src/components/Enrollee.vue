<template>
  <main>
    <div class="content container mt-5">
      <b-card :title="enrollee.name">
        <b-card-sub-title><router-link :to='"/specialization/" + enrollee.specId'>{{ enrollee.specialization }}</router-link></b-card-sub-title>
        <div class="my-1"></div>
        <b-card-text>
          Паспорт: {{ enrollee.passport }}
        </b-card-text>
        <b-card-text>
          Аттестат: {{ enrollee.certificate }}
        </b-card-text>
        <b-card-text>
          Дата подачи: {{ enrollee.date }}
        </b-card-text>
        <b-card-text>
          Форма обучения: <em>{{ enrollee.educationForm }}</em>
        </b-card-text>
        <b-card-text>
          Баллы по профильным дисциплинам: {{ enrollee.profilePoints }}
        </b-card-text>
        <b-card-text>
          Баллы по общим дисциплинам: {{ enrollee.commonPoints }}
        </b-card-text>
        <b-card-text>
          Средний балл аттестата: {{ enrollee.avgMark }}
        </b-card-text>
        <b-card-text>
          Состояние: <em>{{ enrollee.state }}</em>
        </b-card-text>
        <b-card-text>
          Ответственный: <em>{{ enrollee.secretary }}</em>
        </b-card-text>
      </b-card>
    </div>
  </main>
</template>
<script>
export default {
  name: 'Enrollee',
  data () {
    return {
      enrollee: {
        name: '',
        specialization: '',
        specId: 0,
        date: '',
        educationForm: '',
        state: '',
        secretary: '',
        passport: 0,
        certificate: 0,
        profilePoints: 0,
        commonPoints: 0,
        avgMark: 0,
      },
      enrolleeData: {}
    }
  },
  mounted () {
    this.axios
      .get(`http://${window.location.hostname}:8005/api/applications/${this.id}`)
      .then(response => { this.enrolleeData = response; this.getEnrollee() })
      .catch(err => { console.error('API', err) })    
  },
  methods: {
    getEnrollee () {
      let enrolleeData = this.enrolleeData.data

      let enrollee = {};

      enrollee.name = `${enrolleeData.enrollee.last_name} ${enrolleeData.enrollee.first_name} ${enrolleeData.enrollee.patronymic}`
      enrollee.specialization = enrolleeData.specialization.name
      enrollee.specId = parseInt(enrolleeData.specialization.id)
      enrollee.date = enrolleeData.date
      enrollee.educationForm = enrolleeData.education_form
      enrollee.state = enrolleeData.state
      enrollee.secretary = `${enrolleeData.secretary.last_name} ${enrolleeData.secretary.first_name} ${enrolleeData.secretary.patronymic}`
      enrollee.passport = enrolleeData.enrollee.documents.passport_num
      enrollee.certificate = enrolleeData.enrollee.documents.certificate_num
      enrollee.profilePoints = enrolleeData.enrollee.exams.profile_points
      enrollee.commonPoints = enrolleeData.enrollee.exams.common_points
      enrollee.avgMark = enrolleeData.enrollee.certificate_avg.avg_mark

      this.enrollee = enrollee
    }
  },
  props: ['id']
}

</script>
<style scoped>
</style>
