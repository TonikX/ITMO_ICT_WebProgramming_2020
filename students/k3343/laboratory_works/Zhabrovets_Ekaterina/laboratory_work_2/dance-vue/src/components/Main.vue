<template>
    <mu-container>
<!--        <link rel="stylesheet" href="../../static/material-icons.css">-->
        <link rel="stylesheet" href="../../static/style.css">
<!--        <link rel="stylesheet" href="../../static/bootstrap.min.css">-->
<!--        <link rel="stylesheet" href="../../static/font-awesome.min.css">-->
<!--        <link rel="stylesheet" href="../../static/templatemo-gray.css">-->
<!--         <video-background class="video-container" src="../static/Dance.mp4" style="max-height: 400px; height: 100vh;">-->
<!--    <h1 style="color: white;">Hello welcome!</h1></video-background>-->
        <mu-tabs color="primary" full-width>
            <mu-tab active="0" @click="loadmain">Workshops</mu-tab>
            <mu-tab active="1" @click="loadPers">Клиенты</mu-tab>
            <mu-tab active="2" @click="loadChor">Хореографы</mu-tab>
            <mu-tab active="3" @click="loadRep">Информация по выручкам танц.школ</mu-tab>
        </mu-tabs>
        <div>
            <Workshops v-if="active==0"></Workshops>
        </div>
        <div v-if="active == 1">
            <mu-row>
            <mu-container v-for="person in persons">
            <mu-card style="width: 100%; max-width: 375px; margin: 0 auto;">
                {{ person.fullname }}<br>
                <mu-row>
                <mu-col>
                <div class="strange">
                Адрес эл. почты: {{person.email}}<br>
                Телефон: {{person.telephone}}<br>
                Дата рождения: {{person.birth_date}}<br>
                    <mu-button @click="loadedit(person.id)">Редактировать</mu-button>
                    <EditPart :id=person.id v-if="show_edit===person.id"></EditPart>
                </div>
                </mu-col>
                </mu-row>
        </div>
<!--        <div v-if="active == 2">-->
<!--            <mu-row>-->
<!--            <mu-container v-for="teach in teachers">-->
<!--            <mu-card style="width: 100%; max-width: 375px; margin: 0 auto;">-->
<!--                <mu-row>-->
<!--                <mu-col>-->
<!--                    <mu-expansion-panel>-->
<!--                    <div slot="header">{{ teach.full_name }}, {{ teach.style.name }}</div>-->
<!--&lt;!&ndash;                        <div v-if="show_n===teach.id">&ndash;&gt;-->
<!--&lt;!&ndash;                            Ближайший мастер-класс: {{w.date}}&ndash;&gt;-->
<!--&lt;!&ndash;                        </div>&ndash;&gt;-->
<!--                    </mu-expansion-panel>-->
<!--                </mu-col>-->
<!--                </mu-row>-->
<!--&lt;!&ndash;                <mu-row>&ndash;&gt;-->
<!--&lt;!&ndash;                <mu-col>&ndash;&gt;-->
<!--&lt;!&ndash;                    <mu-ripple>&ndash;&gt;-->
<!--&lt;!&ndash;                      Редактировать&ndash;&gt;-->
<!--&lt;!&ndash;                    </mu-ripple>&ndash;&gt;-->
<!--&lt;!&ndash;                </mu-col>&ndash;&gt;-->
<!--&lt;!&ndash;                </mu-row>&ndash;&gt;-->
<!--            </mu-card>-->
<!--            </mu-container>-->
<!--            </mu-row>-->
<!--        </div>-->
        <div v-if="active == 3">
                <mu-paper :z-depth="1">
                    <mu-data-table :columns="cols" :data="reports">

                    </mu-data-table>
                </mu-paper>
        </div>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Workshops from "./Workshops";
    import EditPart from "./EditPart";

    export default {
        name: "Main",
        components: {Workshops, EditPart},
        data() {
            return {
                persons: '',
                active: 0,
                reports: '',
                teachers: '',
                show_n: '',
                w: '',
                show_edit:'',
                cols: [{title: 'Название школы',  width: 220, name:'name'}, {
                    title: 'Количество прошедших мастер-классов',
                    width: 200,
                    name: 'number_prev',
                    align: 'center'
                }, {title: 'Выручка(руб.)', width: 250, name:'gained_profit' , align: 'center'}, {
                    title: 'Количество грядущих мастер-классов',
                    width: 200,
                    name: 'number_fut',
                    align: 'center'
                }, {title: 'Ожид. прибыль(руб.)', width: 250, name:'fut_profit', align: 'center'}]
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
            loadmain() {
                this.active = 0
            },
            loadRep() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/report/",
                    type: "GET",
                    success: (response) => {
                        this.reports = response.data.data
                        this.active = 3
                    }
                })
            },
            loadChor() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/all_teachers/",
                    type: "GET",
                    success: (response) => {
                        this.teachers = response.data.data
                        this.active = 2
                    }
                })
            },
            loadedit(id) {
                this.show_edit = id
            }

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
    .bar{
        position: fixed;
top: 0;
left: 0;
right: 0;
    }
 html, body {

            background-color: #000;

            font-family: 'Nunito', sans-serif;

        }

        .video-container{

            max-height: 400px;

            height: 100vh;

        }
</style>
