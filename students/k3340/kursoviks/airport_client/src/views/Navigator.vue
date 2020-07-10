<template>
        <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>Штурман</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table class="paleBlueRows" width="60%">
                    <tr>
                        <td>Фамилия</td>
                        <td>{{navigator.last_name}}</td>
                    </tr>
                    <tr>
                        <td>Имя</td>
                        <td>{{navigator.first_name}}</td>
                    </tr>
                    <tr>
                        <td>Отчество</td>
                        <td>{{navigator.second_name}}</td>
                    </tr>
                    <tr>
                        <td>Дата рождения</td>
                        <td>{{navigator.date_of_birth}}</td>
                    </tr>
                    <tr>
                        <td>Образование</td>
                        <td>{{navigator.education}}</td>
                    </tr>
                    <tr>
                        <td>Опыт работы в годах</td>
                        <td>{{navigator.work_experience}}</td>
                    </tr>
                    <tr>
                        <td>Допуск на рейс</td>
                        <td>{{navigator.flight_admission}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
            <br>
        <mu-row>
            <mu-col>
                <mu-button v-if="!isUpdateVisible" @click="showUpdate" color="primary">Изменить</mu-button>
            </mu-col>
            <mu-col>
                <mu-button color="primary" @click="deleteNavigator(navigator.id)">Удалить</mu-button>
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

                <mu-button color="primary" @click="updateNavigator(navigator.id)">Внести изменения
                </mu-button>
                </mu-col>
            </mu-row>
            <br>
    </mu-container>
</template>

<script>
    export default {
        name: "Navigator",
        props: ['id'],
        data() {
            return {
                navigator: {},
                isUpdateVisible: false,
                form: {}
            }
        },
        created() {
            this.loadNavigator()
        },
        methods: {
            async loadNavigator() {
                this.navigator = await fetch(
                    `http://127.0.0.1:8000/api/v1/navigator/${this.id}`
                ).then(response => response.json())
            },
            async deleteNavigator(navigator) {
                const {id} = navigator;
                const response = await fetch(`http://127.0.0.1:8000/api/v1/navigator/${this.id}/delete`, {
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
                await alert('Вы уволили штурмана')
                await this.$router.push({name: "Сотрудники"})
            },
            showUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async updateNavigator() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/navigator/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form)
                });
                this.isUpdateVisible = !this.isUpdateVisible
                await alert('Вы успешно изменили данные о штурмане')
                await this.loadNavigator()
            },
        }
    }
</script>

<style scoped>

</style>