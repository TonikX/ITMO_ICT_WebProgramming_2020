<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>
                    Досье учителя
                </h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <table class="table-fill">
                    <thead>
                    <tr>
                        <th colspan="2" class="text-center"></th>
                    </tr>
                    </thead>
                    <tbody class="table-hover">
                    <tr>
                        <td class="text-left">Фамилия</td>
                        <td class="text-left">{{teacher.last_name}}
                        <br>
                            <mu-text-field v-if="isUpdateVisible" v-model="form.last_name"></mu-text-field>
                        </td>
                    </tr>
                    <tr>
                        <td class="text-left">Имя</td>
                        <td class="text-left">{{teacher.first_name}}
                        <br>
                            <mu-text-field v-if="isUpdateVisible" v-model="form.first_name"></mu-text-field>
                        </td>
                    </tr>
                    <tr>
                        <td class="text-left">Отчество</td>
                        <td class="text-left">{{teacher.second_name}}
                        <br>
                            <mu-text-field v-if="isUpdateVisible" v-model="form.second_name"></mu-text-field></td>
                    </tr>
                    <tr>
                        <td class="text-left">Предмет</td>
                        <td class="text-left">{{teacher.subject}}</td>
                    </tr>
                    <tr v-for="klass in teacher.klass" :key="klass.id">
                        <td class="text-left">Имеет классное руководство</td>
                        <td class="text-left"> {{klass.number}} "{{klass.litera}}"</td>
                    </tr>
                    <tr v-for="cabinet in teacher.cabinet" :key="cabinet.id">
                        <td class="text-left">Имеет закрепленный за собой кабинет</td>
                        <td class="text-left">Кабинет №{{cabinet.number}}</td>
                    </tr>
                    <tr>
                        <td class="text-left">Преподает до</td>
                        <td class="text-left">{{teacher.teaching_period}}
                        <br>
                            <mu-text-field v-if="isUpdateVisible" v-model="form.teaching_period"></mu-text-field>
                    </td>
                    </tr>
                    </tbody>
                </table>
                <br>
            </mu-col>
        </mu-row>

        <mu-row align="center">
            <mu-col>
                <mu-button v-if="isUpdateVisible" color="success" @click="updateTeacher(teacher.id)">Внести изменения
                </mu-button>
                <mu-button v-else color="success" @click="showUpdate">Изменить данные об учителе</mu-button>
            </mu-col>
            <mu-col>
                <mu-button color="error" @click="deleteTeacher(teacher.id)">Удалить учителя</mu-button>
                <br>
                <br>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "Teacher_single",
        props: ['id'],
        data() {
            return {
                isUpdateVisible: false,
                teacher: {},
                form: {},
            }
        },
        created() {
            this.loadTeacher()
        },
        methods: {
            async loadTeacher() {
                this.teacher = await fetch(
                    `${this.$store.getters.getServerUrl}/teacher/${this.id}`
                ).then(response => response.json())
            },
            async deleteTeacher(teacher) {
                const {id} = teacher;
                const response = await fetch(`http://127.0.0.1:8000/api/v1/teacher/${this.id}/delete`, {
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
                await alert('Вы успешно уволили учителя! Так ему и надо')
                await this.$router.push({name: "Учителя"})
            },
            showUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async updateTeacher(pupil) {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/teacher/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form)
                });
                this.isUpdateVisible = !this.isUpdateVisible
                await alert('Вы успешно изменили данные об учителе')
                await this.loadTeacher()
            },
        }
    }
</script>

<style scoped>

</style>