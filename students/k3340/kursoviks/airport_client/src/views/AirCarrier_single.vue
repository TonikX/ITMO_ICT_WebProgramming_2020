<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>
                    Авиакомпания "{{aircarrier.name}}"
                </h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>Страна, в которой основана компания: {{aircarrier.country}}</mu-col>
            <mu-col>Дата основания компании: {{aircarrier.founded_in}}</mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button color="primary" @click="showPlane">
                    Самолеты
                </mu-button>
            </mu-col>
            <mu-col>
                <mu-button color="primary" @click="showCrew">
                    Экипажи
                </mu-button>
            </mu-col>
        </mu-row>
        <br>
        <mu-row align="center" v-if="isPlaneVisible">
            <mu-col>
                <table class="paleBlueRows" width="60%" v-for="plane in aircarrier.planes" :key="plane.id">
                <tr>
                    <th colspan="2">Самолет номер {{plane.number}}</th>
                </tr>
                    <tr>
                        <td>Тип самолета</td>
                        <td>{{plane.type}}</td>
                    </tr>
                    <tr>
                        <td>Количество сидений</td>
                        <td>{{plane.number_of_seats}}</td>
                    </tr>
                    <tr>
                        <td>Скорость самолета</td>
                        <td>{{plane.speed}} км/ч</td>
                    </tr>
                    <tr>
                        <td>Находится в ремонте</td>
                        <td>{{plane.on_repairing}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
        <mu-row align="center" v-if="isCrewVisible">
            <mu-col>
                <table class="paleBlueRows" width="60%" v-for="crew in aircarrier.crews" :key="crew.id">
                <tr>
                    <th colspan="2">Экипаж номер {{crew.id}}</th>
                </tr>
                    <tr>
                        <td>Командир экипажа</td>
                        <td>{{crew.crew_commander}}</td>
                    </tr>
                    <tr>
                        <td>Второй пилот</td>
                        <td>{{crew.second_pilot}}</td>
                    </tr>
                    <tr>
                        <td>Штурман</td>
                        <td>{{crew.navigator}}</td>
                    </tr>
                    <tr>
                        <td>Бортпроводники</td>
                        <td>
                            <p v-for="steward in crew.stewards" :key="steward.id">{{steward.last_name}} </p>
                        </td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "AirCarrier_single",
        props: ['id'],
        data() {
            return {
                aircarrier: {},
                isCrewVisible: false,
                isPlaneVisible: false,
            }
        },
        created() {
            this.loadAirCarrier()
        },
        methods: {
            async loadAirCarrier() {
                this.aircarrier = await fetch(
                    `http://127.0.0.1:8000/api/v1/aircarrier/${this.id}`
                ).then(response => response.json())
            },
            showCrew() {
                this.isCrewVisible = !this.isCrewVisible
            },
            showPlane() {
                this.isPlaneVisible = !this.isPlaneVisible
            },
        }
    }
</script>

<style scoped>

</style>