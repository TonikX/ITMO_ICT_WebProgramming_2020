<template>
  <div>
      <h3>Список клубов</h3>
      <mu-expansion-panel v-for="club in clubs" :key="club.id">
          <div slot="header">{{ club.club_name }}</div>
          <div>
              <p><b>Город</b>: {{ club.town_club }}</p>
          </div>
      </mu-expansion-panel>
  </div>
</template>

<script>
export default {
    name: "ClubsPage",
    computed: {
        clubs() {
            return this.$store.state.club.list;
        }
    }
}
</script>

<style scoped>

</style>