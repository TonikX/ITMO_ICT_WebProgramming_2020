<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Водитель №{{driver.id}}</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table>
                    <tr>
                        <td>ФИО водителя</td>
                        <td>{{driver.fio}}</td>
                    </tr>
                    <tr>
                        <td>Номер паспорта</td>
                        <td>{{driver.passport_number}}</td>
                    </tr>
                    <tr>
                        <td>Водительский класс</td>
                        <td>{{driver.driver_class}}</td>
                    </tr>
                    <tr>
                        <td>Стаж работы</td>
                        <td>{{driver.work_exp}}</td>
                    </tr>
                    <tr>
                        <td>Оклад</td>
                        <td>{{driver.salary}}</td>
                    </tr>
                </table>
            </mu-col>
            <mu-col v-if="isUpdateVisible">
                <mu-form label-position="left">
                    <mu-form-item prop="input" label="ФИО водителя">
                        <mu-text-field v-model="form_update.fio"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Номер паспорта">
                        <mu-text-field v-model="form_update.passport_number"></mu-text-field>
                    </mu-form-item>
                    <mu-select v-model="form_update.driver_class" label="Водительский класс">
                        <mu-option value="1_класс" label="1 класс"></mu-option>
                        <mu-option value="2_класс" label="2 класс"></mu-option>
                        <mu-option value="3_класс" label="3 класс"></mu-option>
                    </mu-select>
                    <mu-form-item prop="input" label="Стаж работы">
                        <mu-text-field v-model="form_update.work_exp"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Оклад">
                        <mu-text-field v-model="form_update.salary"></mu-text-field>
                    </mu-form-item>
                </mu-form>
                <mu-button @click="UpdateDriver">Обновить информацию</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
        <mu-button @click="ShowUpdate">Изменить информацию</mu-button>
            </mu-col>
            <mu-col>
        <mu-button @click="DeleteDriver">Удалить водителя</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "DriverSingle",
        props: ['id'],
        components: {},
        data() {
            return {
                driver: {},
                isUpdateVisible: false,
                form_update: {
                    fio: '',
                    passport_number: '',
                    driver_class: '',
                    work_exp: '',
                    salary: '',
                },
            }
        },
        created() {
            this.loadDriver()
        },
        methods: {
            async loadDriver() {
                this.driver = await fetch(
                    `http://127.0.0.1:8000/api/v1/driver/${this.id}/`
                ).then(response => response.json())
            },
            async DeleteDriver() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/driver/${this.id}/delete`, {
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
                await this.$router.push({name: "Водители"})
            },
            ShowUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async UpdateDriver() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/driver/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_update)
                });
                await alert('Данные о водителе успешно изменены')
                this.isUpdateVisible = !this.isUpdateVisible
                await this.loadDriver()
            },

        }
    }
</script>

<style scoped>

</style>