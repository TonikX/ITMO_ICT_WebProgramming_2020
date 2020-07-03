<template>
    <mu-container>
      <mu-appbar style="width: 100%;" color="primary">
        <mu-button @click="goLogin" v-if="!auth" flat slot="right">Вход</mu-button>
        <mu-button @click="logout" v-if="auth" flat slot="right">Выход</mu-button>
        <mu-button @click="openAbitFormAction " v-if="auth" flat slot="left">Добавить абитуриента</mu-button>
      </mu-appbar>
      <mu-row>
        <abits v-if="auth"></abits>
      </mu-row>

      <mu-dialog title="Добавление абитуриента" width="560" scrollable :open.sync="openAbitForm">
        <mu-form :model="formAbit" class="mu-demo-form" label-position="top" label-width="100">
          <mu-form-item prop="surname" label="Фамилия">
            <mu-text-field v-model="formAbit.surname"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="name" label="Имя">
            <mu-text-field v-model="formAbit.name"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="secondname" label="Отчество">
            <mu-text-field v-model="formAbit.secondname"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="document_type" label="Тип документа">
            <mu-radio v-model="formAbit.document_type" value=1 label="Паспорт"></mu-radio>
            <mu-radio v-model="formAbit.document_type" value=2 label="Свидетельство о рождении"></mu-radio>
          </mu-form-item>
          <mu-form-item prop="document_number" label="Номер документа">
            <mu-text-field v-model="formAbit.document_number"></mu-text-field>
          </mu-form-item>
          <mu-select label="Место учебы" v-model="formAbit.study_place" full-width>
            <mu-option v-for="option in places" :key="option.name" :label="option.name" :value="option.id"></mu-option>
            <mu-button full-width color="success" @click="openPlaceFormAction">Добавить школу</mu-button>
          </mu-select>
          <mu-form-item prop="study_date" label="Дата окончания">
            <mu-date-input  v-model="formAbit.study_date" label="" label-float full-width :date-time-format="enDateFormat"></mu-date-input>
          </mu-form-item>
          <mu-form-item prop="document_type" label="Тип награды">
            <mu-radio v-model="formAbit.award_type" value=1 label="Нет"></mu-radio>
            <mu-radio v-model="formAbit.award_type" value=2 label="Серебрянная медаль"></mu-radio>
            <mu-radio v-model="formAbit.award_type" value=3 label="Золотая медаль"></mu-radio>
          </mu-form-item>
          <mu-form-item prop="study_type" label="Форма обучения">
            <mu-radio v-model="formAbit.study_type" value=1 label="Очная"></mu-radio>
            <mu-radio v-model="formAbit.study_type" value=2 label="Очно-заочная"></mu-radio>
            <mu-radio v-model="formAbit.study_type" value=3 label="Заочная"></mu-radio>
          </mu-form-item>
          <mu-form-item prop="contract_type" label="Тип контракта">
            <mu-radio v-model="formAbit.contract_type" value=1 label="Бюджет"></mu-radio>
            <mu-radio v-model="formAbit.contract_type" value=2 label="Платный"></mu-radio>
          </mu-form-item>
          <mu-form-item prop="abit_type" label="Тип поступления">
            <mu-radio v-model="formAbit.abit_type" value=1 label="После 9-го"></mu-radio>
            <mu-radio v-model="formAbit.abit_type" value=2 label="После 11-го"></mu-radio>
          </mu-form-item>
          <mu-form-item prop="student_type" label="Тип студента">
            <mu-radio v-model="formAbit.student_type" value=1 label="Нет"></mu-radio>
            <mu-radio v-model="formAbit.student_type" value=2 label="Целевик"></mu-radio>
            <mu-radio v-model="formAbit.student_type" value=3 label="Инвалид"></mu-radio>
            <mu-radio v-model="formAbit.student_type" value=4 label="Сирота"></mu-radio>
          </mu-form-item>
          <mu-form-item prop="marks" label="Сумма баллов">
            <mu-text-field v-model="formAbit.marks"></mu-text-field>
          </mu-form-item>
          <mu-select label="Программа обучения" v-model="formAbit.study_program" full-width>
            <mu-option v-for="option in programs" :key="option.name" :label="option.name" :value="option.id"></mu-option>
          </mu-select>
        </mu-form>
        <mu-button slot="actions" flat color="primary" @click="closeAbitFormAction">Закрыть</mu-button>
        <mu-button slot="actions" flat color="success" @click="addAbit">Добавить</mu-button>
      </mu-dialog>

      <mu-dialog title="Добавление школы" width="560" scrollable :open.sync="openPlaceForm">
        <mu-form :model="formPlace" class="mu-demo-form" label-position="right" label-width="100">
          <mu-form-item prop="name" label="Название">
            <mu-text-field v-model="formPlace.name"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="place" label="Город">
            <mu-text-field v-model="formPlace.place"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="type" label="Тип">
            <mu-radio v-model="formPlace.type" value=1 label="Школа"></mu-radio>
            <mu-radio v-model="formPlace.type" value=2 label="Колледж"></mu-radio>
          </mu-form-item>
        </mu-form>
        <mu-button slot="actions" flat color="primary" @click="closePlaceFormAction">Закрыть</mu-button>
        <mu-button slot="actions" flat color="success" @click="addPlace">Добавить</mu-button>
      </mu-dialog>
    </mu-container>
</template>

<script>
    import Abits from "./Abits";
    import $ from "jquery";
    import moment from 'moment'

    const dayAbbreviation = ['S', 'M', 'T', 'W', 'T', 'F', 'S'];
    const dayList = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
      'Oct', 'Nov', 'Dec'];
    const monthLongList = ['January', 'February', 'March', 'April', 'May', 'June',
      'July', 'August', 'September', 'October', 'November', 'December'];

    const enDateFormat = {
      formatDisplay (date) {
        return `${dayList[date.getDay()]}, ${monthList[date.getMonth()]} ${date.getDate()}`;
      },
      formatMonth (date) {
        return `${monthLongList[date.getMonth()]} ${date.getFullYear()}`;
      },
      getWeekDayArray (firstDayOfWeek) {
        let beforeArray = [];
        let afterArray = [];
        for (let i = 0; i < dayAbbreviation.length; i++) {
          if (i < firstDayOfWeek) {
            afterArray.push(dayAbbreviation[i]);
          } else {
            beforeArray.push(dayAbbreviation[i]);
          }
        }
        return beforeArray.concat(afterArray);
      },
      getMonthList () {
        return monthList;
      }
    };

    export default {
        data () {
          return {
            enDateFormat,
            places: '',
            programs: '',
            openAbitForm: false,
            openPlaceForm: false,
            formPlace: {
              name: '',
              place: '',
              type: 1,
            },
            formAbit: {
              surname: '',
              name: '',
              secondname: '',
              document_type: '',
              document_number: '',
              study_place: '',
              study_date: '',
              award_type: '',
              study_type: '',
              contract_type: '',
              abit_type: '',
              student_type: '',
              study_program: '',
              marks: '',
            },
          };
        },
        name: "Home",
        components: {
          Abits
        },
        created() {

        },
        methods: {
          openAbitFormAction () {
            this.openAbitForm = true;
            this.loadPrograms()
            this.loadPlaces()
          },
          closeAbitFormAction () {
            this.openAbitForm = false;
          },
          openPlaceFormAction () {
            this.openPlaceForm = true;
          },
          closePlaceFormAction () {
            this.openPlaceForm = false;
            alert(this.form.name);
          },
          goLogin() {
            this.$router.push({name: 'login'})
          },
          logout() {
            sessionStorage.removeItem("auth_token")
            window.location = '/'
          },
          addPlace() {
            $.ajax({
              url: "http://127.0.0.1:8000/api/places/",
              type: "POST",
              data: this.formPlace,
              success: (response) => {
                alert("Информация успешно добавлена")
                this.loadPlaces()
                this.closePlaceFormAction()
              },
              error: (response) => {
                alert(response.statusText)
              }
            })
          },
          addAbit() {
            this.formAbit.study_date = moment(String(this.formAbit.study_date)).format('YYYY-MM-DD')
            $.ajax({
              url: "http://127.0.0.1:8000/api/abits/",
              type: "POST",
              data: this.formAbit,
              success: (response) => {
                alert("Информация успешно добавлена")
                this.closeAbitFormAction()
                window.location = '/'
              },
              error: (response) => {
                alert(response.statusText)
              }
            })
          },
          loadPlaces() {
            $.ajax({
              url: "http://127.0.0.1:8000/api/places/",
              type: "GET",
              success: (response) => {
                this.places = response.data.values
              }
            })
          },
          loadPrograms() {
          $.ajax({
            url: "http://127.0.0.1:8000/api/programs/",
            type: "GET",
            success: (response) => {
              this.programs = response.data.values
            }
          })
        },
        },
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
    }
</script>

<style scoped>

</style>
