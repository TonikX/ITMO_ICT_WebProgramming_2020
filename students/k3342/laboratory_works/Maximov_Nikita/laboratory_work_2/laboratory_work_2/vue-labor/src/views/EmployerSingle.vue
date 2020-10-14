<template>
    <mu-container>
        <mu-row align="left">
            <mu-col>
                <h1>Информация о работодателе</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <table>
                    <tr>
                        <td>Название компании</td>
                        <td>{{employer.name}}
                            <mu-form label-position="left" v-if="isUpdateVisible">
                                <mu-form-item prop="input" label="">
                                    <mu-text-field v-model="form_update.name"></mu-text-field>
                                </mu-form-item>
                            </mu-form>
                        </td>
                    </tr>
                    <tr>
                        <td>Руководитель компании</td>
                        <td>{{employer.contact}}
                            <mu-form label-position="left" v-if="isUpdateVisible">
                                <mu-form-item prop="input" label="">
                                    <mu-text-field v-model="form_update.contact"></mu-text-field>
                                </mu-form-item>
                            </mu-form>
                        </td>
                    </tr>
                    <tr>
                        <td>Адрес центрального офиса</td>
                        <td>{{employer.address}}
                            <mu-form label-position="left" v-if="isUpdateVisible">
                                <mu-form-item prop="input" label="">
                                    <mu-text-field v-model="form_update.address"></mu-text-field>
                                </mu-form-item>
                            </mu-form>
                        </td>
                    </tr>
                    <tr>
                        <td>ИНН</td>
                        <td>{{employer.inn}}
                            <mu-form label-position="left" v-if="isUpdateVisible">
                                <mu-form-item prop="input" label="">
                                    <mu-text-field v-model="form_update.inn"></mu-text-field>
                                </mu-form-item>
                            </mu-form>
                        </td>
                    </tr>
                    <tr>
                        <td>Адрес электорнной почты</td>
                        <td>{{employer.email}}
                            <mu-form label-position="left" v-if="isUpdateVisible">
                                <mu-form-item prop="input" label="">
                                    <mu-text-field v-model="form_update.email"></mu-text-field>
                                </mu-form-item>
                            </mu-form>
                        </td>
                    </tr>
                    <tr>
                        <td>Контактный телефон</td>
                        <td>{{employer.phone}}
                            <mu-form label-position="left" v-if="isUpdateVisible">
                                <mu-form-item prop="input" label="">
                                    <mu-text-field v-model="form_update.phone"></mu-text-field>
                                </mu-form-item>
                            </mu-form>
                        </td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
        <mu-row v-if="isUpdateVisible">
            <mu-col>
                <mu-button @click="UpdateEmployer">Внести изменения</mu-button>
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
    export default {
        name: "EmployerSingle",
        props: ['id'],
        data() {
            return {
                employer: {},
                isUpdateVisible: false,
                form_update: {
                    name: '',
                    contact: '',
                    address: '',
                    inn: '',
                    email: '',
                    phone: '',
                }
            }
        },
        created() {
            this.loadEmployer()
        },
        methods: {
            async loadEmployer() {
                this.employer = await fetch(
                    `http://127.0.0.1:8000/api/v1/employer/${this.id}/`
                ).then(response => response.json())
            },
            ShowUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async UpdateEmployer() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/employer/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_update)
                });
                await alert('Данные о работодателе успешно изменены')
                this.isUpdateVisible = !this.isUpdateVisible
                await this.loadEmployer()
            },
        }
    }
</script>

<style scoped>

</style>