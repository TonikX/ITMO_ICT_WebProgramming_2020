<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>График работы водителей</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-form label-position="left">
                    <mu-form-item prop="radio" label="День недели">
                        <mu-radio v-model="form_filter.day" value="Понедельник" label="Понедельник"></mu-radio>
                        <mu-radio v-model="form_filter.day" value="Вторник" label="Вторник"></mu-radio>
                        <mu-radio v-model="form_filter.day" value="Среда" label="Среда"></mu-radio>
                        <mu-radio v-model="form_filter.day" value="Четверг" label="Четверг"></mu-radio>
                        <mu-radio v-model="form_filter.day" value="Пятница" label="Пятница"></mu-radio>
                        <mu-radio v-model="form_filter.day" value="Суббота" label="Суббота"></mu-radio>
                        <mu-radio v-model="form_filter.day" value="Воскресенье" label="Воскресенье"></mu-radio>
                        <mu-radio v-model="form_filter.day" value="" label="Любой"></mu-radio>
                    </mu-form-item>
                </mu-form>
            </mu-col>
            <mu-col>
                <mu-form label-position="left">
                    <mu-form-item prop="select" label="Маршрут">
                        <mu-select v-model="form_filter.route">
                            <mu-option v-for="route in listRoute" :key="route.id"
                                       :label="route.starting_point+route.final_destination"
                                       :value="route.id"></mu-option>
                            <mu-option label="     " value=""></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-form label-position="left">
                    <mu-form-item prop="select" label="Автобус">
                        <mu-select v-model="form_filter.bus">
                            <mu-option v-for="bus in listBus" :key="bus.id" :label="bus.number"
                                       :value="bus.id"></mu-option>
                            <mu-option label="     " value=""></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-col>
            <mu-col>
                <mu-form label-position="left">
                    <mu-form-item prop="select" label="Водитель">
                        <mu-select v-model="form_filter.driver">
                            <mu-option v-for="driver in listDriver" :key="driver.id" :label="driver.fio"
                                       :value="driver.id"></mu-option>
                            <mu-option label="     " value=""></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button @click="Filter">Отфильтровать</mu-button>
            </mu-col>
            <mu-col>
                <mu-button @click="FilterReset">Сбросить фильтры</mu-button>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table>
                    <tr>
                        <td>День недели</td>
                        <td>Маршрут</td>
                        <td>Автобус</td>
                        <td>Водитель</td>
                    </tr>
                    <tr v-for="schedule in listSchedule" :key="schedule.id" align="center">
                        <td>
                            <mu-radio v-if="isDeleteVisible" v-model="form_delete" :value="schedule.id"
                                      label=""></mu-radio>
                            <mu-radio v-if="isUpdateVisible" v-model="form_update.id" :value="schedule.id"
                                      label=""></mu-radio>
                            {{schedule.day}}
                        </td>
                        <td>{{schedule.route.starting_point}} - {{schedule.route.final_destination}}</td>
                        <td>{{schedule.bus}}</td>
                        <td>{{schedule.driver}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button @click="ShowCreate">Добавить маршрут</mu-button>
            </mu-col>
            <mu-col>
                <mu-button @click="ShowUpdate">Изменить маршрут</mu-button>
            </mu-col>
            <mu-col>
                <mu-button @click="ShowDelete">Удалить маршрут</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col v-if="isCreateVisible">
                <mu-form label-position="left">
                    <mu-form-item prop="radio" label="День недели">
                        <mu-radio v-model="form_create.day" value="Понедельник" label="Понедельник"></mu-radio>
                        <mu-radio v-model="form_create.day" value="Вторник" label="Вторник"></mu-radio>
                        <mu-radio v-model="form_create.day" value="Среда" label="Среда"></mu-radio>
                        <mu-radio v-model="form_create.day" value="Четверг" label="Четверг"></mu-radio>
                        <mu-radio v-model="form_create.day" value="Пятница" label="Пятница"></mu-radio>
                        <mu-radio v-model="form_create.day" value="Суббота" label="Суббота"></mu-radio>
                        <mu-radio v-model="form_create.day" value="Воскресенье" label="Воскресенье"></mu-radio>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Маршрут">
                        <mu-select v-model="form_create.route">
                            <mu-option v-for="route in listRoute" :key="route.id"
                                       :label="route.starting_point+route.final_destination"
                                       :value="route.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Автобус">
                        <mu-select v-model="form_create.bus">
                            <mu-option v-for="bus in listBus" :key="bus.id" :label="bus.number"
                                       :value="bus.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Водитель">
                        <mu-select v-model="form_create.driver">
                            <mu-option v-for="driver in listDriver" :key="driver.id" :label="driver.fio"
                                       :value="driver.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
                <mu-button @click="CreateSchedule">Добавить</mu-button>
            </mu-col>
            <mu-col v-if="isUpdateVisible">
                <mu-form label-position="left">
                    <mu-form-item prop="radio" label="День недели">
                        <mu-radio v-model="form_update.day" value="Понедельник" label="Понедельник"></mu-radio>
                        <mu-radio v-model="form_update.day" value="Вторник" label="Вторник"></mu-radio>
                        <mu-radio v-model="form_update.day" value="Среда" label="Среда"></mu-radio>
                        <mu-radio v-model="form_update.day" value="Четверг" label="Четверг"></mu-radio>
                        <mu-radio v-model="form_update.day" value="Пятница" label="Пятница"></mu-radio>
                        <mu-radio v-model="form_update.day" value="Суббота" label="Суббота"></mu-radio>
                        <mu-radio v-model="form_update.day" value="Воскресенье" label="Воскресенье"></mu-radio>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Маршрут">
                        <mu-select v-model="form_update.route">
                            <mu-option v-for="route in listRoute" :key="route.id"
                                       :label="route.starting_point+route.final_destination"
                                       :value="route.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Автобус">
                        <mu-select v-model="form_update.bus">
                            <mu-option v-for="bus in listBus" :key="bus.id" :label="bus.number"
                                       :value="bus.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Водитель">
                        <mu-select v-model="form_update.driver">
                            <mu-option v-for="driver in listDriver" :key="driver.id" :label="driver.fio"
                                       :value="driver.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
                <mu-button @click="UpdateSchedule">Подтвердить</mu-button>
            </mu-col>
            <mu-col v-if="isDeleteVisible">
                <mu-button @click="DeleteSchedule">Удалить</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "Schedule",
        components: {},
        data() {
            return {
                listSchedule: [],
                listRoute: [],
                listDriver: [],
                listBus: [],
                isCreateVisible: false,
                isUpdateVisible: false,
                isDeleteVisible: false,
                form_filter: {
                    driver: '',
                    bus: '',
                    route: '',
                    day: '',
                },
                form_create: {
                    driver: '',
                    bus: '',
                    route: '',
                    day: '',
                },
                form_delete: {},
                form_update: {
                    id: '',
                    driver: '',
                    bus: '',
                    route: '',
                    day: '',
                },
            }
        },
        created() {
            this.loadListRoute()
            this.loadListBus()
            this.loadListDriver()
            this.loadListSchedule()
            this.loadListScheduleFull()
        },
        methods: {
            async loadListRoute() {
                this.listRoute = await fetch(
                    `http://127.0.0.1:8000/api/v1/route/`
                ).then(response => response.json())
            },
            async loadListSchedule() {
                this.listSchedule = await fetch(
                    `http://127.0.0.1:8000/api/v1/schedule/?day=${this.form_filter.day}&driver=${this.form_filter.driver}&bus=${this.form_filter.bus}&route=${this.form_filter.route}`
                ).then(response => response.json())
            },
            async loadListScheduleFull() {
                this.listSchedule = await fetch(
                    `http://127.0.0.1:8000/api/v1/schedule/`
                ).then(response => response.json())
            },
            Filter() {
                this.loadListSchedule()
            },
            FilterReset() {
                this.loadListScheduleFull()
            },
            async loadListBus() {
                this.listBus = await fetch(
                    `http://127.0.0.1:8000/api/v1/bus/`
                ).then(response => response.json())
            },
            async loadListDriver() {
                this.listDriver = await fetch(
                    `http://127.0.0.1:8000/api/v1/driver/`
                ).then(response => response.json())
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            CreateSchedule() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/schedule/create",
                    type: "POST",
                    data: {
                        driver: this.form_create.driver,
                        bus: this.form_create.bus,
                        route: this.form_create.route,
                        day: this.form_create.day,
                    },
                    success: (response) => {
                        alert("Запись в график успешно добавлена")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListSchedule()
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
            async DeleteSchedule() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/schedule/${this.form_delete}/delete`, {
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
                await alert('График удален')
                this.isDeleteVisible = !this.isDeleteVisible
                await this.loadListSchedule()
            },
            ShowUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async UpdateSchedule() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/schedule/${this.form_update.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_update)
                });
                await alert('Данные о графике успешно изменены')
                this.isUpdateVisible = !this.isUpdateVisible
                await this.loadListSchedule()
            },
        }
    }
</script>

<style scoped>

</style>