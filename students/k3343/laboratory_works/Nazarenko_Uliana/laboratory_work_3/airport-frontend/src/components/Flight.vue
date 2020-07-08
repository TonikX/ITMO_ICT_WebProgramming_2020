<template>
  <b-card>
    <b-card-title>
      {{ arrival }} - {{ departure }}
    </b-card-title>
    <b-card-sub-title>Цена: {{ price }} рублей</b-card-sub-title>
    <b-card-text>
      Расстояние: {{ distance }} км
    </b-card-text>
    <b-card-text>
      Количество оставшихся билетов: {{ tickets }}
    </b-card-text>
    <b-card-text>
      Есть ли транзитные посадки: {{ transit }}
    </b-card-text>
  </b-card>
</template>
<script>
export default {
  name: 'Flight',
  props: {
    arrival: String,
    departure: String,
    price: Number,
    tickets: Number,
    transit: String,
    distance: Number
  }
}

</script>
<style></style>
