<template>
    <mu-container class="demo-text" style="width: 1536px" >
        <mu-tabs color=#616161 full-width>
            <mu-tab active="0" @click="loadmain">Workshops</mu-tab>
            <mu-tab active="1" @click="loadPers">Клиенты</mu-tab>
            <mu-tab active="2">Хореографы</mu-tab>
            <mu-tab active="3">Отчеты</mu-tab>
        </mu-tabs>
        <div><Workshops v-if="active==0"></Workshops></div>
        <div v-if="active == 1">
            <mu-container v-for="person in persons">
                {{ person.fullname }}
            </mu-container>
        </div>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Workshops from "./Workshops";
    export default {
        name: "Main",
        components: {Workshops},
        data() {
            return {
                persons: '',
                active: 0,
            }
        },
        methods: {
            loadPers() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/part/",
                    type: "GET",
                    success: (response) => {
                        this.persons = response.data.data
                        this.active = 1
                    }
                })
            },
            loadmain(){
                this.active = 0
            }
        }

    }
</script>


<style scoped>
    .demo-text {
        height: 100%;
    }
</style>
