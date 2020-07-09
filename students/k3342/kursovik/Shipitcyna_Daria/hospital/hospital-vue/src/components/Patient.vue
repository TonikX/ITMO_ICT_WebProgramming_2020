<template>
    <mu-container>
        <Home></Home>
        <mu-row v-if="auth">
            <h1>Список пациентов клиники</h1>
            <h3><button class="btn btn-success" @click="openSimpleDialog1">+ Добавить пациента</button></h3>
        </mu-row>
        <mu-col v-else>
            <h1>Вы не авторизованы!</h1>
            <p>Для просмотра этого контента вам необходимо авторизоваться или зарегистрироваться</p>
            <mu-button color="success" @click="goLogin">Войти</mu-button>
        </mu-col>
        <mu-dialog scrollable title="Добавить пациента" width="600" :open.sync="openSimple1">
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
                         <mu-radio v-model="form.sex" value="мужской" label="Мужской"></mu-radio>
                         <mu-radio v-model="form.sex" value="женский" label="Женский"></mu-radio>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Мобильный телефон:">
                        <mu-text-field v-model="form.phone"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Почта:">
                        <mu-text-field v-model="form.email"></mu-text-field>
                    </mu-form-item>
            </mu-form>
            <mu-button class="btn-send" round color="success" @click="addPatient">Отправить</mu-button>
            <mu-button slot="actions" flat color="primary" @click="closeSimpleDialog1">Закрыть</mu-button>
        </mu-dialog>
        <mu-row>
            <mu-col xl="5">
                <div v-for="patient in patients">
                <table>
                <tr>
                    <th width=100></th>
                    <th width=300><h3 @click="openMedCard(patient.id)">{{patient.surname}} {{patient.name}} {{patient.patronymic}}</h3></th>
                </tr>
                <tr>
                    <td>Дата рождения</td>
                    <td>{{patient.birth_date}}</td>
                </tr>
                <tr>
                    <td>Пол</td>
                    <td>{{patient.sex}}</td>
                </tr>
                <tr>
                    <td>Email</td>
                    <td>{{patient.email}}</td>
                </tr>
                <tr>
                    <td>Телефон</td>
                    <td>{{patient.phone}}</td>
                </tr>
            </table>
            <br>
            <mu-button color="info" @click="openEditDialog(patient.id); loadPatientDetail(patient.id)">Редактировать</mu-button>
            <mu-button color="error" @click="openDeleteDialog(patient.id)">Удалить</mu-button>
            <mu-dialog scrollable title="Редактировать информацию о пациенте" width="600" :open.sync="openEdit">
                        <mu-form :model="edit" class="mu-demo-form" label-width="100">
                                  <mu-form-item prop="input" label="Фамилия:">
                                      <mu-text-field v-model="edit.surname"></mu-text-field>
                                  </mu-form-item>
                                  <mu-form-item prop="input" label="Имя:">
                                      <mu-text-field v-model="edit.name" :placeholder="patient_detail.name"></mu-text-field>
                                  </mu-form-item>
                                  <mu-form-item prop="input" label="Отчество:">
                                      <mu-text-field v-model="edit.patronymic" :placeholder="patient_detail.patronymic"></mu-text-field>
                                  </mu-form-item>
                                  <mu-form-item prop="input" label="Дата рождения:">
                                      <mu-text-field type="date" v-model="edit.birth_date" :placeholder="patient_detail.birth_date"></mu-text-field>
                                  </mu-form-item>
                                  <mu-form-item prop="radio" label="Пол:">
                                       <mu-radio v-model="edit.sex" value="мужской" label="Мужской"></mu-radio>
                                       <mu-radio v-model="edit.sex" value="женский" label="Женский"></mu-radio>
                                  </mu-form-item>
                                  <mu-form-item prop="input" label="Мобильный телефон:">
                                      <mu-text-field type="date" v-model="edit.phone" :placeholder="patient_detail.phone"></mu-text-field>
                                  </mu-form-item>
                                  <mu-form-item prop="input" label="Почта:">
                                      <mu-text-field type="date" v-model="edit.email" :placeholder="patient_detail.email"></mu-text-field>
                                  </mu-form-item>
                        </mu-form>
                        <mu-button class="btn-send" round color="success" @click="editPatient(edited.id)">Редактировать</mu-button>
                        <mu-button slot="actions" flat color="primary" @click="closeEditDialog">Закрыть</mu-button>
                    </mu-dialog>
                    <br>
                    <mu-dialog title="Удалить пациента" width="600" :open.sync="openDelete">
                        <p>Вы уверены, что хотите удалить пациента?</p>
                        <mu-button color="success" @click="deletePatient(deleted.id)">Да</mu-button>
                        <mu-button color="error" @click="closeDeleteDialog">Нет</mu-button>
                        <mu-button slot="actions" flat color="primary" @click="closeDeleteDialog">Закрыть</mu-button>
                    </mu-dialog>
                    <br>
                </div>
            </mu-col>
            <mu-col xl="6">
                <div v-for="rec in diagnosis">
                <h3>Медицинская запись # {{rec.id}}</h3>
                    <table width="100%">
                        <tr>
                            <th scope="row" align="left">Лечащий врач</th>
                            <th scope="row" align="left">{{rec.doctor}}</th>
                        </tr>
                        <tr>
                            <th scope="row" align="left">Диагноз и лечение</th>
                            <th scope="row" align="left">{{rec.diagnosis}}</th>
                        </tr>
                        <tr>
                            <th scope="row" align="left">Дата назначения</th>
                            <th scope="row" align="left">{{rec.date}}</th>
                        </tr>
                    </table>
                    <br>
                </div>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Appointment from '@/components/Appointment.vue'
    import Home from '@/components/Home.vue'

    export default {
        name: 'Patient',
        components: {
            Appointment,
            Home,
        },
        data() {
            return {
                patients: '',
                patient_detail: '',
                diagnosis: '',
                edited: {
                    id: '',
                },
                deleted: {
                    id: '',
                },
                form: {
                    surname: '',
                    name: '',
                    patronymic: '',
                    birth_date: '',
                    sex: '',
                    phone: '',
                    email: '',
                },
                edit: {
                    surname: '',
                    name: '',
                    patronymic: '',
                    birth_date: '',
                    sex: '',
                    phone: '',
                    email: '',
                },
                openSimple1: false,
                openEdit: false,
                openDelete: false,
            }
        },
        created() {
            $.ajaxSetup({
                  headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
              });
              this.loadPatients()
        },
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            goLogin() {
                  this.$router.push({name: "login"})
            },
            loadPatients() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/patients/",
                    type: "GET",
                    success: (response) => {
                        this.patients = response.data.data
                    }
                })
            },
            loadPatientDetail(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/patient/" + this.edited.id + "/",
                    type: "GET",
                    data: {
                        id: id
                    },
                    success: (response) => {
                        this.patient_detail = response.data.attributes,
                        this.edit = response.data.attributes
                    }
                })
            },
            addPatient() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/patients/",
                    type: "POST",
                    data: {
                        surname: this.form.surname,
                        name: this.form.name,
                        patronymic: this.form.patronymic,
                        birth_date: this.form.birth_date,
                        sex: this.form.sex,
                        phone: this.form.phone,
                        email: this.form.email
                    },
                    success: (response) => {
                        this.openSimple1 = false,
                        alert("Данные о пациенте успешно добавлены"),
                        this.loadPatients()
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            },
            openMedCard(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/med_card/",
                    type: "GET",
                    data: {
                        id: id,
                    },
                    success: (response) => {
                        this.diagnosis = response.data.data
                    }
                })
            },
            editPatient(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/patient/" + this.edited.id + "/edit/",
                    type: "PUT",
                    data: {
                        id: id,
                        surname: this.edit.surname,
                        name: this.edit.name,
                        patronymic: this.edit.patronymic,
                        birth_date: this.edit.birth_date,
                        sex: this.edit.sex,
                        phone: this.edit.phone,
                        email: this.edit.email
                    },
                    success: (response) => {
                        alert("Данные о пациенте успешно отредактированы"),
                        this.loadPatients(),
                        this.openEdit = false
                        }
                 })
            },
            deletePatient(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/patient/" + this.deleted.id + "/delete/",
                    type: "DELETE",
                    data: {
                        id: id
                    },
                    success: (response) => {
                        alert("Пациент удален"),
                        this.loadPatients(),
                        this.openDelete = false
                    }
                })
            },
            openSimpleDialog1 () {
              this.openSimple1 = true;
            },
            closeSimpleDialog1 () {
              this.openSimple1 = false;
            },
            openEditDialog(id) {
              this.openEdit = true,
              this.edited.id = id
            },
            closeEditDialog() {
              this.openEdit = false;
            },
            openDeleteDialog(id) {
              this.openDelete = true,
              this.deleted.id = id
            },
            closeDeleteDialog() {
              this.openDelete = false;
            }
        }
    }
</script>

<style>
padding {
      margin: 20px;
  }

table {
        border-collapse: collapse;
    }
    table th, td {
        padding: 10px;
        border: 1px solid #000;
    }

</style>
