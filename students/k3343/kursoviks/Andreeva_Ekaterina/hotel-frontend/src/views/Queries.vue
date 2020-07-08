<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>Запросы к курсовой работе</h1>
                <p>Работа с системой предполагает получение следующей информации:</p>
                <ul>
                    <li>Запрос №1</li>
                    <p>о клиентах, проживавших в заданном номере</p>
                    <mu-form :model="form_query1" class="mu-demo-form" label-width="100" style="width: 50%">
                        <mu-form-item prop="select" label="Номер">
                            <mu-select v-model="form_query1.room_number">
                                <mu-option v-for="room in listRoom" :key="room.id"
                                           :label="room.room_number"
                                           :value="room.id"></mu-option>
                            </mu-select>
                        </mu-form-item>
                    </mu-form>
                    <mu-button color="primary" @click="Query1">Выполнить запрос</mu-button>
                    <p v-if="isQueryVis">Результат выполнения запроса</p>
                    <table v-if="isQueryVis">
                        <tr v-for="query_1 in query1">
                            <td>{{query_1.fio}}</td>
                        </tr>
                    </table>
                    <li>Запрос №2</li>
                    <p>о количестве клиентов, прибывших из заданного города</p>
                    <table>
                        <tr>
                            <th>Город</th>
                            <th>Количество клиентов</th>
                        </tr>
                        <tr v-for="query_3 in query2.result">
                            <td>{{query_3.from_town}}</td>
                            <td>{{query_3.fio__count}}</td>
                        </tr>
                    </table>
                    <li>Запрос №3</li>
                    <p>о том, кто из служащих убирал номер указанного клиента в заданный день недели</p>
                    <mu-form :model="form_query3" class="mu-demo-form" label-width="100" style="width: 50%">
                        <mu-form-item prop="select" label="Клиент">
                            <mu-select v-model="form_query3.resident">
                                <mu-option v-for="resident in listResident" :key="resident.id"
                                           :label="resident.fio"
                                           :value="resident.room"></mu-option>
                            </mu-select>
                        </mu-form-item>
                        <mu-form-item prop="radio" label="День недели">
                            <mu-radio v-model="form_query3.day" value="Понедельник" label="Понедельник"></mu-radio>
                            <mu-radio v-model="form_query3.day" value="Вторник" label="Вторник"></mu-radio>
                            <mu-radio v-model="form_query3.day" value="Среда" label="Среда"></mu-radio>
                            <mu-radio v-model="form_query3.day" value="Четверг" label="Четверг"></mu-radio>
                            <mu-radio v-model="form_query3.day" value="Пятница" label="Пятница"></mu-radio>
                            <mu-radio v-model="form_query3.day" value="Суббота" label="Суббота"></mu-radio>
                        </mu-form-item>
                    </mu-form>
                    <mu-button color="primary" @click="Query3">Выполнить запрос</mu-button>
                    <p v-if="isQuery3Vis">Результат выполнения запроса</p>
                    <h3 v-if="isQuery3Vis">{{query3}}</h3>
                    <li>Запрос №4</li>
                    <p>сколько в гостинице свободных номеров</p>
                    <h3>Количество свободных номеров на данный момент: {{query4.result}}</h3>
                    <li>Запрос №5</li>
                    <p>список клиентов с указанием места жительства</p>
                    <table>
                        <tr>
                            <th>ФИО</th>
                            <th>Номер</th>
                            <th>Место жительства</th>
                        </tr>
                        <tr v-for="resident in listResident" :key="resident.id">
                            <td>{{resident.fio}}</td>
                            <td>{{resident.room}}</td>
                            <td>{{resident.from_town}}</td>
                        </tr>
                    </table>
                </ul>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Queries",
        data() {
            return {
                query1: '',
                query2: {
                    result: []
                },
                query3: {
                    result: []
                },
                query4: {
                    result: []
                },
                query5: [],
                form_query1: {
                    room_number: '',
                },
                form_query3: {
                    resident: '',
                    room: '',
                },
                form_query5: {
                    resident: '',
                },
                isQueryVis: false,
                isQuery3Vis: false,
                isQuery5Vis: false,
                listRoom: [],
                listResident: [],
            }
        },
        created() {
            this.Query1()
            this.Query2()
            this.Query4()
            this.Query3()
            this.Query5()
            this.loadListRoom()
            this.loadListResident()
        },
        methods: {
            async loadListRoom() {
                this.listRoom = await fetch(
                    `http://127.0.0.1:8000/api/v1/room/`
                ).then(response => response.json())
            },
            async loadListResident() {
                this.listResident = await fetch(
                    `http://127.0.0.1:8000/api/v1/resident/`
                ).then(response => response.json())
            },
            async Query5() {
                this.query5 = await fetch(
                    `http://127.0.0.1:8000/api/v1/specialty/`
                ).then(response => response.json())
            },
            async Query4() {
                this.query4 = await fetch(
                    `http://127.0.0.1:8000/api/v1/query4/`
                ).then(response => response.json())
            },
            async Query3() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/query3/",
                    type: "GET",
                    data: {
                        resident: this.form_query3.resident,
                        day: this.form_query3.day,
                    },
                    success: (response) => {
                        this.query3 = response.result
                        this.isQuery3Vis = true
                        console.log(this.query3)
                    }
                })
            },
            async Query2() {
                this.query2 = await fetch(
                    `http://127.0.0.1:8000/api/v1/query2/`
                ).then(response => response.json())
                console.log(this.listRoom)
            },
            Query1() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/query1/",
                    type: "GET",
                    data: {
                        room_number: this.form_query1.room_number,
                    },
                    success: (response) => {
                        this.query1 = response.result
                        this.isQueryVis = true
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>