<template>
  <main>
    <section class="content">
      <v-form>
        <v-select :items="cage_ids" v-model="cage_id"></v-select>
        <v-select :items="workers" v-model="worker"></v-select>
        <v-text-field v-model="content" type="content" label="Type your report here"></v-text-field>
        <v-btn @click="addReport">
          <v-icon>mdi-send</v-icon>Submit
        </v-btn>
      </v-form>
    </section>
  </main>
</template>
<script>
export default {
  name: "AddReport",
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
      worker: null,
      workers:
        [
          {value: '1', text: 'user1'},
          {value: '2', text: 'user2'},
          {value: '3', text: 'user3'},
        ],
      content: '',
    }
  },
  methods: {
    addReport() {
      let report = {
        cage_id: this.cage_id,
        worker: this.worker,
        content: this.content
      }
      this.axios
        .post('http://127.0.0.1:8000/api/reports/add', report)
        .then(response => {
          console.log(response)
          localStorage.setItem('report', response.data.id)
          this.$router.push('/reports')
        })
    }
  }
}
</script>
<style></style>
