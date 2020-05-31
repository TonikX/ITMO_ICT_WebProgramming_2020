<template>
  <v-card color="teal" class="my-3" dark>
    <div class="d-flex flex-no-wrap justify-space-between">
      <div>
        <v-card-title class="headline" v-text="patient"></v-card-title>
        <v-card-subtitle v-text="doctor"></v-card-subtitle>
        <p class="mx-4" v-if="price">Стоимость: {{ price }}</p>
      </div>
    </div>
    <v-card-actions v-if="link">
      <v-btn text :to="link">Подробнее</v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
export default {
  name: 'AppointmentInfo',
  props: {
    patient: String,
    doctor: String,
    price: String,
    link: String
  }
}

</script>
<style>
</style>
