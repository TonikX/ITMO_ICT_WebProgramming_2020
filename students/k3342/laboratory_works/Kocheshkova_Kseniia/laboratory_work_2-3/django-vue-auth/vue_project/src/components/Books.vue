<template>
  <main>
    <section class="content">
      <h2>Books list: {{ books.length }}</h2>
      <v-container fluid>
        <v-row>
          <v-card class="my-1 mx-1" width=320 color="brown" dark v-for="book in books" :key="book.id">
            <v-card-title class="headline"> Book number: {{ book.book_number }} </v-card-title>
            <v-card-text class="title">Name: {{ book.name }} </v-card-text>
            <v-card-text class="title">Author_s: {{ book.author_s }} </v-card-text>
            <v-card-text>Published by {{ book.publishing_house }} in {{ book.the_year_of_publishing }} </v-card-text>
            <v-card-text>Number of copies: {{ book.number_of_copies}} </v-card-text>
            <v-card-text> Status: {{ book.status }} </v-card-text>
          </v-card>
        </v-row>
      </v-container>
      <v-btn href="/books/add">New book</v-btn>
    </section>
  </main>
</template>
<script>
  export default {
    name: 'Books',
    data () {
      return {
          books: []
      }
    },
    mounted() {
      this.axios
      .get(`http://192.168.99.100:8000/api/books`)
      .then(response => { this.showBooks(response.data) })
      .catch(err => { console.error(err) })
    },
    methods: {
      showBooks(data) {
        this.books = []
        for (let i = 0; i < data.length; i++) {
          let book = {}
          book.book_number = data[i].book_number
          book.name = data[i].name
          book.author_s = data[i].author_s
          book.publishing_house  = data[i].publishing_house
          book.the_year_of_publishing = data[i].the_year_of_publishing
          book.number_of_copies  = data[i].number_of_copies
          book.status = data[i].status
          console.log(book)
          this.books.push(book)
        }
      },
    }
  }
</script>
<style></style>
