<template>
  <mu-row>
    <mu-col span="2" xl="2">
      <h2>Читатели:</h2>
      <div v-for="reader in readers" v-bind:key="reader.id" class="readers">
        <h3 @click="openFull(reader.id)">{{reader.attributes.full_name}}</h3>
        <small>Читательский билет №{{reader.attributes.library_card_num}}</small><br>
      </div>
    </mu-col>
    <reader_books v-if="reader_full.show" :id="reader_full.id"></reader_books>
  </mu-row>
</template>

<script>
// eslint-disable-next-line
import Reader_books from './Reader_books'

export default {
  name: 'Reader',
  components: {
    Reader_books
  },
  data () {
    return {
      readers: '',
      reader_full: {
        id: '',
        show: false
      }
    }
  },
  methods: {
    loadReader () {
      // eslint-disable-next-line
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/reader_old/',
        type: 'GET',
        success: (response) => {
          this.readers = response.data
          console.log(response)
        }
      })
    },
    openFull (id) {
      if (this.reader_full.show === true) {
        let id2 = id
        this.reader_full.show = false
        setTimeout(function (id) {
          this.reader_full.id = id
          this.reader_full.show = true
        }.bind(this), 10, id = id2)
      } else {
        this.reader_full.id = id
        this.reader_full.show = true
      }
    }
  },
  created () {
    // eslint-disable-next-line
    $.ajaxSetup({
      headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
    })
    this.loadReader()
  }
}
</script>

<style scoped>
  h3 {
    cursor: pointer
  }
  .readers {
    box-shadow: 1px 2px 3px #888888
  }
</style>
