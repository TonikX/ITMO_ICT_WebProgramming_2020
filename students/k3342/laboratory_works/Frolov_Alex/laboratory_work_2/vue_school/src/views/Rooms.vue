<template>
    <mu-container>
        <mu-row align="center">
            <mu-col span="10" align-self="center">
                <h1>Список кабинетов школы</h1>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col span="10">
                <ol class="ball" v-for="room in listRoom" :key="room.id">
                    <li><a href="#">Кабинет №{{room.number}}</a></li>
                </ol>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "Rooms",
        data() {
            return {
                listRoom: []
            }
        },
        components: {},
        created() {
            this.loadListRoom()
        },
        methods: {
            async loadListRoom() {
                this.listRoom = await fetch(
                    `${this.$store.getters.getServerUrl}/room`
                ).then(response => response.json())
            },
        }
    }
</script>

<style scoped>
</style>