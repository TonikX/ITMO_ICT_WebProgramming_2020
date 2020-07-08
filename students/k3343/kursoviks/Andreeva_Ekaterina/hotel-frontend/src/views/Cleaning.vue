<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>График уборки номеров</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <mu-button @click="ShowFilter">Показать фильтры</mu-button>
                <mu-container v-if="isFilterVisible">
                <br>
                <mu-select v-model="form_filter.servant" label="Фильтр по служащему">
                            <mu-option v-for="servant in listServant" :key="servant.id" :label="servant.fio"
                                       :value="servant.id"></mu-option>
                            <mu-option label="        " value=""></mu-option>
                        </mu-select>
                <mu-select v-model="form_filter.floor" label="Фильтр по этажу">
                            <mu-option v-for="floor in listFloor" :key="floor.id" :label="floor.floor_number"
                                       :value="floor.id"></mu-option>
                            <mu-option label="        " value=""></mu-option>
                        </mu-select>
                <mu-select v-model="form_filter.day" label="Фильтр по дню недели">
                            <mu-option value="Понедельник" label="Понедельник"></mu-option>
                            <mu-option value="Вторник" label="Вторник"></mu-option>
                            <mu-option value="Среда" label="Среда"></mu-option>
                            <mu-option value="Четверг" label="Четверг"></mu-option>
                            <mu-option value="Пятница" label="Пятница"></mu-option>
                            <mu-option value="Суббота" label="Суббота"></mu-option>
                            <mu-option value="Воскресенье" label="Воскресенье"></mu-option>
                            <mu-option label="        " value=""></mu-option>
                        </mu-select>
                <br>
                <br>
                <mu-button @click="Filter">Отфильтровать</mu-button>
                </mu-container>
                <br>
                <br>
                <table>
                    <tr>
                        <th>День недели</th>
                        <th>Этаж</th>
                        <th>Служащий</th>
                    </tr>
                    <tr v-for="cleaning in listCleaning" :key="cleaning.id">
                        <td>{{cleaning.day}}</td>
                        <td>{{cleaning.floor}}</td>
                        <td>{{cleaning.servant}}</td>
                        <td v-if="isDeleteVisible">
                            <mu-radio v-model="form_delete" :value="cleaning.id"
                                      label=""></mu-radio>
                        </td>
                        <td v-if="isUpdateVisible">
                            <mu-radio v-model="form_update.id" :value="cleaning.id"
                                      label=""></mu-radio>
                        </td>
                    </tr>
                </table>
                <br>
                <mu-button color="primary" @click="ShowCreate">Добавить запись</mu-button>
                <mu-button color="primary" @click="ShowUpdate">Изменить запись</mu-button>
                <mu-button color="primary" @click="ShowDelete">Удалить запись</mu-button>
                <br>
                <br>
                <mu-button color="black" v-if="isDeleteVisible" @click="deleteCleaning">Подтвердить удаление</mu-button>
            </mu-col>
            <mu-col v-if="isUpdateVisible">
                <mu-radio v-model="form_update.day" value="Понедельник" label="Понедельник"></mu-radio>
                <br>
                <mu-radio v-model="form_update.day" value="Вторник" label="Вторник"></mu-radio>
                <br>
                <mu-radio v-model="form_update.day" value="Среда" label="Среда"></mu-radio>
                <br>
                <mu-radio v-model="form_update.day" value="Четверг" label="Четверг"></mu-radio>
                <br>
                <mu-radio v-model="form_update.day" value="Пятница" label="Пятница"></mu-radio>
                <br>
                <mu-radio v-model="form_update.day" value="Суббота" label="Суббота"></mu-radio>
                <br>
                <mu-button color="black" @click="UpdateCleaning">Внести изменения</mu-button>
            </mu-col>
            <mu-col v-if="isCreateVisible">
                <mu-form style="width: 50%" :model="form_create" class="mu-demo-form"
                         label-width="200">
                    <mu-form-item prop="select" label="Служащий">
                        <mu-select v-model="form_create.servant">
                            <mu-option v-for="servant in listServant" :key="servant.id" :label="servant.fio"
                                       :value="servant.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Этаж">
                        <mu-select v-model="form_create.floor">
                            <mu-option v-for="floor in listFloor" :key="floor.id" :label="floor.floor_number"
                                       :value="floor.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="radio" label="День недели">
                                <mu-radio v-model="form_create.day" value="Понедельник" label="Понедельник"></mu-radio>
                                <mu-radio v-model="form_create.day" value="Вторник" label="Вторник"></mu-radio>
                                <mu-radio v-model="form_create.day" value="Среда" label="Среда"></mu-radio>
                                <mu-radio v-model="form_create.day" value="Четверг" label="Четверг"></mu-radio>
                                <mu-radio v-model="form_create.day" value="Пятница" label="Пятница"></mu-radio>
                                <mu-radio v-model="form_create.day" value="Суббота" label="Суббота"></mu-radio>
                                <mu-radio v-model="form_create.day" value="Воскресенье" label="Воскресенье"></mu-radio>
                            </mu-form-item>
                </mu-form>
                <mu-button color="black" @click="CreateCleaning">Добавить</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Cleaning",
        props: ['id'],
        components: {},
        data() {
            return {
                listCleaning: [],
                listCleaningFilter: [],
                listFloor: [],
                listServant: [],
                isCreateVisible: false,
                isUpdateVisible: false,
                isDeleteVisible: false,
                form_create: {
                    day: '',
                    servant: '',
                    floor: '',
                },
                form_update: {
                    id: '',
                    day: '',
                },
                form_delete: {},
                form_filter:{
                    servant:'',
                    day:'',
                    floor:'',
                },
                isFilterVisible: false,
            }
        },
        created() {
            this.loadListCleaning()
            this.loadListServant()
            this.loadListFloor()
        },
        methods: {
            async loadListCleaning() {
                this.listCleaning = await fetch(
                    `http://127.0.0.1:8000/api/v1/cleaning/?servant=${this.form_filter.servant}&day=${this.form_filter.day}&floor=${this.form_filter.floor}`
                ).then(response => response.json())
                this.listCleaningFilter = await fetch(
                    `http://127.0.0.1:8000/api/v1/cleaning/`
                ).then(response => response.json())
            },
            Filter(){
                this.loadListCleaning()
            },
            async ShowFilter(){
                this.isFilterVisible = !this.isFilterVisible
                this.listCleaning = await fetch(
                    `http://127.0.0.1:8000/api/v1/cleaning/`
                ).then(response => response.json())

            },
            async loadListServant() {
                this.listServant = await fetch(
                    `http://127.0.0.1:8000/api/v1/servant/`
                ).then(response => response.json())
            },
            async loadListFloor() {
                this.listFloor = await fetch(
                    `http://127.0.0.1:8000/api/v1/floor/`
                ).then(response => response.json())
            },
            ShowDelete() {
                this.isDeleteVisible = !this.isDeleteVisible
            },
            async deleteCleaning() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/cleaning/${this.form_delete}/delete`, {
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
                await alert('Запись удалена')

                this.isDeleteVisible = !this.isDeleteVisible
                await this.loadListCleaning()
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            CreateCleaning() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/cleaning/create",
                    type: "POST",
                    data: {
                        day: this.form_create.day,
                        servant: this.form_create.servant,
                        floor: this.form_create.floor,
                    },
                    success: (response) => {
                        this.$router.push({name: "Уборка"})
                        alert("Добавлена запись в график уборки")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListCleaning()
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Данные введены неверно")
                        }
                    }

                })
            },
            ShowUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async UpdateCleaning() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/cleaning/${this.form_update.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_update)
                });
                await alert('График уборки успешно изменен')
                this.isUpdateVisible = !this.isUpdateVisible
                await this.loadListCleaning()
            },

        }
    }
</script>

<style scoped>

</style>е о проживающем