<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>
                    Расписание занятий {{klass.number}} "{{klass.litera}}" класса
                </h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <table class="table-fill" v-for="timetable in klass.timetable" :key="timetable.id">
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
                            <mu-option label="1-8:00-8:45" value="1-8:00-8:45">1-8:00-8:45</mu-option>
                            <mu-option label="2-8:50-9:35" value="2-8:50-9:35">2-8:50-9:35</mu-option>
                            <mu-option label="3-9:40-10:25" value="3-9:40-10:25">3-9:40-10:25</mu-option>
                            <mu-option label="4-10:40-11:25" value="4-10:40-11:25">4-10:40-11:25</mu-option>
                            <mu-option label="5-11:30-12:15" value="5-11:30-12:15">5-11:30-12:15</mu-option>
                            <mu-option label="6-12:20-13:05" value="6-12:20-13:05">6-12:20-13:05</mu-option>
                            <mu-option label="7-13:05-13:50" value="7-13:05-13:50">7-13:05-13:50</mu-option>
                            <mu-option label="8-14:00-14:45" value="8-14:00-14:45">8-14:00-14:45</mu-option>
                        </mu-select>
                    </td>
                    <td class="text-left">Кабинет №{{timetable.cabinet_number}}</td>
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
                <mu-button color="success" @click="showModal">Добавить запись в расписание</mu-button>
                <br>
                <br>
                <modal
                        v-show="isModalVisible"
                        @close="closeModal"
                />
            </mu-col>
            <mu-col>
                <br>
                <mu-button color="primary" v-if="!isUpdateVisible" @click="showUpdate">Изменить одну из записей
                </mu-button>
                <mu-button color="primary" v-if="isUpdateVisible" @click="updateTimetable(form.update_timetable)">Внести
                    изменения
                </mu-button>
            </mu-col>
            <mu-col>
                <br>
                <mu-button color="error" v-if="!isDeleteVisible" @click="showDelete">Удалить одну из записей</mu-button>
                <mu-button color="error" v-if="isDeleteVisible" @click="deleteTimetable(form.delete_timetable)">
                    Подтвердить
                </mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import modal from '../components/Add_timetable.vue';

    export default {
        name: "Klass_timetable",
        props: ['id'],
        data() {
            return {
                klass: {},
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
            this.loadKlass()
        },
        methods: {
            async loadKlass() {
                this.klass = await fetch(
                    `${this.$store.getters.getServerUrl}/klass/${this.id}`
                ).then(response => response.json())
                console.log(this.klass)
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
                await alert('Вы успешно удалили запись из расписания!')
                this.isDeleteVisible = false
                await this.loadKlass()
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
                await alert('Вы успешно изменили запись в расписании')
                this.isUpdateVisible = false
                await this.loadPupil()
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