<template>
    <div>
        <h2>Change information about a pupil</h2>
        <mu-container>
            <mu-button color="#4db6ac" @click="returnHome">Home</mu-button>
            <mu-button color="#4db6ac" @click="previous">Back to Pupils list</mu-button>
            <mu-button color="#4db6ac" v-if="!auth" @click="goLogin">Log in</mu-button><br v-if="!auth"><br v-if="!auth">
            <mu-button color="#4db6ac" v-if="auth" @click="logout">Log out</mu-button><br v-if="auth"><br v-if="auth">
            <mu-row>
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="select" label="Name:">
                        <mu-select v-model="the_name">
                            <mu-option v-for="option,index in this.pupils" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-row>
            <mu-button color="#4db6ac" @click="loadOnePupil">Edit</mu-button>
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
            <mu-button v-if="the_pupil" color="#4db6ac" @click="editPupil">Submit</mu-button>
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
            this.$router.push({name: "pupils"})
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
                    this.the_pupil = response.data
                    this.name = response.data.attributes.name
                    this.gender = response.data.attributes.gender
                    this.study_class = response.data.relationships.study_class.data.id
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
                    id: this.the_pupil.id,
                    name: this.name,
                    gender: this.gender,
                    study_class: this.study_class,
                },
                success: (response) => {
                    alert("Record edited successfully.")
                    this.$router.push({name: "pupils"})
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
