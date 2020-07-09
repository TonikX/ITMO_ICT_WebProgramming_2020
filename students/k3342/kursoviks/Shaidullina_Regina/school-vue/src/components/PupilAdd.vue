<template>
    <div>
        <mu-container class="button-wrapper">
            <mu-button color="#5c6bc0" textColor="white" @click="returnHome">Home</mu-button><br>
        </mu-container>
        <h2>Add information about a new pupil</h2>
        <mu-container>
            <mu-row>
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="input" label="Name:">
                        <mu-text-field v-model="form.name"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="radio" label="Gender:">
                        <mu-radio v-model="form.gender" value="male" label="Male"></mu-radio>
                        <mu-radio v-model="form.gender" value="female" label="Female"></mu-radio>
                        <!-- <mu-radio v-model="form.gender" value="non-binary" label="Non-binary"></mu-radio> -->
                    </mu-form-item>
                    <mu-form-item prop="select" label="Class:">
                        <mu-select v-model="form.selectCls">
                            <mu-option v-for="option,index in this.classes" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-row>
            <mu-container class="button-wrapper2">
                <mu-button color="#5c6bc0" textColor="white" @click="sendPupil">Add</mu-button>
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
            classes: '',
            labelPosition: 'left',
            form: {
                name: '',
                gender: '',
                selectCls: '',
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
                    this.pupils = response.data.data
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
        sendPupil() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/pupils/",
                type: "POST",
                data: {
                    name: this.form.name,
                    gender: this.form.gender,
                    study_class: this.form.selectCls,
                },
                success: (response) => {
                    alert("New record added successfully.")
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
