<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Маршруты</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <table class="paleBlueRows"
                       width="100%">
                    <tr>
                        <th class="is-right">Номер маршрута</th>
                        <th class="is-right">Расстояние в км</th>
                        <th class="is-right">Место вылета</th>
                        <th class="is-right">Дата и время вылета</th>
                        <th class="is-right">Место прилета</th>
                        <th class="is-right">Дата и время прилета</th>
                        <th class="is-right">Транзитная посадка</th>
                    </tr>
                    <tr v-for="route in listRoute" :key="route.id">
                        <td class="is-right">{{route.number}}</td>
                        <td class="is-right">{{route.distance}}</td>
                        <td class="is-right">{{route.departure_from}}</td>
                        <td class="is-right">{{route.departure_time}}</td>
                        <td class="is-right">{{route.arrival_to}}</td>
                        <td class="is-right">{{route.arrival_time}}</td>
                        <td class="is-right">{{route.transit_landing}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "Route",
        props: ['id'],
        components: {},
        data() {
            return {
                listRoute: []
            }
        },
        created() {
            this.loadListRoute()
        },
        methods: {
            async loadListRoute() {
                this.listRoute = await fetch(
                    `http://127.0.0.1:8000/api/v1/route`
                ).then(response => response.json())
            },

        }
    }
</script>

<style scoped>

</style>