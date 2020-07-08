<template>
  <main>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h1>Создать заявку</h1>
      </v-col>
      <v-col cols="8" class="mx-auto">
        <form>
          <p class="headline">Продукт</p>
          <v-text-field v-model="product_name" label="Название продукта" required></v-text-field>
          <v-text-field v-model="product_thematic" label="Опишите тематику продукта" required></v-text-field>
          <v-textarea v-model="product_desc" label="Опишите свой проудкт" required></v-textarea>
          <p class="headline">Услуга</p>
          <v-select v-model="service" :items="services" label="Выберите услугу" required></v-select>
          <v-textarea v-model="desc" label="Опишите желаемый результат" required></v-textarea>
          <v-textarea v-model="materials" label="Опишите какие материалы вы бы хотели использовать" required></v-textarea>
          <v-btn dark color="indigo accent-4" @click="submit">Отправить</v-btn>
          <v-btn dark color="deep-orange accent-4" @click="clear">Очистить</v-btn>
        </form>
      </v-col>
    </section>
    <v-dialog v-model="success" max-width="350">
      <v-card>
        <v-card-title class="headline">Спасибо за заявку!</v-card-title>
        <v-card-text>
          Ваша заявка уже поступила в обработку и скоро мы с Вами свяжемся!
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="indigo lighten-2" text @click="success = false">
            Ок
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </main>
</template>
<script>
export default {
  name: 'NewRequest',
  created () {
    if (sessionStorage.getItem('token') === null || sessionStorage.getItem('username') === null) {
      this.$router.push('/auth')
    }
  },
  data () {
    return {
      services: [],
      product_name: '',
      product_thematic: '',
      product_desc: '',
      service: '',
      desc: '',
      materials: '',
      client_id: '',
      company_id: '',
      success: false,
      current_date: ''
    }
  },
  methods: {
    showServices (data) {
      for (let i = 0; i < data.length; i++) {
        let service = {}
        service.value = data[i].id
        service.text = data[i].name

        this.services.push(service)
      }

      this.axios
        .get(`http://localhost:8000/api/is/client?username=${sessionStorage.getItem('username')}`)
        .then(response => { this.client_id = response.data[0].id; this.company_id = response.data[0].company.id })
        .catch(err => { console.error(err) })
    },
    submit () {
      let product = {
        name: this.product_name,
        desc: this.product_desc,
        thematic: this.product_thematic,
        company: this.company_id
      }

      this.axios
        .post('http://localhost:8000/api/product/new', product)
        .then(response => { this.addRequest(response.data.id) })
        .catch(err => { console.error(err) })
    },
    addRequest (productId) {
      let request = {
        service: this.service,
        client: this.client_id,
        target: this.desc,
        materials: this.materials,
        state: 2,
        date: this.current_date,
        product: productId,
        executor: 1
      }

      this.axios
        .post(`http://localhost:8000/api/request/new`, request)
        .then(response => { this.addRequestService(response.data.id) })
        .catch(err => { console.error(err) })
    },
    addRequestService (requestId) {
      let requestService = {
        request: requestId,
        service: this.service
      }

      this.axios
        .post('http://localhost:8000/api/request/service', requestService)
        .then(response => { console.log(response); this.clear(); this.success = true })
        .catch(err => { console.error(err) })
    },
    clear () {
      this.product_name = ''
      this.product_thematic = ''
      this.product_desc = ''
      this.service = ''
      this.desc = ''
      this.materials = ''
    },
    getCurrentDate () {
      let date = new Date()
      let currDate = {
        y: `${date.getFullYear()}`,
        m: `${date.getMonth()}`.length > 1 ? `${date.getMonth() + 1}` : `0${date.getMonth() + 1}`,
        d: `${date.getDate()}`.length > 1 ? `${date.getDate()}` : `0${date.getDate()}`
      }

      let today = `${currDate.y}-${currDate.m}-${currDate.d}`

      this.current_date = today
    }
  },
  mounted () {
    this.axios
      .get(`http://localhost:8000/api/services/all`)
      .then(response => { this.showServices(response.data) })
      .catch(err => { console.error(err) })

    this.getCurrentDate()
  }
}
</script>
<style scoped>
</style>
