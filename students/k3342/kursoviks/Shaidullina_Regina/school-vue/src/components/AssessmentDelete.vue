<template>
    <div>
        <mu-container class="button-wrapper">
            <mu-button color="#5c6bc0" textColor="white" @click="returnHome">Home</mu-button><br>
        </mu-container>
        <h2>Delete a grade</h2>
        <mu-container>
            <mu-row>
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="input" label="Term:">
                        <mu-select v-model="form.term">
                            <mu-option v-for="option,index in this.all_terms" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
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
            <mu-button color="#5c6bc0" textColor="white" @click="deleteGrade">Delete</mu-button>
        </mu-container>
    </div>
</template>

<script>
/* eslint-disable */

export default {
    name: 'Assessment',
    data() {
        return {
            all_terms: '',
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
        this.loadA()
    },
    methods: {
        returnHome() {
            window.location = '/'
        },

        loadA() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/assessments/",
                type: "GET",
                success: (response) => {
                    this.grades = response.data.data
                    this.all_terms = new Set(this.grades.map(function (item) { return item.term }))
                    this.all_pupils = new Set(this.grades.map(function (item) { return item.pupil }))
                    this.all_subjects = new Set(this.grades.map(function (item) { return item.subject }))
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
