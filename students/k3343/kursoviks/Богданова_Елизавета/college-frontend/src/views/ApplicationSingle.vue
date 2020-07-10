<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>Заявка №{{application.id}}</h1>
                <table align="left">
                    <tr>
                        <td>Статус</td>
                        <td>{{application.status}}</td>
                    </tr>
                    <tr>
                        <td>ФИО абитуриента</td>
                        <td>{{application.enrollee}}</td>
                    </tr>
                    <tr>
                        <td>Факультет</td>
                        <td>{{application.faculty}}</td>
                    </tr>
                    <tr>
                        <td>Специальность</td>
                        <td>{{application.specialty}}</td>
                    </tr>
                    <tr>
                        <td>Форма обучения</td>
                        <td>{{application.form_types}}</td>
                    </tr>
                    <tr>
                        <td>Бюджет/Контракт</td>
                        <td>{{application.form}}</td>
                    </tr>
                    <tr>
                        <td>Дата подачи заявки</td>
                        <td>{{application.date}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>

        <mu-row>
            <mu-col>
                                <mu-button @click="deleteApplication">Удалить заявку</mu-button>
                                <mu-button @click="ShowUpdateApp">Изменить заявку</mu-button>
            </mu-col>
        </mu-row>        <mu-row v-if="isUpdateVisible">
            <mu-col>
                <mu-form style="width: 50%" :model="form_update" class="mu-demo-form" :label-position="labelPosition"
                         label-width="200">

                    <mu-form-item prop="input" label="Дата регистрации заявки">
                        <mu-text-field v-model="form_update.date"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Статус заявки">
                        <mu-select v-model="form_update.status">
                            <mu-option label="Зачислен" value="Зачислен"></mu-option>
                            <mu-option label="В очереди" value="В_очереди"></mu-option>
                            <mu-option label="Не зачислен" value="Не_зачислен"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Форма обучения">
                        <mu-select v-model="form_update.form_types">
                            <mu-option label="Очная" value="Очная"></mu-option>
                            <mu-option label="Очно-заочная" value="Очно-заочная"></mu-option>
                            <mu-option label="Заочная" value="Заочная"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Основа обучения">
                        <mu-select v-model="form_update.form">
                            <mu-option label="Бюджет" value="Бюджет"></mu-option>
                            <mu-option label="Контракт" value="Контракт"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
                <br>
                <mu-button color="secondary" @click="UpdateApp()">Внести изменения</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "ApplicationSingle",
        props: ['id'],
        data() {
            return {
                application: {},
                isUpdateVisible: false,
                form_update: {
                    date: '',
                    status: '',
                    form_types: '',
                    form: '',
                }
            }
        },
        created() {
            this.loadApplication()
        },
        methods: {
            async loadApplication() {
                this.application = await fetch(
                    `http://127.0.0.1:8000/api/v1/application/${this.id}`
                ).then(response => response.json())
            },
            async deleteApplication() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/application/${this.id}/delete`, {
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
                await this.$router.push({name: "Заявки"})
            },
            ShowUpdateApp() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async UpdateApp() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/application/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_update)
                });
                await alert('Заявка успешно изменена')
                this.isUpdateVisible = false
                await this.loadApplication()
            },

        }
    }
</script>

<style scoped>

</style>