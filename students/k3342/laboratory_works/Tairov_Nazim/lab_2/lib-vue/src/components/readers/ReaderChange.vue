<template>
  <mu-container>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
    <mu-appbar style="width: 100%;" color="#34495E">
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
      Библиотека
      <mu-button @click="logout()" flat slot="right">Выход</mu-button>
    </mu-appbar>
    <mu-container>
      <mu-row>
        <mu-col span="10">
          <h3>Читатель {{person.full_name}}</h3>
          <h4>Нынешние данные:</h4>
        </mu-col>
        <mu-col></mu-col>
        <mu-col justify-content="end">
          <mu-button color="error" class="button-del" @click="personDel">
            Удалить читателя
          </mu-button>
        </mu-col>
      </mu-row>
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
      <mu-row>
        <mu-col span="10">
          <h4>Новые данные:</h4>
          <h5>(Заполняйте только те поля, значения которых собираетесь изменить)</h5>
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
          <mu-button color="success" @click="applyChanges()">
            Применить изменения
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
  name: 'ReaderChange',
  props: ['person'],
  data () {
    return {
      form: {
        id: '',
        full_name: '',
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
      h_options: [[2, 'Зал №2, Главный'],
        [3, 'Зал №3, Малый'],
        [4, 'Зал №4, Новый']],
      d_options: ['есть', 'отсутствует']
    }
  },
  methods: {
    logout () {
      sessionStorage.removeItem('auth_token')
      this.$router.push({'name': 'home'})
    },
    applyChanges () {
      let idPers = this.person.id
      let attr = {}
      for (let key in this.form) {
        if (this.form[key]) {
          attr[key] = this.form[key]
        }
      }
      if (attr.degree) {
        if (attr.degree === 'есть') {
          attr.degree = true
        } else {
          attr.degree = false
        }
      }
      let data = {
        data: {
          type: 'Reader',
          id: idPers,
          attributes: attr
        }
      }
      fetch(`http://127.0.0.1:8000/api/lib/reader_change/${this.person.id}/`,
        {
          method: 'PUT',
          headers: {
            'Authorization': 'Token ' + sessionStorage.getItem('auth_token'),
            'Content-Type': 'application/vnd.api+json'
          },
          body: JSON.stringify(data)
        }
      ).then(response => {
        alert('Данные читателя успешно изменены')
        this.goBack()
      })
    },
    goBack () {
      this.$router.push({'name': 'home'})
    },
    goBooks () {
      this.$router.push({'name': 'books'})
    },
    personDel () {
      // eslint-disable-next-line
      $.ajaxSetup({
        headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
      })
      // eslint-disable-next-line
      $.ajax({
        url: 'http://127.0.0.1:8000/api/lib/reader/',
        type: 'GET',
        data: {
          reader: this.person.id
        },
        success: (response) => {
          if (response.data.books.length === 0) {
            // eslint-disable-next-line
            $.ajax({
              url: 'http://127.0.0.1:8000/api/lib/reader_del/' + this.person.id + '/',
              type: 'DELETE',
              success: (response) => {
                alert('Читатель успешно удалён')
                this.goBack()
              }
            })
          } else {
            alert('Невозможно удалить читателя, он вернул не все взятые книги')
          }
        }
      })
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
  .button-del {
    margin-top: 10px;
    font: 10pt sans-serif;
  }
</style>
