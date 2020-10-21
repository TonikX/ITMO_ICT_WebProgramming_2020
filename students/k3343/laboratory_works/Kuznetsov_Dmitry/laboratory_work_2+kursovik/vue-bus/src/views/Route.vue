<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Маршруты</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <table>
                    <tr>
                        <td>Начальный пункт движения</td>
                        <td>Конечный пункт движения</td>
                        <td>Время начала движения</td>
                        <td>Время окончания движения</td>
                        <td>Интервал движения в минутах</td>
                        <td>Протяженность в минутах</td>
                        <td>Протяженность в километрах</td>
                    </tr>
                    <tr v-for="route in listRoute" :key="route.id">
                        <td>
                        <mu-radio v-if="isDeleteVisible" v-model="form_delete" :value="route.id"
                                      label=""></mu-radio>
                        <mu-radio v-if="isUpdateVisible" v-model="form_update.id" :value="route.id"
                                      label=""></mu-radio>
                            {{route.starting_point}}</td>
                        <td>{{route.final_destination}}</td>
                        <td>{{route.time_start}}</td>
                        <td>{{route.time_end}}</td>
                        <td>{{route.interval_of_movement}}</td>
                        <td>{{route.length_in_min}}</td>
                        <td>{{route.length_in_km}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button @click="ShowCreate">Добавить маршрут</mu-button>
            </mu-col>
            <mu-col>
                <mu-button @click="ShowUpdate">Изменить маршрут</mu-button>
            </mu-col>
            <mu-col>
                <mu-button @click="ShowDelete">Удалить маршрут</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col v-if="isCreateVisible">
                <mu-form label-position="left">
                    <mu-form-item prop="input" label="Начальный пункт движения">
                        <mu-text-field v-model="form_create.starting_point"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Конечный пункт движения">
                        <mu-text-field v-model="form_create.final_destination"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Время начала движения">
                        <mu-text-field v-model="form_create.time_start"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Время окончания движения">
                        <mu-text-field v-model="form_create.time_end"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Интервал движения в минутах">
                        <mu-text-field v-model="form_create.interval_of_movement"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Протяженность в минутах">
                        <mu-text-field v-model="form_create.length_in_min"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Протяженность в километрах">
                        <mu-text-field v-model="form_create.length_in_km"></mu-text-field>
                    </mu-form-item>
                </mu-form>
                <mu-button @click="CreateRoute">Добавить</mu-button>
            </mu-col>
            <mu-col v-if="isUpdateVisible">
                <mu-form label-position="left">
                    <mu-form-item prop="input" label="Начальный пункт движения">
                        <mu-text-field v-model="form_update.starting_point"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Конечный пункт движения">
                        <mu-text-field v-model="form_update.final_destination"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Время начала движения">
                        <mu-text-field v-model="form_update.time_start"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Время окончания движения">
                        <mu-text-field v-model="form_update.time_end"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Интервал движения в минутах">
                        <mu-text-field v-model="form_update.interval_of_movement"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Протяженность в минутах">
                        <mu-text-field v-model="form_update.length_in_min"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Протяженность в километрах">
                        <mu-text-field v-model="form_update.length_in_km"></mu-text-field>
                    </mu-form-item>
                </mu-form>
                <mu-button @click="UpdateRoute">Подтвердить</mu-button>
            </mu-col>
            <mu-col v-if="isDeleteVisible">
                <mu-button @click="DeleteRoute">Удалить</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "Route",
        components: {},
        data() {
            return {
                listRoute: [],
                isCreateVisible: false,
                isUpdateVisible: false,
                isDeleteVisible: false,
                form_create: {
                    starting_point: '',
                    final_destination: '',
                    time_start: '',
                    time_end: '',
                    interval_of_movement: '',
                    length_in_min: '',
                    length_in_km: '',
                },
                form_delete: {},
                form_update: {
                    id: '',
                    starting_point: '',
                    final_destination: '',
                    time_start: '',
                    time_end: '',
                    interval_of_movement: '',
                    length_in_min: '',
                    length_in_km: '',
                },
            }
        },
        created() {
            this.loadListRoute()
        },
        methods: {
            async loadListRoute() {
                this.listRoute = await fetch(
                    `http://127.0.0.1:8000/api/v1/route/`
                ).then(response => response.json())
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            CreateRoute() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/route/create",
                    type: "POST",
                    data: {
                        starting_point: this.form_create.starting_point,
                        final_destination: this.form_create.final_destination,
                        time_start: this.form_create.time_start,
                        time_end: this.form_create.time_end,
                        interval_of_movement: this.form_create.interval_of_movement,
                        length_in_min: this.form_create.length_in_min,
                        length_in_km: this.form_create.length_in_km,
                    },
                    success: (response) => {
                        alert("Маршрут успешно добавлен")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListRoute()
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Данные введены неверно")
                        }
                    }

                })
            },
            ShowDelete() {
                this.isDeleteVisible = !this.isDeleteVisible
            },
            async DeleteRoute() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/route/${this.form_delete}/delete`, {
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
                await alert('Маршрут удален')
                this.isDeleteVisible = !this.isDeleteVisible
                await this.loadListRoute()
            },
            ShowUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async UpdateRoute() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/route/${this.form_update.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_update)
                });
                await alert('Данные о маршруте успешно изменены')
                this.isUpdateVisible = !this.isUpdateVisible
                await this.loadListRoute()
            },

        }
    }
</script>

<style scoped>

</style>