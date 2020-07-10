<template>
  <main>
    <b-alert v-if="success" show variant="success">Ваше заявление успешно подано, вы сможете отследить его в личном кабинете</b-alert>
    <div class="content container mt-5">
      <h1 class="text-center">Подача заявления</h1>
      <div class="d-flex flex-row">
        <div class="m-auto w-75">
          <b-form>
            <div class="m-1">
              <label for="specialization">Специальность</label>
              <b-form-select id="specialization" v-model="specialization" :options="specializations" :value="null"></b-form-select>
            </div>
            <div class="m-1">
              <label for="educationForm">Форма</label>
              <b-form-select id="educationForm" v-model="educationForm" :options="educationForms" :value="null"></b-form-select>
            </div>
            <div class="m-1 mt-4">
              <b-button variant="primary" @click="submit()">Подать</b-button>
            </div>
          </b-form>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  name: 'Application',
  data () {
    return {
      specialization: null,
      educationForm: null,
      specializations: [
        { text: 'Выберите специальность', value: null, disabled: true }
      ],
      educationForms: [
        { text: 'Выберите форму обучения', value: null, disabled: true },
        { text: 'Контракт', value: '1' },
        { text: 'Бюджет', value: '2' }
      ],
      success: false
    }
  },
  methods: {
    submit () {
      let date = new Date()
      let currDate = {
        y: `${date.getFullYear()}`,
        m: `${date.getMonth()}`.length > 1 ? `${date.getMonth() + 1}` : `0${date.getMonth() + 1}`,
        d: `${date.getDate()}`.length > 1 ? `${date.getDate()}` : `0${date.getDate()}`
      }

      let today = `${currDate.y}-${currDate.m}-${currDate.d}`

      this.axios
        .post(`http://${window.location.hostname}:8005/api/add/application/`, { enrollee: localStorage.getItem('enrollee'), specialization: this.specialization, educationForm: this.educationForm, date: today })
        .then(response => { console.log(response); this.success = true; setTimeout(() => { this.success = false }, 5000)})
        .catch(err => { console.error(err) })
    },
    getSpec () {
      let s = this.specData.data

      for (let i = 0; i < s.length; i++) {
        let specialization = {}

        specialization.text = s[i].name
        specialization.value = s[i].id

        this.specializations.push(specialization)
      }
    }
  },
  mounted() {
    if (!sessionStorage.getItem('token')) {
      this.$router.push('/signin')
      return
    }

    this.axios
      .get(`http://${window.location.hostname}:8005/api/specializations/`)
      .then(response => { this.specData = response; this.getSpec() })
  }
}

</script>
