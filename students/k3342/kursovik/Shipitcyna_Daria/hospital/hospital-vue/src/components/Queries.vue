<template>
    <mu-container>
        <Home></Home>
        <mu-col v-if="auth">
        <mu-col>
            <h1>Запросы</h1>
        </mu-col>
        <mu-col>
            <h3>Запрос 1</h3>
            <p>Количество приемов у каждого врача</p>
            <div align='center'>
            <table>
                <tr>
                    <th>Фамилия врача</th>
                    <th>Количество</th>
                </tr>
                <tr v-for="rec in query_1">
                    <td width=500>{{rec.record__doctor__surname}}</td>
                    <td width=100>{{rec.amount}}</td>
                </tr>
            </table>
            </div>
        </mu-col>
         <mu-col align='center'>
            <h3>Запрос 2</h3>
            <p>Количество врачей каждой специализации</p>
            <table>
                <tr>
                    <th>Специализация</th>
                    <th>Количество</th>
                </tr>
                <tr v-for="rec in query_2">
                    <td width=500>{{rec.type}}</td>
                    <td width=100>{{rec.amount}}</td>
                </tr>
            </table>
        </mu-col>
         <mu-col>
            <h3>Запрос 3</h3>
            <p>Сумма стоимостей всех приемов у каждого врача</p>
            <div align='center'>
            <table>
                <tr>
                    <th>Фамилия врача</th>
                    <th>Сумма</th>
                </tr>
                <tr v-for="rec in query_3">
                    <td width=500>{{rec.record__doctor__surname}}</td>
                    <td width=100>{{rec.amount}}</td>
                </tr>
            </table>
            </div>
        </mu-col>
         <mu-col>
            <h3>Запрос 4</h3>
            <p>Количество приемов у выбранного врача по дате</p>
            <div>
            <input v-model="filter.doctor" placeholder="Фамилия врача"></input>
            <input v-model="filter.date" placeholder="Дата приема"></input>
            <mu-button small color="success" @click="query4">Найти</mu-button>
            </div>
            <div v-for="rec in query_4" align='center'>
            <table>
                <tr>
                    <td width=350>{{rec.record__doctor__surname}}</td>
                    <td width=150>{{rec.record__app_time__date}}</td>
                    <td width=100>{{rec.amount}}</td>
                </tr>
            </table>
            </div>
        </mu-col>
        <mu-col>
            <h2>Отчет по выручке</h2>
            <p>Общая выручка за выбранный период</p>
            <div>
            <input v-model="filter.date_start" placeholder="Начало периода"></input>
            <input v-model="filter.date_end" placeholder="Конец периода"></input>
            <mu-button small color="success" @click="report_cash">Найти</mu-button>
            </div>
            <div v-for="rec in report">
                <p>Выручка за период с {{filter.date_start}} по {{filter.date_end}} составила <b>{{rec.amount}}</b> рублей</p>
            </div>
        </mu-col>
        </mu-col>
        <mu-col v-else>
            <h1>Вы не авторизованы!</h1>
            <p>Для просмотра этого контента вам необходимо авторизоваться или зарегистрироваться</p>
            <mu-button color="success" @click="goLogin">Войти</mu-button>
        </mu-col>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Home from '@/components/Home.vue'

    export default {
        name: 'Queries',
        components: {
            Home,
        },
        data() {
            return {
                query_1: '',
                query_2: '',
                query_3: '',
                query_4: '',
                report: '',
                filter: {
                    date: '',
                    doctor: '',
                    date_start: '',
                    date_end: ''
                }
        }},
        created() {
            $.ajaxSetup({
                  headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
              });
              this.query1(),
              this.query2(),
              this.query3()
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
            query1() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/query_1/",
                    type: "GET",
                    success: (response) => {
                    this.query_1 = response.data.data
                    }
                })
            },
            query2() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/query_2/",
                    type: "GET",
                    success: (response) => {
                    this.query_2 = response.data.data
                    }
                })
            },
            query3() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/query_3/",
                    type: "GET",
                    success: (response) => {
                    this.query_3 = response.data.data
                    }
                })
            },
            query4() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/query_4/",
                    type: "GET",
                    data: {
                        date: this.filter.date,
                        doctor: this.filter.doctor
                    },
                    success: (response) => {
                    this.query_4 = response.data.data
                    }
                })
            },
            report_cash() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/report/",
                    type: "GET",
                    data: {
                        date_start: this.filter.date_start,
                        date_end: this.filter.date_end
                    },
                    success: (response) => {
                    this.report = response.data.data
                    }
                })
            }
        }
    }
</script>

<style scoped>
table {
        border-collapse: collapse;
    }
    table td {
        padding: 10px;
        border: 1px solid #000;
    }
</style>
