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
      <mu-button @click="logout()" flat slot="right">Выход</mu-button>
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
              <mu-form-item prop="unattached" label="Показывать только незакреплённые ни за кем в данный момент книги">
                <mu-switch v-model="micro_form.unattached"></mu-switch>
              </mu-form-item>
            </mu-form>
          </mu-flex>
          <mu-flex>
            {{unattachedBooks}}
          </mu-flex>
          <mu-flex>Для внесения изменений нажмите на шифр книги</mu-flex>
          <mu-paper :z-depth="1">
            <mu-data-table border stripe :columns="columns" :sort.sync="sort"
                           @sort-change="handleSortChange" :data="finalBooksList">
              <template slot-scope="scope">
                <td class="is-left"><strong>
                  <div @click="goToBook(scope.row.cipher)" class="cipher-link">
                    {{scope.row.cipher}}
                  </div>
                </strong></td>
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
            <mu-form :model="micro_form" class="cipher-search-form"
                     :label-position="labelPosition" label-width="490">
              <mu-form-item prop="unattached" label="Искать только среди незакреплённых ни за кем в данный момент книг">
                <mu-switch v-model="micro_form.unattached"></mu-switch>
              </mu-form-item>
            </mu-form>
          </mu-flex>
        </mu-row>
        <mu-row>
          <mu-col span="8">
            <mu-flex style="margin-left: 11px">
              Для поиска с учётом изменения положения переключателя нажмите кнопку "Искать" ещё раз
            </mu-flex>
          </mu-col>
          <mu-col span="5" style="color: #ffffff;">
            {{unattachedBooks}}
          </mu-col>
        </mu-row>
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
        <div v-if="foundBooksShow">
          <div v-for="book in foundBooksList" v-bind:key="book.cipher"><mu-row>
            <mu-col span="1"><strong>{{book.cipher}}</strong></mu-col>
            <mu-col>
              <mu-flex class="title">Книга: {{book.title}}</mu-flex>
              <mu-flex>Автор: {{book.author}}</mu-flex>
              <mu-flex>Издатель: {{book.publisher}}</mu-flex>
              <mu-flex>Год издания: {{book.edition_year}}</mu-flex>
              <mu-flex>Сфера: {{book.sphere}}</mu-flex>
              <mu-flex>Дата поступления: {{book.receipt_date}}</mu-flex>
              <mu-flex>Зал: {{book.hall}}</mu-flex>
              <mu-flex>
                <mu-button color="indigo400" @click="changeBook(book)"
                           small class="search-form-button">
                  Изменить/Списать книгу
                </mu-button>
              </mu-flex>
            </mu-col>
            <mu-col justify-content="end">
              <mu-flex>
                <mu-form :model="add_form[book.id]" class="add-form"
                         :label-position="labelPosition" label-width="50">
                  <mu-form-item prop="bookTitle" label="Зал:">
                    <mu-select v-model="add_form[book.id].hall">
                      <mu-option v-for="option in h_options" :key="option[0]"
                                 :label="option[1]" :value="option[0]"></mu-option>
                    </mu-select>
                  </mu-form-item>
                </mu-form>
              </mu-flex>
              <mu-flex>
                <mu-form :model="add_form[book.id]" class="add-form"
                         :label-position="labelPosition" label-width="150">
                  <mu-form-item prop="receiptDate" label="Дата поступления">
                    <mu-text-field v-model="add_form[book.id].receipt_date"></mu-text-field>
                  </mu-form-item>
                </mu-form>
              </mu-flex>
              <mu-flex>
                <mu-button color="success" @click="addCopy(book.id)" small class="copy-form-button">
                  Добавить экземпляр книги
                </mu-button>
              </mu-flex>
            </mu-col>
            <div v-if="micro_form.unattached">
              <mu-row justify-content="start">
                <mu-flex class="near-att-form-text">Закрепить данную книгу за читателем:</mu-flex>
              </mu-row>
              <mu-row>
                <mu-flex justify-content="start">
                  <mu-form :model="add_form[book.id]" class="attachment-form" :label-position="labelPosition" label-width="250">
                    <mu-form-item prop="date" label="Дата закрепления" help-text="В формате: год(4 цифры)-месяц-день">
                      <mu-text-field v-model="add_form[book.id].date"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="library_card_num" label="Номер читательского билета">
                      <mu-text-field v-model="add_form[book.id].library_card_num"></mu-text-field>
                    </mu-form-item>
                  </mu-form>
                </mu-flex>
              </mu-row>
              <mu-flex justify-content="start" class="attachment-button">
                <mu-button color="success" @click="addAtt(book.id)">
                  Закрепить
                </mu-button>
              </mu-flex>
            </div>
          </mu-row></div>
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
      bookList: [],
      i: '',
      j: '',
      ii: '',
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
      foundBooksShow: false,
      notFound: false,
      micro_form: {
        unattached: false
      },
      unattachedBooksList: [],
      finalBooksList: [],
      add_form: [],
      goalBook: ''
    }
  },
  created () {
    // eslint-disable-next-line
    $.ajaxSetup({
      headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
    })
    this.loadBooks()
    this.checkAttachments()
    this.finalBooksList = this.bookList
  },
  computed: {
    unattachedBooks: function () {
      if (this.micro_form.unattached) {
        // eslint-disable-next-line
        this.finalBooksList = this.unattachedBooksList
        return 'Показаны только не закреплённые ни за кем в данный момент книги'
      } else {
        // eslint-disable-next-line
        this.finalBooksList = this.bookList
        return 'Показаны все книги'
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
      this.finalBooksList = this.finalBooksList.sort(function (a, b) {
        if (order === 'asc') {
          return parseFloat(a[name]) + 0.0001 * parseInt(a[name].split('/')[1]) - parseFloat(b[name]) - 0.0001 * parseInt(b[name].split('/')[1])
        } else {
          return parseFloat(b[name]) + 0.0001 * parseInt(b[name].split('/')[1]) - parseFloat(a[name]) - 0.0001 * parseInt(a[name].split('/')[1])
        }
      })
    },
    loadBooks () {
      // eslint-disable-next-line
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/books/',
        type: 'GET',
        success: (response) => {
          this.bookList = response.data
          this.i = 0
          let idList = []
          for (let p = 0; p < this.bookList.length; p++) {
            idList.push(this.bookList[p].id)
          }
          let maxNum = Math.max(...idList)
          for (let m = 0; m < maxNum + 1; m++) {
            this.add_form.push({
              id: m,
              hall: '',
              receipt_date: '',
              library_card_num: '',
              date: ''
            })
          }
          this.bookList.forEach(function () {
            let newVal = {}
            for (let key in this.bookList[this.i].attributes) {
              newVal[key] = this.bookList[this.i].attributes[key]
            }
            newVal['hall'] = this.bookList[this.i].relationships.hall.data.id
            newVal['id'] = this.bookList[this.i].id
            this.bookList[this.i] = newVal
            this.add_form[newVal.id].receipt_date = newVal.receipt_date
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
          this.checkAttachments()
          this.finalBooksList = this.bookList
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
        this.search_form.bookTitle = ''
      }
      this.j = 0
      let neededLength = this.search_form.bookCipher.length
      this.finalBooksList.forEach(function () {
        if (this.finalBooksList[this.j].cipher.substring(0, neededLength) === this.search_form.bookCipher) {
          this.foundBooksList.push(this.finalBooksList[this.j])
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
    },
    openByTitle () {
      this.notFound = false
      if (this.foundBooksShow) {
        this.foundBooksShow = false
        this.foundBooksList = []
        this.search_form.bookCipher = ''
      }
      this.j = 0
      let neededLength = this.search_form.bookTitle.length
      this.finalBooksList.forEach(function () {
        if (this.finalBooksList[this.j].title.substring(0, neededLength) === this.search_form.bookTitle) {
          this.foundBooksList.push(this.finalBooksList[this.j])
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
    },
    checkAttachments () {
      // eslint-disable-next-line
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/check_att/',
        type: 'GET',
        success: (response) => {
          let attachedBooksList = response.data.data
          let k = 0
          attachedBooksList.forEach(function () {
            attachedBooksList[k] = attachedBooksList[k].book.cipher
            k++
          })
          let l = 0
          this.bookList.forEach(function () {
            if (attachedBooksList.indexOf(this.bookList[l].cipher) === -1) {
              this.unattachedBooksList.push(this.bookList[l])
            }
            l++
          }.bind(this))
        }
      })
    },
    changeBook (book) {
      this.$router.push({name: 'book_change', params: {book}})
    },
    addCopy (bookId) {
      // Получаю данные о книге, экземпляр который хочу добавить (по id)
      this.ii = 0
      this.bookList.forEach(function () {
        if (this.bookList[this.ii].id === bookId) {
          this.goalBook = this.bookList[this.ii]
        }
        this.ii++
      }.bind(this))
      // Ищу последний экземпляр данной книги
      let numList = []
      let numBookList = []
      for (let n = 0; n < this.bookList.length; n++) {
        if (this.bookList[n].title === this.goalBook.title) {
          let cipherTempList = this.bookList[n].cipher.split('/')
          let numTemp = parseInt(cipherTempList[1])
          numList.push(numTemp)
          numBookList.push(this.bookList[n])
        }
      }
      let maxNum = Math.max(...numList)
      let maxNumId = numList.indexOf(maxNum)
      this.goalBook = numBookList[maxNumId]
      maxNum += 1
      // Формирую шифр
      let cipherList = this.goalBook.cipher.split('/')
      let newCipher = cipherList[0] + '/' + maxNum
      // Формирую данные для отправки POST-запросом
      let data = {
        cipher: newCipher,
        title: this.goalBook.title,
        author: this.goalBook.author,
        publisher: this.goalBook.publisher,
        edition_year: this.goalBook.edition_year,
        sphere: this.goalBook.sphere,
        receipt_date: this.add_form[bookId].receipt_date,
        hall: this.add_form[bookId].hall
      }
      // eslint-disable-next-line
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/book_add/',
        type: 'POST',
        data: data,
        success: (response) => {
          alert('Новая книга успешно добавлена')
          this.loadBooks()
          this.active = 0
          this.finalBooksList = this.bookList
          this.goalBook = ''
          this.search_form = {
            bookCipher: '',
            bookTitle: ''
          }
          this.foundBooksList = []
          this.foundBooksShow = false
        },
        error: (response) => {
          alert('Error')
        }
      })
    },
    goToBook (bookCipher) {
      this.notFound = false
      if (this.foundBooksShow) {
        this.foundBooksShow = false
        this.foundBooksList = []
        this.search_form.bookTitle = ''
      }
      this.j = 0
      this.search_form.bookCipher = bookCipher
      this.finalBooksList.forEach(function () {
        if (this.finalBooksList[this.j].cipher === this.search_form.bookCipher) {
          this.foundBooksList.push(this.finalBooksList[this.j])
          this.j++
        } else {
          this.j++
        }
      }.bind(this))
      this.active = 1
      this.foundBooksShow = true
    },
    addAtt (bookId) {
      // eslint-disable-next-line
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/reader_get_id/',
        type: 'GET',
        data: {
          library_card_num: this.add_form[bookId].library_card_num
        },
        success: (response) => {
          if (response.data.length !== 0) {
            let data = {
              reader: response.data[0].id,
              book: bookId,
              attachment_starting_date: this.add_form[bookId].date
            }
            // eslint-disable-next-line
            $.ajax({
              url: 'http://127.0.0.1:8000/api/lib/reader/',
              type: 'POST',
              data: data,
              success: (response) => {
                alert('Закрепление добавлено')
                this.loadBooks()
                this.unattachedBooksList = []
                this.checkAttachments()
                this.finalBooksList = this.bookList
                this.active = 0
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
    margin-bottom: 10px;
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
  .add-form {
    width: 240px;
    height: 50px;
    margin-left: 10px;
  }
  .copy-form-button {
    margin-left: 12px;
  }
  .cipher-link {
    cursor: pointer
  }
  .attachment-form {
    width: 500px;
    height: 120px;
    margin-right: 300px;
    margin-left: 80px;
  }
  .attachment-button {
    margin-left: 90px;
    margin-bottom: 20px;
  }
  .near-att-form-text {
    margin-top: 9px;
    margin-left: 90px;
  }
  .title {
    text-align: justify;
  }
</style>
