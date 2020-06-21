<template>
    <div>
        <mu-container class="button-wrapper">
            <mu-button color="#5c6bc0" textColor="white" @click="returnHome">Home</mu-button><br>
        </mu-container>
        <h2>Change information about a pupil</h2>
        <mu-container>
            <mu-row>
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="select" label="Name:">
                        <mu-select v-model="the_name">
                            <mu-option v-for="option,index in this.pupils" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-row>
            <mu-button color="#5c6bc0" textColor="white" @click="loadOnePupil">Edit</mu-button>
            <mu-row v-if="the_pupil">
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="input" label="Name:">
                        <mu-text-field v-model="name"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Gender:">
                        <mu-text-field v-model="gender"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Class:">
                        <mu-select v-model="study_class">
                            <mu-option v-for="option,index in this.classes" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-row>
            <mu-container class="button-wrapper2">
                <mu-button v-if="the_pupil" color="#5c6bc0" textColor="white" @click="editPupil">Submit</mu-button>
            </mu-container>
        </mu-container>
    </div>
</template>

<script>
/* eslint-disable */

export default {
    name: 'Pupil',
    data() {
        return {
            pupils: '',
            the_name: '',
            name: '',
            gender: '',
            study_class: '',
            the_pupil: '',
            classes: '',
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
        this.loadPupil()
        this.loadClass()
    },
    methods: {
        returnHome() {
            window.location = '/'
        },
        loadPupil() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/pupils/",
                type: "GET",
                success: (response) => {
                    this.pupils_list = response.data.data
                    this.pupils = this.pupils_list.map(function (item) { return item.name })
                }
            })
        },
        loadOnePupil() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/pupil/",
                type: "GET",
                data: {
                    name: this.the_name,
                },
                success: (response) => {
                    this.the_pupil = response.data.data
                    this.name = response.data.data.name
                    this.gender = response.data.data.gender
                    this.study_class = response.data.data.study_class
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
        editPupil() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/pupils/",
                type: "PUT",
                data: {
                    name: this.name,
                    gender: this.gender,
                    study_class: this.study_class,
                },
                success: (response) => {
                    alert("Record edited successfully.")
                    // this.$router.push({name: "pupils"})
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
