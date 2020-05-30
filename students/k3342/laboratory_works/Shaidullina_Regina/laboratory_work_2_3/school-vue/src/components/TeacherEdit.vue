<template>
    <div>
        <h2>Change information about a teacher</h2>
        <mu-container>
            <mu-button color="#4db6ac" @click="returnHome">Home</mu-button>
            <mu-button color="#4db6ac" @click="previous">Back to Teachers list</mu-button>
            <mu-button color="#4db6ac" v-if="!auth" @click="goLogin">Log in</mu-button><br v-if="!auth"><br v-if="!auth">
            <mu-button color="#4db6ac" v-if="auth" @click="logout">Log out</mu-button><br v-if="auth"><br v-if="auth">
            <mu-row>
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="select" label="Name:">
                        <mu-select v-model="the_name">
                            <mu-option v-for="option,index in this.teachers" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-row>
            <mu-button color="#4db6ac" @click="loadOneTeacher">Edit</mu-button>
            <mu-row v-if="the_teacher">
                <br>{{ the_teacher }}<br>
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
<!--                     <mu-form-item prop="select" label="Subjects:">
                        <mu-select v-model="subjects">
                            <mu-option v-for="option,i in this.all_subjects" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item> -->
                    <mu-form-item prop="select" label="Subjects:">
                        <mu-select filterable multiple v-model="filterable" full-width>
                            <mu-option v-for="option,i in this.all_subjects" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
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
            <mu-button v-if="the_teacher" color="#4db6ac" @click="sendTeacher">Confirm, then</mu-button>
            <mu-button v-if="the_teacher" color="#4db6ac" @click="editDependencies">update teacher</mu-button><br><br>
            <!-- <mu-button v-if="the_teacher" color="#4db6ac" @click="editTeacher">Update Teacher info</mu-button> -->
            <!-- <mu-button v-if="the_teacher" color="#4db6ac" @click="editClass">Update Classes table</mu-button> -->
            <!-- <mu-button v-if="the_teacher" color="#4db6ac" @click="editRoom">Update Rooms table</mu-button> -->
            <!-- <mu-button v-if="the_teacher" color="#4db6ac" @click="editTeaching">Update Teaching table</mu-button> -->
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
            all_subjects: '',
            classes: '',
            rooms: '',
            the_teacher: '',
            name: '',
            gender: '',
            experience: '',
            filterable: [],
            classs: '',
            room: '',
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
        this.loadSubject()
        this.loadClass()
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
        previous() {
            this.$router.push({name: "teachers"})
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
                }
            })
        },
        loadSubject() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/subjects/",
                type: "GET",
                success: (response) => {
                    this.subjects_list = response.data.data
                    this.all_subjects = this.subjects_list.map(function (item) { return item.name })
                }
            })
        },
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
                    id: this.the_teacher.id,
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
                    guiding_teacher: this.name
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
                    teacher: this.name
                },
                // success: (response) => {
                //     alert("Room edited successfully.")
                // }
            })
        },
        editTeaching() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/teaching/",
                type: "PUT",
                data: {
                    teacher: this.name,
                    subject: this.filterable
                },
                success: (response) => {
                    // alert("Teaching edited successfully.")
                    alert("Record edited successfully.")
                    this.$router.push({name: "teachers"})
                }
            })
        },
        editDependencies() {
            this.editClass()
            this.editRoom()
            this.editTeaching()
        },
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
        font-size: 16px; font-weight: 400; text-align: center;
    }
</style>
