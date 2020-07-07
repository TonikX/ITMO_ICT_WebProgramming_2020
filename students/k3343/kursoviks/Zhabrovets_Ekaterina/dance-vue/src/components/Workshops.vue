<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <mu-container v-if="workshops.length === 0">Нет мастер-классов для заданных дат</mu-container>
                <mu-container v-else v-for="wsh in workshops">
                    <mu-card style="width: 100%; max-width: 375px; margin: 10px auto;">
                        <mu-card-title :title="wsh.name"
                                       :sub-title="'Мест занято: ' + wsh.participants.length + '/' + wsh.place.capacity">
                        </mu-card-title>
                        <div class="strange" style="padding-left: 10px">
                            <div v-if="wsh.choreographer[0]">
                                Стиль: {{wsh.choreographer[0]["style"]["name"]}}
                            </div>
                            Место: {{wsh.place.school.name}}<br>
                            Дата: {{wsh.date}}<br>
                            Время: {{wsh.time}}<br>
                            Продолжительность: {{wsh.duration}} час(-а)<br>
                            Цена посещения: {{wsh.price}} руб.<br>
                            <mu-row>
                                Хореограф(-ы):
                                <div v-for="teach in wsh.choreographer">
                                    {{teach.full_name}},
                                </div>
                            </mu-row>
                            <mu-flex>
                                <mu-expand-transition>
                                    <div class="mu-transition-box mu-inverse" v-show="!show1">
                                        <div v-if="wsh.participants.length > 0">
                                            <mu-list>
                                                <mu-list-item v-for="part in wsh.participants">
                                                    <mu-row>
                                                        {{part.fullname}}
                                                        <mu-button small color="error"
                                                                   @click="deletePart(wsh.id, part.id)">Удалить
                                                        </mu-button>
                                                    </mu-row>
                                                </mu-list-item>
                                            </mu-list>
                                        </div>
                                        <div v-else>
                                            <mu-list>
                                                <mu-list-item>Участников пока нет</mu-list-item>
                                            </mu-list>
                                        </div>
                                    </div>
                                </mu-expand-transition>
                            </mu-flex>
                        </div>
                        <div class="dob">
                            <mu-badge color="primary" content="Записаться" @click="loadNon(wsh.id)"></mu-badge>
                        </div>
                        <NonPart :id="wsh.id" v-if="show2===wsh.id" @closeaddPart="closeaddPart"></NonPart>
                        <div class="dob">
                            <mu-badge v-if="is_superuser" color="secondary" content="Открыть список участников"
                                      @click="openPartic(wsh.id)"></mu-badge>
                            <ParticipantsForWSH :id="wsh.id" v-if="show_partic===wsh.id"></ParticipantsForWSH>
                        </div>
                    </mu-card>
                </mu-container>
            </mu-col>
            <mu-col>
                <mu-card style=" margin: 10px auto; padding-left: 10px">
                    <mu-row><h3>Фильтровать мастер-классы по дате</h3></mu-row>
                    <mu-row>
                        <mu-date-input v-model="date_start" label="C" label-float :date-time-format="enDateFormat">
                        </mu-date-input>
                        <mu-date-input v-model="date_end" label="По" label-float :date-time-format="enDateFormat">
                        </mu-date-input>
                    </mu-row>
                    <mu-button color="primary" @click="loadWshFilt">Фильтровать</mu-button>
                </mu-card>
                <mu-card v-if="is_superuser" style="margin-top: 10px; padding-left: 10px">
                    <mu-row><h3>Доступные действия</h3></mu-row>
                    <mu-button color="primary" @click="loadAdd">Добавить мастер-класс</mu-button>
                    <mu-badge :content="count_queries" circle color="secondary">
                        <mu-tooltip content="Заявки на участие"><mu-button icon @click="openQuiries">
                            <mu-icon value="notifications"></mu-icon>
                        </mu-button>
                        </mu-tooltip>
                    </mu-badge>
                    <AddWsh @closeAddWsh="closeAddWsh" v-if="show3"></AddWsh>
                    <Queries v-if="show4"></Queries>
                </mu-card>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    import NonPart from "./NonPart";
    import AddWsh from "./AddWsh";
    import Queries from "./Queries";
    import ParticipantsForWSH from "./ParticipantsForWSH";

    const dayAbbreviation = ['Вс', 'Пон', 'Вт', 'Ср', 'Чт', 'Пт', 'Суб'];
    const dayList = ['Вс', 'Пон', 'Вт', 'Ср', 'Чт', 'Пт', 'Суб'];
    const monthList = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сент', 'Окт', 'Нояб', 'Дек'];
    const monthLongList = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
        'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'];
    const enDateFormat = {
        formatDisplay(date) {
            return `${dayList[date.getDay()]}, ${monthList[date.getMonth()]} ${date.getDate()}`;
        },
        formatMonth(date) {
            return `${monthLongList[date.getMonth()]} ${date.getFullYear()}`;
        },
        getWeekDayArray(firstDayOfWeek) {
            let beforeArray = [];
            let afterArray = [];
            for (let i = 0; i < dayAbbreviation.length; i++) {
                if (i < firstDayOfWeek) {
                    afterArray.push(dayAbbreviation[i]);
                } else {
                    beforeArray.push(dayAbbreviation[i]);
                }
            }
            return beforeArray.concat(afterArray);
        },
        getMonthList() {
            return monthList;
        }
    };


    export default {
        name: "Workshops",
        components: {ParticipantsForWSH, Queries, AddWsh, NonPart},
        data() {
            return {
                workshops: '',
                show1: 'false',
                show2: '',
                show3: '',
                date: '',
                show4: '',
                enDateFormat,
                date_start: null,
                date_end: null,
                is_teacher: '',
                is_superuser: '',
                show_partic: '',
                count_queries: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadInfo()
            this.loadWsh()
            this.loadQueries()
        },
        methods: {
            loadWsh() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/wsh_all/",
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
            openQuiries() {
                this.show4 = true
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
            },
            closeaddPart() {
                this.show2 = 0
            },
            loadWshFilt() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/wsh_filter/",
                    type: "GET",
                    data: {
                        date_start: this.date_start.toISOString().slice(0, 10),
                        date_end: this.date_end.toISOString().slice(0, 10),
                    },
                    success: (response) => {
                        this.workshops = response.data.data
                    },
                    error: (response) => {
                        console.log(this.date_end)
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
                    },
                    error: (response) => {
                        console.log(this.date_end)
                    }
                })
            },
            loadQueries() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/quieries_to_approve2/",
                    type: "GET",
                    success: (response) => {
                        this.count_queries = response.data.count
                    }
                })
            },
            // loadPartic() {
            //     $.ajax({
            //         url: "http://127.0.0.1:8000/api/v1/dance/user_info/",
            //         type: "GET",
            //         success: (response) => {
            //             this.is_teacher = response.data.data.is_teacher
            //             this.is_superuser = response.data.data.is_superuser
            //         },
            //         error: (response) => {
            //             console.log(this.date_end)
            //         }
            //     })
            // }
            openPartic(id) {
                this.show_partic = id
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
        text-align: left
    }

    .dob {
        cursor: pointer;
    }
</style>
