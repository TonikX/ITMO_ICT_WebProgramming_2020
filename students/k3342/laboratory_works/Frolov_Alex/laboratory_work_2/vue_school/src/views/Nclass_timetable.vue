<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>
                    Расписание занятий {{nclass.number}} "{{nclass.letter}}" класса
                </h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <table class="table-fill" v-for="timetable in nclass.timetable" :key="timetable.id">
                <thead>
                <tr>
                    <th colspan="4" class="text-left">{{timetable.day}}
                        <mu-radio v-if="isUpdateVisible" v-model="form.day" value="Понедельник"
                                  label="Понедельник"></mu-radio>
                        <mu-radio v-if="isUpdateVisible" v-model="form_update.day" value="Вторник"
                                  label="Вторник"></mu-radio>
                        <mu-radio v-if="isUpdateVisible" v-model="form_update.day" value="Среда"
                                  label="Среда"></mu-radio>
                        <mu-radio v-if="isUpdateVisible" v-model="form_update.day" value="Четверг"
                                  label="Четверг"></mu-radio>
                        <mu-radio v-if="isUpdateVisible" v-model="form_update.day" value="Пятница"
                                  label="Пятница"></mu-radio>
                        <mu-radio v-if="isUpdateVisible" v-model="form_update.day" value="Суббота"
                                  label="Суббота"></mu-radio>
                    </th>
                </tr>
                </thead>
                <tbody class="table-hover">
                <tr>
                    <td class="text-left">{{timetable.lesson}}
                        <br>
                        <mu-radio v-if="isDeleteVisible" v-model="form.delete_timetable" :value="timetable.id"
                                  label="Удалить"></mu-radio>
                        <mu-radio v-if="isUpdateVisible" v-model="form.update_timetable" :value="timetable.id"
                                  label="Изменить"></mu-radio>
                        <br>
                        <mu-select v-if="isUpdateVisible" v-model="form_update.lesson">
                            <mu-option label="1-8:30-9:10" value="1-8:30-9:10">1-8:30-9:10</mu-option>
                            <mu-option label="2-9:20-10:00" value="2-9:20-10:00">2-9:20-10:00</mu-option>
                            <mu-option label="3-10:10-10:50" value="3-10:10-10:50">3-10:10-10:50</mu-option>
                            <mu-option label="4-11:00-11:40" value="4-11:00-11:40">4-11:00-11:40</mu-option>
                            <mu-option label="5-12:10-12:50" value="5-12:10-12:50">5-12:10-12:50</mu-option>
                            <mu-option label="6-13:10-13:50" value="6-13:10-13:50">6-13:10-13:50</mu-option>
                            <mu-option label="7-14:00-14:40" value="7-14:00-14:40">7-14:00-14:40</mu-option>
                            <mu-option label="8-14:45-15:25" value="8-14:45-15:25">8-14:45-15:25</mu-option>
                        </mu-select>
                    </td>
                    <td class="text-left">Кабинет №{{timetable.room_number}}</td>
                    <td class="text-left">{{timetable.subject_name}}</td>
                    <td class="text-left">{{timetable.teacher_name}}</td>
                </tr>
                </tbody>
            </table>
            <br>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <br>
                <mu-button color="success" style: text-color="black" @click="showModal">Добавить запись в расписание</mu-button>
                <br>
                <br>
                <modal
                        v-show="isModalVisible"
                        @close="closeModal"
                />
            </mu-col>
            <mu-col>
                <br>
                <mu-button color="yellow" style: text-color="black" v-if="!isUpdateVisible" @click="showUpdate">Изменить одну из записей
                </mu-button>
                <mu-button color="yellow" style: text-color="black"  v-if="isUpdateVisible" @click="updateTimetable(form.update_timetable)">Внести
                    изменения
                </mu-button>
            </mu-col>
            <mu-col>
                <br>
                <mu-button color="error" style: text-color="black" v-if="!isDeleteVisible" @click="showDelete">Удалить одну из записей</mu-button>
                <mu-button color="error" style: text-color="black" v-if="isDeleteVisible" @click="deleteTimetable(form.delete_timetable)">
                    Подтвердить
                </mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import modal from '../components/Add_timetable.vue';
    export default {
        name: "Nclass_timetable",
        props: ['id'],
        data() {
            return {
                nclass: {},
                isModalVisible: false,
                isDeleteVisible: false,
                isUpdateVisible: false,
                form: {
                    delete_timetable: '',
                    update_timetable: '',
                },
                form_update: {
                    day: '',
                    lesson: '',
                }
            }
        },
        components: {modal},
        created() {
            this.loadNclass()
        },
        methods: {
            async loadNclass() {
                this.nclass = await fetch(
                    `${this.$store.getters.getServerUrl}/nclass/${this.id}/`
                ).then(response => response.json())
                console.log(this.nclass)
                console.log(this.id)
            },
            showModal() {
                this.isModalVisible = true;
            },
            closeModal() {
                this.isModalVisible = false;
            },
            showDelete() {
                this.isDeleteVisible = !this.isDeleteVisible
            },
            async deleteTimetable(delete_timetable) {
                console.log(this.form.delete_timetable)
                const response = await fetch(`http://127.0.0.1:8000/api/v1/timetable/${this.form.delete_timetable}/delete`, {
                        method: 'DELETE',
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        }
                    }
                );
                if (response.status !== 204) {
                    alert(JSON.stringify(await response.json(), null, 2));
                }
                await alert('Вы удалили запись из расписания')
                this.isDeleteVisible = false
                await this.loadNclass()
            },
            showUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async updateTimetable(pupil) {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/timetable/${this.form.update_timetable}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_update)
                });
                await alert('Вы изменили запись в расписании')
                this.isUpdateVisible = false
                await this.loadChildren()
            },
        }
    }
</script>

<style scoped>
    .label {
        text-underline-color: #9ea7af;
        font-color: white;
    }
</style>