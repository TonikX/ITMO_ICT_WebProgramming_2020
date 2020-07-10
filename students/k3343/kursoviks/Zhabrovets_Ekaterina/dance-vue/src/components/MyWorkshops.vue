<template>
    <div>
        <mu-row gutter>
            <mu-col span="5" lg="6">
                <h1>Мои заявки</h1>
                <div v-if="workshops_fut.length === 0">
                    Вы пока не отправили ни одной заявки
                </div>
                <div v-else v-for="wsh in workshops_fut">
                    <mu-card style="width: 100%; max-width: 375px; margin: 10px auto;">
                        <mu-card-title :title="wsh.workshop.name"/>
                        <div class="strange">
                            <div style="padding-left: 10px">
                            <div v-if="wsh.workshop.choreographer[0]">
                                Стиль: {{wsh.workshop.choreographer[0]["style"]["name"]}}
                            </div>
                            Место: {{wsh.workshop.place.school.name}}<br>
                            Дата: {{wsh.workshop.date}}<br>
                            Время: {{wsh.workshop.time}}<br>
                            Продолжительность: {{wsh.workshop.duration}} час(-а)<br>
                            <mu-row>
                                Хореограф(-ы):
                                <div v-for="teach in wsh.workshop.choreographer">
                                    {{teach.full_name}},
                                </div>
                            </mu-row>
                            </div>
                        </div>
                        <mu-alert v-if="wsh.approved" color="success">
                            <mu-icon left value="check_circle"></mu-icon>
                            Заявка одобрена
                        </mu-alert>
                        <mu-alert v-else color="warning">
                            <mu-icon left value="priority_high"></mu-icon>
                            Заявка находится на стадии рассмотрения
                        </mu-alert>
                    </mu-card>
                </div>
            </mu-col>
            <mu-col span="5" lg="6">
                <h1>Посещенные мастер-классы</h1>
                <div v-if="workshops_prev.length===0">
                    Вы пока не посетили ни одного мастер-класса
                </div>
                <div v-else v-for="wsh in workshops_prev" class="dob">
                    <mu-card style="width: 100%; max-width: 375px; margin: 10px auto;">
                        <mu-card-title :title="wsh.name"/>
                        <div class="strange">
                            <div style="padding-left: 10px">
                            <div v-if="wsh.choreographer[0]">
                                Стиль: {{wsh.choreographer[0]["style"]["name"]}}
                            </div>
                            Место: {{wsh.place.school.name}}<br>
                            Дата: {{wsh.date}}<br>
                            Время: {{wsh.time}}<br>
                            Продолжительность: {{wsh.duration}} час(-а)<br>
                            <mu-row>
                                Хореограф(-ы):
                                <div v-for="teach in wsh.choreographer">
                                    {{teach.full_name}},
                                </div>
                            </mu-row>
                            </div>
                        </div>
                        <mu-alert @click="writeFeed(wsh.id)" color="info">
                            <mu-icon left value="create"></mu-icon>
                            Спасибо, что посетили данный МК!<br/>
                            Напишите отзыв!
                        </mu-alert>
                    </mu-card>
                    <WriteFeedback @closeWriteFeedback="closeWriteFeedback" :id="wsh.id"
                                   v-if="write_report===wsh.id"></WriteFeedback>
                </div>
            </mu-col>
        </mu-row>
    </div>
</template>

<script>
    import $ from "jquery";
    import WriteFeedback from "./WriteFeedback";

    export default {
        name: "MyWorkshops",
        components: {WriteFeedback},
        data() {
            return {
                workshops_fut: '',
                workshops_prev: '',
                write_report: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadMyFutureWSH()
        },
        methods: {
            loadMyFutureWSH() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/query_part_info/",
                    type: "GET",
                    success: (response) => {
                        this.workshops_fut = response.data.data_fut
                        this.workshops_prev = response.data.data_prev
                    }
                })
            },
            writeFeed(id) {
                this.write_report = id
            },
            closeWriteFeedback() {
                this.write_report = 0
            }
        }
    }
</script>

<style scoped>
    .strange {
        text-align: left
    }

    .dob {
        cursor: pointer;
    }
</style>
