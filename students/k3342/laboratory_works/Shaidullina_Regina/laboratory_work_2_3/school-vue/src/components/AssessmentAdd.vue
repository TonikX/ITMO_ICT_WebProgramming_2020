<template>
    <div>
        <mu-container class="button-wrapper">
            <mu-button color="#5c6bc0" textColor="white" @click="returnHome">Home</mu-button><br>
        </mu-container>
        <h2>Add a new grade</h2>
        <mu-container>
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
                    <mu-form-item prop="radio" label="Grade:">
                        <mu-radio v-model="form.grade" value="2" label="2"></mu-radio>
                        <mu-radio v-model="form.grade" value="3" label="3"></mu-radio>
                        <mu-radio v-model="form.grade" value="4" label="4"></mu-radio>
                        <mu-radio v-model="form.grade" value="5" label="5"></mu-radio>
                    </mu-form-item>
                </mu-form>
            </mu-row>
            <mu-button color="#5c6bc0" textColor="white" @click="sendGrade">Add</mu-button>
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
                grade: ''
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
        returnHome() {
            window.location = '/'
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
        sendGrade() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/assessments/",
                type: "POST",
                data: {
                    term: this.form.term,
                    pupil: this.form.pupil,
                    subject: this.form.subject,
                    grade: this.form.grade
                },
                success: (response) => {
                    alert("New record added successfully.")
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
