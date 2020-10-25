<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Водители</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>

                <mu-form label-position="left">
                    <mu-select v-model="form_filter.driver_class" label="Водительский класс">
                        <mu-option value="1_класс" label="1 класс"></mu-option>
                        <mu-option value="2_класс" label="2 класс"></mu-option>
                        <mu-option value="3_класс" label="3 класс"></mu-option>
                    </mu-select>
                </mu-form>
            </mu-col>
            <mu-col>
                <mu-button @click="Filter">Отфильтровать</mu-button>
            </mu-col>
            <mu-col>
                <mu-button @click="FilterReset">Сбросить фильтры</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <ul>
                    <li v-for="driver in listDriver" :key="driver.id">
                        <mu-radio v-if="isDeleteVisible" v-model="form_delete" :value="driver.id"
                                      label=""></mu-radio>
                        <a @click="goTo(driver.id)">{{driver.fio}}</a>
                    </li>
                </ul>
            </mu-col>
            <mu-col v-if="isCreateVisible">
                <mu-form label-position="left">
                    <mu-form-item prop="input" label="ФИО водителя">
                        <mu-text-field v-model="form_create.fio"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Номер паспорта">
                        <mu-text-field v-model="form_create.passport_number"></mu-text-field>
                    </mu-form-item>
                    <mu-select v-model="form_create.driver_class" label="Водительский класс">
                        <mu-option value="1_класс" label="1 класс"></mu-option>
                        <mu-option value="2_класс" label="2 класс"></mu-option>
                        <mu-option value="3_класс" label="3 класс"></mu-option>
                    </mu-select>
                    <mu-form-item prop="input" label="Стаж работы">
                        <mu-text-field v-model="form_create.work_exp"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Оклад">
                        <mu-text-field v-model="form_create.salary"></mu-text-field>
                    </mu-form-item>
                </mu-form>
                <mu-button @click="CreateDriver">Добавить</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col v-if="isDeleteVisible">
                <mu-button @click="DeleteDriver">Удалить</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button @click="ShowCreate">Добавить водителя</mu-button>
            </mu-col>
            <mu-col>
                <mu-button @click="ShowDelete">Удалить водителя</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from "jquery";
    export default {
        name: "Driver",
        components: {},
        data() {
            return {
                listDriver: [],
                isCreateVisible: false,
                isDeleteVisible: false,
                form_create: {
                    fio: '',
                    passport_number: '',
                    driver_class: '',
                    work_exp: '',
                    salary: '',
                },
                form_delete: {},
                form_filter: {
                    driver_class: '',
                },
            }
        },
        created() {
            this.loadListDriver()
            this.loadListDriverFull()
        },
        methods: {
            async loadListDriver() {
                this.listDriver = await fetch(
                    `http://127.0.0.1:8000/api/v1/driver/?driver_class=${this.form_filter.driver_class}`
                ).then(response => response.json())
            },
            async loadListDriverFull() {
                this.listDriver = await fetch(
                    `http://127.0.0.1:8000/api/v1/driver/`
                ).then(response => response.json())
            },
            Filter() {
                this.loadListDriver()
            },
            FilterReset() {
                this.loadListDriverFull()
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            goTo(id) {
                this.$router.push({name: 'Водитель', params: {id: id}})
            },
            CreateDriver() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/driver/create",
                    type: "POST",
                    data: {
                        fio: this.form_create.fio,
                        passport_number: this.form_create.passport_number,
                        driver_class: this.form_create.driver_class,
                        work_exp: this.form_create.work_exp,
                        salary: this.form_create.salary,
                    },
                    success: (response) => {
                        alert("Водитель успешно добавлен")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListDriverFull()
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
            async DeleteDriver() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/driver/${this.form_delete}/delete`, {
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
                await alert('Водитель удален')
                this.isDeleteVisible = !this.isDeleteVisible
                await this.loadListDriverFull()
            },
        }
    }
</script>

<style scoped>

</style>