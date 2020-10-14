<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>Вакансия №{{vacancy.id}}</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table width="70%">
                    <tr>
                        <td>Должность</td>
                        <td>{{vacancy.profession}}</td>
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
                        <td><a @click="goToEmployer(vacancy.id)">{{vacancy.employer}}</a></td>
                    </tr>
                    <tr>
                        <td>Зарплата</td>
                        <td>{{vacancy.salary}}
                            <mu-form label-position="left" v-if="isUpdateVisible">
                                <mu-form-item prop="input" label="">
                                    <mu-text-field v-model="form_update.salary"></mu-text-field>
                                </mu-form-item>
                            </mu-form>
                        </td>
                    </tr>
                    <tr>
                        <td>Статус вакансии</td>
                        <td>{{vacancy.status}}<br>
                            <mu-select v-model="form_update.status" label="Статус вакансии" v-if="isUpdateVisible">
                                <mu-option value="Открыта" label="Открыта"></mu-option>
                                <mu-option value="Закрыта" label="Закрыта"></mu-option>
                            </mu-select>
                        </td>
                    </tr>
                    <tr>
                        <td>Дата размещения вакансии</td>
                        <td>{{vacancy.date}}</td>
                    </tr>
                </table>
                <br>
            </mu-col>
            <mu-col v-if="isCreateApplicationVisible">
                <mu-form label-position="left">
                        <mu-select v-model="form_create_app.resume" label="Резюме">
                            <mu-option v-for="resume in listResume" :key="resume.id"
                                       :label="resume.applicant +  resume.profession"
                                       :value="resume.id"></mu-option>
                        </mu-select>
                    <mu-select v-model="form_create_app.status" label="Статус заявки">
                        <mu-option value="Одобрена" label="Одобрена"></mu-option>
                        <mu-option value="В_процесе" label="В процесе"></mu-option>
                        <mu-option value="Отклонена" label="Отклонена"></mu-option>
                    </mu-select>
                        <mu-form-item prop="input" label="Дата подачи заявки ГГГГ-ММ-ДД">
                            <mu-text-field v-model="form_create_app.date"></mu-text-field>
                        </mu-form-item>
                </mu-form>
                <mu-button @click="CreateApplication">Подтвердить</mu-button>
            </mu-col>
        </mu-row>
        <mu-row v-if="isUpdateVisible">
            <mu-col>
                <mu-button @click="UpdateVacancy">Внести изменения</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button @click="ShowUpdate">Изменить информацию</mu-button>
            </mu-col>
            <mu-col>
                <mu-button @click="ShowCreateApplication">Подать заявку</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "VacancySingle",
        props: ['id'],
        data() {
            return {
                vacancy: {},
                listResume: [],
                isUpdateVisible: false,
                isCreateApplicationVisible: false,
                form_update: {
                    status: '',
                    salary: '',
                },
                form_create_app: {
                    status: '',
                    resume: '',
                    date: '',
                    vacancy: '',
                }
            }
        },
        created() {
            this.loadVacancy()
            this.loadListResume()
        },
        methods: {
            async loadVacancy() {
                this.vacancy = await fetch(
                    `http://127.0.0.1:8000/api/v1/vacancy/${this.id}/`
                ).then(response => response.json())
            },
            async loadListResume() {
                this.listResume = await fetch(
                    `http://127.0.0.1:8000/api/v1/resume`
                ).then(response => response.json())
            },
            goToEmployer() {
                this.$router.push({name: 'Работодатели'})
            },
            ShowUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            ShowCreateApplication() {
                this.isCreateApplicationVisible = !this.isCreateApplicationVisible
            },
            async UpdateVacancy() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/vacancy/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_update)
                });
                await alert('Данные о вакансии успешно изменены')
                this.isUpdateVisible = !this.isUpdateVisible
                await this.loadVacancy()
            },
            CreateApplication() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/application/create",
                    type: "POST",
                    data: {
                        status: this.form_create_app.status,
                        date: this.form_create_app.date,
                        resume: this.form_create_app.resume,
                        vacancy: this.id,
                    },
                    success: (response) => {
                        alert("Заявка создана")
                        this.isCreateApplicationVisible = !this.isCreateApplicationVisible
                        this.loadVacancy()
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