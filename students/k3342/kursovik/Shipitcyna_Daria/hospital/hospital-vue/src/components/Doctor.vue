<template>
    <mu-container>
        <Home></Home>
        <mu-row v-if="auth">
            <h1>Список врачей клиники</h1>
            <h3><button class="btn btn-success" @click="openAddDialog">+ Добавить врача</button></h3>
        </mu-row>
        <mu-col v-else>
            <h1>Вы не авторизованы!</h1>
            <p>Для просмотра этого контента вам необходимо авторизоваться или зарегистрироваться</p>
            <mu-button color="success" @click="goLogin">Войти</mu-button>
        </mu-col>
        <mu-dialog scrollable title="Добавить врача" width="600" :open.sync="openAdd">
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
                    <mu-form-item prop="input" label="Образование:">
                        <mu-text-field v-model="form.education"></mu-text-field>
                    </mu-form-item>
                    <mu-select label="Выберите категорию" v-model="form.category" full-width>
                        <mu-option v-for="cat,index in categories" :key="cat" :label="cat" :value="cat"></mu-option>
                    </mu-select>
                    <mu-select label="Выберите специализацию" v-model="form.type" full-width>
                        <mu-option v-for="type,index in types" :key="type" :label="type" :value="type"></mu-option>
                    </mu-select>
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
                    <div @click="loadAppTimes">
                    <mu-select label="Выберите рабочие часы врача" multiple chips v-model="form.work_times" full-width>
                        <mu-option v-for="time,index in app_times" :key="time.id" :label="time.date + ' ' + time.time_start" :value="time"></mu-option>
                    </mu-select>
                    </div>
            </mu-form>
            <mu-button class="btn-send" round color="success" @click="addDoc">Отправить</mu-button>
            <mu-button slot="actions" flat color="primary" @click="closeAddDialog">Закрыть</mu-button>
        </mu-dialog>
        <mu-row>
        <mu-col xl=5>
            <div v-for="doc in doctors">
            <table>
                <tr>
                    <th width=100></th>
                    <th width=300><h3 @click="openSchedule(doc.id)">{{doc.surname}} {{doc.name}} {{doc.patronymic}}</h3></th>
                </tr>
                <tr>
                    <td>Образование</td>
                    <td>{{doc.education}}</td>
                </tr>
                <tr>
                    <td>Специализация</td>
                    <td>{{doc.type}}</td>
                </tr>
                <tr>
                    <td>Категория</td>
                    <td>{{doc.category}}</td>
                </tr>
                <tr>
                    <td>Пол</td>
                    <td>{{doc.sex}}</td>
                </tr>
                <tr>
                    <td>Телефон</td>
                    <td>{{doc.phone}}</td>
                </tr>
                <tr>
                    <td>Почта</td>
                    <td>{{doc.email}}</td>
                </tr>
            </table>
            <br><br>
            </div>
        </mu-col>
        <mu-col xl=6>
        <h3 v-if="isHidden">Актуальный график врача</h3>
            <div v-for="rec in schedules">
            <table width="100%">
                <tr>
                    <th scope="row" align="left">{{rec.app_time.date}}</th>
                    <th scope="row" align="left">{{rec.app_time.time_start}}</th>
                </tr>
            </table>
            </div>
        </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Home from '@/components/Home.vue'

    export default {
        name: 'Doctor',
        components: {
            Home,
        },
        data() {
            return {
                doctors: '',
                categories: ['1', '2', '3'],
                types: ['гинеколог', 'терапевт', 'окулист', 'кардиолог'],
                app_times: '',
                form: {
                    surname: '',
                    name: '',
                    patronymic: '',
                    type: '',
                    category: '',
                    sex: '',
                    phone: '',
                    email: '',
                    work_times: '',
                },
                schedules: '',
                isHidden: false,
                openAdd: false,
            }
        },
        created() {
            $.ajaxSetup({
                  headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
              });
              this.loadDoctor()
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
            loadDoctor() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/doctors/",
                    type: "GET",
                    success: (response) => {
                    this.doctors = response.data.data
                    }
                })
            },
            openSchedule(id) {
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/hospital/schedule/",
                        type: "GET",
                        data: {
                            id: id,
                        },
                        success: (response) => {
                            this.schedules = response.data.data,
                            this.isHidden = true
                        }
                })
            },
            loadAppTimes() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/app_times/",
                    type: "GET",
                    success: (response) => {
                        this.app_times = response.data.data
                    }
                })
            },
            addDoctor() {
            $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/doctors/",
                    type: "POST",
                    data: {
                        surname: this.form.surname,
                        name: this.form.name,
                        patronymic: this.form.patronymic,
                        type: this.form.type,
                        category: this.form.category,
                        sex: this.form.sex,
                        phone: this.form.phone,
                        email: this.form.email,
                        work_times: this.form.work_times
                    },
                    success: (response) => {
                        this.openAdd = false,
                        alert("Данные о враче успешно добавлены"),
                        this.loadDoctor()
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            },
            addDoc() {
                console.log(JSON.stringify(this.form));
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/doctors/",
                    method: "POST",
                    data: {
                        surname: this.form.surname,
                        name: this.form.name,
                        patronymic: this.form.patronymic,
                        type: this.form.type,
                        category: this.form.category,
                        sex: this.form.sex,
                        phone: this.form.phone,
                        email: this.form.email
                    },
                    success: (response) => {

                        this.openAdd = false,
                        alert("Данные о враче успешно добавлены"),
                        this.loadDoctor()
                    },
                    error: (jqXHR, textStatus, errorThrown) => {
                        console.log(textStatus, errorThrown)
                    }
                })
            },
            openAddDialog () {
              this.openAdd = true;
            },
            closeAddDialog () {
              this.openAdd = false;
            },
            }
        }
</script>

<style scoped>

table {
        border-collapse: collapse;
    }
    table th, td{
        padding: 10px;
        border: 1px solid #000;
    }
</style>
