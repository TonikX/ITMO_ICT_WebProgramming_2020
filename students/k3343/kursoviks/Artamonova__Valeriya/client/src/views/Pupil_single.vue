<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>
                    Досье ученика
                </h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <table class="table-fill">
                    <thead>
                    <tr>
                        <th colspan="3" class="text-center"></th>
                    </tr>
                    </thead>
                    <tbody class="table-hover">
                    <tr>
                        <td class="text-left">Фамилия</td>
                        <td colspan="2" class="text-left">{{pupil.last_name}}
                            <br>
                            <mu-text-field v-if="isElVisible" v-model="form.last_name"></mu-text-field>
                        </td>
                    </tr>
                    <tr>
                        <td class="text-left">Имя</td>
                        <td colspan="2" class="text-left">{{pupil.first_name}}
                            <br>
                            <mu-text-field v-if="isElVisible" v-model="form.first_name"></mu-text-field>

                        </td>
                    </tr>
                    <tr>
                        <td class="text-left">Отчество</td>
                        <td colspan="2" class="text-left">{{pupil.second_name}}

                            <br>
                            <mu-text-field v-if="isElVisible" v-model="form.second_name"></mu-text-field>
                        </td>
                    </tr>
                    <tr>
                        <td class="text-left">Пол</td>
                        <td colspan="2" class="text-left">{{pupil.gender}}
                        </td>
                    </tr>
                    <tr>
                        <td class="text-left">Класс</td>
                        <td colspan="2" class="text-left">{{pupil.klass}}</td>
                    </tr>
                    </tbody>
                </table>
                <table class="table-fill">
                    <thead>
                    <tr>
                        <th colspan="3" class="text-center">Оценки за четверть
                            <br>
                            <mu-button color="success" @click="showModal">Добавить оценку</mu-button>
                            <modal
                                    v-show="isModalVisible"
                                    @close="closeModal"
                            />
                            <mu-button color="primary" v-if="!isUpdateVisible" @click="showGradeUpdate">Изменить оценку
                            </mu-button>
                            <mu-button color="primary" v-if="isUpdateVisible"
                                       @click="updateGrade(form_change.update_grade)">Внести
                                изменения
                            </mu-button>
                            <mu-button color="error" v-if="!isDeleteVisible" @click="showDelete">Удалить одну из
                                оценок
                            </mu-button>
                            <mu-button color="error" v-if="isDeleteVisible"
                                       @click="deleteGrade(form_change.delete_grade)">
                                Подтвердить
                            </mu-button>
                        </th>
                    </tr>
                    </thead>
                    <tbody class="table-hover" v-for="grade in pupil.grades" :key="grade.id">
                    <tr>
                        <td class="text-left">{{grade.subject}}
                        </td>
                        <td class="text-left">{{grade.grade}}
                        </td>
                        <td class="text-center" v-if="isDeleteVisible">
                            <mu-radio v-model="form_change.delete_grade" :value="grade.id"
                                      label="Удалить"></mu-radio>
                        </td>
                        <td class="text-center" v-if="isUpdateVisible">
                            <mu-radio v-model="form_change.update_grade" :value="grade.id"
                                      label="Изменить"></mu-radio>
                            <br>
                            <mu-text-field v-model="form_grade.grade"></mu-text-field>
                        </td>
                    </tr>
                    </tbody>
                </table>
                <br>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <mu-button v-if="isElVisible" color="success" @click="updatePupil(pupil.id)">Внести изменения
                </mu-button>
                <mu-button v-if="!isElVisible" color="success" @click="showUpdate">Изменить данные об ученике
                </mu-button>
            </mu-col>
            <mu-col>
                <mu-button color="error" @click="deletePupil(pupil.id)">Удалить ученика</mu-button>
                <br>
                <br>
            </mu-col>
        </mu-row>
        <mu-row>
        </mu-row>
    </mu-container>
</template>

<script>
    import modal from '../components/Add_grade.vue';
    import $ from 'jquery'

    export default {
        name: "Pupil_single",
        props: ['id'],
        data() {
            return {
                isElVisible: false,
                isGradeVisible: false,
                isModalVisible: false,
                listSubject: [],
                pupil: {},
                grades: {},
                klass: {},
                labelPosition: 'right',
                form: {},
                form_grade: {
                    grade: '',
                    student: this.id,
                },
                isDeleteVisible: false,
                isUpdateVisible: false,
                form_change: {
                    delete_grade: '',
                    update_grade: '',
                },
            }
        },
        components: {
            modal
        },
        created() {
            this.loadListSubject()
            this.loadPupil()
        },
        methods: {
            async loadPupil() {
                this.pupil = await fetch(
                    `${this.$store.getters.getServerUrl}/pupil/${this.id}`
                ).then(response => response.json())
                console.log(this.pupil)
                console.log(this.id)
            },
            async deletePupil(pupil) {
                const {id} = pupil;
                const response = await fetch(`http://127.0.0.1:8000/api/v1/pupil/${this.id}/delete`, {
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
                await alert('Вы успешно удалили ученика! Так ему и надо')
                await this.$router.push({name: "Ученики"})
            },
            showModal() {
                this.isModalVisible = true;
            },
            closeModal() {
                this.isModalVisible = false;
            },
            close() {
                this.$emit('close');
            },
            showUpdate() {
                this.isElVisible = !this.isElVisible
            },
            async updatePupil(pupil) {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/pupil/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form)
                });
                if (response.status !== 202) {
                    await alert('Вы успешно изменили данные об ученике')
                    this.isElVisible = !this.isElVisible
                    await this.loadPupil()
                }

            },
            async loadListSubject() {
                this.listSubject = await fetch(
                    `${this.$store.getters.getServerUrl}/subject`
                ).then(response => response.json())
            },
            async updateGrade(pupil) {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/grade/${this.form_change.update_grade}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_grade)
                });
                await alert('Вы успешно изменили оценку')
                this.isUpdateVisible = false
                await this.loadPupil()
            },
            showDelete() {
                this.isDeleteVisible = !this.isDeleteVisible
            },
            async deleteGrade(delete_grade) {
                console.log(this.form_change)
                const response = await fetch(`http://127.0.0.1:8000/api/v1/grade/${this.form_change.delete_grade}/delete`, {
                        method: 'DELETE',
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        }
                    }
                );
                if (response.status !== 204) {
                    alert(JSON.stringify(await response.json(), null, 2))
                }
                await alert('Вы успешно удалили оценку!')
                this.isDeleteVisible = false
                await this.loadPupil()
            },
            showGradeUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
        }
    }
</script>

<style scoped>
</style>