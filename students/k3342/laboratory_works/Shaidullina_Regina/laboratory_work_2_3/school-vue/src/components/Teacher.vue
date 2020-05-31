<template>
    <mu-container>
        <br><!-- <h2>Teachers</h2> -->
        <mu-container class="button-wrapper2">
            <mu-button v-if="auth" color="#5c6bc0" textColor="white" @click="upd">Update</mu-button>
            <mu-button v-if="auth" color="#5c6bc0" textColor="white" @click="add">Add</mu-button>
            <mu-button v-if="auth" color="#5c6bc0" textColor="white" @click="del">Delete</mu-button><br><br>
        </mu-container>
<!--             <mu-button color="#5c6bc0" textColor="white" @click="returnHome">Home</mu-button>
            <mu-button color="#5c6bc0" textColor="white" v-if="!auth" @click="goLogin">Log in</mu-button><br v-if="!auth"><br v-if="!auth">
            <mu-button color="#5c6bc0" textColor="white" v-if="auth" @click="logout">Log out</mu-button><br v-if="auth"><br v-if="auth"> -->
        <mu-container>
            <mu-paper>
                <mu-data-table border :columns="columns" :data="teachers">
                    <template slot-scope="scope">
                        <td class="is-left">{{ scope.row.name }}</td>
                        <td class="is-left">{{ scope.row.gender }}</td>
                        <td class="is-left">{{ scope.row.experience }}</td>
                        <td class="is-left"><p v-for='s in scope.row.subjects'>{{ s }}</p></td>
                        <td class="is-left"><p v-if="scope.row.class">{{ scope.row.class }}</p><p v-else>None</p></td>
                        <td class="is-left"><p v-if="scope.row.room">{{ scope.row.room }}</p><p v-else>None</p></td>
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
    name: 'Teacher',
    data() {
        return {
            teachers: '',
            columns: [
                { title: 'Name', name: 'name', align: 'center', width: '280' },
                { title: 'Gender', name: 'gender', align: 'center' },
                { title: 'Experience', name: 'experience', align: 'center' },
                { title: 'Subjects', name: 'subjects', align: 'center', width: '190' },
                { title: 'Guided class', name: 'class', align: 'center' },
                { title: 'Room', name: 'room', align: 'center' }
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
        this.loadTeacher()
    },
    methods: {
        // goLogin() {
        //     this.$router.push({name: "login"})
        // },
        // logout() {
        //     sessionStorage.removeItem("auth_token")
        //     window.location = '/'
        // },
        returnHome() {
            window.location = '/'
        },
        add() {
            this.$router.push({name: "teachers_add"})
        },
        upd() {
            this.$router.push({name: "teachers_edit"})
        },
        del() {
            this.$router.push({name: "teachers_delete"})
        },
        loadTeacher() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/teachers/",
                type: "GET",
                success: (response) => {
                    this.teachers = response.data.data
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
    },
    .button-wrapper2 {
        text-align: center;
        .mu-button{
            margin: 8px;
        }
    }
</style>
