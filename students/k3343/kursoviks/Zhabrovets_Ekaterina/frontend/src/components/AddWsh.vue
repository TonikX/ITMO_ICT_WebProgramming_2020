<template>
    <mu-container>
        <mu-dialog width="360" transition="slide-bottom" fullscreen :open.sync="openSimple">
            <mu-appbar color="primary" title="Добавление мастер-класса">
                <mu-button slot="right" flat @click="closeAddWsh">Отмена</mu-button>
            </mu-appbar>
            <div style="padding: 24px;">
                <mu-container>
                    <mu-row>
                        <mu-col>
                            <mu-form>
                                <mu-form-item prop="input" label="Название">
                                    <mu-text-field v-model="title"></mu-text-field>
                                </mu-form-item>
                                <mu-form-item prop="input" label="Продолжительность (часы)">
                                    <mu-text-field v-model="duration"></mu-text-field>
                                </mu-form-item>
                                <mu-form-item prop="input" label="Цена посещения">
                                    <mu-text-field v-model="price"></mu-text-field>
                                </mu-form-item>
                            </mu-form>
                        </mu-col>
                    </mu-row>
                    <mu-row gutter>
                        <mu-col span="12" lg="4" sm="6">
                            <div @click="loadSch">
                                <mu-select label="Выберите локацию" label-float filterable v-model="option_school"
                                           full-width>
                                    <mu-option v-for="school in schools" :key="school.id" :label="school.name"
                                               :value="school.id"></mu-option>
                                </mu-select>
                            </div>
                            <div @click="loadHalls">
                                <mu-select label="Выберите зал" label-float filterable v-model="option_hall" full-width>
                                    <mu-option v-for="hall in halls" :key="hall.id"
                                               :label="hall.name + ' - ' +  hall.capacity + ' мест'"
                                               :value="hall.id"></mu-option>
                                </mu-select>
                            </div>
                        </mu-col>
                        <mu-col span="12" lg="4" sm="6">
                            <mu-date-input v-model="date" label="Дата" label-float :date-time-format="enDateFormat">
                            </mu-date-input>
                            <mu-date-input v-model="time" label="Время" label-float type="time" :view-type="viewType"
                                           :clock-type="type">
                            </mu-date-input>
                        </mu-col>
                        <mu-col span="12" lg="4" sm="6">
                            <div @click="loadStyles">
                                <mu-select label="Выберите стиль" label-float filterable v-model="option_style"
                                           full-width>
                                    <mu-option v-for="style in styles" :key="style.id" :label="style.name"
                                               :value="style.id"></mu-option>
                                </mu-select>
                            </div>
                            <div @click="loadTeachers">
                                <mu-select label="Выберите хорегографа(-ов)" label-float filterable full-width multiple chips v-model="option_teachers">
                                    <mu-option v-for="teacher in teachers" :key="teacher.id"
                                               :label="teacher.full_name"
                                               :value="teacher.id"></mu-option>
                                </mu-select>
                            </div>
                        </mu-col>
                    </mu-row>
                    <mu-row gutter>
                        <mu-form>
                            <mu-form-item prop="input" label="Информация">
                                <mu-text-field v-model="inform"></mu-text-field>
                            </mu-form-item>
                        </mu-form>
                    </mu-row>
                    <mu-row>
                        <mu-button full-width color="primary" @click="final_add">Добавить</mu-button>
                    </mu-row>
                </mu-container>
            </div>
        </mu-dialog>
    </mu-container>
</template>

<script>
    import $ from "jquery";

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
        name: "AddWsh",
        data() {
            return {
                openSimple: true,
                option_school: '',
                schools: '',
                halls: '',
                option_hall: '',
                date: '',
                enDateFormat,
                viewType: 'list',
                display: true,
                type: '24hrs',
                time: '',
                duration: '',
                title: '',
                inform: '',
                styles: '',
                option_style: '',
                teachers: '',
                option_teachers: '',
                price: '',

            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
        },
        methods: {
            loadSch() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/all_schools/",
                    type: "GET",
                    success: (response) => {
                        this.schools = response.data.data
                    }
                })
            },
            loadHalls() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/halls_for_school/",
                    type: "GET",
                    data: {
                        school: this.option_school,
                    },
                    success: (response) => {
                        this.halls = response.data.data
                    }
                })
            },

            addWsh() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/add_wsh/",
                    type: "POST",
                    data: {
                        name: this.title,
                        place: this.option_hall,
                        date: this.date.toISOString().slice(0, 10),
                        time: this.time.toString().slice(16, 24),
                        duration: this.duration,
                        price: this.price,
                        info: this.inform,
                    },
                    // success: (response) => {
                    //     alert("Воркшоп добавлен добавлен")
                    //     window.location = '/'
                    // },
                    // error: (response) => {
                    //     alert("Ошибка")
                    // }
                })
            },

            loadStyles() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/all_styles/",
                    type: "GET",
                    success: (response) => {
                        this.styles = response.data.data
                    }
                })
            },
            loadTeachers() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/teachers_for_style/",
                    type: "GET",
                    data: {
                        style: this.option_style,
                    },
                    success: (response) => {
                        this.teachers = response.data.data
                    }
                })
            },
            addTeachers(teach) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/add_teachers_for_wsh/",
                    type: "POST",
                    data: {
                        teacher: teach
                    },
                    success: (response) => {
                        alert("Все получилось")
                    },
                    error: (response) => {
                        console.log(this.option_teachers)
                    }
                })
            },

            final_add(){
                this.addWsh();
                setTimeout(() => {for (this.i = 0; this.i < this.option_teachers.length; this.i++) {
                    this.addTeachers(this.option_teachers[this.i])}}, 1000)
                this.$router.push({name: "Main"})
            },

            closeAddWsh() {
                this.$emit('closeAddWsh')
            }
        }
    }
</script>

<style scoped>

</style>
