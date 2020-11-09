<template>
    <div>
        <mu-container>
        <mu-list>
            <mu-header><h3>Наши хореографы</h3></mu-header>
            <mu-list-item v-for="teach in teachers" avatar button :ripple="false">
                <mu-list-item-action>
                    <mu-avatar>
                        <img src="../assets/1.jpg">
                    </mu-avatar>
                </mu-list-item-action>
                <mu-list-item-title>{{teach.full_name}}</mu-list-item-title>
                <mu-list-item-action>
                    <mu-tooltip content="Узнать больше">
                    <mu-icon value="chat_bubble" @click="showTeacherInfo(teach.id)"></mu-icon>
                    </mu-tooltip>
                </mu-list-item-action>
                <OneTeacher :id="teach.id" v-if="show_teach_info===teach.id" @close="close"></OneTeacher>
            </mu-list-item>
        </mu-list>
        </mu-container>
    </div>
</template>

<script>
    import $ from "jquery";
    import OneTeacher from "./OneTeacher";

    export default {
        name: "Choreographers",
        data() {
            return {
                teachers: '',
                show_teach_info: '',
            }
        },
        components:{OneTeacher},
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadTeach()
        },
        methods: {
            loadTeach() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/teachers/",
                    type: "GET",
                    success: (response) => {
                        this.teachers = response.data.data
                    }
                })
            },
            showTeacherInfo(id) {
                this.show_teach_info = id
            },
            close() {
                this.show_teach_info = ''
            },
        }
    }
</script>

<style scoped>

</style>
