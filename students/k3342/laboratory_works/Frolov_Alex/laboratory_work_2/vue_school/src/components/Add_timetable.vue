<template>
    <transition name="modal-fade">
        <div class="modal-backdrop">
            <div class="modal" role="dialog" aria-labelledby="modalTitle" aria-describedby="modalDescription">
                <header class="modal-header" id="modalTitle">
                    <slot name="header">
                        Добавление записи в расписание
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
                                    <mu-option label="1-8:30-9:10" value="1-8:30-9:10">1-8:30-9:10</mu-option>
                                    <mu-option label="2-9:20-10:00" value="2-9:20-10:00">2-9:20-10:00</mu-option>
                                    <mu-option label="3-10:10-10:50" value="3-10:10-10:50">3-10:10-10:50</mu-option>
                                    <mu-option label="4-11:00-11:40" value="4-11:00-11:40">4-11:00-11:40</mu-option>
                                    <mu-option label="5-12:10-12:50" value="5-12:10-12:50">5-12:10-12:50</mu-option>
                                    <mu-option label="6-13:10-13:50" value="6-13:10-13:50">6-13:10-13:50</mu-option>
                                    <mu-option label="7-14:00-14:40" value="7-14:00-14:40">7-14:00-14:40</mu-option>
                                    <mu-option label="8-14:45-15:25" value="8-14:45-15:25">8-14:45-15:25</mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="select" label="Класс">
                                <mu-select v-model="form.nclass_name">
                                    <mu-option v-for="nclass in listNclass" :key="nclass.id" :label="nclass.number+nclass.letter"
                                               :value="nclass.id"></mu-option>
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
                                    <mu-option v-for="teacher in listTeacher" :key="teacher.id" :label="teacher.surname"
                                               :value="teacher.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="select" label="Кабинет">
                                <mu-select v-model="form.room_number">
                                    <mu-option v-for="room in listRoom" :key="room.id" :label="room.number"
                                               :value="room.id"></mu-option>
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
                            <p @click="close">Добавить</p>
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
                listRoom: [],
                listNclass: [],
                form: {
                    lesson: '',
                    day: '',
                    nclass_name: '',
                    subject_name: '',
                    teacher_name: '',
                    room_number: '',
                }
            }
        },
        created() {
            this.loadListSubject()
            this.loadListTeacher()
            this.loadListRoom()
            this.loadListNclass()
        },
        methods: {
            close() {
                this.$emit('close');
            },
            async loadListRoom() {
                this.listRoom = await fetch(
                    `${this.$store.getters.getServerUrl}/room`
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
            async loadListNclass() {
                this.listNclass = await fetch(
                    `${this.$store.getters.getServerUrl}/nclass`
                ).then(response => response.json())
            },
            addTimetable() {
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/timetable/add",
                        type: "POST",
                        data: {
                            lesson: this.form.lesson,
                            day: this.form.day,
                            nclass_name: this.form.nclass_name,
                            subject_name: this.form.subject_name,
                            teacher_name: this.form.teacher_name,
                            room_number: this.form.room_number,
                        },
                        success: (response) => {
                            this.close()
                            alert("Вы добавили запись в расписание")
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
        justify-content: left;
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
        padding: 30px;
        display: flex;
    }
    .modal-header {
        border-bottom: 1px solid #0b0aff;
        color: #22262e;
        justify-content: space-between;
    }
    .modal-footer {
        border-top: 1px solid #0b0aff;
        justify-content: flex-end;
    }
    .modal-body {
        position: relative;
        padding: 10px 10px;
    }
    .btn-close {
        border: none;
        font-size: 20px;
        padding: 20px;
        cursor: pointer;
        font-weight: bold;
        color: red;
        background: transparent;
    }
    .btn-green {
        color: black;
        background: limegreen;
        border: 1px solid limegreen;
        border-radius: 10px;
    }
</style>