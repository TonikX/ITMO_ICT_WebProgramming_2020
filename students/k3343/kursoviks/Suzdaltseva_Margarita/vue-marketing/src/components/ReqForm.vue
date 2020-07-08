<template>
  <main>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h2>Оставить заявку на рекламу</h2>
      </v-col>
      <v-col cols="8" class="mx-auto">
        <form>
          <v-select v-model="req_service" :items="services" label="Услуга" required></v-select>
          <v-text-field v-model="req_description" label="Краткое описание" required></v-text-field>
          <v-text-field v-model="req_materials" label="Необходимые материалы" required></v-text-field>
          <v-btn dark class="mr-4 pink accent-3" @click="submitRequest">Отправить</v-btn>
          <v-btn dark @click="clearRequest" class="mr-4 pink accent-4">Очистить</v-btn>
        </form>
      </v-col>
    </section>
  </main>
</template>
<script>
export default {
  name: 'ReqForm',
  created () {
    if (sessionStorage.getItem('token') === null || sessionStorage.getItem('user') === null) {
      this.$router.push('/auth')
    }
  },
  data () {
    return {
      services: [],
      req_service: '',
      req_description: '',
      req_materials: '',
      req_client: '',
      req_id: '',
      price: ''
    }
  },
  methods: {
    getServices (data) {
      for (let i = 0; i < data.length; i++) {
        let service = {}
        service.value = data[i].id
        service.text = data[i].name

        this.services.push(service)
      }

      this.axios
        .get(`http://${window.location.hostname}:8000/api/getclient?user=${sessionStorage.getItem('user')}`)
        .then(response => { console.log(response); this.getClient(response.data) })
        .catch(err => { console.error(err) })
    },
    getClient (data) {
      this.req_client = data[0].id
    },
    submitRequest () {
      console.log('client is', this.req_client)
      let data = {
        service: this.req_service,
        client: this.req_client,
        description: this.req_description,
        materials: this.req_materials
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/request/new/`, data)
        .then(response => { console.log(response); this.getPrice(response.data) })
        .catch(err => { console.error(err) })
    },
    getPrice (data) {
      this.req_id = data.id

      this.axios
        .get(`http://${window.location.hostname}:8000/api/request/${this.req_id}`)
        .then(response => { console.log(response); this.createPayment(response.data) })
        .catch(err => { console.error(err) })
    },
    createPayment (data) {
      this.price = data.service.price
      console.log('price is', this.price)

      let paydata = {
        amount: this.price,
        request: this.req_id
      }

      this.axios
        .post(`http://${window.location.hostname}:8000/api/payment/new`, paydata)
        .then(response => { console.log(response); this.clearRequest() })
        .catch(err => { console.error(err) })
    },
    clearRequest () {
      this.req_service = ''
      this.req_description = ''
      this.req_materials = ''
      this.req_id = ''
      this.price = ''
    }
  },
  mounted () {
    this.axios
      .get(`http://${window.location.hostname}:8000/api/service/all`)
      .then(response => { this.getServices(response.data) })
      .catch(err => { console.error(err) })
  }
}
</script>
<style scoped>
</style>
