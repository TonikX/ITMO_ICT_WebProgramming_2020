<template>
    <mu-container>
        <mu-row>
            <mu-button @click="show1 = !show1">Показать список участников</mu-button>
            <mu-col span="8" sm="6" md="4" lg="3" xl="3">
                <div class="grid-cell">
                <mu-flex justify-content="center">
                    <mu-button @click="loadAdd">Добавить мастер-класс</mu-button>
                    <AddWsh @closeAddWsh="closeAddWsh" v-if="show3"></AddWsh>
                </mu-flex>
                </div>
            </mu-col>
                <mu-container>
                    <mu-container v-for="wsh in workshops">
                        {{wsh.name}}<br>
                        {{wsh.place.school.name}}<br>
                        {{wsh.date}}<br>
                        {{wsh.time}}<br>
                        Всего участников: {{wsh.participants.length}}
                        <mu-flex>
                            <mu-expand-transition>
                                <div class="mu-transition-box mu-inverse" v-show="!show1">
                                    <div v-if="wsh.participants.length > 0">
                                        <mu-list>
                                            <mu-list-item v-for="part in wsh.participants">
                                                <mu-row>
                                                    {{part.fullname}}
                                                    <mu-button small color="error" align="center"
                                                               @click="deletePart(wsh.id, part.id)">Удалить
                                                    </mu-button>
                                                </mu-row>
                                            </mu-list-item>
                                        </mu-list>
                                    </div>
                                    <div v-else>
                                        <mu-list>
                                            <mu-list-item align="center">Участников пока нет</mu-list-item>
                                        </mu-list>
                                    </div>
                                </div>
                            </mu-expand-transition>
                        </mu-flex>
                        <p @click="loadNon(wsh.id)">Добавить участника</p>
                        <NonPart :id="wsh.id" v-if="show2===wsh.id"></NonPart>
                    </mu-container>
                </mu-container>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    import NonPart from "./NonPart";
    import AddWsh from "./AddWsh";

    export default {
        name: "Workshops",
        components: {AddWsh, NonPart},
        data() {
            return {
                workshops: '',
                show1: 'false',
                show2: '',
                show3: '',
                date: '',
            }
        },
        created() {
            this.loadWsh()
        },

        methods: {
            loadWsh() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/add_part/",
                    type: "GET",
                    success: (response) => {
                        this.workshops = response.data.data
                    }
                })
            },
            loadNon(i) {
                this.show2 = i
            },
            loadAdd() {
                this.show3 = true
            },
            deletePart(w, p) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/remove_part/",
                    type: "POST",
                    data: {
                        wsh: w,
                        partic: p,
                    },
                    success: (response) => {
                        alert("Пользователь удален")
                        window.location = '/'

                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            closeAddWsh() {
                this.show3 = false
            }
        }
    }
</script>

<style scoped>
    .mu-button {
        margin: 8px;
        vertical-align: top;
    }

    .icon-container {
        display: flex;
        width: 300px;
        justify-content: space-around;
    }

    .icon-container .mu-icon {
        margin-bottom: 12px;
    }

    .strange {

    }
</style>
