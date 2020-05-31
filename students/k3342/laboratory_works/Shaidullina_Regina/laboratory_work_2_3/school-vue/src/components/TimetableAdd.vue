<template>
    <div>
        <mu-container class="button-wrapper">
            <mu-button color="#5c6bc0" textColor="white" @click="returnHome">Home</mu-button><br>
        </mu-container>
        <h2>Add a timetable entry</h2>
        <mu-container>
            <mu-row>
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="input" label="Weekday:">
                        <mu-text-field v-model="form.weekday" help-text="3 letters, first capital"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Class:">
                        <mu-select v-model="form.class">
                            <mu-option v-for="option,index in this.all_classes" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Lesson num:">
                        <mu-text-field v-model="form.lesson"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Subject:">
                        <mu-select v-model="form.subject">
                            <mu-option v-for="option,index in this.all_subjects" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Room:">
                        <mu-select v-model="form.room">
                            <mu-option v-for="option,index in this.all_rooms" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Teacher:">
                        <mu-select v-model="form.teacher">
                            <mu-option v-for="option,index in this.all_teachers" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-row>
            <mu-button color="#5c6bc0" textColor="white" @click="sendT">Add</mu-button>
        </mu-container>
    </div>
</template>

<script>
/* eslint-disable */

export default {
    name: 'Timetable',
    data() {
        return {
            all_classes: '',
            all_subjects: '',
            all_rooms: '',
            all_teachers: '',
            labelPosition: 'left',
            form: {
                weekday: '',
                class: '',
                lesson: '',
                subject: '',
                room: '',
                teacher: ''
            },
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
        this.loadClasses()
        this.loadSubjects()
        this.loadRooms()
        this.loadTeachers()
    },
    methods: {
        returnHome() {
            window.location = '/'
        },
        loadClasses() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/classes/",
                type: "GET",
                success: (response) => {
                    this.classes = response.data.data
                    this.all_classes = this.classes.map(function (item) { return item.name })
                }
            })
        },
        loadSubjects() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/subjects/",
                type: "GET",
                success: (response) => {
                    this.subjects = response.data.data
                    this.all_subjects = this.subjects.map(function (item) { return item.name })
                }
            })
        },
        loadRooms() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/rooms/",
                type: "GET",
                success: (response) => {
                    this.rooms = response.data.data
                    this.all_rooms = this.rooms.map(function (item) { return item.number })
                }
            })
        },
        loadTeachers() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/teachers/",
                type: "GET",
                success: (response) => {
                    this.teachers = response.data.data
                    this.all_teachers = this.teachers.map(function (item) { return item.name })
                }
            })
        },
        sendT() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/timetable/",
                type: "POST",
                data: {
                    day_of_week: this.form.weekday,
                    study_class: this.form.class,
                    lesson_num: this.form.lesson,
                    subject: this.form.subject,
                    room: this.form.room,
                    teacher: this.form.teacher,
                },
                success: (response) => {
                    alert("New timetable entry added successfully.")
                    window.location = '/'
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
    .button-wrapper {
        text-align: right;
        .mu-button{
            margin: 8px;
        }
    },
    .button-wrapper2 {
        text-align: center;
        .mu-button{
            margin: 8px;
        }
    }
</style>
