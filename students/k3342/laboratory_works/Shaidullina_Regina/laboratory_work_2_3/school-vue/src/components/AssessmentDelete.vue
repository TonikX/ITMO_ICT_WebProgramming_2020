<template>
    <div>
        <h2>Delete a grade</h2>
        <mu-container>
            <mu-button color="#4db6ac" @click="returnHome">Home</mu-button>
            <mu-button color="#4db6ac" @click="previous">Back to Assessment Table</mu-button>
            <mu-button color="#4db6ac" v-if="!auth" @click="goLogin">Log in</mu-button><br v-if="!auth"><br v-if="!auth">
            <mu-button color="#4db6ac" v-if="auth" @click="logout">Log out</mu-button><br v-if="auth"><br v-if="auth">
            <mu-row>
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="input" label="Term:">
                        <mu-text-field v-model="form.term"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Pupil:">
                        <mu-select v-model="form.pupil">
                            <mu-option v-for="option,index in this.all_pupils" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Subject:">
                        <mu-select v-model="form.subject">
                            <mu-option v-for="option,index in this.all_subjects" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-row>
            <mu-button color="#4db6ac" @click="deleteGrade">Delete</mu-button>
        </mu-container>
    </div>
</template>

<script>
/* eslint-disable */

export default {
    name: 'Assessment',
    data() {
        return {
            all_pupils: '',
            all_subjects: '',
            labelPosition: 'left',
            form: {
                term: '',
                pupil: '',
                subject: '',
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
        this.loadPupils()
        this.loadSubjects()
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
            this.$router.push({name: "assessments"})
        },
        loadPupils() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/pupils/",
                type: "GET",
                success: (response) => {
                    this.pupils_list = response.data.data
                    this.all_pupils = this.pupils_list.map(function (item) { return item.name })
                }
            })
        },
        loadSubjects() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/subjects/",
                type: "GET",
                success: (response) => {
                    this.subjects_list = response.data.data
                    this.all_subjects = this.subjects_list.map(function (item) { return item.name })
                }
            })
        },
        deleteGrade() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/assessments/",
                type: "DELETE",
                data: {
                    term: this.form.term,
                    pupil: this.form.pupil,
                    subject: this.form.subject,
                },
                success: (response) => {
                    alert("Record deleted successfully.")
                    this.$router.push({name: "assessments"})
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
        font-size: 16px; font-weight: 400; text-align: center;
    }
</style>
