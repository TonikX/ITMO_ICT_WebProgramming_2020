<template>
  <main>
    <section>
      <v-col cols="8" class="mx-auto">
        <v-col cols="12">
          <v-row>
            <h1 class="headline">Отель "Белорусская"</h1>
            <v-btn color="red" @click="logout" dark class="ml-auto">Выход</v-btn>
          </v-row>
        </v-col>
        <p>На этой странице Вы можете узнать и изменить рабочее расписание сотрудников и сформировать отчёт о приыбли отеля.</p>
      </v-col>
    </section>
    <section>
      <admin-servant />
    </section>
    <section>
      <admin-report />
    </section>
    <section>
      <admin-challenger />
    </section>
  </main>
</template>
<script>
import AdminServant from './AdminServant'
import AdminReport from './AdminReport'
import AdminChallenger from './AdminChallenger'

export default {
  name: 'Admin',
  data () {
    return {}
  },
  methods: {
    logout () {
      localStorage.clear()
      this.$router.push('/')
    }
  },
  mounted () {
    if (!localStorage.getItem('token')) {
      this.$router.push('/login')
    }

    if (!localStorage.getItem('admin')) {
      this.$router.push('/servant')
    }
  },
  components: { AdminServant, AdminReport, AdminChallenger }
}

</script>
<style></style>
