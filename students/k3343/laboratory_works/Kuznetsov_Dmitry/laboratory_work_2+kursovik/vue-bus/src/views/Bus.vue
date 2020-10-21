<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Автобусы</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col align="center">
                <table>
                    <tr>
                        <td>Тип автобуса</td>
                        <td>Вместимость</td>
                        <td>Автобусы</td>
                    </tr>
                    <tr v-for="bus_type in listBusType" :key="bus_type.id">
                        <td>{{bus_type.bus_type}}</td>
                        <td>{{bus_type.capacity}} человек</td>
                        <td>
                            <ol>
                                <li v-for="bus in bus_type.buses" :key="bus.id">
                        <mu-radio v-if="isDeleteVisible" v-model="form_delete" :value="bus.id"
                                      label=""></mu-radio>
                                    <a @click="goTo(bus.id)">{{bus.number}}</a>
                                </li>
                            </ol>
                        </td>
                    </tr>
                </table>
            </mu-col>
            <mu-col v-if="isCreateVisible">
                <mu-form label-position="left">
                    <mu-select v-model="form_create.bus_type" label="Тип автобуса">
                        <mu-option v-for="bus_type in listBusType" :key="bus_type.id" :label="bus_type.bus_type"
                                   :value="bus_type.id"></mu-option>
                    </mu-select>
                    <mu-form-item prop="input" label="Номер автобуса">
                        <mu-text-field v-model="form_create.number"></mu-text-field>
                    </mu-form-item>
                </mu-form>
                <mu-button @click="CreateBus">Добавить</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col v-if="isDeleteVisible">
                <mu-button @click="DeleteBus">Удалить</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button @click="ShowCreate">Добавить автобус</mu-button>
            </mu-col>
            <mu-col>
                <mu-button @click="ShowDelete">Удалить автобус</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Bus",
        components: {},
        data() {
            return {
                listBusType: [],
                isCreateVisible: false,
                isDeleteVisible: false,
                form_create: {
                    number: '',
                    bus_type: '',
                },
                form_delete: {},
            }
        },
        created() {
            this.loadListBusType()
        },
        methods: {
            async loadListBusType() {
                this.listBusType = await fetch(
                    `http://127.0.0.1:8000/api/v1/bus_type/`
                ).then(response => response.json())
            },
            goTo(id) {
                this.$router.push({name: 'Автобус', params: {id: id}})
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            CreateBus() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/bus/create",
                    type: "POST",
                    data: {
                        bus_type: this.form_create.bus_type,
                        number: this.form_create.number,
                    },
                    success: (response) => {
                        alert("Авотбус успешно добавлен")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListBusType()
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
            async DeleteBus() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/bus/${this.form_delete}/delete`, {
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
                await alert('Автобус удален')

                this.isDeleteVisible = !this.isDeleteVisible
                await this.loadListBusType()
            },

        }
    }
</script>

<style scoped>

</style>