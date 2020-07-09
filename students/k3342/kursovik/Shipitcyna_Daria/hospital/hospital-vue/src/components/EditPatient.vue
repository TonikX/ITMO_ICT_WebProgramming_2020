<template>
  <mu-container>
       <mu-dialog title="Редактировать информацию пациенте" width="600" :open.sync="openScroll">
            <mu-form :model="form" class="mu-demo-form" label-width="100">
                      <mu-form-item prop="input" label="Фамилия:">
                          <mu-text-field v-model="form.surname"></mu-text-field>
                      </mu-form-item>
                      <mu-form-item prop="input" label="Имя:">
                          <mu-text-field v-model="form.name"></mu-text-field>
                      </mu-form-item>
                      <mu-form-item prop="input" label="Отчество:">
                          <mu-text-field v-model="form.patronymic"></mu-text-field>
                      </mu-form-item>
                      <mu-form-item prop="input" label="Дата рождения:">
                          <mu-text-field type="date" v-model="form.birth_date"></mu-text-field>
                      </mu-form-item>
                      <mu-form-item prop="radio" label="Пол:">
                           <mu-radio v-model="form.sex" value="male" label="Мужской"></mu-radio>
                           <mu-radio v-model="form.sex" value="female" label="Женский"></mu-radio>
                      </mu-form-item>
            </mu-form>
                      <mu-button class="btn-send" round color="success" @click="editPatient">Подтвердить</mu-button>
       </mu-dialog>
  </mu-container>

</template>

<script>
    import $ from 'jquery'
    import Home from '@/components/Home.vue'

    export default {
        name: 'EditPatient',
        components: {
            Home,
        },
        props: {id: ''},
        data() {
            return {
                openScroll: true,
                form: {
                    surname: '',
                    name: '',
                    patronymic: '',
                    birth_date: '',
                    sex: '',
                }
            }
        },
        computed: {
              auth() {
                  if (sessionStorage.getItem("auth_token")) {
                      return true
                  }
              }
        },
        methods: {
            editPatient() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/patient/" + this.id + "/edit/",
                    type: "PUT",
                    data: {
                        surname: this.form.surname,
                        name: this.form.name,
                        patronymic: this.form.patronymic,
                        birth_date: this.form.birth_date,
                        sex: this.form.sex,
                    }

                })
            }
        }
    }
</script>

<style scoped>

</style>
