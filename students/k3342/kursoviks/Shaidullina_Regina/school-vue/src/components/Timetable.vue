<template>
    <mu-container><br>
        <mu-container class="button-wrapper2">
            <!-- <mu-button v-if="auth" color="#5c6bc0" textColor="white" @click="">Update</mu-button> -->
            <mu-button v-if="auth" color="#5c6bc0" textColor="white" @click="add">Add</mu-button>
            <mu-button v-if="auth" color="#5c6bc0" textColor="white" @click="del">Delete</mu-button><br><br>
        </mu-container>
        <mu-container>
            <mu-paper>
                <mu-data-table border :columns="columns" :data="timetable">
                    <template slot-scope="scope">
                        <td class="is-left">{{ scope.row.study_class }}</td>
                        <td class="is-left">{{ scope.row.day_of_week }}</td>
                        <td class="is-left">{{ scope.row.lesson_num }}</td>
                        <td class="is-left">{{ scope.row.subject }}</td>
                        <td class="is-left">{{ scope.row.room }}</td>
                        <td class="is-left">{{ scope.row.teacher }}</td>
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
    name: 'Timetable',
    data() {
        return {
            timetable: '',
            columns: [
                { title: 'Class', name: 'class', align: 'center' },
                { title: 'Day of Week', name: 'day', align: 'center' },
                { title: 'Lesson number', name: 'lesson_num', align: 'center' },
                { title: 'Subject', name: 'subject', align: 'center' },
                { title: 'Room', name: 'room', align: 'center' },
                { title: 'Teacher', name: 'teacher', width: '250', align: 'center' }
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
        this.loadTimetable()
    },
    methods: {
        returnHome() {
            window.location = '/'
        },
        add() {
            this.$router.push({name: "timetable_add"})
        },
        del() {
            this.$router.push({name: "timetable_delete"})
        },
        loadTimetable() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/timetable/",
                type: "GET",
                success: (response) => {
                    this.timetable = response.data.data
                }
            })
        }
    }
}
</script>

<style scoped>
    .button-wrapper {
        text-align: center;
        .mu-button{
            margin: 8px;
        }
    }
</style>
