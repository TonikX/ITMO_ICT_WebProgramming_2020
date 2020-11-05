<template>
  <main>
    <section class="content">
      <v-form>
        <v-text-field v-model="book_number" type="content" label="Type book number"></v-text-field>
        <v-text-field v-model="name" type="content" label="Type book name"></v-text-field>
        <v-text-field v-model="author_s" type="content" label="Type authors"></v-text-field>
        <v-text-field v-model="publishing_house" type="content" label="Type publishing house"></v-text-field>
        <v-text-field v-model="the_year_of_publishing" type="content" label="Type the year of publishing"></v-text-field>
        <v-text-field v-model="number_of_copies" type="content" label="Type number of copies"></v-text-field>
        <v-text-field v-model="status" type="content" label="Type status"></v-text-field>
        <v-btn @click="addBook">
          <v-icon>mdi-send</v-icon>Submit
        </v-btn>
      </v-form>
    </section>
  </main>
</template>
<script>
export default {
  name: "AddBook",
  data() {
    return {
      book_number: '',
      name: '',
      author_s: '',
      publishing_house: '',
      the_year_of_publishing: '',
      number_of_copies: '',
      status: '',
    }
  },
  methods: {
    addBook() {
      let book = {
        book_number: this.book_number,
        name: this.name,
        author_s: this.author_s,
        publishing_house: this.publishing_house,
        the_year_of_publishing: this.the_year_of_publishing,
        number_of_copies: this.number_of_copies,
        status: this.status
      }
      this.axios
        .post('http://192.168.99.100:8000/api/books/add', book)
        .then(response => {
          console.log(response)
          localStorage.setItem('book', response.data.id)
          this.$router.push('/books')
        })
    }
  }
}
</script>
<style></style>
