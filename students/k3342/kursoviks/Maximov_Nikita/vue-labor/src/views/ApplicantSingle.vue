<template>
    <mu-container>
        <mu-row align="left">
            <mu-col>
                <h1>Информация о соискателе</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table width="70%">
                    <tr>
                        <td>ФИО</td>
                        <td>{{applicant.fio}}
                            <mu-form label-position="left" v-if="isUpdateVisible">
                                <mu-form-item prop="input" label="">
                                    <mu-text-field v-model="form_update.fio"></mu-text-field>
                                </mu-form-item>
                            </mu-form>
                        </td>
                    </tr>
                    <tr>
                        <td>Возраст</td>
                        <td>{{applicant.age}}
                            <mu-form label-position="left" v-if="isUpdateVisible">
                                <mu-form-item prop="input" label="">
                                    <mu-text-field v-model="form_update.age"></mu-text-field>
                                </mu-form-item>
                            </mu-form>
                        </td>
                    </tr>
                    <tr>
                        <td>Адрес</td>
                        <td>{{applicant.address}}
                            <mu-form label-position="left" v-if="isUpdateVisible">
                                <mu-form-item prop="input" label="">
                                    <mu-text-field v-model="form_update.address"></mu-text-field>
                                </mu-form-item>
                            </mu-form>
                        </td>
                    </tr>
                    <tr>
                        <td>Образование</td>
                        <td>{{applicant.education}}</td>
                    </tr>
                    <tr>
                        <td>Трудовой стаж</td>
                        <td>{{applicant.work_experience}}
                            <mu-form label-position="left" v-if="isUpdateVisible">
                                <mu-form-item prop="input" label="">
                                    <mu-text-field v-model="form_update.work_experience"></mu-text-field>
                                </mu-form-item>
                            </mu-form>
                        </td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
        <mu-row v-if="isUpdateVisible">
            <mu-col>
                <mu-button @click="UpdateApplicant">Внести изменения</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button @click="ShowResume">Просмотреть резюме</mu-button>
            </mu-col>
            <mu-col>
                <mu-button @click="ShowGratuity">Просмотреть пособия</mu-button>
            </mu-col>
            <mu-col>
                <mu-button @click="ShowCertificate">Просмотреть сертификаты курсов</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col v-if="isResumeVisible" align="center">
                <h2>Имеются резюме</h2>
                <table v-for="resume in applicant.resumes">
                    <tr>
                        <td>ID</td>
                        <td>{{resume.id}}</td>
                    </tr>
                    <tr>
                        <td>Профессия</td>
                        <td>{{resume.profession}}</td>
                    </tr>
                    <tr>
                        <td>Разряд</td>
                        <td>{{resume.rank}}</td>
                    </tr>
                    <tr>
                        <td>Зарплата</td>
                        <td>{{resume.salary}}</td>
                    </tr>
                </table>
                <mu-button @click="ShowCreateResume">Добавить резюме</mu-button>
                <mu-container v-if="isCreateResumeVisible">
                    <mu-form label-position="left">
                        <mu-select v-model="form_resume.profession" label="Профессия">
                            <mu-option v-for="profession in listProfession" :key="profession.id"
                                       :label="profession.name"
                                       :value="profession.id"></mu-option>
                        </mu-select>
                        <mu-form-item prop="input" label="Разряд">
                            <mu-text-field v-model="form_resume.rank"></mu-text-field>
                        </mu-form-item>
                        <mu-form-item prop="input" label="Зарплата">
                            <mu-text-field v-model="form_resume.salary"></mu-text-field>
                        </mu-form-item>
                    </mu-form>
                    <mu-button @click="CreateResume">Добавить</mu-button>
                </mu-container>
            </mu-col>
            <mu-col v-if="isGratuityVisible" align="center">
                <h2>Имеются пособия</h2>
                <table v-for="gratuity in applicant.gratuities">
                    <tr>
                        <td>Сумма выплаты</td>
                        <td>{{gratuity.salary}}</td>
                    </tr>
                    <tr>
                        <td>Дата начала выплаты пособия</td>
                        <td>{{gratuity.date_start}}</td>
                    </tr>
                    <tr>
                        <td>Дата окончания выплаты пособия</td>
                        <td>{{gratuity.date_end}}</td>
                    </tr>
                </table>
            </mu-col>
            <mu-col v-if="isCertificateVisible" align="center">
                <h2>Имеются сертификаты</h2>
                <table v-for="courses_certificate in applicant.courses_certificates">
                    <tr>
                        <td>Название курса</td>
                        <td>{{courses_certificate.course}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button @click="ShowUpdate">Изменить информацию</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "ApplicantSingle",
        props: ['id'],
        data() {
            return {
                applicant: {},
                isUpdateVisible: false,
                isResumeVisible: false,
                isCreateResumeVisible: false,
                isGratuityVisible: false,
                isCertificateVisible: false,
                listProfession: [],
                form_update: {
                    address: '',
                    age: '',
                    work_experience: '',
                    fio: '',
                },
                form_resume: {
                    salary: '',
                    rank: '',
                    profession: '',
                    applicant: '',
                },
            }
        },
        created() {
            this.loadApplicant()
            this.loadListProfession()
        },
        methods: {
            async loadApplicant() {
                this.applicant = await fetch(
                    `http://127.0.0.1:8000/api/v1/applicant/${this.id}/`
                ).then(response => response.json())
            },
            async loadListProfession() {
                this.listProfession = await fetch(
                    `http://127.0.0.1:8000/api/v1/profession`
                ).then(response => response.json())
            },
            ShowUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            ShowResume() {
                this.isResumeVisible = !this.isResumeVisible
            },
            ShowGratuity() {
                this.isGratuityVisible = !this.isGratuityVisible
            },
            ShowCertificate() {
                this.isCertificateVisible = !this.isCertificateVisible
            },
            async UpdateApplicant() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/applicant/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_update)
                });
                await alert('Данные о соискателе успешно изменены')
                this.isUpdateVisible = !this.isUpdateVisible
                await this.loadApplicant()
            },
            ShowCreateResume() {
                this.isCreateResumeVisible = !this.isCreateResumeVisible
            },
            CreateResume() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/resume/create",
                    type: "POST",
                    data: {
                        profession: this.form_resume.profession,
                        rank: this.form_resume.rank,
                        salary: this.form_resume.salary,
                        applicant: this.id,
                    },
                    success: (response) => {
                        alert("Резюме успешно добавлено")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadApplicant()
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