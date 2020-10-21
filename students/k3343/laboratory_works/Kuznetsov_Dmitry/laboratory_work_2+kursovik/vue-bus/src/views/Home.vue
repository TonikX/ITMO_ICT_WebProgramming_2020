<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <mu-icon size="56" value="directions_bus"></mu-icon>
                <a href="#/bus"><h1>Автобусы</h1></a>
            </mu-col>
            <mu-col>
                <mu-icon size="56" value="perm_contact_calendar"></mu-icon>
                <a href="#/driver"><h1>Водители</h1></a>
            </mu-col>
            <mu-col>
                <mu-icon size="56" value="map"></mu-icon>
                <a href="#/route"><h1>Маршруты</h1></a>
            </mu-col>
            <mu-col>
                <mu-icon size="56" value="departure_board"></mu-icon>
                <a href="#/schedule"><h1>График работы водителей</h1></a>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <h1>Журнал автобусного парка</h1>
                <mu-form label-position="left">
                    <mu-form-item prop="input" label="Дата">
                        <mu-text-field v-model="form_filter.date"></mu-text-field>
                    </mu-form-item>
                <mu-select v-model="form_filter.status" label="Статус">
                    <mu-option value="Вышел_на_линию" label="Вышел на линию"></mu-option>
                    <mu-option value="Не_вышел_на_линию" label="Не вышел на линию"></mu-option>
                            <mu-option label="     " value=""></mu-option>
                </mu-select>
                </mu-form>
                <mu-button @click="Filter">Отфильтровать</mu-button>
                <mu-button @click="FilterReset">Сбросить фильтры</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col align="center">
                <table>
                    <tr>
                        <td>Дата</td>
                        <td>Маршрут</td>
                        <td>Автобус</td>
                        <td>Водитель</td>
                        <td>Статус</td>
                        <td>Комментарий</td>
                    </tr>
                    <tr v-for="journal in listJournal" :key="journal.id" align="center">
                        <td>
                        <mu-radio v-if="isDeleteVisible" v-model="form_delete" :value="journal.id"
                                      label=""></mu-radio>
                            {{journal.date}}
                        </td>
                        <td>{{journal.schedule.route.starting_point}} - {{journal.schedule.route.final_destination}}</td>
                        <td>{{journal.schedule.bus}}</td>
                        <td>{{journal.schedule.driver}}</td>
                        <td>{{journal.status}}</td>
                        <td>{{journal.comment}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
            <mu-button @click="ShowCreate">Добавить запись в журнал</mu-button>
        </mu-col>
            <mu-col>
            <mu-button @click="ShowDelete">Удалить запись из журнала</mu-button>
        </mu-col>
        </mu-row>
        <mu-row>
            <mu-col v-if="isCreateVisible">
                <mu-form label-position="left">
                    <mu-select v-model="form_create.schedule" label="График">
                        <mu-option v-for="schedule in listSchedule" :key="schedule.id" :label="schedule.driver+schedule.day"
                                   :value="schedule.id"></mu-option>
                    </mu-select>
                <mu-select v-model="form_create.status" label="Статус">
                    <mu-option value="Вышел_на_линию" label="Вышел на линию"></mu-option>
                    <mu-option value="Не_вышел_на_линию" label="Не вышел на линию"></mu-option>
                </mu-select>
                    <mu-form-item prop="input" label="Комментарий">
                        <mu-text-field v-model="form_create.comment"></mu-text-field>
                    </mu-form-item>
                </mu-form>
            <mu-button @click="CreateJournal">Добавить</mu-button>
            </mu-col>
            <mu-col v-if="isDeleteVisible">
                <mu-button @click="DeleteJournal">Удалить</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: 'Home',
        components: {},
        data() {
            return {
                listJournal: [],
                listSchedule: [],
                isCreateVisible: false,
                isDeleteVisible: false,
                form_create:{
                    status:'',
                    comment: '',
                    schedule: '',
                },
                form_filter:{
                    date: '',
                    status: '',
                },
                form_delete: {},
            }
        },
        created() {
            this.loadListJournal()
            this.loadListJournalFull()
            this.loadListSchedule()
        },
        methods: {
            async loadListJournal() {
                this.listJournal = await fetch(
                    `http://127.0.0.1:8000/api/v1/journal/?date=${this.form_filter.date}&status=${this.form_filter.status}`
                ).then(response => response.json())
            },
            async loadListJournalFull() {
                this.listJournal = await fetch(
                    `http://127.0.0.1:8000/api/v1/journal/`
                ).then(response => response.json())
            },
            async loadListSchedule() {
                this.listSchedule = await fetch(
                    `http://127.0.0.1:8000/api/v1/schedule/`
                ).then(response => response.json())
            },
            Filter() {
                this.loadListJournal()
            },
            FilterReset() {
                this.loadListJournalFull()
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            CreateJournal() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/journal/create",
                    type: "POST",
                    data: {
                        status: this.form_create.status,
                        schedule: this.form_create.schedule,
                        comment: this.form_create.comment,
                    },
                    success: (response) => {
                        alert("Запись в журнал успешно добавлена")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListJournal()
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Данные введены неверно")
                        }
                    }

                })
            },
            ShowDelete() {
                this.isDeleteVisible = !this.isDeleteVisible
            },
            async DeleteJournal() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/journal/${this.form_delete}/delete`, {
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
                await alert('Запись удалена')

                this.isDeleteVisible = !this.isDeleteVisible
                await this.loadListJournalFull()
            },

        }
    }
</script>
