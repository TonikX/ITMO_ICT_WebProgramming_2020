<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Список всех полученных заявок</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col align="left">
                <ul v-for="application in listApp" :key="application.id">
                    <li><a @click="goTo(application.id)">Заявка №{{application.id}}</a>
                        <ul>
                            <li>Абитуриент - {{application.enrollee}}</li>
                            <li>Специальность - {{application.specialty}}</li>
                            <li>Статус заявки - {{application.status}}</li>
                            <mu-radio v-if="isDeleteVisible" v-model="form_delete" :value="application.id"
                                      label="Удалить"></mu-radio>
                        </ul>
                    </li>
                </ul>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button @click="ShowCreate">Добавить заявку</mu-button>
                <mu-button @click="showDelete">Удалить заявку</mu-button>
            </mu-col>
        </mu-row>
        <mu-row v-if="isDeleteVisible">
            <mu-col>
                <br>
                <mu-button color="error" @click="deleteApplication">Подтвердить удаление</mu-button>
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
                    <mu-form-item prop="select" label="Абитуриент">
                        <mu-select v-model="form.enrollee">
                            <mu-option v-for="enrollee in listEnrollee" :key="enrollee.id" :label="enrollee.fio"
                                       :value="enrollee.id"></mu-option>
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
    </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "Application",
        props: ['id'],
        components: {},
        data() {
            return {
                listApp: [],
                listEnrollee: [],
                listSpecialty: [],
                listFaculty: [],
                isDeleteVisible: false,
                isCreateVisible: false,
                form_delete: {},
                form: {
                    date: '',
                    status: '',
                    form_types: '',
                    form: '',
                    enrollee: '',
                    specialty: '',
                    faculty: '',
                },
            }
        },
        created() {
            this.loadListApp()
            this.loadListEnrollee()
            this.loadListFaculty()
            this.loadListSpecialty()
        },
        methods: {
            async loadListApp() {
                this.listApp = await fetch(
                    `http://127.0.0.1:8000/api/v1/application/`
                ).then(response => response.json())
            },
            goTo(id) {
                this.$router.push({name: 'Заявка', params: {id: id}})
            },
            showDelete() {
                this.isDeleteVisible = !this.isDeleteVisible
            },
            async deleteApplication() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/application/${this.form_delete}/delete`, {
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
                await alert('Заявка удалена')
                await this.loadListApp()
                this.isDeleteVisible = !this.isDeleteVisible
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            async loadListEnrollee() {
                this.listEnrollee = await fetch(
                    `http://127.0.0.1:8000/api/v1/enrollee/`
                ).then(response => response.json())
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
                        enrollee: this.form.enrollee,
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
            }

        }
    }
</script>

<style scoped>

</style>