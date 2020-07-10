<template>
  <b-card>
    <b-card-title>{{ name }}</b-card-title>
    <b-card-sub-title><router-link :to='"/specialization/" + specId'>{{ specialization }}</router-link></b-card-sub-title>
    <b-card-text></b-card-text>
    <b-card-text>
      Дата подачи: {{ date }}
    </b-card-text>
    <b-card-text>
      Форма обучения: <em>{{ educationForm }}</em>
    </b-card-text>
    <b-card-text>
      Состояние: <em>{{ state }}</em>
    </b-card-text>
    <b-card-text>
      Ответственный: <em>{{ secretary }}</em>
    </b-card-text>
    <router-link :to="'/enrollee/'+ id" class="card-link">Подробнее</router-link>
  </b-card>
</template>
<script>
export default {
  name: 'EnrolleeCard',
  data () {
    return {}
  },
  props: {
    id: Number,
    name: String,
    specialization: String,
    specId: Number,
    date: String,
    educationForm: String,
    state: String,
    secretary: String
  }
}
</script>
<style></style>
