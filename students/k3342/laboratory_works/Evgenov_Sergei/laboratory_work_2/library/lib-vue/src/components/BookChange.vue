<template>
  <mu-container>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
    <mu-appbar style="width: 100%;" color="#8B4513">
      <mu-menu slot="left">
        <mu-button flat icon>
          <mu-icon value="menu"></mu-icon>
        </mu-button>
        <mu-list slot="content">
          <mu-list-item button @click="goHome()">
            <mu-list-item-content>
              <mu-list-item-title>Читатели</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button @click="goBooks()">
            <mu-list-item-content>
              <mu-list-item-title>Книги</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
        </mu-list>
      </mu-menu>
      Сайт библиотеки на Vue.js
      <mu-button @click="logout()" flat slot="right">Выход</mu-button>
    </mu-appbar>
    <mu-container>
      <mu-row>
        <mu-col span="10" align-items="start">
          <h3>Книга {{book.cipher}}</h3>
          <h4>Нынешние данные:</h4>
        </mu-col>
        <mu-col></mu-col>
        <mu-col justify-content="end">
          <mu-button color="error" class="button-del" @click="bookDel()">
            Списать книгу
          </mu-button>
        </mu-col>
      </mu-row>
      <mu-row>
        <mu-col>
          <mu-row>
            <strong><mu-col span="3" class="attr">Название:</mu-col></strong>
            <mu-col class="title">{{book.title}}</mu-col>
          </mu-row>
          <mu-row>
            <strong><mu-col span="3" class="attr">Автор:</mu-col></strong>
            <mu-col class="title">{{book.author}}</mu-col>
          </mu-row>
          <mu-row>
            <strong><mu-col span="3" class="attr">Издатель:</mu-col></strong>
            <mu-col class="title">{{book.publisher}}</mu-col>
          </mu-row>
          <mu-row>
            <strong><mu-col span="3" class="attr">Год&nbsp;издания:</mu-col></strong>
            <mu-col class="title">{{book.edition_year}}</mu-col>
          </mu-row>
          <mu-row>
            <strong><mu-col span="3" class="attr">Сфера:</mu-col></strong>
            <mu-col class="title">{{book.sphere}}</mu-col>
          </mu-row>
          <mu-row>
            <strong><mu-col span="3" class="attr">Дата&nbsp;поступления:</mu-col></strong>
            <mu-col class="title">{{book.receipt_date}}</mu-col>
          </mu-row>
          <mu-row>
            <strong><mu-col span="3" class="attr">Зал:</mu-col></strong>
            <mu-col class="title">{{book.hall}}</mu-col>
          </mu-row>
        </mu-col>
      </mu-row>
      <mu-row>
        <mu-col span="10">
          <h4>Новые данные:</h4>
          <h5>(Заполняйте только те поля, значения которых собираетесь изменить)</h5>
        </mu-col>
        <mu-col></mu-col>
      </mu-row>
      <mu-form :model="change_form" class="book-change-form" :label-position="labelPosition" label-width="180">
        <mu-form-item prop="cipher" label="Шифр">
          <mu-text-field v-model="change_form.cipher"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="title" label="Название">
          <mu-text-field multi-line :rows="3" :rows-max="4" v-model="change_form.title"></mu-text-field>
        </mu-form-item>
        <mu-form-item  prop="author" label="Автор">
          <mu-text-field v-model="change_form.author"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="publisher" label="Издатель">
          <mu-text-field v-model="change_form.publisher"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="edition_year" label="Год издания">
          <mu-text-field v-model="change_form.edition_year"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="sphere" label="Раздел">
          <mu-text-field v-model="change_form.sphere"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="receipt_date" label="Дата поступления" help-text="В формате: год(4 цифры)-месяц-день">
          <mu-text-field v-model="change_form.receipt_date"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="hall" label="Зал">
          <mu-select v-model="change_form.hall">
            <mu-option v-for="option in h_options" :key="option[0]"
                       :label="option[1]" :value="option[0]"></mu-option>
          </mu-select>
        </mu-form-item>
      </mu-form>
      <mu-flex><hr/></mu-flex>
      <mu-row>
        <mu-col span="2"></mu-col>
        <mu-col justify-content="end">
          <mu-button color="success" @click="applyChanges()">
            Применить изменения
          </mu-button>
          <mu-button color="error" @click="goBooks()">
            Назад
          </mu-button>
        </mu-col>
      </mu-row>
      <mu-flex><hr/></mu-flex>
    </mu-container>
  </mu-container>
</template>

<script>
export default {
  name: 'BookChange',
  props: ['book'],
  data () {
    return {
      change_form: {
        cipher: '',
        title: '',
        author: '',
        publisher: '',
        edition_year: '',
        sphere: '',
        receipt_date: '',
        hall: ''
      },
      labelPosition: 'left',
      h_options: [[2, 'Зал №2, Главный'],
        [3, 'Зал №3, Малый'],
        [4, 'Зал №4, Новый']]
    }
  },
  created () {
    // eslint-disable-next-line
    $.ajaxSetup({
      headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
    })
  },
  methods: {
    logout () {
      sessionStorage.removeItem('auth_token')
      this.$router.push({name: 'home'})
    },
    goHome () {
      this.$router.push({name: 'home'})
    },
    goBooks () {
      this.$router.push({name: 'books'})
    },
    bookDel () {
      // eslint-disable-next-line
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/attachment_books/',
        type: 'GET',
        data: {
          book: this.book.id
        },
        success: (response) => {
          if (response.data.data.length === 0) {
            // eslint-disable-next-line
            $.ajax({
              url: 'http://127.0.0.1:8000/api/lib/book_del/' + this.book.id + '/',
              type: 'DELETE',
              success: (response) => {
                alert('Книга успешно списана')
                this.goBooks()
              }
            })
          } else {
            alert('Невозможно списать книгу, так как она закреплена за читателем')
          }
        }
      })
    },
    applyChanges () {
      let idBook = this.book.id
      let attr = {}
      for (let key in this.change_form) {
        if (this.change_form[key]) {
          attr[key] = this.change_form[key]
        }
      }
      let data = {
        data: {
          type: 'Book',
          id: idBook,
          attributes: attr
        }
      }
      fetch(`http://127.0.0.1:8000/api/lib/book_change/${this.book.id}/`,
        {
          method: 'PUT',
          headers: {
            'Authorization': 'Token ' + sessionStorage.getItem('auth_token'),
            'Content-Type': 'application/vnd.api+json'
          },
          body: JSON.stringify(data)
        }
      ).then(response => {
        alert('Данные книги успешно изменены')
        this.goBooks()
      })
    }
  }
}
</script>

<style scoped>
  .book-change-form {
    width: 800px;
    height: 560px;
    text-align: justify;
  }
  .button-del {
    margin-top: 10px;
    font: 10pt sans-serif;
  }
  .title {
    text-align: justify;
  }
  .attr {
    text-align: justify;
    width: 180px;
  }
</style>
