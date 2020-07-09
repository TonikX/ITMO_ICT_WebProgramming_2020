<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Запросы к курсовой работе</h1>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col span="10">
                <ol class="ball">
                    <li><a @click="showQuery1">Запрос №1</a>
                        <p>Какой предмет будет в заданном классе, в заданный день недели на заданном уроке?</p>
                        <p v-if="isQuery1Vis">Пожалуйста, выберите данные для выполнения запроса</p>
                        <mu-form v-if="isQuery1Vis" :model="form_query1" class="mu-demo-form"
                                 :label-position="labelPosition" label-width="100">
                            <mu-form-item prop="radio" label="День недели">
                                <mu-radio v-model="form_query1.day" value="Понедельник" label="Понедельник"></mu-radio>
                                <mu-radio v-model="form_query1.day" value="Вторник" label="Вторник"></mu-radio>
                                <mu-radio v-model="form_query1.day" value="Среда" label="Среда"></mu-radio>
                                <mu-radio v-model="form_query1.day" value="Четверг" label="Четверг"></mu-radio>
                                <mu-radio v-model="form_query1.day" value="Пятница" label="Пятница"></mu-radio>
                                <mu-radio v-model="form_query1.day" value="Суббота" label="Суббота"></mu-radio>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Урок">
                                <mu-select v-model="form_query1.lesson">
                                    <mu-option label="1-8:00-8:45" value="1-8:00-8:45">1-8:00-8:45</mu-option>
                                    <mu-option label="2-8:50-9:35" value="2-8:50-9:35">2-8:50-9:35</mu-option>
                                    <mu-option label="3-9:40-10:25" value="3-9:40-10:25">3-9:40-10:25</mu-option>
                                    <mu-option label="4-10:40-11:25" value="4-10:40-11:25">4-10:40-11:25</mu-option>
                                    <mu-option label="5-11:30-12:15" value="5-11:30-12:15">5-11:30-12:15</mu-option>
                                    <mu-option label="6-12:20-13:05" value="6-12:20-13:05">6-12:20-13:05</mu-option>
                                    <mu-option label="7-13:05-13:50" value="7-13:05-13:50">7-13:05-13:50</mu-option>
                                    <mu-option label="8-14:00-14:45" value="8-14:00-14:45">8-14:00-14:45</mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="select" label="Класс">
                                <mu-select v-model="form_query1.klass_name">
                                    <mu-option v-for="klass in listKlass" :key="klass.id"
                                               :label="klass.number+klass.litera"
                                               :value="klass.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                        </mu-form>
                        <mu-button v-if="isQuery1Vis" color="primary" @click="Query1">Выполнить запрос</mu-button>
                        <p v-if="isQuery1ResultVis">Результат выполнения запроса</p>
                        <table v-if="isQuery1ResultVis" class="table-fill">
                            <thead>
                            <tr>
                                <th colspan="2" class="text-center"></th>
                            </tr>
                            </thead>
                            <tbody class="table-hover">
                            <tr v-for="a, b in query1">
                                <td class="text-left">{{a}}</td>
                                <td class="text-left">{{b}}</td>
                            </tr>
                            </tbody>
                        </table>
                    </li>
                    <li><a @click="showQuery2">Запрос №2</a>
                        <p>Сколько учителей преподает каждую из дисциплин в школе?</p>
                        <table v-if="isQuery2Vis" class="table-fill">
                            <thead>
                            <tr>
                                <th colspan="2" class="text-center">Результат выполнения запроса</th>
                            </tr>
                            </thead>
                            <tbody class="table-hover">
                            <tr>
                                <td class="text-left">Предмет</td>
                                <td class="text-left">Количество учителей</td>
                            </tr>
                            <tr v-for="subject,counter in query2">
                                <td class="text-left">{{counter}}</td>
                                <td class="text-left">{{subject}}</td>
                            </tr>
                            </tbody>
                        </table>
                    </li>
                    <li><a @click="showQuery3">Запрос №3</a>
                        <p>Список учителей, преподающих те же предметы, что и учитель, ведущий информатику в заданном
                            классе.</p>
                        <mu-form v-if="isQuery3Vis" :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">

                            <mu-form-item prop="select" label="Класс">
                                <mu-select v-model="form.klass_name">
                                    <mu-option v-for="klass in listKlass" :key="klass.id"
                                               :label="klass.number+klass.litera"
                                               :value="klass.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="select" label="Предмет">
                                <mu-select v-model="form.subject">
                                    <mu-option v-for="subject in listSubject" :key="subject.id" :label="subject.subject"
                                               :value="subject.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                        </mu-form>
                        <mu-button v-if="isQuery3Vis" color="primary" @click="Query3">Выполнить запрос</mu-button>
                        <p v-if="isQuery3ResultVis">Результат выполнения запроса</p>
                        <p v-if="isQuery3ResultVis" v-for="result in query3">{{result}}</p>

                    </li>
                    <li><a @click="showQuery4">Запрос №4</a>
                        <p>Сколько мальчиков и девочек в каждом классе?</p>
                        <table v-if="isQuery4Vis" class="table-fill">
                            <thead>
                            <tr>
                                <th colspan="3" class="text-center">Результат выполнения запроса</th>
                            </tr>
                            </thead>
                            <tbody class="table-hover">
                            <tr>
                                <td class="text-left">Класс</td>
                                <td class="text-left">Пол</td>
                                <td class="text-left">Количество учеников</td>
                            </tr>
                            <tr v-for="object in query4">
                                <td class="text-left">{{object.klass}}</td>
                                <td class="text-left">{{object.gender}}</td>
                                <td class="text-left">{{object.gender__count}}</td>
                            </tr>
                            </tbody>
                        </table>
                    </li>
                    <li><a @click="showQuery5">Запрос №5</a>
                        <p>Сколько кабинетов в школе для базовых и профильных дисциплин?</p>
                        <table v-if="isQuery5Vis" class="table-fill">
                            <thead>
                            <tr>
                                <th colspan="2" class="text-center">Результат выполнения запроса</th>
                            </tr>
                            </thead>
                            <tbody class="table-hover">
                            <tr>
                                <td class="text-left">Тип кабинета</td>
                                <td class="text-left">Количество кабинетов</td>
                            </tr>
                            <tr v-for="profile,counter in query5">
                                <td class="text-left">{{counter}}</td>
                                <td class="text-left">{{profile}}</td>
                            </tr>
                            </tbody>
                        </table>
                    </li>
                </ol>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Queries",
        data() {
            return {
                isQuery1Vis: false,
                isQuery1ResultVis: false,
                isQuery2Vis: false,
                isQuery3Vis: false,
                isQuery3ResultVis: false,
                isQuery4Vis: false,
                isQuery5Vis: false,
                listKlass: [],
                listSubject: [],
                form_query1: {
                    day: '',
                    klass_name: '',
                    lesson: '',
                },
                form: {
                    klass_name: '',
                    subject_name: '',
                },
                query1: '',
                query2: '',
                query3: '',
                query4: '',
                query5: '',
            }

        },
        created() {
            this.loadListKlass()
            this.loadListSubject()
        },
        methods: {
            showQuery1() {
                this.isQuery1Vis = !this.isQuery1Vis;
            },
            async loadListKlass() {
                this.listKlass = await fetch(
                    `${this.$store.getters.getServerUrl}/klass`
                ).then(response => response.json())
            },
            async loadListSubject() {
                this.listSubject = await fetch(
                    `${this.$store.getters.getServerUrl}/subject`
                ).then(response => response.json())
            },
            Query1() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/query1/",
                    type: "GET",
                    data: {
                        day: this.form_query1.day,
                        klass: this.form_query1.klass_name,
                        lesson: this.form_query1.lesson,
                    },
                    success: (response) => {
                        this.query1 = response.data
                        this.isQuery1ResultVis = !this.isQuery1ResultVis
                        console.log(this.query1)
                    }
                })
            },
            showQuery2() {
                this.isQuery2Vis = !this.isQuery2Vis;
                this.Query2()
            },
            Query2() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/query2/",
                    type: "GET",
                    success: (response) => {
                        this.query2 = response.data
                        console.log(this.query2)
                    }
                })
            },
            showQuery3() {
                this.isQuery3Vis = !this.isQuery3Vis;
            },
            Query3() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/query3/",
                    type: "GET",
                    data: {
                        klass: this.form.klass_name,
                        subject: this.form.subject,
                    },
                    success: (response) => {
                        this.query3 = response.data
                        this.isQuery3ResultVis = !this.isQuery3ResultVis
                        console.log(this.query1)
                    }
                })
            },
            showQuery4() {
                this.isQuery4Vis = !this.isQuery4Vis;
                this.Query4()
            },
            Query4() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/query4/",
                    type: "GET",
                    success: (response) => {
                        this.query4 = response.data
                        console.log(this.query4)
                    }
                })
            },
            showQuery5() {
                this.isQuery5Vis = !this.isQuery5Vis;
                this.Query5()
            },
            Query5() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/query5/",
                    type: "GET",
                    success: (response) => {
                        this.query5 = response.data
                        console.log(this.query5)
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>