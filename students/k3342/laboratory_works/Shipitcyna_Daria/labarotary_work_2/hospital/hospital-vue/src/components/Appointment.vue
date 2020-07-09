<template>
    <mu-container>
        <Home></Home>
        <mu-row v-if="auth">
            <h1>Список приемов клиники</h1>
            <h3><button class="btn btn-success" @click="openAddDialog">+ Добавить прием</button></h3>
        </mu-row>
        <mu-col v-else>
            <h1>Вы не авторизованы!</h1>
            <p>Для просмотра этого контента вам необходимо авторизоваться или зарегистрироваться</p>
            <mu-button color="success" @click="goLogin">Войти</mu-button>
        </mu-col>
        <mu-col>
        <mu-dialog scrollable title="Добавить прием" width="600" :open.sync="openAdd">
            <mu-form :model="form" class="mu-demo-form" label-width="100">
                <div @click="loadPatient">
                    <mu-select label="Выберите пациента" v-model="form.patient" full-width>
                        <mu-option v-for="patient in patients" :key="patient.id" :label="patient.surname" :value="patient.id"></mu-option>
                    </mu-select>
                </div>
                <div @click="loadDoctor">
                    <mu-select label="Выберите врача" v-model="form.doctor" full-width>
                        <mu-option v-for="doc in doctors" :key="doc.id" :label="doc.surname" :value="doc.id"></mu-option>
                    </mu-select>
                </div>
                <div @click="loadServices">
                    <mu-select label="Выберите услуги" multiple chips v-model="form.service" full-width>
                        <mu-option v-for="service,index in services" :key="service.id" :label="service.service" :value="service.id"></mu-option>
                    </mu-select>
                </div>
                <div @click="loadDocFreeTime">
                    <mu-select label="Выберите дату и время приема" v-model="form.date" full-width>
                        <mu-option v-for="date in dates" :key="date.id" :label="date.date + ' ' + date.time_start" :value="date.id"></mu-option>
                    </mu-select>
                </div>
            </mu-form>
            <mu-button class="btn-send" round color="success" @click="addApp">Добавить</mu-button>
            <mu-button slot="actions" flat color="primary" @click="closeAddDialog">Закрыть</mu-button>
        </mu-dialog>
        </mu-col>
        <br>
        <mu-col align='center'>
            <div v-for="app in apps">
            <table>
                <tr>
                    <th width=200></th>
                    <th width=400>Прием # {{app.id}}</th>
                </tr>
                <tr>
                    <td width=200>Врач</td>
                    <td width=400>{{app.record.doctor.surname}} {{app.record.doctor.name}} {{app.record.doctor.patronymic}}</td>
                </tr>
                <tr>
                    <td width=200>Пациент</td>
                    <td width=400>{{app.patient.surname}} {{app.patient.name}}</td>
                </tr>
                <tr>
                    <td width=200>Дата и время приема</td>
                    <td width=400>{{app.record.app_time.date}} {{app.record.app_time.time_start}}</td>
                </tr>
                <tr>
                    <td width=200>Назначение</td>
                    <td width=400>{{app.diagnosis}}</td>
                </tr>
                <tr>
                    <td width=200>Услуги</td>
                    <td width=400 v-for="rec in app.service">{{rec.service}}</td>
                </tr>
                <tr>
                    <td width=200>Стоимость</td>
                    <td width=400 v-for="rec in app.service">{{rec.price}}</td>
                </tr>
            </table>
            <br><br>
            </div>
        </mu-col>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Home from '@/components/Home.vue'
    import axios from 'axios';

    export default {
        name: 'Appointment',
        components: {
            Home,
        },
        data() {
            return {
                services: '',
                apps: '',
                edited: {
                    id: '',
                },
                edit: {
                    patient: '',
                    doctor: '',
                    service: '',
                    diagnosis: '',
                    date: '',
                },
                patients: '',
                doctors: '',
                dates: '',
                filtered: '',
                filter: {
                    records: '',
                    doctor: '',
                    doctor_type: '',
                    patient: '',
                    date: '',
                },
                form: {
                    patient: '',
                    doctor: '',
                    service: '',
                    date: '',
                },
                openAdd: false,
                openEdit: false
            }
        },
        created() {
            $.ajaxSetup({
                  headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
              });
              this.loadApp();

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
            loadApp() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/apps/",
                    type: "GET",
                    success: (response) => {
                    this.apps = response.data.data
                    }
                })
            },
            loadPatient() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/patients/",
                    type: "GET",
                    success: (response) => {
                    this.patients = response.data.data
                    }
                })
            },
            AppDetail(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/app/" + id,
                    type: "GET",
                    success: (response) => {
                        this.edit = response.data.attributes
                    }
                })
            },
            loadDoctor() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/doctors/",
                    type: "GET",
                    success: (response) => {
                    this.doctors = response.data.data
                    }
                })
            },
            loadDocFreeTime() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/doc_free_time/",
                    data: {
                        doctor: this.form.doctor
                    },
                    type: "GET",
                    success: (response) => {
                        this.dates = response.data.data
                    }
                })

            },
            loadServices() {
                console.log('ok');
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/services/",
                    type: "GET",
                    success: (response) =>
                    {
                        this.services = response.data.data
                        //console.log(this.services[0].service)
                    },
                     error: (jqXHR, textStatus, errorThrown) => {
                        console.log(textStatus, errorThrown)
                    }
                })
            },
            addApp() {
                console.log(JSON.stringify(this.form));
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/add_app/",
                    method: "POST",
                    contentType: 'application/json',
                    data: JSON.stringify(this.form),
                    success: (response) => {
                        this.openAdd = false,
                        alert("Данные о приеме успешно добавлены"),
                        this.loadApp()
                    },
                    error: (jqXHR, textStatus, errorThrown) => {
                        console.log(textStatus, errorThrown)
                    }
                })
            },
            filterApp() {
                $.ajax ({
                    url: "http://127.0.0.1:8000/api/v1/hospital/appointments/?record__doctor__surname=" + this.filter.doctor + "&patient__surname=" + this.filter.patient + "&record__doctor__type=" + this.filter.doctor_type + "&record__app_time__date=" + this.filter.date,
                    type: "GET",
                    success: (response) => {
                        var i;
                        for (i = 0; i < response.data.length; i++){
                            this.filtered += response.data[i].id
                        }
                    }
                })
            },
            editApp(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/app/" + id + "/edit/",
                    type: "PUT",
                    contentType: 'application/json',
                    data: JSON.stringify(this.edit),
                    success: (response) => {
                        alert("Данные о приеме успешно отредактированы"),
                        this.loadApp(),
                        this.openEdit = false
                        }
                 })
            },
            openAddDialog () {
              this.openAdd = true;
            },
            closeAddDialog () {
              this.openAdd = false;
            },
            openEditDialog(id) {
              this.openEdit = true,
              this.edited.id = id
            },
            closeEditDialog() {
              this.openEdit = false;
            },
        }
    }
</script>

<style scoped>
table {
        border-collapse: collapse;
    }
    table td, th {
        padding: 10px;
        border: 1px solid #000;
    }
</style>
