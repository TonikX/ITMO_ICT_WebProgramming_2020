<template>
  <main>
    <section class="content">
      <v-form>
        <v-text-field v-model="book_number" type="number" label="Start_of_owning"></v-text-field>
        <v-text-field v-model="book_number" type="number" label="Start_of_owning"></v-text-field>
        <v-text-field v-model="book_number" type="number" label="Start_of_owning"></v-text-field>
        <v-text-field v-model="finish_of_owning" type="number" label="Finish_of_owning"></v-text-field>
        <v-text-field v-model="returning" type="number" label="Returning"></v-text-field>
        <v-btn @click="addOwnership">
          <v-icon>mdi-send</v-icon>Submit
        </v-btn>
      </v-form>
    </section>
  </main>
</template>
<script>
export default {
  name: "AddOwnership",
  data() {
    return {
      library_card_number: null,
      library_card_numbers:'',
      book_number:'',
      start_of_owning: '',
      finish_of_owning: '',
      returning: ''
    }
  },
  methods: {
    addOwnership() {
      let ownership = {
        library_card_number: this.library_card_number,
        book_number: this.book_number,
        start_of_owning: this.start_of_owning,
        finish_of_owning: this.finish_of_owning,
        returning: this.returning
      }
      this.axios
        .post('http://192.168.99.100:8000/api/ownership/add', ownership)
        .then(response => {
          console.log(response)
          localStorage.setItem('ownership', response.data.id)
          this.$router.push('/ownership')
        })
    }
  }
}
</script>
<style></style>
