<template>
    <mu-container>
        <mu-row align="left">
            <mu-col>
                <h1>Профессиональное обучение</h1>
                <h2>Курсы</h2>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col>
                <mu-select v-model="form_filter.profession" style="width: 50%;" label="Фильтр по профессиям" full-width>
                    <mu-option v-for="profession in listProfession" :key="profession.id" :label="profession.name"
                               :value="profession.id"></mu-option>
                    <mu-option label="        " value=""></mu-option>
                </mu-select>
                <br>
                <mu-button @click="Filter">Отфильтровать</mu-button>
                <br><br><br>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-container width="90%" bgcolor="red" align="center" v-for="course in listCourse" :key="course.id">
                    <h2>Курс №{{course.id}} {{course.name}}</h2>
                    <table v-if="isInfoVisible" width="70%">
                        <tr>
                            <td>Профессия</td>
                            <td>{{course.profession}}</td>
                        </tr>
                        <tr>
                            <td>Разряд</td>
                            <td>{{course.rank}}</td>
                        </tr>
                        <tr>
                            <td>Продолжительность курса в месяцах</td>
                            <td>{{course.lasting}}</td>
                        </tr>
                        <tr>
                            <td>Курc проводит</td>
                            <td>{{course.author}}</td>
                        </tr>
                    </table>
                </mu-container>
            </mu-col>
            <mu-col v-if="isCountVisible">
                <br>
                <br>
                <table>
                        <tr>
                            <th>Курс</th>
                            <th>Количество записавшихся</th>
                        </tr>
                        <tr v-for="count_course in count_course.result">
                            <td>Курс №{{count_course.course}}</td>
                            <td>{{count_course.applicant__count}}</td>
                        </tr>
                    </table>
            </mu-col>
            <mu-col v-if="isCreateVisible">
                <mu-form>
                    <mu-form-item prop="select" label="Выберите курс">
                        <mu-select v-model="form.course">
                            <mu-option v-for="course in listCourse" :key="course.id" :label="course.name"
                                       :value="course.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Выберите соискателя">
                        <mu-select v-model="form.applicant">
                            <mu-option v-for="applicant in listApplicant" :key="applicant.id" :label="applicant.fio"
                                       :value="applicant.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
                <mu-button @click="CreateCourseReg">Записать на курс</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button @click="ShowCourseInfo">Подробная информация о курсах</mu-button>
            </mu-col>
            <mu-col>
                <mu-button @click="ShowCreate">Записать соискателя на курс</mu-button>
            </mu-col>
            <mu-col>
                <mu-button @click="ShowCount">Количество соискателей на каждом курсе</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Course",
        props: ['id'],
        components: {},
        data() {
            return {
                listCourse: [],
                listApplicant: [],
                listProfession: [],
                isCreateVisible: false,
                isInfoVisible: false,
                isCountVisible: false,
                form: {
                    course: '',
                    applicant: '',
                },
                form_filter:{
                    profession: '',
                },
                count_course: {
                    result: []
                },
            }
        },
        created() {
            this.loadListCourse()
            this.loadListApplicant()
            this.loadListProfession()
            this.CountCourse()
        },
        methods: {
            async loadListCourse() {
                this.listCourse = await fetch(
                    `http://127.0.0.1:8000/api/v1/course/?profession=${this.form_filter.profession}`
                ).then(response => response.json())
            },
            async loadListProfession() {
                this.listProfession = await fetch(
                    `http://127.0.0.1:8000/api/v1/profession`
                ).then(response => response.json())
            },
            Filter(){
                this.loadListCourse()
            },
            ShowCourseInfo() {
                this.isInfoVisible = !this.isInfoVisible
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            ShowCount() {
                this.isCountVisible = !this.isCountVisible
            },
            async loadListApplicant() {
                this.listApplicant = await fetch(
                    `http://127.0.0.1:8000/api/v1/applicant/`
                ).then(response => response.json())
            },
            async CountCourse() {
                this.count_course = await fetch(
                    `http://127.0.0.1:8000/api/v1/count_course/`
                ).then(response => response.json())
            },
            CreateCourseReg() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/course_certificate/create",
                    type: "POST",
                    data: {

                        course: this.form.course,
                        applicant: this.form.applicant,
                    },
                    success: (response) => {
                        this.$router.push({name: "Курсы"})
                        alert("Соискатель записан на курс")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListCourse()
                        this.CountCourse()
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Данные введены неверно")
                        }
                    }

                })
            }

        }
    }
</script>

<style scoped>

</style>