<template>
  <main>
    <div class="container">
      <h2>Личный кабинет</h2>
      <p>Здесь вы можете увидеть все поданные резюме</p>
    </div>
    <div class="container">
      <h3 v-if="challengers.length">Найдено {{ challengers.length }} резюме</h3>
      <h3 v-if="!challengers.length">Пока нет резюме :(</h3>
      <challenger-card class="mt-2 mb-2" v-for="challenger in challengers" :key="challenger.id" :num="challenger.id" :last_name="challenger.last_name" :first_name="challenger.first_name" :patronymic="challenger.patronymic" :age="challenger.age" :position="challenger.position" :education="challenger.education" :work_experience="challenger.work_experience" :is_hired="challenger.is_hired" :passport="challenger.passport"></challenger-card>
    </div>
  </main>
</template>
<script>
import ChallengerCard from './ChallengerCard'
export default {
  name: 'Cabinet',
  data () {
    return {
      challengers: []
    }
  },
  components: {
    ChallengerCard
  },
  mounted () {
    if (!sessionStorage.getItem('token') && !sessionStorage.getItem('username')) {
      this.$router.push('/login')
      return
    }

    this.axios
      .get(`http://${window.location.hostname}:8000/api/challengers/list`)
      .then(response => { this.challengers = response.data })
      .catch(err => { console.error(err) })
  }
}

</script>
<style></style>
