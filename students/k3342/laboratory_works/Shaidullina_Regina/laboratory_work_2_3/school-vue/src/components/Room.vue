<template>
    <div>
        <h2>Rooms</h2>
        <mu-container>
            <mu-button color="#4db6ac" @click="returnHome">Home</mu-button>
            <mu-button color="#4db6ac" v-if="!auth" @click="goLogin">Log in</mu-button><br v-if="!auth"><br v-if="!auth">
            <mu-button color="#4db6ac" v-if="auth" @click="logout">Log out</mu-button><br v-if="auth"><br v-if="auth">
            <mu-paper>
                <p v-for='room in rooms' v-bind:key="room.number">
                    Room {{ room.number }} is located on the floor {{ room.floor }}.<br>
                    It is the primary room for {{ room.subject.name }}, a {{ room.subject.sub_type }} subject.<br>
                    Assigned teacher: <span v-if="room.teacher">{{ room.teacher.name }}</span><span v-else>None</span>
                </p>
            </mu-paper>
        </mu-container>
    </div>
</template>

<script>
/* eslint-disable */

export default {
    name: 'Room',
    data() {
        return {
            rooms: '',
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
        goLogin() {
            this.$router.push({name: "login"})
        },
        logout() {
            sessionStorage.removeItem("auth_token")
            window.location = '/'
        },
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
        color: #004d40;
    },
    p {
        font-size: 16px; font-weight: 400;
    }
</style>
