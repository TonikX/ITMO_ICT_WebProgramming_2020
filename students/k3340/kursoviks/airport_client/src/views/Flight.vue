<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Рейсы</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <table class="paleBlueRows" width="100%">
                    <tr>
                        <th>Номер рейса</th>
                        <th>Номер экипажа</th>
                        <th>Самолет</th>
                        <th>Пункт прибытия</th>
                        <th>Количество проданных билетов</th>
                    </tr>
                    <tr v-for="flight in listFlight" :key="flight.id">
                        <td>{{flight.number}}</td>
                        <td>{{flight.crew}}</td>
                        <td>{{flight.plane}}</td>
                        <td>{{flight.route}}</td>
                        <td>{{flight.number_of_tickets}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "Flight",
        props: ['id'],
        components: {},
        data() {
            return {
                listFlight: []
            }
        },
        created() {
            this.loadListFlight()
        },
        methods: {
            async loadListFlight() {
                this.listFlight = await fetch(
                    `http://127.0.0.1:8000/api/v1/flight`
                ).then(response => response.json())
            },

        }
    }
</script>

<style scoped>

</style>