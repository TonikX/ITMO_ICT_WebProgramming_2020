<template>
  <div>
    <ul>
      <li v-for="reader in readers" v-bind:key="reader.id">
        <h3>{{reader.attributes.full_name}}</h3>
        Читательский билет №{{reader.attributes.library_card_num}}<br>
        Адрес: {{reader.attributes.home_address}}
      </li>
    </ul>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Reader',
  data () {
    return {
      readers: ''
    }
  },
  methods: {
    loadReader () {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/reader_old/',
        type: 'GET',
        success: (response) => {
          this.readers = response.data
          console.log(response)
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Логин или пароль не верен')
          }
        }
      })
    }
  },
  created () {
    $.ajaxSetup({
      headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
    })
    this.loadReader()
  }
}
</script>

<style scoped>

</style>
