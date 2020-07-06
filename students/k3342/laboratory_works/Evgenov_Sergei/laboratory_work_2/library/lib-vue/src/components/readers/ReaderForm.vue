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
          <mu-list-item button @click="goBack()">
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
      <mu-button @click="logout" flat slot="right">Выход</mu-button>
    </mu-appbar>
    <mu-container>
      <mu-row>
        <mu-col span="1"></mu-col>
        <mu-col span="10">
          <h3>Новый читатель</h3>
        </mu-col>
        <mu-col></mu-col>
      </mu-row>
      <mu-row class="near-form">
        <mu-col span="1"></mu-col>
        <mu-col justify-content="start">
          <mu-form :model="form" class="reader-form" :label-position="labelPosition" label-width="300">
            <mu-form-item prop="library_card_num" label="Номер читательского билета">
              <mu-text-field v-model="form.library_card_num"></mu-text-field>
            </mu-form-item>
            <mu-form-item prop="full_name" label="Полное имя (ФИО)">
              <mu-text-field v-model="form.full_name"></mu-text-field>
            </mu-form-item>
            <mu-form-item prop="hall" label="Зал">
              <mu-select v-model="form.hall">
                <mu-option v-for="option in h_options" :key="option[0]"
                           :label="option[1]" :value="option[0]"></mu-option>
              </mu-select>
            </mu-form-item>
            <mu-form-item  prop="home_address" label="Адрес">
              <mu-text-field multi-line :rows="2" :rows-max="3" v-model="form.home_address"></mu-text-field>
            </mu-form-item>
            <mu-form-item prop="passport_data" label="Паспортные данные">
              <mu-text-field v-model="form.passport_data"></mu-text-field>
            </mu-form-item>
            <mu-form-item prop="birth_date" label="Дата рождения" help-text="В формате: год(4 цифры)-месяц-день">
              <mu-text-field v-model="form.birth_date"></mu-text-field>
            </mu-form-item>
            <mu-form-item prop="phone_num" label="Контактный номер">
              <mu-text-field v-model="form.phone_num"></mu-text-field>
            </mu-form-item>
            <mu-form-item prop="education" label="Образование">
              <mu-select v-model="form.education">
                <mu-option v-for="option in e_options" :key="option"
                           :label="option" :value="option"></mu-option>
              </mu-select>
            </mu-form-item>
            <mu-form-item prop="degree" label="Наличие учёной степени">
              <mu-select v-model="form.degree">
                <mu-option v-for="option in d_options" :key="option"
                           :label="option" :value="option"></mu-option>
              </mu-select>
            </mu-form-item>
          </mu-form>
        </mu-col>
      </mu-row>
      <mu-flex><hr/></mu-flex>
      <mu-row>
        <mu-col span="4"></mu-col>
        <mu-col justify-content="end">
          <mu-button color="success" @click="addReader()">
            Добавить читателя
          </mu-button>
          <mu-button color="error" @click="goBack()">
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
  name: 'ReaderCh',
  props: ['person'],
  data () {
    return {
      form: {
        ful_name: '',
        library_card_num: '',
        hall: '',
        home_address: '',
        passport_data: '',
        birth_date: '',
        phone_num: '',
        education: '',
        degree: ''
      },
      labelPosition: 'left',
      e_options: [
        'среднее общее', 'среднее профессиональное', 'неполное высшее',
        'бакалавр', 'специалист', 'магистр', 'аспирантура'
      ],
      h_options: [
        [2, 'Зал №2, Главный'],
        [3, 'Зал №3, Малый'],
        [4, 'Зал №4, Новый']
      ],
      d_options: ['есть', 'отсутствует']
    }
  },
  methods: {
    logout () {
      sessionStorage.removeItem('auth_token')
      this.$router.push({'name': 'home'})
    },
    addReader () {
      if (this.form.degree === 'есть') {
        this.form.degree = true
      } else {
        this.form.degree = false
      }
      // eslint-disable-next-line
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/reader_add/',
        type: 'POST',
        data: this.form,
        success: (response) => {
          alert('Новый читатель успешно добавлен')
          this.$router.push({'name': 'home'})
        },
        error: (response) => {
          alert('Error')
        }
      })
    },
    goBack () {
      this.$router.push({'name': 'home'})
    },
    goBooks () {
      this.$router.push({'name': 'books'})
    }
  }
}
</script>

<style scoped>
  .reader-form {
    width: 800px;
    height: 50px;
  }
  .near-form {
    height: 580px;
  }
</style>
