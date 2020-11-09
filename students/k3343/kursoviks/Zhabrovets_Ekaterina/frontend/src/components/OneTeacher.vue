<template>
    <div>
        <mu-dialog width="360" transition="slide-left" fullscreen :open.sync="openFullscreen">
            <mu-appbar color="primary" title="Информация о хореографе">
                <mu-button slot="right" flat @click="close">
                    <mu-icon value="close"></mu-icon>
                </mu-button>
            </mu-appbar>
            <div style="padding: 24px;">
                <mu-container>
                    <mu-card style="width: 100%; max-width: 375px; margin: 0 auto;">
                        <mu-card-header :title="teacher_info.full_name"
                                        :sub-title="'Стиль: ' + teacher_info.style.name">
                            <mu-avatar slot="avatar">
                                <img src="../assets/1.jpg">
                            </mu-avatar>
                        </mu-card-header>
                        <mu-card-text>
                            Страна: {{teacher_info.country}}<br/>
                            О себе: {{teacher_info.biography}}
                        </mu-card-text>
                    </mu-card>
                </mu-container>
                <mu-container>
                    <div @click="loadFeedbacks">
                    <mu-expansion-panel>
                        <div slot="header" style="padding-left: 440px"><h4>Показать/скрыть отзывы</h4></div>
                        <mu-row gutter>
                            <div v-for="feed in teacher_feedbacks">
                                <mu-col md="12">
                                <mu-sub-header>
                                    О мастер-классе за {{feed.workshop.date}}
                                </mu-sub-header>
                                    <div style="padding-left: 15px">
                                Оценка: {{feed.rating}}<br>
                                Комментарий: {{feed.text}}
                                    </div>
                                <mu-sub-header>
                                    Автор: {{feed.user.full_name}}, Создан: {{feed.created}}
                                </mu-sub-header>
                                </mu-col>
                            </div>
                        </mu-row>
                    </mu-expansion-panel>
                    </div>
                </mu-container>
            </div>
        </mu-dialog>
    </div>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "OneTeacher",
        props: {
            id: ''
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadTeachOne();
        },
        data() {
            return {
                openFullscreen: true,
                teacher_info: '',
                teacher_feedbacks: '',
            }
        },
        methods: {
            loadTeachOne() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/one_teacher/",
                    type: "GET",
                    data: {
                        teacher: this.id,
                    },
                    success: (response) => {
                        this.teacher_info = response.data.data
                    }
                })
            },
            loadFeedbacks() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/feedbacks/",
                    type: "GET",
                    data: {
                        teacher: this.id,
                    },
                    success: (response) => {
                        this.teacher_feedbacks = response.data.data
                    }
                })
            },
            close() {
                this.$emit('close')
            }
        }
    }
</script>

<style scoped>

</style>
