<template>
    <mu-container>
        <mu-row align="left">
            <mu-col>
                <h1>Каталог вакансий</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-select v-model="form_filter.profession" label="Профессия">
                    <mu-option v-for="profession in listProfession" :key="profession.id" :label="profession.name"
                               :value="profession.id"></mu-option>
                    <mu-option label="        " value=""></mu-option>
                </mu-select>
            </mu-col>
            <mu-col>
                <mu-select v-model="form_filter.education" label="Образование">
                    <mu-option v-for="education in listEducation" :key="education.id" :label="education.name"
                               :value="education.id"></mu-option>
                    <mu-option label="        " value=""></mu-option>
                </mu-select>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-select v-model="form_filter.types" label="Тип работы">
                    <mu-option value="Стажировка" label="Стажировка"></mu-option>
                    <mu-option value="Постоянная" label="Постоянная"></mu-option>
                    <mu-option value="Временная" label="Временная"></mu-option>
                    <mu-option value="Сезонная" label="Сезонная"></mu-option>
                    <mu-option value="Дистанционная" label="Дистанционная"></mu-option>
                </mu-select>
            </mu-col>
            <mu-col>
                <mu-select v-model="form_filter.status" label="Статус вакансии">
                    <mu-option value="Открыта" label="Открыта"></mu-option>
                    <mu-option value="Закрыта" label="Закрыта"></mu-option>
                </mu-select>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <p>Опыт работы в годах</p>
                <br>
                <mu-form label-position="left">
                    <mu-form-item style="width: 50%;" prop="input" label="От">
                        <mu-text-field v-model="form_filter.work_experience_min"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item style="width: 50%;" prop="input" label="До">
                        <mu-text-field v-model="form_filter.work_experience_max"></mu-text-field>
                    </mu-form-item>
                </mu-form>
            </mu-col>
            <mu-col>
                <p>Зарплата</p>
                <br>
                <mu-form label-position="left">
                    <mu-form-item style="width: 50%;" prop="input" label="От">
                        <mu-text-field v-model="form_filter.salary_min"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item style="width: 50%;" prop="input" label="До">
                        <mu-text-field v-model="form_filter.salary_max"></mu-text-field>
                    </mu-form-item>
                </mu-form>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <mu-button full-width style="width: 80%;" color="#b5bdc4" @click="Filter">Отфильтровать</mu-button>
            </mu-col>
            <mu-col>
                <mu-button full-width style="width: 80%;" color="#b5bdc4" @click="FilterReset">Сбросить фильтры</mu-button>
            </mu-col>
        </mu-row>
        <br>
        <br>
        <mu-row v-for="vacancy in listVacancy" :key="vacancy.id" align="center">
            <mu-col>
                <table width="50%">
                    <tr>
                        <td colspan="2"><a @click="goTo(vacancy.id)">{{vacancy.profession}}</a></td>
                    </tr>
                    <tr>
                        <td>Разряд</td>
                        <td>{{vacancy.rank}}</td>
                    </tr>
                    <tr>
                        <td>Образование</td>
                        <td>{{vacancy.education}}</td>
                    </tr>
                    <tr>
                        <td>Опыт работы в годах</td>
                        <td>{{vacancy.work_experience}}</td>
                    </tr>
                    <tr>
                        <td>Тип работы</td>
                        <td>{{vacancy.type}}</td>
                    </tr>
                    <tr>
                        <td>Работодатель</td>
                        <td>{{vacancy.employer}}</td>
                    </tr>
                    <tr>
                        <td>Зарплата</td>
                        <td>{{vacancy.salary}}</td>
                    </tr>
                    <tr>
                        <td>Статус вакансии</td>
                        <td>{{vacancy.status}}</td>
                    </tr>
                </table>
                <br>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col v-if="isCreateVisible">
                <mu-form>
                    <mu-select v-model="form.employer" label="Работодатель">
                        <mu-option v-for="employer in listEmployer" :key="employer.id" :label="employer.name"
                                   :value="employer.id"></mu-option>
                    </mu-select>
                    <mu-select v-model="form.profession" label="Профессия">
                        <mu-option v-for="profession in listProfession" :key="profession.id" :label="profession.name"
                                   :value="profession.id"></mu-option>
                    </mu-select>
                    <mu-select v-model="form.education" label="Образование">
                        <mu-option v-for="education in listEducation" :key="education.id" :label="education.name"
                                   :value="education.id"></mu-option>
                    </mu-select>
                    <mu-select v-model="form.type" label="Тип работы">
                        <mu-option value="Стажировка" label="Стажировка"></mu-option>
                        <mu-option value="Постоянная" label="Постоянная"></mu-option>
                        <mu-option value="Временная" label="Временная"></mu-option>
                        <mu-option value="Сезонная" label="Сезонная"></mu-option>
                        <mu-option value="Дистанционная" label="Дистанционная"></mu-option>
                    </mu-select>
                    <mu-select v-model="form.status" label="Статус вакансии">
                        <mu-option value="Открыта" label="Открыта"></mu-option>
                        <mu-option value="Закрыта" label="Закрыта"></mu-option>
                    </mu-select>
                    <mu-form-item prop="input" label="Разряд">
                        <mu-text-field v-model="form.rank"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Зарплата">
                        <mu-text-field v-model="form.salary"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Опыт работы в годах">
                        <mu-text-field v-model="form.work_experience"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Дата подачи заявки ГГГГ-ММ-ДД">
                        <mu-text-field v-model="form.date"></mu-text-field>
                    </mu-form-item>
                </mu-form>
                <mu-button @click="CreateVacancy">Добавить</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button full-width style="width: 50%;" color="#b5bdc4" @click="ShowCreate">Добавить новую вакансию</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Vacancy",
        props: ['id'],
        components: {},
        data() {
            return {
                listVacancy: [],
                listProfession: [],
                listEducation: [],
                listEmployer: [],
                isCreateVisible: false,
                isInfoVisible: false,
                form: {
                    status: '',
                    date: '',
                    salary: '',
                    type: '',
                    work_experience: '',
                    rank: '',
                    education: '',
                    employer: '',
                    profession: '',
                },
                form_filter: {
                    status: '',
                    education: '',
                    profession: '',
                    types: '',
                    work_experience_min: '',
                    work_experience_max: '',
                    salary_min: '',
                    salary_max: '',
                },
            }
        },
        created() {
            this.loadListVacancy()
            this.loadListVacancyFull()
            this.loadListEducation()
            this.loadListProfession()
            this.loadListEmployer()
        },
        methods: {
            async loadListVacancy() {
                this.listVacancy = await fetch(
                    `http://127.0.0.1:8000/api/v1/vacancy/?profession=${this.form_filter.profession}&status=${this.form_filter.status}&education=${this.form_filter.education}&types=${this.form_filter.types}&work_experience_min=${this.form_filter.work_experience_min}&work_experience_max=${this.form_filter.work_experience_max}&salary_min=${this.form_filter.salary_min}&salary_max=${this.form_filter.salary_max}`
                ).then(response => response.json())
            },
            async loadListProfession() {
                this.listProfession = await fetch(
                    `http://127.0.0.1:8000/api/v1/profession`
                ).then(response => response.json())
            },
            async loadListEducation() {
                this.listEducation = await fetch(
                    `http://127.0.0.1:8000/api/v1/education/`
                ).then(response => response.json())
            },
            async loadListVacancyFull() {
                this.listVacancy = await fetch(
                    `http://127.0.0.1:8000/api/v1/vacancy/`
                ).then(response => response.json())
            },
            async loadListEmployer() {
                this.listEmployer = await fetch(
                    `http://127.0.0.1:8000/api/v1/employer/`
                ).then(response => response.json())
            },
            Filter() {
                this.loadListVacancy()
            },
            FilterReset() {
                this.loadListVacancyFull()
            },
            goTo(id) {
                this.$router.push({name: 'Вакансия', params: {id: id}})
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            CreateVacancy() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/vacancy/create",
                    type: "POST",
                    data: {
                        status: this.form.status,
                        date: this.form.date,
                        salary: this.form.salary,
                        type: this.form.type,
                        work_experience: this.form.work_experience,
                        rank: this.form.rank,
                        education: this.form.education,
                        employer: this.form.employer,
                        profession: this.form.profession,
                    },
                    success: (response) => {
                        this.$router.push({name: "Вакансии"})
                        alert("Вакансия успешно добавлена")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListVacancy()
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