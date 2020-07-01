<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>Командир экипажа</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table class="paleBlueRows" width="60%">
                    <tr>
                        <td>Фамилия</td>
                        <td>{{crewcommander.last_name}}</td>
                    </tr>
                    <tr>
                        <td>Имя</td>
                        <td>{{crewcommander.first_name}}</td>
                    </tr>
                    <tr>
                        <td>Отчество</td>
                        <td>{{crewcommander.second_name}}</td>
                    </tr>
                    <tr>
                        <td>Дата рождения</td>
                        <td>{{crewcommander.date_of_birth}}</td>
                    </tr>
                    <tr>
                        <td>Образование</td>
                        <td>{{crewcommander.education}}</td>
                    </tr>
                    <tr>
                        <td>Опыт работы в годах</td>
                        <td>{{crewcommander.work_experience}}</td>
                    </tr>
                    <tr>
                        <td>Допуск на рейс</td>
                        <td>{{crewcommander.flight_admission}}</td>
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
                <mu-button color="primary" @click="deleteCrewCommander(crewcommander.id)">Удалить</mu-button>
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

                <mu-button color="primary" @click="updateCrewCommander(crewcommander.id)">Внести изменения
                </mu-button>
                </mu-col>
            </mu-row>
        <br>
    </mu-container>
</template>

<script>
    export default {
        name: "CrewCommander",
        props: ['id'],
        data() {
            return {
                crewcommander: {},
                isUpdateVisible: false,
                form: {}
            }
        },
        created() {
            this.loadCrewCommander()
        },
        methods: {
            async loadCrewCommander() {
                this.crewcommander = await fetch(
                    `http://127.0.0.1:8000/api/v1/crewcommander/${this.id}`
                ).then(response => response.json())
            },
            async deleteCrewCommander(crewcommander) {
                const {id} = crewcommander;
                const response = await fetch(`http://127.0.0.1:8000/api/v1/crewcommander/${this.id}/delete`, {
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
                await alert('Вы уволили командира экипажа')
                await this.$router.push({name: "Сотрудники"})
            },
            showUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async updateCrewCommander() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/crewcommander/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form)
                });
                this.isUpdateVisible = !this.isUpdateVisible
                await alert('Вы успешно изменили данные о командире экипажа')
                await this.loadCrewCommander()
            },
        }
    }
</script>

<style scoped>

</style>