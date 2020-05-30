<template>
    <div>
        <mu-container>
            <mu-row>
                <mu-col span="4"><div class="grid-cell"></div></mu-col>
                <mu-col span="4"><div class="grid-cell">
                    <h1>School</h1>
                </div></mu-col>
                <mu-col span="4"><div class="grid-cell">
                    <mu-button v-if="!auth" color="#4db6ac" @click="goLogin">Log in</mu-button>
                    <mu-button v-if="auth" color="#4db6ac" @click="logout">Log out</mu-button>
                </div></mu-col>
            </mu-row>
            <mu-row>
                <mu-container>
                    <mu-button v-if="auth" color="#4db6ac" @click="">Queries</mu-button>
                    <mu-button v-if="auth" color="#4db6ac" @click="">Report</mu-button><br><br>
                    <mu-button v-if="auth" color="#4db6ac" @click="getTimetable">Timetable</mu-button>
                    <mu-button v-if="auth" color="#4db6ac" @click="getTeachers">Teachers</mu-button>
                    <mu-button v-if="auth" color="#4db6ac" @click="getPupils">Pupils</mu-button>
                    <mu-button v-if="auth" color="#4db6ac" @click="getAssessments">Assessments</mu-button>
                    <mu-button v-if="auth" color="#4db6ac" @click="getClasses">Classes</mu-button>
                    <mu-button v-if="auth" color="#4db6ac" @click="getSubjects">Subjects</mu-button>
                    <mu-button v-if="auth" color="#4db6ac" @click="getRooms">Rooms</mu-button>
                </mu-container>
            </mu-row>
            <mu-row>
                <mu-container>
                    <br><br><img width="350" src="https://cdn.shopify.com/s/files/1/2562/6932/articles/teacher-tired-humor-teacher-memes-funny_1200x679_crop_top.jpg?v=1518395627">
                    <!-- <timetable v-if="auth"></timetable> -->
                </mu-container>
            </mu-row>
        </mu-container>
    </div>
</template>

<script>
/* eslint-disable */

// import Timetable from '@/components/Timetable.vue'

export default {
    name: 'Home',
    // components: {
    //     Timetable
    // },
    computed: {
        auth() {
            if (sessionStorage.getItem("auth_token")) {
                return true
            }
        }
    },
    methods: {
        goLogin() {
            this.$router.push({name: "login"})
        },
        logout() {
            sessionStorage.removeItem("auth_token")
            window.location = '/'
        },
        getTeachers() {
            this.$router.push({name: "teachers"})
        },
        getPupils() {
            this.$router.push({name: "pupils"})
        },
        getClasses() {
            this.$router.push({name: "classes"})
        },
        getSubjects() {
            this.$router.push({name: "subjects"})
        },
        getRooms() {
            this.$router.push({name: "rooms"})
        },
        getAssessments() {
            this.$router.push({name: "assessments"})
        },
        getTimetable() {
            this.$router.push({name: "timetable"})
        }
    }
}
</script>

<style scoped>
    h1 {
        font-size: 60px; 
        font-weight: 300;
        text-align: center;
        color: #004d40;
    }
</style>
