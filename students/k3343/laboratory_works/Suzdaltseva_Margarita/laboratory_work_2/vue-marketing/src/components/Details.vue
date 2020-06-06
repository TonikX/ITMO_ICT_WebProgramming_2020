<template>
  <main>
    <section>
      <v-col cols="8" class="my-1 mx-auto">
        <h2>Детали заявки</h2>
        <p>Подробная информация о выбранной заявке</p>
      </v-col>
      <v-col  cols="12" class="my-1 mx-auto">
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">Номер заявки</th>
                <th class="text-left">Услуга</th>
                <th class="text-left">Клиент</th>
                <th class="text-left">Сотрудник</th>
                <th class="text-left">Краткое описание</th>
                <th class="text-left">Материалы</th>
                <th class="text-left">Дата</th>
                <th class="text-left">Статус</th>
              </tr>
            </thead>
            <tbody>
              <tr>
              <td>{{ request.id }}</td>
              <td>{{ request.service.service_type  }}: {{ request.service.name }}</td>
              <td>{{ request.client.user.first_name }} {{ request.client.user.last_name }} ({{ request.client.user.username }}) {{ request.client.company.company_type }} "{{ request.client.company.name }}" Контакты: {{ request.client.user.email }} {{ request.client.phone }}</td>
              <td>{{ request.employee.user.first_name }} {{ request.employee.user.last_name }} ({{request.employee.user.username }}) {{ request.employee.position }} Контакты: {{ request.employee.user.email }} {{ request.employee.phone }}</td>
              <td>{{ request.description }}</td>
              <td>{{ request.materials }}</td>
              <td>{{ request.date }}</td>
              <td>{{ request.status }}</td>
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
  name: 'Details',
  data () {
    return {
      request: {
        id: '',
        service: '',
        client: '',
        employee: '',
        description: '',
        materials: '',
        date: '',
        status: ''
      }
    }
  },
  mounted () {
    this.axios
      .get(`http://${window.location.hostname}:8000/api/request/${this.id}`)
      .then(response => { this.getRequest(response.data) })
      .catch(err => { console.error('API', err) })
  },
  methods: {
    getRequest (data) {
      let request = {}

      request.id = data.id
      request.service = data.service
      request.client = data.client
      request.employee = data.employee
      request.description = data.description
      request.materials = data.materials
      request.date = data.date
      request.status = data.status

      this.request = request
    }
  },
  props: ['id']
}
</script>
<style scoped>
</style>
