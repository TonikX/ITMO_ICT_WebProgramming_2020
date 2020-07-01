<template>
        <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>Второй пилот</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table class="paleBlueRows" width="60%">
                    <tr>
                        <td>Фамилия</td>
                        <td>{{secondpilot.last_name}}</td>
                    </tr>
                    <tr>
                        <td>Имя</td>
                        <td>{{secondpilot.first_name}}</td>
                    </tr>
                    <tr>
                        <td>Отчество</td>
                        <td>{{secondpilot.second_name}}</td>
                    </tr>
                    <tr>
                        <td>Дата рождения</td>
                        <td>{{secondpilot.date_of_birth}}</td>
                    </tr>
                    <tr>
                        <td>Образование</td>
                        <td>{{secondpilot.education}}</td>
                    </tr>
                    <tr>
                        <td>Опыт работы в годах</td>
                        <td>{{secondpilot.work_experience}}</td>
                    </tr>
                    <tr>
                        <td>Допуск на рейс</td>
                        <td>{{secondpilot.flight_admission}}</td>
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
                <mu-button color="primary" @click="deleteSecondPilot(secondpilot.id)">Удалить</mu-button>
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

                <mu-button color="primary" @click="updateSecondPilot(secondpilot.id)">Внести изменения
                </mu-button>
                </mu-col>
            </mu-row>
            <br>
    </mu-container>
</template>

<script>
    export default {
        name: "SecondPilot",
        props: ['id'],
        data() {
            return {
                secondpilot: {},
                isUpdateVisible: false,
                form: {}
            }
        },
        created() {
            this.loadSecondPilot()
        },
        methods: {
            async loadSecondPilot() {
                this.secondpilot = await fetch(
                    `http://127.0.0.1:8000/api/v1/secondpilot/${this.id}`
                ).then(response => response.json())
            },
            async deleteSecondPilot(secondpilot) {
                const {id} = secondpilot;
                const response = await fetch(`http://127.0.0.1:8000/api/v1/secondpilot/${this.id}/delete`, {
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
                await alert('Вы уволили второго пилота')
                await this.$router.push({name: "Сотрудники"})
            },
            showUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async updateSecondPilot() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/secondpilot/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form)
                });
                this.isUpdateVisible = !this.isUpdateVisible
                await alert('Вы успешно изменили данные о втором пилоте')
                await this.loadSecondPilot()
            },
        }
    }
</script>

<style scoped>

</style>