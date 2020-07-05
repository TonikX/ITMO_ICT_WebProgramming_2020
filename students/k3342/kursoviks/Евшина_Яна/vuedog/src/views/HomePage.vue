<template>
  <div>
      <h3>Список выставок</h3>
      <mu-expansion-panel v-for="show in shows" :key="show.id">
          <div slot="header">{{ show.show_name }}</div>
          <div>
              <p><b>Город</b>: {{ show.show_town }}</p>
              <p><b>Тип выставки</b>: {{ show.type === '1' ? 'одна порода' : 'много пород' }}</p>
              <p><b>Дата начала</b>: {{ show.start_date.split('-').join('.') }}</p>
              <p><b>Дата конца</b>: {{ show.end_date.split('-').join('.') }}</p>
          </div>
         <mu-button slot="action" flat color="primary" @click="navigateToShow(show.id)">Подробнее</mu-button>
      </mu-expansion-panel>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  computed: {
    shows() {
      return this.$store.state.show.list;
    },
  },
  data() {
    return {

    }
  },
  methods: {
      navigateToShow(showId) {
          this.$router.push(`/shows/${showId}`)
      }
  }
};
</script>

<style scoped>
</style>