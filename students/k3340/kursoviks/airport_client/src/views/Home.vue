<template>
    <div class="home">
        <mu-container>
            <mu-row align="center">
                <mu-col>
                    <h1>Компании-авиаперевозчики</h1>
                </mu-col>
            </mu-row>
            <mu-row v-for="aircarrier in listAirCarrier" :key="aircarrier.id">
                <mu-col>
                    <a href="#" @click="goTo(aircarrier.id)">{{aircarrier.name}}</a>
                </mu-col>
            </mu-row>
        </mu-container>
    </div>
</template>

<script>
    // @ is an alias to /src

    export default {
        name: 'Home',
        props: ['id'],
        components: {},
        data() {
            return {
                listAirCarrier: []
            }
        },
        created() {
            this.loadListAirCarrier()
        },
        methods: {
            async loadListAirCarrier() {
                this.listAirCarrier = await fetch(
                    `http://127.0.0.1:8000/api/v1/aircarrier`
                ).then(response => response.json())
            },
            goTo(id) {
                this.$router.push({name: 'Авиаперевозчик', params: {id: id}})
            },
        }
    }
</script>
