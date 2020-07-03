<template>
  <mu-container>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
    <mu-appbar style="width: 100%;" color="primary">
      <mu-menu slot="left">
        <mu-button flat icon>
          <mu-icon value="menu"></mu-icon>
        </mu-button>
        <mu-list slot="content">
          <mu-list-item button>
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
    <mu-container>
      <mu-row>
        <mu-col span="10">
          <h3>Читатель {{person.full_name}}</h3>
          <h4>Нынешние данные:</h4>
        </mu-col>
        <mu-col></mu-col>
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
            <mu-form-item prop="hall" label="Зал">
              <mu-text-field v-model="form.hall"></mu-text-field>
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
                <mu-option v-for="option in options" :key="option" :label="option" :value="option"></mu-option>
              </mu-select>
            </mu-form-item>
            <mu-form-item prop="degree" label="Наличие учёной степени">
              <mu-switch v-model="form.degree"></mu-switch>
            </mu-form-item>
          </mu-form>
        </mu-col>
      </mu-row>
      <mu-flex><hr/></mu-flex>
      <mu-row>
        <mu-col span="4"></mu-col>
        <mu-col justify-content="end">
          <mu-button color="success" @click="changeReader(person_books.reader[0])">
            Применить изменения
          </mu-button>
          <mu-button color="error" @click="changeReader(person_books.reader[0])">
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
      options: [
        'среднее общее', 'среднее профессиональное', 'неполное высшее',
        'бакалавр', 'специалист', 'магистр', 'аспирантура'
      ]
    }
  },
  methods: {
    logout () {
      sessionStorage.removeItem('auth_token')
      this.$router.push({'name': 'home'})
    },
    applyChanges (idAtt, idForm) {
      this.detachment_form[idForm].attachment = idAtt
      console.log(this.detachment_form[idForm].attachment + ' ' + this.detachment_form[idForm].date)
      let data = {
        data: {
          type: 'Attachment',
          id: idAtt,
          attributes: {
            attachment_finishing_date: this.detachment_form[idForm].date
          }
        }
      }
      fetch(`http://127.0.0.1:8000/api/lib/detach/${this.detachment_form[idForm].attachment}/`,
        {
          method: 'PUT',
          headers: {
            'Authorization': 'Token ' + sessionStorage.getItem('auth_token'),
            'Content-Type': 'application/vnd.api+json'
          },
          body: JSON.stringify(data)
        }
      ).then(response => {
        alert('Книга успешно откреплена')
        this.loadBooks()
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
    height: 500px;
  }
</style>
