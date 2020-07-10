<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Документы, предоставляемые абитуриентами</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <h2>Аттестаты</h2>
                <ul v-for="attestat in listAttestat" :key="attestat.id">
                    <li>Аттестат №{{attestat.id}}
                        <ul>
                            <li>Абитуриент - {{attestat.enrollee}}</li>
                            <li>Средний балл - {{attestat.average}}</li>
                            <li>
                                <table width="60%">
                                    <tr>
                                        <th colspan="2">Оценки</th>
                                    </tr>
                                    <tr v-for="mark in attestat.marks" :key="mark.id">
                                        <td>{{mark.subject}}</td>
                                        <td>{{mark.mark}}</td>
                                    </tr>
                                </table>
                            </li>
                        </ul>
                    </li>
                </ul>
                <mu-button @click="showCreateAttestat">Добавить аттестат</mu-button>
                <mu-container v-if="isCreateAttestatVisible">
                <mu-form style="width: 50%" :model="form_atestat" class="mu-demo-form" :label-position="labelPosition"
                                 label-width="200">
                    <mu-form-item prop="select" label="Абитуриент">
                        <mu-select v-model="form_atestat.enrollee">
                            <mu-option v-for="enrollee in listEnrollee" :key="enrollee.id" :label="enrollee.fio"
                                       :value="enrollee.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                            <mu-form-item prop="input" label="Средний балл">
                                <mu-text-field v-model="form_atestat.average"></mu-text-field>
                            </mu-form-item>
                </mu-form>
                <mu-button @click="CreateAttestat">Добавить оценки</mu-button>
                </mu-container>
            </mu-col>
            <mu-col>
                <h2>Сертификаты ЕГЭ</h2>
                <ul v-for="ege in listEge" :key="ege.id">
                    <li>Сертификат ЕГЭ №{{ege.id}}
                        <ul>
                            <li>Абитуриент - {{ege.enrollee}}</li>
                            <li>
                                <table width="60%">
                                    <tr>
                                        <th colspan="2">Результаты</th>
                                    </tr>
                                    <tr v-for="mark in ege.marks" :key="mark.id">
                                        <td>{{mark.subject}}</td>
                                        <td>{{mark.mark}}</td>
                                    </tr>
                                </table>
                            </li>
                        </ul>
                    </li>
                </ul>
                <mu-button @click="showCreateEge">Добавить сертификат ЕГЭ</mu-button>
                <mu-container v-if="isCreateEgeVisible">
                <mu-form style="width: 50%" :model="form_ege" class="mu-demo-form" :label-position="labelPosition"
                                 label-width="200">
                    <mu-form-item prop="select" label="Абитуриент">
                        <mu-select v-model="form_ege.enrollee">
                            <mu-option v-for="enrollee in listEnrollee" :key="enrollee.id" :label="enrollee.fio"
                                       :value="enrollee.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
                <mu-button @click="CreateEge">Добавить результаты</mu-button>
                </mu-container>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "Documents",
        props: ['id'],
        components: {},
        data() {
            return {
                isCreateEgeVisible: false,
                isCreateAttestatVisible: false,
                listAttestat: [],
                listEnrollee: [],
                listEge: [],
                form_atestat: {
                    enrollee: '',
                    average: '',
                },
                form_ege: {
                    enrollee: '',
                },
            }
        },
        created() {
            this.loadListAttestat()
            this.loadListEge()
            this.loadListEnrollee()
        },
        methods: {
            async loadListAttestat() {
                this.listAttestat = await fetch(
                    `http://127.0.0.1:8000/api/v1/attestat/`
                ).then(response => response.json())
            },
            async loadListEge() {
                this.listEge = await fetch(
                    `http://127.0.0.1:8000/api/v1/ege/`
                ).then(response => response.json())
            },
            async loadListEnrollee() {
                this.listEnrollee = await fetch(
                    `http://127.0.0.1:8000/api/v1/enrollee/`
                ).then(response => response.json())
            },
            showCreateAttestat() {
                this.isCreateAttestatVisible = !this.isCreateAttestatVisible
            },
            CreateAttestat() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/attestat/create",
                    type: "POST",
                    data: {
                        enrollee: this.form_atestat.enrollee,
                        average: this.form_atestat.average,
                    },
                    success: (response) => {
                        this.$router.push({name: "Оценки"})
                        alert("Аттестат добавлен")
                        this.isCreateAttestatVisible = !this.isCreateAttestatVisible
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Данные введены неверно")
                        }
                    }

                })
            },
            showCreateEge() {
                this.isCreateEgeVisible = !this.isCreateEgeVisible
            },
            CreateEge() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/ege/create",
                    type: "POST",
                    data: {
                        enrollee: this.form_ege.enrollee,
                    },
                    success: (response) => {
                        this.$router.push({name: "Результаты"})
                        alert("Сертификат ЕГЭ добавлен")
                        this.isCreateEgeVisible = !this.isCreateEgeVisible
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