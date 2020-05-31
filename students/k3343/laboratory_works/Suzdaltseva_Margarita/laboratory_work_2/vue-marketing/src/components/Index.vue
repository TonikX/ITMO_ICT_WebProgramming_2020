<template>
  <main>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h1>Отдел маркетинга рекламного агенства "ЛУЧ"</h1>
        <p>Делаем рекламу со вкусом </p>
        <v-btn :to='"/newReq"' dark class="mr-4 pink accent-3">Хочу рекламу!</v-btn>
      </v-col>
    </section>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h2>Прайс-лист</h2>
        <p>Список предоставляемых услуг</p>
      </v-col>
      <v-col  cols="8" class="my-1 mx-auto">
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">Тип</th>
                <th class="text-left">Название</th>
                <th class="text-left">Цена</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in services" :key="item.name">
              <td>{{ item.service_type }}
              <td>{{ item.name }}</td>
              <td>{{ item.price }}</td>
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
      services: []
    }
  },
  methods: {
    getServices (data) {
      for (let i = 0; i < data.length; i++) {
        let service = {}
        service.service_type = data[i].service_type
        service.name = data[i].name
        service.price = data[i].price

        this.services.push(service)
      }
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
<style>
</style>
