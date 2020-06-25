<template>
    <mu-container>
            <mu-row>
                <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="select" label="Name:">
                        <mu-select v-model="form.name">
                            <mu-option v-for="option,index in this.childrens" :key="option" :label="option" :value="option">{{childrens.surname}}</mu-option>
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
        name: "Delete_children",
    data() {
        return {
            childrens: '',
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
        this.loadChildren()
    },
    methods: {
        returnHome() {
            window.location = '/'
        },
        loadChildren() {
            $.ajax({
                url: "http://127.0.0.1:8000/api/v1/children/",
                type: "GET",
                success: (response) => {
                    this.childrens_list = response
                    this.childrens = this.childrens_list.map(function (item) { return item.name })
                }
            })
        },
        deleteChildren() {
            $.ajax({
                url: "http://127.0.0.1:8000/api/v1/children/${this.id}/delete",
                type: "DELETE",
                data: {
                    name: this.form.name
                },
                success: (response) => {
                    alert("Record deleted successfully.")
                    // this.$router.push({name: "childrens"})
                    window.location = '/'
                }
            })
        }
    }
    }
</script>

<style scoped>
</style>