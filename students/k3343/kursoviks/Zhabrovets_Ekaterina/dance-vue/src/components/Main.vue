<template>
    <!--        <link rel="stylesheet" href="../../static/material-icons.css">-->
    <!--        <link rel="stylesheet" href="../../static/style.css">-->
    <!--        <link rel="stylesheet" href="../../static/bootstrap.min.css">-->
    <!--        <link rel="stylesheet" href="../../static/font-awesome.min.css">-->
    <!--        <link rel="stylesheet" href="../../static/templatemo-gray.css">-->

    <!--    <h1 style="color: white;">Hello welcome!</h1></video-background>-->
    <div>
<!--        <div v-if="is_superuser">
            <mu-tabs color="primary" full-width>
                <mu-tab active="0" @click="loadmain">Workshops</mu-tab>
                <mu-tab active="1" @click="loadPers">Клиенты</mu-tab>
                <mu-tab active="2" @click="loadChor">Хореографы</mu-tab>
            </mu-tabs>
        </div>
        <div v-else>-->
            <mu-tabs color="primary" full-width>
                <mu-tab active="0" @click="loadcomp(0)">Афиша</mu-tab>
                <mu-tab active="1" @click="loadcomp(1)">Мои мастер-классы</mu-tab>
                <mu-tab active="2" @click="loadcomp(2)">Хореографы</mu-tab>
                <mu-tab active="3" @click="loadcomp(3)">Топ посетителей</mu-tab>
                <mu-tab active="5" v-if="is_superuser" @click="loadcomp(5)">Отчет по школам</mu-tab>
                <mu-tab>
                    <mu-menu>Мой профиль
                        <mu-list slot="content">
                            <mu-list-item button @click="loadcomp(4)">
                                <mu-list-item-content>
                                    <mu-list-item-title>Данные профиля</mu-list-item-title>
                                </mu-list-item-content>
                            </mu-list-item>
<!--                            <mu-list-item button v-if="is_teacher" @click=''>-->
<!--                                <mu-list-item-content>-->
<!--                                    <mu-list-item-title>Моя бизнес-информация</mu-list-item-title>-->
<!--                                </mu-list-item-content>-->
                            </mu-list-item>
                            <mu-list-item button  @click="logout">
                                <mu-list-item-content>
                                    <mu-list-item-title>Выход</mu-list-item-title>
                                </mu-list-item-content>
                            </mu-list-item>
                        </mu-list>
                    </mu-menu>
                </mu-tab>
            </mu-tabs>
<!--        </div>-->
        <div>
            <Workshops v-if="active===0"></Workshops>
            <MyWorkshops v-else-if="active===1"></MyWorkshops>
            <Choreographers v-else-if="active===2"></Choreographers>
            <TopUsers v-else-if="active===3"></TopUsers>
            <SchoolReport v-else-if="active===5"></SchoolReport>
            <AboutMe :id_login_user="id_login_user" v-else-if="active===4"></AboutMe>
        </div>
    </div>
</template>

<script>
    import $ from 'jquery'
    import Workshops from "./Workshops";
    import EditPart from "./EditPart";
    import MyWorkshops from "./MyWorkshops";
    import AboutMe from "./AboutMe";
    import Choreographers from "./Choreographers";
    import TopUsers from "./TopUsers";
    import SchoolReport from "./SchoolReport";

    export default {
        name: "Main",
        components: {SchoolReport, TopUsers, Choreographers, AboutMe, MyWorkshops, Workshops, EditPart},
        data() {
            return {
                active: 0,
                reports: '',
                teachers: '',
                show_n: '',
                w: '',
                show_edit: '',
                is_teacher: '',
                is_superuser: '',
                id_login_user: '',
                cols: [{title: 'Название школы', width: 220, name: 'name'}, {
                    title: 'Количество прошедших мастер-классов',
                    width: 200,
                    name: 'number_prev',
                    align: 'center'
                }, {title: 'Выручка(руб.)', width: 250, name: 'gained_profit', align: 'center'}, {
                    title: 'Количество грядущих мастер-классов',
                    width: 200,
                    name: 'number_fut',
                    align: 'center'
                }, {title: 'Ожид. прибыль(руб.)', width: 250, name: 'fut_profit', align: 'center'}]
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadInfo()
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
            loadcomp(num) {
                this.active = num
            },
            loadRep() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/report/",
                    type: "GET",
                    success: (response) => {
                        this.reports = response.data.data
                        this.active = 5
                    }
                })
            },
            loadInfo() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/user_info/",
                    type: "GET",
                    success: (response) => {
                        this.is_teacher = response.data.data.is_teacher
                        this.is_superuser = response.data.data.is_superuser
                        this.id_login_user = response.data.data.id
                    },
                    error: (response) => {
                        console.log(this.date_end)
                    }
                })
            },
            logout() {
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            },

            // showNear(i) {
            //     $.ajax({
            //         url: "http://127.0.0.1:8000/api/v1/dance/wsh_nearest/",
            //         type: "GET",
            //         data: {
            //             choreographer: i,
            //         },
            //         success: (response) => {
            //             this.w = response.data.data
            //             this.show_n = i
            //         }
            //     })
            // },
        },
    }
</script>

<style scoped>
    .demo-text {
        height: 100%;
    }

    .strange {
        text-align: left
    }

    .flex-wrapper {
        width: 100%;
        height: 56px;
    }

    .bar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
    }

    html, body {

        background-color: #000;

        font-family: 'Nunito', sans-serif;

    }

    .video-container {

        max-height: 400px;

        height: 100vh;

    }
</style>
