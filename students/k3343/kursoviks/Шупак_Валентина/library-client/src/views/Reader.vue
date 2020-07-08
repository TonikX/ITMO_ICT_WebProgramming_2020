<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Читатели</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col v-if="isCreateVisible">
                <mu-form style="width: 80%; height: 20%" :model="form" class="mu-demo-form" label-width="40">
                    <mu-form-item prop="input" label="Номер читательского билета">
                        <mu-text-field v-model="form.library_card"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="ФИО">
                        <mu-text-field v-model="form.fio"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Номер паспорта">
                        <mu-text-field v-model="form.passport_number"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Дата рождения гггг-мм-дд">
                        <mu-text-field v-model="form.date_of_birth"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Адрес">
                        <mu-text-field v-model="form.address"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Номер телефона">
                        <mu-text-field v-model="form.phone"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Образование">
                        <mu-select v-model="form.education">
                            <mu-option label="Начальное" value="Начальное"></mu-option>
                            <mu-option label="Среднее неоконченное" value="Среднее_неоконченное"></mu-option>
                            <mu-option label="Среднее" value="Среднее"></mu-option>
                            <mu-option label="Высшее неоконченное" value="Высшее_неоконченное"></mu-option>
                            <mu-option label="Высшее" value="Высшее"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="radio" label="Ученая степень">
                        <mu-radio v-model="form.academic" value="True" label="Есть"></mu-radio>
                        <mu-radio v-model="form.academic" value="False" label="Нет"></mu-radio>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Читальный зал">
                        <mu-select v-model="form.reading_room">
                            <mu-option v-for="room in listRoom" :key="room.id" :label="room.name"
                                       :value="room.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
                <mu-button color="black" @click="CreateReader">Добавить</mu-button>
            </mu-col>
            <mu-col>
                <table>
                    <tr>
                        <th>Читательский билет</th>
                        <th>ФИО</th>
                        <th></th>
                    </tr>
                    <tr v-for="reader in listReader" :key="reader.id">
                        <td>
                            <mu-radio v-if="isDeleteVisible" v-model="form_delete" :value="reader.id"></mu-radio>
                            {{reader.library_card}}
                        </td>
                        <td>{{reader.fio}}</td>
                        <td>
                            <mu-button color="indigo" @click="goTo(reader.id)">Подробнее</mu-button>
                        </td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
        <mu-row v-if="isDeleteVisible" align="center">
            <mu-col>
                <br>
                <mu-button color="error" @click="deleteReader">Подтвердить удаление</mu-button>
                <br>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <br>
            <mu-col>
                <br>
                <mu-button color="indigo" @click="ShowCreate">Добавить читателя</mu-button>
            </mu-col>
            <mu-col>
                <br>
                <mu-button color="indigo" @click="ShowDelete">Удалить читателя</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Reader",
        props: ['id'],
        components: {},
        data() {
            return {
                listReader: [],
                listRoom: [],
                isCreateVisible: false,
                isDeleteVisible: false,
                form: {
                    library_card: '',
                    fio: '',
                    date_of_birth: '',
                    passport_number: '',
                    address: '',
                    phone: '',
                    education: '',
                    academic: '',
                    reading_room: '',
                },
                form_delete: {},
            }
        },
        created() {
            this.loadListReader()
            this.loadListReadingRoom()
        },
        methods: {
            async loadListReadingRoom() {
                this.listRoom = await fetch(
                    `http://127.0.0.1:8000/api/v1/reading_room/`
                ).then(response => response.json())
            },
            async loadListReader() {
                this.listReader = await fetch(
                    `http://127.0.0.1:8000/api/v1/reader/`
                ).then(response => response.json())
            },
            goTo(id) {
                this.$router.push({name: 'Читатель', params: {id: id}})
            },
            ShowDelete() {
                this.isDeleteVisible = !this.isDeleteVisible
            },
            async deleteReader() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/reader/${this.form_delete}/delete`, {
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
                await alert('Читатель удален')

                this.isDeleteVisible = !this.isDeleteVisible
                await this.loadListReader()
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            CreateReader() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/reader/create",
                    type: "POST",
                    data: {

                        library_card: this.form.library_card,
                        fio: this.form.fio,
                        passport_number: this.form.passport_number,
                        date_of_birth: this.form.date_of_birth,
                        address: this.form.address,
                        phone: this.form.phone,
                        education: this.form.education,
                        academic: this.form.academic,
                        reading_room: this.form.reading_room,
                    },
                    success: (response) => {
                        this.$router.push({name: "Читатели"})
                        alert("Читатель добавлен")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListReader()
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Данные введены неверно")
                        }
                    }

                })
            }
        }
    }
</script>

<style scoped>

</style>