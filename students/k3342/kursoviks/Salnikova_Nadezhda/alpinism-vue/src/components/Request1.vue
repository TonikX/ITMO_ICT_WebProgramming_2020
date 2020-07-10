<template>
    <div>
        <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="goHome">Home</mu-button>
        </mu-container>

        <h1>Find all ascents to the specific mountain</h1>

        <br/>
        <h3>Please, select a mountain from the list below</h3>
        <mu-select v-model="mountain_name">
            <mu-option v-for="option,index in options.data" :key="option.mountain_name" :label="option.mountain_name"
                       :value="option.mountain_name"></mu-option>
        </mu-select>

        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="loadAnswer">Find</mu-button>
        </mu-container>

        <div v-for="answer in answers">
            <mu-container style="text-align: center">
                <mu-paper class="demo-paper" :z-depth="1" style="padding: 15px">
                    Ascent code: {{ answer.attributes.ascent_code }}
                    </br>
                    Ascent id: {{ answer.id }}
                    </br>
                    Group id: {{ answer.relationships.group.data.id }}
                    </br>
                    Started: {{ answer.attributes.start_date }}
                    </br>
                    Finished: {{ answer.attributes.end_date }}
                    <mu-divider></mu-divider>
                </mu-paper>
            </mu-container>
        </div>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Request1",
        data() {
            return {
                options: [],
                mountain_name: '',
                ascent: '',
                group: '',
                answers: {}
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            }),
                this.loadMountains()
        },
        methods: {
            loadMountains() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/mountains/',
                    type: 'GET',
                    success: (response) => {
                        this.options = response.data
                        console.log(response.data)
                    }
                })
            },
            loadAnswer() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/request1/',
                    type: 'GET',
                    data: {
                        mountain_name: this.mountain_name,
                    },
                    success: (response) => {
                        this.answers = response.data
                    },
                    error: (response) => {
                        console.log(response)
                    }
                })
            },
            showAnswers() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/groups/',
                    type: 'GET',
                    data: {
                        id: this.mountain_name,
                    },
                    success: (response) => {
                        this.answers = response.data
                    },
                    error: (response) => {
                        console.log(response)
                    }
                })
            },
            goHome() {
                this.$router.push({name: "main_page"})
            }
        }
    }
</script>

<style scoped>

</style>
