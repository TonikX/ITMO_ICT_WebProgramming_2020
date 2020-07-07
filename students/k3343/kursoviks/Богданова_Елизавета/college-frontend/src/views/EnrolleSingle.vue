<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Абитуриент {{enrollee.id}}</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table>
                    <tr>
                        <td>Фамилия Имя Отчество</td>
                        <td>{{enrollee.fio}}</td>
                    </tr>
                    <tr>
                        <td>Учебное заведение</td>
                        <td>{{enrollee.school}}</td>
                    </tr>
                    <tr>
                        <td>Дата окончания</td>
                        <td>{{enrollee.finish_school}}</td>
                    </tr>
                    <tr>
                        <td>Наличие медали</td>
                        <td>{{enrollee.medal}}</td>
                    </tr>
                    <tr>
                        <td>Серия и номер паспорта</td>
                        <td>{{enrollee.passport_number}}</td>
                    </tr>
                    <tr>
                        <td>Домашний адрес</td>
                        <td>{{enrollee.address}}</td>
                    </tr>
                    <tr>
                        <td>Льготы</td>
                        <td>{{enrollee.privileges}}</td>
                    </tr>
                    <tr>
                        <td>Целевой прием</td>
                        <td>{{enrollee.target}}</td>
                    </tr>
                </table>
                <br>
            </mu-col>

            <mu-col v-if="isAppsVisible">
                <table v-for="app in enrollee.apps" :key="app.id">
                    <tr>
                        <th colspan="2">Заявка №{{app.id}}</th>
                    </tr>
                    <tr>
                        <td>Факультет</td>
                        <td>{{app.faculty}}</td>
                    </tr>
                    <tr>
                        <td>Специальность</td>
                        <td>{{app.specialty}}</td>
                    </tr>
                    <tr>
                        <td>Дата подачи заявки</td>
                        <td>{{app.date}}</td>
                    </tr>
                    <tr>
                        <td>Статус заявки</td>
                        <td>{{app.status}}</td>
                    </tr>
                    <tr>
                        <td>Форма обучения</td>
                        <td>{{app.form_types}}</td>
                    </tr>
                    <tr>
                        <td>Основа обучения</td>
                        <td>{{app.form}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
        <mu-row >
            <mu-col>
                <mu-button @click="deleteEnrollee">Абитуриент забрал документы</mu-button>
                <mu-button @click="ShowUpdateEnrollee">Изменить данные об абитуриенте</mu-button>
                <mu-button @click="showCreateApp">Добавить заявку на поступление</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <br>
                <mu-button @click="ShowAppsEnrollee">Показать заявки</mu-button>
                <br>
                <mu-button href="#/docs">Просмотреть документы</mu-button>
            </mu-col>
        </mu-row>
        <mu-row align="center" v-if="isCreateVisible">
            <mu-col>
                <mu-form style="width: 50%" :model="form" class="mu-demo-form" :label-position="labelPosition"
                         label-width="200">
                    <mu-form-item prop="input" label="Дата регистрации заявки">
                        <mu-text-field v-model="form.date"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Статус заявки">
                        <mu-select v-model="form.status">
                            <mu-option label="Зачислен" value="Зачислен"></mu-option>
                            <mu-option label="В очереди" value="В_очереди"></mu-option>
                            <mu-option label="Не зачислен" value="Не_зачислен"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Форма обучения">
                        <mu-select v-model="form.form_types">
                            <mu-option label="Очная" value="Очная"></mu-option>
                            <mu-option label="Очно-заочная" value="Очно-заочная"></mu-option>
                            <mu-option label="Заочная" value="Заочная"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Основа обучения">
                        <mu-select v-model="form.form">
                            <mu-option label="Бюджет" value="Бюджет"></mu-option>
                            <mu-option label="Контракт" value="Контракт"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Факультет">
                        <mu-select v-model="form.faculty">
                            <mu-option v-for="faculty in listFaculty" :key="faculty.id" :label="faculty.name"
                                       :value="faculty.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Специальность">
                        <mu-select v-model="form.specialty">
                            <mu-option v-for="specialty in listSpecialty" :key="specialty.id" :label="specialty.name"
                                       :value="specialty.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
                <br>
                <mu-button color="secondary" @click="CreateApplication">Внести заявку</mu-button>
            </mu-col>
        </mu-row>
        <mu-row v-if="isUpdateVisible">
            <mu-col>
                <mu-form style="width: 50%" :model="form_update" class="mu-demo-form" :label-position="labelPosition"
                         label-width="200">
                    <mu-form-item prop="input" label="ФИО">
                        <mu-text-field v-model="form_update.fio"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Оконченное учебное заведение">
                        <mu-text-field v-model="form_update.school"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Дата окончания учебного заведения">
                        <mu-text-field v-model="form_update.finish_school"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Медаль">
                        <mu-select v-model="form_update.medal">
                            <mu-option label="Золотая" value="Золотая"></mu-option>
                            <mu-option label="Серебряная" value="Серебряная"></mu-option>
                            <mu-option label="Отсутствует" value="Отсутствует"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Номер паспорта">
                        <mu-text-field v-model="form_update.passport_number"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Адрес">
                        <mu-text-field v-model="form_update.address"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="radio" label="Целевой прием">
                        <mu-radio v-model="form_update.target" value="True"
                                  label="Да"></mu-radio>
                        <mu-radio v-model="form_update.target" value="False"
                                  label="Нет"></mu-radio>
                    </mu-form-item>
                </mu-form>
                <br>
                <mu-button color="secondary" @click="UpdateEnrollee()">Внести изменения</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "EnrolleSingle",
        props: ['id'],
        data() {
            return {
                enrollee: {},
                isCreateVisible: false,
                isUpdateVisible: false,
                isAppsVisible: false,
                form: {
                    date: '',
                    status: '',
                    form_types: '',
                    form: '',
                    specialty: '',
                    faculty: '',
                },
                form_update: {
                    fio: '',
                    school: '',
                    finish_school: '',
                    medal: '',
                    passport_number: '',
                    address: '',
                    privileges: '',
                    target: '',
                }
            }
        },
        created() {
            this.loadEnrollee()
            this.loadListFaculty()
            this.loadListSpecialty()
        },
        methods: {
            async loadEnrollee() {
                this.enrollee = await fetch(
                    `http://127.0.0.1:8000/api/v1/enrollee/${this.id}/`
                ).then(response => response.json())
            },
            async deleteEnrollee() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/enrollee/${this.id}/delete`, {
                        method: 'DELETE',
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        }
                    }
                );
                if (response.status !== 204) {
                    alert(JSON.stringify(await response.json(), null, 2));
                }
                await alert('Абитуриент удален')
                await this.$router.push({name: "Абитуриенты"})
            },
            showCreateApp() {
                this.isCreateVisible = !this.isCreateVisible
            },
            async loadListSpecialty() {
                this.listSpecialty = await fetch(
                    `http://127.0.0.1:8000/api/v1/specialty/`
                ).then(response => response.json())
            },
            async loadListFaculty() {
                this.listFaculty = await fetch(
                    `http://127.0.0.1:8000/api/v1/faculty/`
                ).then(response => response.json())
            },
            CreateApplication() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/application/create",
                    type: "POST",
                    data: {
                        date: this.form.date,
                        status: this.form.status,
                        form: this.form.form,
                        form_types: this.form.form_types,
                        enrollee: this.id,
                        specialty: this.form.specialty,
                        faculty: this.form.faculty,
                    },
                    success: (response) => {
                        this.$router.push({name: "Заявки"})
                        alert("Заявка добавлена")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListApp()
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Данные введены неверно")
                        }
                    }

                })
            },
            ShowUpdateEnrollee() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async UpdateEnrollee() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/enrollee/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_update)
                });
                await alert('Данные об абитуриенте изменены')
                this.isUpdateVisible = !this.isUpdateVisible
                await this.loadEnrollee()
            },
            ShowAppsEnrollee() {
                this.isAppsVisible = !this.isAppsVisible
            },

        }
    }
</script>

<style scoped>

</style>