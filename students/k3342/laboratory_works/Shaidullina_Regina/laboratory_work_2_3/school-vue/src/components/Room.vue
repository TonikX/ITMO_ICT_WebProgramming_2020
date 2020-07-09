<template>
    <mu-container><h2>Rooms</h2>
        <mu-container>
            <mu-paper>
                <mu-data-table border :columns="columns" :data="rooms">
                    <template slot-scope="scope">
                        <td class="is-left">{{ scope.row.number }}</td>
                        <td class="is-left">{{ scope.row.floor }}</td>
                        <td class="is-left">{{ scope.row.subject }}</td>
                        <td class="is-left"><p v-if="scope.row.teacher">{{ scope.row.teacher }}</p><p v-else>None</p></td>
                    </template>
                </mu-data-table>
            </mu-paper>
            <br><br>
        </mu-container>
    </mu-container>
</template>

<script>
/* eslint-disable */

export default {
    name: 'Room',
    data() {
        return {
            rooms: '',
            columns: [
                { title: 'Room', name: 'room', align: 'center', width: '200' },
                { title: 'Floor', name: 'floor', align: 'center', width: '150' },
                { title: 'Subject', name: 'subject', align: 'center', width: '340' },
                { title: 'Teacher', name: 'subject', align: 'center', width: '401' },
            ]
        }
    },
    computed: {
        auth() {
            if (sessionStorage.getItem("auth_token")) {
                return true
            }
        }
    },
    created() {
        $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.loadRoom()
    },
    methods: {
        returnHome() {
            window.location = '/'
        },
        loadRoom() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/rooms/",
                type: "GET",
                success: (response) => {
                    this.rooms = response.data.data
                }
            })
        }
    }
}
</script>

<style scoped>
    h2 {
        font-size: 48px; 
        font-weight: 400;
        text-align: center;
        color: #1a237e;
    }
</style>
