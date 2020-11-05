<template>
  <main>
    <section class="content">
      <v-form>
        <v-select :items="cage_ids" v-model="cage_id"></v-select>
        <v-select :items="workers" v-model="worker"></v-select>
        <v-text-field v-model="content" type="content" label="Type your rent here"></v-text-field>
        <v-btn @click="addRent">
          <v-icon>mdi-send</v-icon>Submit
        </v-btn>
      </v-form>
    </section>
  </main>
</template>
<script>
export default {
  name: "AddRent",
  data() {
    return {
      hall_name: null,
      hall_name:
        [
          {value: '1', text: 'library_card_numbers 1'},
          {value: '2', text: 'library_card_numbers 2'},
          {value: '3', text: 'library_card_numbers 3'},
          {value: '4', text: 'library_card_numbers 4'},
          {value: '5', text: 'library_card_numbers 5'},
          {value: '6', text: 'library_card_numbers 6'},
          {value: '7', text: 'library_card_numbers 7'}
        ],
      library_card_number: null,
      library_card_number:
        [
          {value: '1', text: 'user1'},
          {value: '2', text: 'user2'},
          {value: '3', text: 'user3'},
        ],
      event_name: '',
    }
  },
  methods: {
    addRent() {
      let Rent = {
        library_card_number: this.library_card_number,
        hall_name: this.hall_name,
        event_name: this.event_name
      }
      this.axios
        .post('http://192.168.99.100:8000/api/rents/add', rent)
        .then(response => {
          console.log(response)
          localStorage.setItem('rent', response.data.id)
          this.$router.push('/rents')
        })
    }
  }
}
</script>
<style></style>
