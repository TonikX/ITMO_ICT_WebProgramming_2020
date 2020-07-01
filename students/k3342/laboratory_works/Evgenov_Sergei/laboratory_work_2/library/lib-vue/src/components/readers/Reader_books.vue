<template>
  <mu-col span="9" xl="9">
    <mu-container><div v-for="person in person_books.reader" v-bind:key="person.id">
      <h3>Читатель {{person.full_name}}</h3>
      <mu-row>
        <mu-col span="1"></mu-col>
        <mu-col justify-content="end">
          <mu-flex>Номер читательского билета: {{person.library_card_num}}</mu-flex>
          <mu-flex>Зал: {{person.hall}}</mu-flex>
          <mu-flex>Адрес: {{person.home_address}}</mu-flex>
          <mu-flex>Паспортные данные: {{person.passport_data}}</mu-flex>
        </mu-col>
        <mu-col justify-content="end">
          <mu-flex>Дата рождения: {{person.birth_date}}</mu-flex>
          <mu-flex>Контактный номер: {{person.phone_num}}</mu-flex>
          <mu-flex>Образование: {{person.education}}</mu-flex>
          <mu-flex v-if="person.degree">Имеется учёная степень</mu-flex>
          <mu-flex v-else>Отсутствует учёная степень</mu-flex>
        </mu-col>
      </mu-row>
      <mu-flex><h4>Закреплённые за читателем в данный момент книги:</h4></mu-flex>
    </div>
    <div v-for="book in person_books.books" v-bind:key="book.book.cipher">
      <mu-row>
        <mu-col span="1"><strong>{{book.book.cipher}}</strong></mu-col>
        <mu-col>
          <mu-flex class="title">Книга: {{book.book.title}}</mu-flex>
          <mu-flex>Автор: {{book.book.author}}</mu-flex>
          <mu-flex>Зал: {{book.book.hall}}</mu-flex>
          <mu-flex>Дата закрепления: {{book.attachment_starting_date}}</mu-flex>
        </mu-col>
      </mu-row>
      <mu-row><mu-flex><hr/></mu-flex></mu-row>
    </div>
    <mu-row>
      <mu-flex><strong>Добавить новое закрепление книги за данным читателем:</strong></mu-flex>
    </mu-row>
    <mu-row>
      <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="150">
        <mu-form-item prop="input" label="Шифр книги">
          <mu-text-field v-model="form.input"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="date" label="Дата закрепления" help-text="В формате: год(4 цифры)-месяц-день">
          <mu-text-field v-model="form.date"></mu-text-field>
        </mu-form-item>
        <mu-form-item>
          <mu-button color="primary" @click="addAtt">Добавить</mu-button>
        </mu-form-item>
      </mu-form>
    </mu-row></mu-container>
  </mu-col>
</template>

<script>
export default {
  name: 'Reader_books',
  props: {
    id: ''
  },
  data () {
    return {
      person_books: '',
      labelPosition: 'left',
      book_form: '',
      form: {
        input: '',
        date: ''
      }
    }
  },
  created () {
    // eslint-disable-next-line
    $.ajaxSetup({
      headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
    })
    this.loadBooks()
  },
  methods: {
    loadBooks () {
      // eslint-disable-next-line
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/reader/',
        type: 'GET',
        data: {
          reader: this.id
        },
        success: (response) => {
          this.person_books = response.data
        }
      })
    },
    addAtt () {
      // eslint-disable-next-line
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/book/',
        type: 'GET',
        data: {
          book: this.form.input
        },
        success: (response) => {
          console.log(response.data)
          if (response.data.length !== 0) {
            this.book_form = response.data[0].id
            // eslint-disable-next-line
            $.ajax({
              url: 'http://127.0.0.1:8000/api/lib/reader/',
              type: 'POST',
              data: {
                reader: this.id,
                book: this.book_form,
                attachment_starting_date: this.form.date
              },
              success: (response) => {
                alert('Закрепление добавлено')
                this.loadBooks()
              },
              error: (response) => {
                alert('Error')
              }
            })
          } else {
            alert('Книга с введённым шифром отсутствует в библиотеке')
          }
        },
        error: (response) => {
          alert('Error')
        }
      })
    }
  }
}
</script>

<style scoped>
  .mu-demo-form {
    width: 100%;
    max-width: 460px;
  }
  .title {
    text-align: justify;
  }
</style>
