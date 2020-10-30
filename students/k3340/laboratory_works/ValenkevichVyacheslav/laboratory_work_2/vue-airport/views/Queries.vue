<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Запросы для курсовой работы</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <ul>
                    <li>Определить наличие свободных мест на заданный рейс.</li>
                    <mu-form :model="form_query3" class="mu-demo-form" label-width="100" style="width: 50%">
                        <mu-form-item prop="select" label="Выберите рейс">
                            <mu-select v-model="form_query3.flight">
                                <mu-option v-for="flight in listFlight" :key="flight.id"
                                           :label="flight.number"
                                           :value="flight.id"></mu-option>
                            </mu-select>
                        </mu-form-item>
                    </mu-form><mu-button color="primary" @click="Query3">Выполнить запрос</mu-button>
                    <p v-if="isQuery3Vis">Результат выполнения запроса</p>
                    <H3 v-if="isQuery3Vis">На данный момент свободно {{query3}} мест</H3>
                    <li>Определить количество самолетов, находящихся в ремонте.</li>
                    <h3>Количество самолетов, находящихся в ремонте: {{query4}}</h3>
                    <li>Определить количество работников аэропорта.</li>
                    <h3>Всего в аэропорту работает {{query5}} человек</h3>
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
                form_query3:{
                    flight:'',
                },
                query3: {},
                query4: {},
                query5: {
                    result:{},
                },
                listRoute:[],
                listFlight:[],
                isQuery3Vis: false,
            }
        },
        created() {
            this.Query3()
            this.Query4()
            this.Query5()
            this.loadListRoute()
            this.loadListFlight()
        },
        methods: {
            async loadListRoute() {
                this.listRoute = await fetch(
                    `http://127.0.0.1:8000/api/v1/route`
                ).then(response => response.json())
            },
            async loadListFlight() {
                this.listFlight = await fetch(
                    `http://127.0.0.1:8000/api/v1/flight`
                ).then(response => response.json())
            },
            Query3() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/query3/",
                    type: "GET",
                    data: {
                        number: this.form_query3.flight,
                    },
                    success: (response) => {
                        this.query3 = response.result
                        this.isQuery3Vis = true
                        console.log(this.query3)
                    }
                })
            },
            Query4() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/query4/",
                    type: "GET",
                    success: (response) => {
                        this.query4 = response.result
                        console.log(this.query4)
                    }
                })
            },
            Query5() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/query5/",
                    type: "GET",
                    success: (response) => {
                        this.query5 = response.result
                        console.log(this.query5)
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>