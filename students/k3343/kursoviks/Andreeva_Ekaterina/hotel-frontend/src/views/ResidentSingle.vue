<template>

    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Проживающий</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table width="70%">
                    <tr>
                        <td>Номер</td>
                        <td>{{resident.room}}</td>
                    </tr>
                    <tr>
                        <td>ФИО</td>
                        <td>{{resident.fio}}</td>
                    </tr>
                    <tr>
                        <td>Номер паспорта</td>
                        <td>{{resident.passport_number}}</td>
                    </tr>
                    <tr>
                        <td>Прибыл(а) из города</td>
                        <td>{{resident.from_town}}</td>
                    </tr>
                    <tr>
                        <td>Дата заселения</td>
                        <td>{{resident.check_in}}</td>
                    </tr>
                    <tr>
                        <td>Дата выселения</td>
                        <td>{{resident.check_out}}</td>
                    </tr>
                </table>
                <mu-button color="primary" @click="ShowUpdate">Изменить данные</mu-button>
                <mu-button color="primary" @click="deleteResident">Удалить проживающего</mu-button>
            </mu-col>
            <mu-col v-if="isUpdateVisible">
                <mu-form style="width: 50%" :model="form_update" class="mu-demo-form" :label-position="labelPosition"
                         label-width="200">
                    <mu-form-item prop="input" label="ФИО">
                        <mu-text-field v-model="form_update.fio"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Номер паспорта">
                        <mu-text-field v-model="form_update.passport_number"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Прибыл(а) из города">
                        <mu-text-field v-model="form_update.from_town"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Дата заселения гггг-мм-дд">
                        <mu-text-field v-model="form_update.check_in"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Дата выселения гггг-мм-дд">
                        <mu-text-field v-model="form_update.check_out"></mu-text-field>
                    </mu-form-item>
                </mu-form>
                <mu-button color="black" @click="UpdateResident">Внести изменения</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "ResidentSingle",
        props: ['id'],
        data() {
            return {
                resident: {},
                isUpdateVisible: false,
                form_update: {
                    fio: '',
                    passport_number: '',
                    from_town: '',
                    check_in: '',
                    check_out: '',
                }
            }
        },
        created() {
            this.loadResident()
        },
        methods: {
            async loadResident() {
                this.resident = await fetch(
                    `http://127.0.0.1:8000/api/v1/resident/${this.id}/`
                ).then(response => response.json())
            },
            async deleteResident() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/resident/${this.id}/delete`, {
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
                await alert('Проживающий удален')
                await this.$router.push({name: "Проживающие"})
            },
            ShowUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async UpdateResident() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/resident/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_update)
                });
                await alert('Данные о проживающем успешно изменены')
                this.isUpdateVisible = !this.isUpdateVisible
                await this.loadResident()
            },
        }
    }
</script>

<style scoped>

</style>