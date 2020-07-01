<template>
  <mu-col span="2" xl="2">
    <h2>Читатели:</h2>
    <div v-for="reader in readers" v-bind:key="reader.id" class="readers">
      <h3 @click="openFull(reader.id)">{{reader.attributes.full_name}}</h3>
      <small>Читательский билет №{{reader.attributes.library_card_num}}</small><br>
    </div>
  </mu-col>
</template>

<script>
export default {
  name: 'Reader',
  data () {
    return {
      readers: ''
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
      this.$emit('openFull', id)
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
