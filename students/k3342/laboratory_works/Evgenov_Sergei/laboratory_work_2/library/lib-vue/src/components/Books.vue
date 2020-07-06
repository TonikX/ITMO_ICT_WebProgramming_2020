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
          <mu-list-item button>
            <mu-list-item-content>
              <mu-list-item-title>Книги</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
        </mu-list>
      </mu-menu>
      Сайт библиотеки на Vue.js
      <mu-button @click="logout" flat slot="right">Выход</mu-button>
    </mu-appbar>
      <mu-tabs :value.sync="active" color="#C08E67">
        <mu-tab>Список книг</mu-tab>
        <mu-tab>Поиск и изменение книг</mu-tab>
        <mu-tab>Добавить новую книгу</mu-tab>
      </mu-tabs>
      <div class="demo-text" v-if="active === 0">
        <mu-container>
          <mu-flex>
            <mu-form :model="micro_form" class="cipher-search-form"
                     :label-position="labelPosition" label-width="490">
              <mu-form-item prop="unattached" label="Показывать только незакреплённые в данный момент за кем-то книги">
                <mu-switch v-model="micro_form.unattached"></mu-switch>
              </mu-form-item>
            </mu-form>
          </mu-flex>
          <mu-flex>
            {{unattachedBooks}}
          </mu-flex>
          <mu-flex>Для внесения изменений нажмите на шифр книги</mu-flex>
          <mu-paper :z-depth="1">
            <mu-data-table border stripe :columns="columns"
                           :sort.sync="sort"
                           @sort-change="handleSortChange"
                           :data="bookList">
              <template slot-scope="scope">
                <td class="is-left"><strong>{{scope.row.cipher}}</strong></td>
                <td class="is-left">{{scope.row.title}}</td>
                <td class="is-left">{{scope.row.author}}</td>
                <td class="is-left">{{scope.row.publisher}}</td>
                <td class="is-left">{{scope.row.edition_year}}</td>
                <td class="is-left">{{scope.row.sphere}}</td>
                <td class="is-left">{{scope.row.receipt_date}}</td>
                <td class="is-left">{{scope.row.hall}}</td>
              </template>
            </mu-data-table>
          </mu-paper>
        </mu-container>
      </div>
      <div class="demo-text" v-if="active === 1">
        <mu-row>
          <mu-flex>
            <div class="near-form-text">Поиск по шифру:</div>
            <mu-form :model="search_form" class="cipher-search-form"
                     :label-position="labelPosition" label-width="100">
              <mu-form-item prop="bookCipher" label="Шифр книги">
                <mu-text-field v-model="search_form.bookCipher"></mu-text-field>
              </mu-form-item>
            </mu-form>
            <mu-button color="primary" @click="openByCipher()" small class="search-form-button">
              Искать
            </mu-button>
          </mu-flex>
          <mu-flex>
            <div class="near-form-text">Поиск по названию:</div>
            <mu-form :model="search_form" class="title-search-form"
                     :label-position="labelPosition" label-width="240">
              <mu-form-item prop="bookTitle" label="Начните вводить название книги">
                <mu-text-field v-model="search_form.bookTitle"></mu-text-field>
              </mu-form-item>
            </mu-form>
            <mu-button color="primary" @click="openByTitle()" small class="search-form-button">
              Искать
            </mu-button>
          </mu-flex>
        </mu-row>
        <div v-if="this.foundBooksShow">
          <mu-row v-for="book in this.foundBooksList" v-bind:key="book.cipher">
            <mu-col span="1"><strong>{{book.cipher}}</strong></mu-col>
            <mu-col>
              <mu-flex class="title">Книга: {{book.title}}</mu-flex>
              <mu-flex>Автор: {{book.author}}</mu-flex>
              <mu-flex>Издатель: {{book.publisher}}</mu-flex>
              <mu-flex>Год издания: {{book.edition_year}}</mu-flex>
              <mu-flex>Сфера: {{book.sphere}}</mu-flex>
              <mu-flex>Дата поступления: {{book.receipt_date}}</mu-flex>
              <mu-flex>Зал: {{book.hall}}</mu-flex>
            </mu-col>
          </mu-row>
        </div>
        <div v-if="notFound">
          По вашему запросу книг не найдено
        </div>
      </div>
      <div class="demo-text" v-if="active === 2">
        <mu-form :model="form" class="book-form" :label-position="labelPosition" label-width="180">
            <mu-form-item prop="cipher" label="Шифр">
              <mu-text-field v-model="form.cipher"></mu-text-field>
            </mu-form-item>
            <mu-form-item prop="title" label="Название">
              <mu-text-field multi-line :rows="3" :rows-max="4" v-model="form.title"></mu-text-field>
            </mu-form-item>
            <mu-form-item  prop="author" label="Автор">
              <mu-text-field v-model="form.author"></mu-text-field>
            </mu-form-item>
            <mu-form-item prop="publisher" label="Издатель">
              <mu-text-field v-model="form.publisher"></mu-text-field>
            </mu-form-item>
            <mu-form-item prop="edition_year" label="Год издания">
              <mu-text-field v-model="form.edition_year"></mu-text-field>
            </mu-form-item>
            <mu-form-item prop="sphere" label="Раздел">
              <mu-text-field v-model="form.sphere"></mu-text-field>
            </mu-form-item>
            <mu-form-item prop="receipt_date" label="Дата поступления" help-text="В формате: год(4 цифры)-месяц-день">
              <mu-text-field v-model="form.receipt_date"></mu-text-field>
            </mu-form-item>
            <mu-form-item prop="hall" label="Зал">
              <mu-select v-model="form.hall">
                <mu-option v-for="option in h_options" :key="option[0]"
                           :label="option[1]" :value="option[0]"></mu-option>
              </mu-select>
            </mu-form-item>
        </mu-form>
        <mu-flex>
          <mu-button color="success" @click="addBook()">
            Добавить книгу
          </mu-button>
        </mu-flex>
      </div>
    </mu-container>
</template>

<script>
export default {
  name: 'Books',
  data () {
    return {
      sort: {
        name: '',
        order: 'asc'
      },
      columns: [
        {
          title: 'Шифр',
          width: 100,
          name: 'cipher',
          sortable: true
        },
        {
          title: 'Название книги',
          width: 300,
          // align: 'left',
          name: 'title'
        },
        {
          title: 'Автор',
          // width: 120,
          // align: 'left',
          name: 'author'
        },
        {
          title: 'Издатель',
          // width: 120,
          // align: 'left'
          name: 'publisher'
        },
        {
          title: 'Год издания',
          // width: 100,
          // align: 'left'
          name: 'edition_year'
        },
        {title: 'Раздел',
          width: 100,
          // align: 'left'
          name: 'sphere'
        },
        {title: 'Дата поступления',
          // width: 120,
          // align: 'left'
          name: 'receipt_date'
        },
        {title: 'Зал',
          width: 70,
          // align: 'left'
          name: 'hall'
        }
      ],
      bookList: '',
      i: '',
      active: 0,
      form: {
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
      h_options: [
        [2, 'Зал №2, Главный'],
        [3, 'Зал №3, Малый'],
        [4, 'Зал №4, Новый']
      ],
      search_form: {
        bookCipher: '',
        bookTitle: ''
      },
      rawBooksList: '',
      foundBooksList: [],
      j: '',
      foundBooksShow: false,
      notFound: false,
      micro_form: {
        unattached: false
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
  computed: {
    unattachedBooks: function () {
      if (this.micro_form.unattached) {
        console.log('doit')
        return 'doit'
      } else {
        return "or don't"
      }
    }
  },
  methods: {
    logout () {
      sessionStorage.removeItem('auth_token')
      this.$router.push({'name': 'home'})
    },
    goHome () {
      this.$router.push({'name': 'home'})
    },
    handleSortChange ({name, order}) {
      this.bookList = this.bookList.sort((a, b) =>
        order === 'asc' ? parseFloat(a[name]) - parseFloat(b[name]) : parseFloat(b[name]) - parseFloat(a[name]))
    },
    loadBooks () {
      // eslint-disable-next-line
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/books/',
        type: 'GET',
        success: (response) => {
          this.bookList = response.data
          this.i = 0
          this.bookList.forEach(function () {
            let newVal = {}
            for (let key in this.bookList[this.i].attributes) {
              newVal[key] = this.bookList[this.i].attributes[key]
            }
            newVal['hall'] = this.bookList[this.i].relationships.hall.data.id
            this.bookList[this.i] = newVal
            this.i++
          }.bind(this))
        }
      })
    },
    addBook () {
      // eslint-disable-next-line
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/book_add/',
        type: 'POST',
        data: this.form,
        success: (response) => {
          alert('Новая книга успешно добавлена')
          for (let key in this.form) {
            this.form[key] = ''
          }
          this.loadBooks()
          this.active = 0
        },
        error: (response) => {
          alert('Error')
        }
      })
    },
    openByCipher () {
      this.notFound = false
      if (this.foundBooksShow) {
        this.foundBooksShow = false
        this.foundBooksList = []
        this.rawBooksList = ''
        this.search_form.bookTitle = ''
      }
      // eslint-disable-next-line
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/one_book/',
        type: 'GET',
        success: (response) => {
          this.rawBooksList = response.data
          this.j = 0
          let neededLength = this.search_form.bookCipher.length
          this.rawBooksList.forEach(function () {
            if (this.rawBooksList[this.j].attributes.cipher.substring(0, neededLength) === this.search_form.bookCipher) {
              let newVal = {}
              for (let key in this.rawBooksList[this.j].attributes) {
                newVal[key] = this.rawBooksList[this.j].attributes[key]
              }
              newVal['hall'] = this.rawBooksList[this.j].relationships.hall.data.id
              this.foundBooksList.push(newVal)
              this.j++
            } else {
              this.j++
            }
          }.bind(this))
          if (this.foundBooksList.length) {
            this.foundBooksShow = true
          } else {
            this.foundBooksShow = true
            this.notFound = true
          }
        }
      })
    },
    openByTitle () {
      this.notFound = false
      if (this.foundBooksShow) {
        this.foundBooksShow = false
        this.foundBooksList = []
        this.rawBooksList = ''
        this.search_form.bookCipher = ''
      }
      // eslint-disable-next-line
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/one_book/',
        type: 'GET',
        success: (response) => {
          this.rawBooksList = response.data
          this.j = 0
          let neededLength = this.search_form.bookTitle.length
          this.rawBooksList.forEach(function () {
            if (this.rawBooksList[this.j].attributes.title.substring(0, neededLength) === this.search_form.bookTitle) {
              let newVal = {}
              for (let key in this.rawBooksList[this.j].attributes) {
                newVal[key] = this.rawBooksList[this.j].attributes[key]
              }
              newVal['hall'] = this.rawBooksList[this.j].relationships.hall.data.id
              this.foundBooksList.push(newVal)
              this.j++
            } else {
              this.j++
            }
          }.bind(this))
          if (this.foundBooksList.length) {
            this.foundBooksShow = true
          } else {
            this.foundBooksShow = true
            this.notFound = true
          }
        }
      })
    }
  }
}
</script>

<style scoped>
  .demo-text {
  padding: 16px;
  background: #ffffff;
  }
  .book-form {
    width: 800px;
    height: 560px;
  }
  .cipher-search-form {
    width: 160px;
    height: 50px;
    margin-left: 10px;
  }
  .search-form-button {
    margin-top: 8px;
    margin-left: 10px;
  }
  .near-form-text {
    margin-top: 9px;
    margin-left: 10px;
  }
  .title-search-form {
    width: 400px;
    height: 50px;
    margin-left: 10px;
  }
</style>
