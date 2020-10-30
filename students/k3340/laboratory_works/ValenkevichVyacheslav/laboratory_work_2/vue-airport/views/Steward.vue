<template>
        <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>Бортпроводник</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table class="paleBlueRows" width="60%">
                    <tr>
                        <td>Фамилия</td>
                        <td>{{steward.last_name}}</td>
                    </tr>
                    <tr>
                        <td>Имя</td>
                        <td>{{steward.first_name}}</td>
                    </tr>
                    <tr>
                        <td>Отчество</td>
                        <td>{{steward.second_name}}</td>
                    </tr>
                    <tr>
                        <td>Дата рождения</td>
                        <td>{{steward.date_of_birth}}</td>
                    </tr>
                    <tr>
                        <td>Образование</td>
                        <td>{{steward.education}}</td>
                    </tr>
                    <tr>
                        <td>Опыт работы в годах</td>
                        <td>{{steward.work_experience}}</td>
                    </tr>
                    <tr>
                        <td>Допуск на рейс</td>
                        <td>{{steward.flight_admission}}</td>
                    </tr>
                    <tr>
                        <td>Экипаж</td>
                        <td>{{steward.crew}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
            <br>
        <mu-row>
            <mu-col>
                <mu-button v-if="!isUpdateVisible" color="primary" @click="showUpdate">Изменить</mu-button>
            </mu-col>
            <mu-col>
                <mu-button color="primary" @click="deleteSteward(steward.id)">Удалить</mu-button>
            </mu-col>
        </mu-row>
            <mu-row v-if="isUpdateVisible" align="center">
                <mu-col>
                    <table class="paleBlueRows">
                        <tr>
                            <td>Новая фамилия</td>
                            <td>Новое имя</td>
                            <td>Новое отчество</td>
                        </tr>
                        <tr>
                            <td><mu-text-field v-model="form.last_name"></mu-text-field></td>
                            <td><mu-text-field v-model="form.first_name"></mu-text-field></td>
                            <td><mu-text-field v-model="form.second_name"></mu-text-field></td>
                        </tr>
                    </table>

                <mu-button color="primary" @click="updateSteward(steward.id)">Внести изменения
                </mu-button>
                </mu-col>
            </mu-row>
            <br>
    </mu-container>
</template>

<script>
    export default {
        name: "Steward",
        props: ['id'],
        data() {
            return {
                steward: {},
                isUpdateVisible: false,
                form: {}
            }
        },
        created() {
            this.loadSteward()
        },
        methods: {
            async loadSteward() {
                this.steward = await fetch(
                    `http://127.0.0.1:8000/api/v1/steward/${this.id}`
                ).then(response => response.json())
            },
            async deleteSteward(steward) {
                const {id} = steward;
                const response = await fetch(`http://127.0.0.1:8000/api/v1/steward/${this.id}/delete`, {
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
                await alert('Вы уволили бортпроводника')
                await this.$router.push({name: "Сотрудники"})
            },
            showUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async updateSteward() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/steward/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form)
                });
                this.isUpdateVisible = !this.isUpdateVisible
                await alert('Вы успешно изменили данные о бортпроводнике')
                await this.loadSteward()
            },
        }
    }
</script>

<style scoped>

</style>