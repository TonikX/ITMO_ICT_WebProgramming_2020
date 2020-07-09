<template>
    <transition name="modal-fade">
        <div class="modal-backdrop">
            <div class="modal" role="dialog" aria-labelledby="modalTitle" aria-describedby="modalDescription">
                <header class="modal-header" id="modalTitle">
                    <slot name="header">
                        Добавление новой записи в расписание
                        <button type="button" class="btn-close" @click="close" aria-label="Close modal">
                            x
                        </button>
                    </slot>
                </header>
                <section class="modal-body" id="modalDescription">
                    <slot name="body">
                        <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                            <mu-form-item prop="radio" label="День недели">
                                <mu-radio v-model="form.day" value="Понедельник" label="Понедельник"></mu-radio>
                                <mu-radio v-model="form.day" value="Вторник" label="Вторник"></mu-radio>
                                <mu-radio v-model="form.day" value="Среда" label="Среда"></mu-radio>
                                <mu-radio v-model="form.day" value="Четверг" label="Четверг"></mu-radio>
                                <mu-radio v-model="form.day" value="Пятница" label="Пятница"></mu-radio>
                                <mu-radio v-model="form.day" value="Суббота" label="Суббота"></mu-radio>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Урок">
                                <mu-select v-model="form.lesson">
                                    <mu-option label="1-8:00-8:45" value="1-8:00-8:45">1-8:00-8:45</mu-option>
                                    <mu-option label="2-8:50-9:35" value="2-8:50-9:35">2-8:50-9:35</mu-option>
                                    <mu-option label="3-9:40-10:25" value="3-9:40-10:25">3-9:40-10:25</mu-option>
                                    <mu-option label="4-10:40-11:25" value="4-10:40-11:25">4-10:40-11:25</mu-option>
                                    <mu-option label="5-11:30-12:15" value="5-11:30-12:15">5-11:30-12:15</mu-option>
                                    <mu-option label="6-12:20-13:05" value="6-12:20-13:05">6-12:20-13:05</mu-option>
                                    <mu-option label="7-13:05-13:50" value="7-13:05-13:50">7-13:05-13:50</mu-option>
                                    <mu-option label="8-14:00-14:45" value="8-14:00-14:45">8-14:00-14:45</mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="select" label="Класс">
                                <mu-select v-model="form.klass_name">
                                    <mu-option v-for="klass in listKlass" :key="klass.id" :label="klass.number+klass.litera"
                                               :value="klass.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="select" label="Предмет">
                                <mu-select v-model="form.subject_name">
                                    <mu-option v-for="subject in listSubject" :key="subject.id" :label="subject.subject"
                                               :value="subject.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="select" label="Учитель">
                                <mu-select v-model="form.teacher_name">
                                    <mu-option v-for="teacher in listTeacher" :key="teacher.id" :label="teacher.last_name"
                                               :value="teacher.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="select" label="Кабинет">
                                <mu-select v-model="form.cabinet_number">
                                    <mu-option v-for="cabinet in listCabinet" :key="cabinet.id" :label="cabinet.number"
                                               :value="cabinet.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                        </mu-form>
                    </slot>
                </section>
                <footer class="modal-footer">
                    <slot name="footer">
                        <button
                                type="button"
                                class="btn-green"
                                @click="addTimetable"
                                aria-label="Close modal">
                            Submit
                        </button>
                    </slot>
                </footer>
            </div>
        </div>
    </transition>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: 'AddTimetable',
        data() {
            return {
                labelPosition: 'right',
                listSubject: [],
                listTeacher: [],
                listCabinet: [],
                listKlass: [],
                form: {
                    lesson: '',
                    day: '',
                    klass_name: '',
                    subject_name: '',
                    teacher_name: '',
                    cabinet_number: '',
                }
            }
        },
        created() {
            this.loadListSubject()
            this.loadListTeacher()
            this.loadListCabinet()
            this.loadListKlass()
        },
        methods: {
            close() {
                this.$emit('close');
            },
            async loadListCabinet() {
                this.listCabinet = await fetch(
                    `${this.$store.getters.getServerUrl}/cabinet`
                ).then(response => response.json())
            },
            async loadListTeacher() {
                this.listTeacher = await fetch(
                    `${this.$store.getters.getServerUrl}/teacher/`
                ).then(response => response.json())
            },
            async loadListSubject() {
                this.listSubject = await fetch(
                    `${this.$store.getters.getServerUrl}/subject`
                ).then(response => response.json())
            },
            async loadListKlass() {
                this.listKlass = await fetch(
                    `${this.$store.getters.getServerUrl}/klass`
                ).then(response => response.json())
            },
            addTimetable() {
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/timetable/add",
                        type: "POST",
                        data: {
                            lesson: this.form.lesson,
                            day: this.form.day,
                            klass_name: this.form.klass_name,
                            subject_name: this.form.subject_name,
                            teacher_name: this.form.teacher_name,
                            cabinet_number: this.form.cabinet_number,
                        },

                        success: (response) => {
                            this.close()
                            alert("Запись успешно добавлена в расписание")
                            this.$router.push({name: "Расписание класса"})
                        },
                        error: (response) => {
                            if (response.status === 400) {
                                alert("Введите все данные")
                            }
                        }
                    }
                )
            },
        }
    }
</script>


<style scoped>
    .modal-backdrop {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: rgba(0, 0, 0, 0.3);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .modal {
        background: #FFFFFF;
        box-shadow: 2px 2px 20px 1px;
        overflow-x: auto;
        display: flex;
        flex-direction: column;
    }

    .modal-header,
    .modal-footer {
        padding: 15px;
        display: flex;
    }

    .modal-header {
        border-bottom: 1px solid #eeeeee;
        color: #4AAE9B;
        justify-content: space-between;
    }

    .modal-footer {
        border-top: 1px solid #eeeeee;
        justify-content: flex-end;
    }

    .modal-body {
        position: relative;
        padding: 20px 10px;
    }

    .btn-close {
        border: none;
        font-size: 20px;
        padding: 20px;
        cursor: pointer;
        font-weight: bold;
        color: #4AAE9B;
        background: transparent;
    }

    .btn-green {
        color: white;
        background: #4AAE9B;
        border: 1px solid #4AAE9B;
        border-radius: 2px;
    }
</style>