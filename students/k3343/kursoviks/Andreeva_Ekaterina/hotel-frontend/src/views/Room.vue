<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Номера</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table width="60%">
                    <tr>
                        <th colspan="2">Типы номеров в гостинице</th>
                    </tr>
                    <tr>
                        <th>Тип номера</th>
                        <th>Стоимость проживания в сутки</th>
                    </tr>
                    <tr v-for="roomtype in listRoomType" :key="roomtype.id">
                        <td>
                            {{roomtype.room_type}}
                        </td>
                        <td>
                            {{roomtype.price}}
                        </td>
                    </tr>
                </table>
                <br>
                <mu-button color="primary" @click="showRoom">Показать все номера</mu-button>
            </mu-col>
        </mu-row>
        <mu-row v-if="isRoomVisible" align="center">
            <mu-col>
                <ul>
                    <li v-for="room in listRoom" :key="room.id">
                       Номер {{room.room_number}}
                        <table v-if="isRoomDetailVisible">
                            <tr>
                                <th>Этаж</th>
                                <th>Тип номера</th>
                                <th>Номер телефона</th>
                            </tr>
                            <tr>
                                <td>{{room.floor}}</td>
                                <td>{{room.room_type}}</td>
                                <td>{{room.phone_number}}</td>
                            </tr>
                        </table>
                    </li>
                </ul>
                <mu-button @click="showRoomDetail">Показать информацию о номерах</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
    
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Room",
        props: ['id'],
        components: {},
        data() {
            return {
                listRoom: [],
                listRoomType: [],
                isRoomVisible: false,
                isRoomDetailVisible: false,
            }
        },
        created() {
            this.loadListRoom()
            this.loadListRoomType()
        },
        methods: {
            async loadListRoom() {
                this.listRoom = await fetch(
                    `http://127.0.0.1:8000/api/v1/room/`
                ).then(response => response.json())
            },
            showRoom(){
              this.isRoomVisible = !this.isRoomVisible
            },
            showRoomDetail(){
              this.isRoomDetailVisible = !this.isRoomDetailVisible
            },
            async loadListRoomType() {
                this.listRoomType = await fetch(
                    `http://127.0.0.1:8000/api/v1/roomtype/`
                ).then(response => response.json())
            },

        }
    }
</script>

<style scoped>

</style>