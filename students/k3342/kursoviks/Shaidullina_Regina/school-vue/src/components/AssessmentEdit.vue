<template>
    <div>
        <mu-container class="button-wrapper">
            <mu-button color="#5c6bc0" textColor="white" @click="returnHome">Home</mu-button><br>
        </mu-container>
        <h2>Change a grade</h2>
        <mu-container>
            <mu-row>
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="input" label="Term:">
                        <mu-text-field v-model="the_term"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Pupil:">
                        <mu-select v-model="the_pupil">
                            <mu-option v-for="option,index in this.all_pupils" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Subject:">
                        <mu-select v-model="the_subject">
                            <mu-option v-for="option,index in this.all_subjects" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
                </mu-form>
            </mu-row>
            <mu-button color="#5c6bc0" textColor="white" @click="loadOneGrade">Edit</mu-button>
            <mu-row v-if="the_grade">
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="radio" label="Grade:">
                        <mu-text-field v-model="the_one_grade"></mu-text-field>
                    </mu-form-item>
                </mu-form>
            </mu-row>
            <mu-button v-if="the_grade" color="#5c6bc0" textColor="white" @click="editGrade">Submit</mu-button>
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
            the_term: '',
            the_pupil: '',
            the_subject: '',
            the_grade: '',
            the_one_grade: '',
            prev_grade: '',
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
        this.loadPupils()
        this.loadSubjects()
    },
    methods: {
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
        loadOneGrade() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/assessment/",
                type: "GET",
                data: {
                    term: this.the_term,
                    pupil: this.the_pupil,
                    subject: this.the_subject,
                },
                success: (response) => {
                    this.the_grade = response.data.data
                    this.the_one_grade = response.data.data.grade
                    this.prev_grade = this.the_one_grade
                }
            })
        },
        editGrade() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/assessments/",
                type: "PUT",
                data: {
                    term: this.the_term,
                    pupil: this.the_pupil,
                    subject: this.the_subject,
                    grade: this.the_one_grade,
                    old_grade: this.prev_grade
                },
                success: (response) => {
                    alert("Record edited successfully.")
                    // this.$router.push({name: "assessments"})
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
