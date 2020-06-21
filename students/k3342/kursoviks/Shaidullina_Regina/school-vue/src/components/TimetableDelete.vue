<template>
    <div>
        <mu-container class="button-wrapper">
            <mu-button color="#5c6bc0" textColor="white" @click="returnHome">Home</mu-button><br>
        </mu-container>
        <h2>Delete a timetable entry</h2>
        <mu-container>
            <mu-row>
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="select" label="Weekday:">
                        <mu-select v-model="form.weekday">
                            <mu-option v-for="option,index in this.all_weekdays" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Class:">
                        <mu-select v-model="form.class">
                            <mu-option v-for="option,index in this.all_classes" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Lesson num:">
                        <mu-select v-model="form.lesson">
                            <mu-option v-for="option,index in this.all_lesson_nums" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
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
            <mu-button color="#5c6bc0" textColor="white" @click="deleteT">Delete</mu-button>
        </mu-container>
    </div>
</template>

<script>
/* eslint-disable */

export default {
    name: 'Timetable',
    data() {
        return {
            timetables: '',
            all_weekdays: '',
            all_classes: '',
            all_lesson_nums: '',
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
        this.loadT()
    },
    methods: {
        returnHome() {
            window.location = '/'
        },
        loadT() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/timetable/",
                type: "GET",
                success: (response) => {
                    this.timetables = response.data.data
                    this.all_weekdays = new Set(this.timetables.map(function (item) { return item.day_of_week }))
                    this.all_classes = new Set(this.timetables.map(function (item) { return item.study_class }))
                    this.all_lesson_nums = new Set(this.timetables.map(function (item) { return item.lesson_num }))
                    this.all_subjects = new Set(this.timetables.map(function (item) { return item.subject }))
                    this.all_rooms = new Set(this.timetables.map(function (item) { return item.room }))
                    this.all_teachers = new Set(this.timetables.map(function (item) { return item.teacher }))
                }
            })
        },
        deleteT() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/timetable/",
                type: "DELETE",
                data: {
                    day_of_week: this.form.weekday,
                    study_class: this.form.class,
                    lesson_num: this.form.lesson,
                    subject: this.form.subject,
                    room: this.form.room,
                    teacher: this.form.teacher,
                },
                success: (response) => {
                    alert("Timetable entry deleted successfully.")
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
