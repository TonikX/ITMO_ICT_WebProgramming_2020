<template>
    <div>
        <h2>Add information about a new teacher</h2>
        <mu-container>
            <mu-button color="#4db6ac" @click="returnHome">Home</mu-button>
            <mu-button color="#4db6ac" @click="previous">Back to Teachers list</mu-button>
            <mu-button color="#4db6ac" v-if="!auth" @click="goLogin">Log in</mu-button><br v-if="!auth"><br v-if="!auth">
            <mu-button color="#4db6ac" v-if="auth" @click="logout">Log out</mu-button><br v-if="auth"><br v-if="auth">
            <mu-row>
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="input" label="Name:">
                        <mu-text-field v-model="form.name"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="radio" label="Gender:">
                        <mu-radio v-model="form.gender" value="male" label="Male"></mu-radio>
                        <mu-radio v-model="form.gender" value="female" label="Female"></mu-radio>
                        <mu-radio v-model="form.gender" value="non-binary" label="Non-binary"></mu-radio>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Experience:">
                        <mu-text-field v-model="form.exp"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Subjects:">
                        <mu-select filterable multiple v-model="filterable" full-width>
                            <mu-option v-for="option,i in this.subjects" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Guide class:">
                        <mu-select v-model="form.selectCls">
                            <mu-option v-for="option,index in this.classes" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Room:">
                        <mu-select v-model="form.selectRoom">
                            <mu-option v-for="option,index in this.rooms" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-row>
            <mu-button color="#4db6ac" @click="sendTeacher">Confirm, then</mu-button>
            <mu-button color="#4db6ac" @click="editDependencies">add teacher</mu-button>
            <!-- <mu-button color="#4db6ac" @click="editClass">Update Classes table</mu-button> -->
            <!-- <mu-button color="#4db6ac" @click="editRoom">Update Rooms table</mu-button> -->
            <!-- <mu-button color="#4db6ac" @click="editTeaching">Update Teaching table</mu-button> -->
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
            subjects: '',
            classes: '',
            rooms: '',
            labelPosition: 'left',
            form: {
                name: '',
                gender: '',
                exp: '',
                selectCls: '',
                selectRoom: ''
            },
            filterable: []
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
                    this.teachers = response.data.data
                }
            })
        },
        loadSubject() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/subjects/",
                type: "GET",
                success: (response) => {
                    this.subjects_list = response.data.data
                    this.subjects = this.subjects_list.map(function (item) { return item.name })
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
        sendTeacher() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/teachers/",
                type: "POST",
                data: {
                    name: this.form.name,
                    gender: this.form.gender,
                    experience: this.form.exp,
                    subjects: this.filterable,
                    class: this.form.selectCls,
                    room: this.form.selectRoom
                },
                // success: (response) => {
                //     alert("New record added successfully.")
                //     this.$router.push({name: "teachers"})
                // }
            })
        },
        editClass() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/classes/",
                type: "PUT",
                data: {
                    name: this.form.selectCls,
                    guiding_teacher: this.form.name
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
                    number: this.form.selectRoom,
                    teacher: this.form.name
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
                    teacher: this.form.name,
                    subject: this.filterable
                },
                success: (response) => {
                    // alert("Teaching edited successfully.")
                    alert("New record added successfully.")
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
