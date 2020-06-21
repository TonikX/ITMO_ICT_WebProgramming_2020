<template>
    <div>
        <mu-container class="button-wrapper">
            <mu-button color="#5c6bc0" textColor="white" @click="returnHome">Home</mu-button><br>
        </mu-container>
        <h2>Change information about a teacher</h2>
        <mu-container>
            <mu-row>
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="select" label="Name:">
                        <mu-select v-model="the_name">
                            <mu-option v-for="option,index in this.teachers" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-row>
            <mu-button color="#5c6bc0" textColor="white" @click="loadOneTeacher">Edit</mu-button>
            <mu-row v-if="the_teacher">
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="input" label="Name:">
                        <mu-text-field v-model="name"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Gender:">
                        <mu-text-field v-model="gender"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Experience:">
                        <mu-text-field v-model="experience"></mu-text-field>
                    </mu-form-item>
                    <!-- <mu-form-item prop="select" label="Subjects:">
                        <mu-select filterable multiple v-model="filterable" full-width>
                            <mu-option v-for="option,i in this.all_subjects" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item> -->
                    <mu-form-item prop="select" label="Guide class:">
                        <mu-select v-model="classs">
                            <mu-option v-for="option,index in this.classes" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Room:">
                        <mu-select v-model="room">
                            <mu-option v-for="option,index in this.rooms" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-row>
            <mu-container class="button-wrapper2">
                <mu-button v-if="the_teacher" color="#5c6bc0" textColor="white" @click="sendTeacher">Confirm</mu-button>
                <mu-button v-if="the_teacher" color="#5c6bc0" textColor="white" @click="editDependencies">update teacher</mu-button><br><br>
            </mu-container>
        </mu-container>
    </div>
</template>

<script>
/* eslint-disable */

export default {
    name: 'Teacher',
    data() {
        return {
            teachers: '',
            the_name: '',
            // all_subjects: '',
            classes: '',
            rooms: '',
            the_teacher: '',
            name: '',
            gender: '',
            experience: '',
            filterable: [],
            classs: '',
            room: '',
            prev_room: '',
            prev_class: '',
            labelPosition: 'left',
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
        // this.loadSubject()
        this.loadClass()
        this.loadRoom()
    },
    methods: {
        returnHome() {
            window.location = '/'
        },
        loadTeacher() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/teachers/",
                type: "GET",
                success: (response) => {
                    this.teachers_list = response.data.data
                    this.teachers = this.teachers_list.map(function (item) { return item.name })
                }
            })
        },
        loadOneTeacher() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/teacher/",
                type: "GET",
                data: {
                    name: this.the_name,
                },
                success: (response) => {
                    this.the_teacher = response.data.data
                    this.name = response.data.data.name
                    this.gender = response.data.data.gender
                    this.experience = response.data.data.experience
                    this.filterable = response.data.data.subjects
                    this.classs = response.data.data.class
                    this.room = response.data.data.room
                    this.prev_room = this.room
                    this.prev_class = this.classs
                }
            })
        },
        // loadSubject() {
        //     $.ajax({
        //         url: "http://127.0.0.1:8000/school/subjects/",
        //         type: "GET",
        //         success: (response) => {
        //             this.subjects_list = response.data.data
        //             this.all_subjects = this.subjects_list.map(function (item) { return item.name })
        //         }
        //     })
        // },
        loadClass() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/classes/",
                type: "GET",
                success: (response) => {
                    this.classes_list = response.data.data
                    this.classes = this.classes_list.map(function (item) { return item.name })
                }
            })
        },
        loadRoom() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/rooms/",
                type: "GET",
                success: (response) => {
                    this.rooms_list = response.data.data
                    this.rooms = this.rooms_list.map(function (item) { return item.number })
                }
            })
        },
        editTeacher() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/teachers/",
                type: "PUT",
                data: {
                    // id: this.the_teacher.id,
                    name: this.name,
                    gender: this.gender,
                    experience: this.experience,
                    subjects: this.filterable,
                    class: this.classs,
                    room: this.room
                },
                // success: (response) => {
                //     alert("Record edited successfully.")
                //     // this.$router.push({name: "teachers"})
                // }
            })
        },
        editClass() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/classes/",
                type: "PUT",
                data: {
                    name: this.classs,
                    guiding_teacher: this.name,
                    old_class: this.prev_class
                },
                // success: (response) => {
                //     alert("Class edited successfully.")
                // }
            })
        },
        editRoom() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/rooms/",
                type: "PUT",
                data: {
                    number: this.room,
                    teacher: this.name,
                    old_room: this.prev_room
                },
                success: (response) => {
                    // alert("Room edited successfully.")
                    alert("Record edited successfully.")
                    // this.$router.push({name: "teachers"})
                    window.location = '/'
                }
            })
        },
        // editTeaching() {
        //     $.ajax({
        //         url: "http://127.0.0.1:8000/school/teaching/",
        //         type: "PUT",
        //         data: {
        //             teacher: this.name,
        //             subject: this.filterable
        //         },
        //         success: (response) => {
        //             // alert("Teaching edited successfully.")
        //             alert("Record edited successfully.")
        //             this.$router.push({name: "teachers"})
        //         }
        //     })
        // },
        editDependencies() {
            this.editClass()
            this.editRoom()
            // this.editTeaching()
        },
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
