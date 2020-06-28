<template>
  <b-card>
    <b-card-title>
      #{{ num }} {{ last_name }} {{ first_name }} {{ patronymic }}, {{ age }} лет
    </b-card-title>
    <b-card-sub-title>Желаемая должность: {{ position }}</b-card-sub-title>
    <b-card-text>
      Обрзование: {{ education }}
    </b-card-text>
    <b-card-text>
      Стаж: {{ work_experience }} лет
    </b-card-text>
    <b-card-text>
      Паспорт: {{ passport }}
    </b-card-text>
    <b-card-text>
      Состояние: <span v-if="is_hired">Принят</span>
      <span v-if="!is_hired">Не принят</span>
    </b-card-text>
  </b-card>
</template>
<script>
export default {
  name: 'ChallengerCard',
  props: {
    num: Number,
    company: String,
    first_name: String,
    last_name: String,
    patronymic: String,
    age: Number,
    education: String,
    work_experience: Number,
    position: String,
    passport: Number,
    is_hired: Boolean
  }
}

</script>
<style></style>
