<template>
  <main>
    <section>
      <v-col cols="10" class="my-4 mx-auto">
        <h1>ООО "Луч - рекламные решения"</h1>
        <p>Прольём свет на вашу компанию. Увидят все.</p>
        <v-btn to='/request/new' dark color="indigo accent-3">Подать заявку</v-btn>
      </v-col>
    </section>
    <section>
      <v-col cols="10" class="my-4 mx-auto">
        <h2>Луч в цифрах</h2>
        <p>Нашим результатам скорость света - не предел.</p>
      </v-col>
      <v-col cols="10" class="my-4 mx-auto">
        <v-row>
          <v-col cols="4" class="mx-auto text-center">
            <v-icon color="light-blue">mdi-account-check</v-icon>
            <h3 class="headline">{{ clients }}</h3>
            <p>Активных клиентов</p>
          </v-col>
          <v-col cols="4" class="mx-auto text-center">
            <v-icon color="indigo">mdi-charity</v-icon>
            <h3 class="headline">{{ requests }}</h3>
            <p>Новых заказов</p>
          </v-col>
          <v-col cols="4" class="mx-auto text-center">
            <v-icon color="teal">mdi-domain</v-icon>
            <h3 class="headline">{{ companies }}</h3>
            <p>Компаний сотрудничают с нами</p>
          </v-col>
        </v-row>
      </v-col>
    </section>
    <section>
      <v-col cols="10" class="my-4 mx-auto">
        <h2>Прайс-лист</h2>
        <p>Любой каприз за Ваши деньги.</p>
      </v-col>
      <v-col cols="10" class="my-4 mx-auto">
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">Название</th>
                <th class="text-left">Цена</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="s in services" :key="s.name">
                <td class="text-left">{{ s.name }}</td>
                <td class="text-left">{{ s.price }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
    </section>
  </main>
</template>
<script>
export default {
  name: 'Index',
  data () {
    return {
      services: [],
      clients: 0,
      requests: 0,
      companies: 0
    }
  },
  methods: {
    showServices (data) {
      for (let i = 0; i < data.length; i++) {
        let service = {}
        service.name = data[i].name
        service.price = data[i].price

        this.services.push(service)
      }
    }
  },
  mounted () {
    this.axios
      .get('http://localhost:8000/api/services/all')
      .then(response => { this.showServices(response.data) })
      .catch(err => { console.error(err) })

    this.axios
      .get('http://localhost:8000/api/company/all')
      .then(respsonse => { this.companies = respsonse.data.length })
      .catch(err => { console.error(err) })

    this.axios
      .get('http://localhost:8000/api/client/all')
      .then(respsonse => { this.clients = respsonse.data.length })
      .catch(err => { console.error(err) })

    this.axios
      .get('http://localhost:8000/api/request/all')
      .then(respsonse => { this.requests = respsonse.data.length })
      .catch(err => { console.error(err) })
  }
}
</script>
<style>
</style>
