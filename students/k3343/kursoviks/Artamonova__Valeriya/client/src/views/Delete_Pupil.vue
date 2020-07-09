<template>
    <mu-container>
            <mu-row>
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="select" label="Name:">
                        <mu-select v-model="form.name">
                            <mu-option v-for="option,index in this.pupils" :key="option" :label="option" :value="option">{{pupils.last_name}}</mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
            </mu-row>
            <mu-container class="button-wrapper2">
                <mu-button color="#5c6bc0" textColor="white" @click="deletePupil">Delete</mu-button>
            </mu-container>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Delete_Pupil",
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
        returnHome() {
            window.location = '/'
        },
        loadPupil() {
            $.ajax({
                url: "http://127.0.0.1:8000/api/v1/pupil/",
                type: "GET",
                success: (response) => {
                    this.pupils_list = response
                    this.pupils = this.pupils_list.map(function (item) { return item.name })
                }
            })
        },
        deletePupil() {
            $.ajax({
                url: "http://127.0.0.1:8000/api/v1/pupil/${this.id}/delete",
                type: "DELETE",
                data: {
                    first_name: this.form.name
                },
                success: (response) => {
                    alert("Record deleted successfully.")
                    // this.$router.push({name: "pupils"})
                    window.location = '/'
                }
            })
        }
    }
    }
</script>

<style scoped>

</style>