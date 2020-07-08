<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Читальные залы</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table>
                    <tr>
                        <th>Номер зала</th>
                        <th>Название зала</th>
                        <th>Вместимость зала</th>
                    </tr>
                    <tr v-for="room in listRoom" :key="room.id">
                        <td>{{room.id}}</td>
                        <td>{{room.name}}</td>
                        <td>{{room.capacity}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "ReadingRoom",
        props: ['id'],
        data() {
            return {
                listRoom: [],
            }
        },
        created() {
            this.loadListReadingRoom()
        },
        methods: {
            async loadListReadingRoom() {
                this.listRoom = await fetch(
                    `http://127.0.0.1:8000/api/v1/reading_room/`
                ).then(response => response.json())
            },
        }
    }
</script>

<style scoped>

</style>