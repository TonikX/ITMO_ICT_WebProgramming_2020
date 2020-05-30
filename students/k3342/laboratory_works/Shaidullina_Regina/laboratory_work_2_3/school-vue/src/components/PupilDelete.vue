<template>
    <div>
        <h2>Choose the pupil to delete info about</h2>
        <mu-container>
            <mu-button color="#4db6ac" @click="returnHome">Home</mu-button>
            <mu-button color="#4db6ac" @click="previous">Back to Pupils list</mu-button>
            <mu-button color="#4db6ac" v-if="!auth" @click="goLogin">Log in</mu-button><br v-if="!auth"><br v-if="!auth">
            <mu-button color="#4db6ac" v-if="auth" @click="logout">Log out</mu-button><br v-if="auth"><br v-if="auth">
            <mu-row>
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="select" label="Name:">
                        <mu-select v-model="form.name">
                            <mu-option v-for="option,index in this.pupils" :key="option" :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-row>
            <mu-button color="#4db6ac" @click="deletePupil">Delete</mu-button>
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
            labelPosition: 'left',
            form: {
                name: '',
            }
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
        deletePupil() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/pupils/",
                type: "DELETE",
                data: {
                    name: this.form.name
                },
                success: (response) => {
                    alert("Record deleted successfully.")
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
