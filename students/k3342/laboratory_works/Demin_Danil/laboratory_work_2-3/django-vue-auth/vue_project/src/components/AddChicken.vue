<template>
  <main>
    <section class="content">
      <v-form>
        <v-select :items="cage_ids" v-model="cage_id"></v-select>
        <v-select :items="breeds" v-model="breed"></v-select>
        <v-text-field v-model="productivity" type="number" label="Productivity"></v-text-field>
        <v-text-field v-model="weight" type="number" label="Weight"></v-text-field>
        <v-text-field v-model="age" type="number" label="Age"></v-text-field>
        <v-btn @click="addChicken">
          <v-icon>mdi-send</v-icon>Submit
        </v-btn>
      </v-form>
    </section>
  </main>
</template>
<script>
export default {
  name: "AddChicken",
  data() {
    return {
      cage_id: null,
      cage_ids:
        [
          {value: '1', text: 'Cage 1'},
          {value: '2', text: 'Cage 2'},
          {value: '3', text: 'Cage 3'},
          {value: '4', text: 'Cage 4'},
          {value: '5', text: 'Cage 5'},
          {value: '6', text: 'Cage 6'},
          {value: '7', text: 'Cage 7'}
        ],
      breed: null,
      breeds:
        [
          {value: '1', text: 'Red'},
          {value: '2', text: 'Blue'},
          {value: '3', text: 'Green'}
        ],
      productivity: '',
      weight: '',
      age: ''
    }
  },
  methods: {
    addChicken() {
      let chicken = {
        cage_id: this.cage_id,
        breed: this.breed,
        productivity: this.productivity,
        weight: this.weight,
        age: this.age
      }
      this.axios
        .post('http://127.0.0.1:8000/api/chickens/add', chicken)
        .then(response => {
          console.log(response)
          localStorage.setItem('chicken', response.data.id)
          this.$router.push('/chickens')
        })
    }
  }
}
</script>
<style></style>
