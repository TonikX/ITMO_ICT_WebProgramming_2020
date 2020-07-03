<template>
    <mu-container>
        <mu-row align="center">
            <mu-col span="10" align-self="center">
                <h1>Список кабинетов школы</h1>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col span="10">
                <ol class="ball" v-for="cabinet in listCabinet" :key="cabinet.id">
                    <li><a href="#">Кабинет №{{cabinet.number}}</a></li>
                </ol>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "Cabinets",
        data() {
            return {
                listCabinet: []
            }
        },
        components: {},
        created() {
            this.loadListCabinet()
        },
        methods: {
            async loadListCabinet() {
                this.listCabinet = await fetch(
                    `${this.$store.getters.getServerUrl}/cabinet`
                ).then(response => response.json())
            },
        }
    }
</script>

<style scoped>

</style>