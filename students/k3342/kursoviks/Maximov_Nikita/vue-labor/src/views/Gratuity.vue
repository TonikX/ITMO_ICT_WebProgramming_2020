<template>
    <mu-container>
        <mu-row align="left">
            <mu-col>
                <h1>Выплачиваемые пособия</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col align="center">
                <table v-for="gratuity in listGratuity" :key="gratuity.id">
                    <tr>
                        <td colspan="2">Пособие №{{gratuity.id}}</td>
                    </tr>
                    <tr>
                        <td>ФИО</td>
                        <td>{{gratuity.applicant}}</td>
                    </tr>
                    <tr>
                        <td>Размер выплаты</td>
                        <td>{{gratuity.salary}}</td>
                    </tr>
                    <tr>
                        <td>Дата начала выплаты</td>
                        <td>{{gratuity.date_start}}</td>
                    </tr>
                    <tr>
                        <td>Дата окончания выплаты</td>
                        <td>{{gratuity.date_end}}</td>
                    </tr>
                </table>
                <br>
            </mu-col>
            <mu-col v-if="isCreateVisible">
                <mu-form label-position="left">
                <mu-select v-model="form.applicant" label="Выберите соискателя">
                    <mu-option v-for="applicant in listApplicant" :key="applicant.id" :label="applicant.fio"
                               :value="applicant.id"></mu-option>
                </mu-select>
                        <mu-form-item prop="input" label="Размер пособия">
                            <mu-text-field v-model="form.salary"></mu-text-field>
                        </mu-form-item>
                        <mu-form-item prop="input" label="Дата начала выплаты пособия ГГГГ-ММ-ДД">
                            <mu-text-field v-model="form.date_start"></mu-text-field>
                        </mu-form-item>
                        <mu-form-item prop="input" label="Дата окончания выплаты пособия ГГГГ-ММ-ДД">
                            <mu-text-field v-model="form.date_end"></mu-text-field>
                        </mu-form-item>
                </mu-form>
                <mu-button @click="CreateGratuity">Добавить</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
            <br><br><br>
                <mu-button @click="ShowCreate">Назначить пособие</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "Gratuity",
        props: ['id'],
        components: {},
        data() {
            return {
                listGratuity: [],
                listApplicant: [],
                isCreateVisible: false,
                form: {
                    applicant: '',
                    date_start: '',
                    salary: '',
                    date_end: '',
                },
            }
        },
        created() {
            this.loadListGratuity()
            this.loadListApplicant()
        },
        methods: {
            async loadListGratuity() {
                this.listGratuity = await fetch(
                    `http://127.0.0.1:8000/api/v1/gratuity/`
                ).then(response => response.json())
            },
            async loadListApplicant() {
                this.listApplicant = await fetch(
                    `http://127.0.0.1:8000/api/v1/applicant/`
                ).then(response => response.json())
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            CreateGratuity() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/gratuity/create",
                    type: "POST",
                    data: {
                        applicant: this.form.applicant,
                        date_start: this.form.date_start,
                        salary: this.form.salary,
                        date_end: this.form.date_end,
                    },
                    success: (response) => {
                        this.$router.push({name: "Пособие"})
                        alert("Пособие назначено")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListGratuity()
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