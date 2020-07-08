<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Читательский билет №{{reader.library_card}}</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table>
                    <tr>
                        <td>ФИО</td>
                        <td>{{reader.fio}}</td>
                    </tr>
                    <tr>
                        <td>Номер паспорта</td>
                        <td>{{reader.passport_number}}</td>
                    </tr>
                    <tr>
                        <td>Дата рождения</td>
                        <td>{{reader.date_of_birth}}</td>
                    </tr>
                    <tr>
                        <td>Адрес</td>
                        <td>{{reader.address}}</td>
                    </tr>
                    <tr>
                        <td>Номер телефона</td>
                        <td>{{reader.phone}}</td>
                    </tr>
                    <tr>
                        <td>Образование</td>
                        <td>{{reader.education}}</td>
                    </tr>
                    <tr>
                        <td>Наличие ученой степени</td>
                        <td>{{reader.academic}}</td>
                    </tr>
                    <tr>
                        <td>Читальный зал</td>
                        <td>{{reader.reading_room}}</td>
                    </tr>
                </table>
            </mu-col>
            <mu-col v-if="isUpdateVisible">
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
                <mu-button color="black" @click="UpdateReader">Добавить</mu-button>
            </mu-col>
            <mu-col v-if="isBookVisible">
                <table v-for="book in reader.books" :key="book.id">
                    <tr>
                        <td>Книга</td>
                        <td>{{book.book}}</td>
                    </tr>
                    <tr>
                        <td>Дата взятия</td>
                        <td>{{book.date_take}}</td>
                    </tr>
                    <tr>
                        <td>Дата возврата</td>
                        <td>{{book.date_back}}</td>
                    </tr>
                </table>
                <mu-button color="indigo" @click="ShowBookAdd">Добавить книгу</mu-button>
                <br>
                <mu-form v-if="isBookAddVisible" style="width: 80%; height: 20%" :model="form_book" class="mu-demo-form"
                         label-width="40">
                    <mu-form-item prop="select" label="Книга">
                        <mu-select v-model="form_book.book">
                            <mu-option v-for="book in listBook" :key="book.id" :label="book.name"
                                       :value="book.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Дата взятия">
                        <mu-text-field v-model="form_book.date_take"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Дата возврата">
                        <mu-text-field v-model="form_book.date_back"></mu-text-field>
                    </mu-form-item>
                </mu-form>
                <mu-button v-if="isBookAddVisible" color="black" @click="AddBook">Добавить</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button color="indigo" @click="ShowUpdate">Изменить данные</mu-button>
            </mu-col>
            <mu-col>
                <mu-button color="indigo" @click="ShowBooks">Показать взятые книги</mu-button>
            </mu-col>
            <mu-col>
                <mu-button color="indigo" @click="deleteReader">Удалить читателя</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "ReaderSingle",
        props: ['id'],
        data() {
            return {
                reader: {},
                listRoom: [],
                listBook: [],
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
                isUpdateVisible: false,
                isBookVisible: false,
                isBookAddVisible: false,
                form_book: {
                    date_take: '',
                    date_back: '',
                    book: '',
                    reader: this.id,
                }
            }
        },
        created() {
            this.loadReader()
            this.loadListReadingRoom()
            this.loadListBook()
        },
        methods: {
            async loadListReadingRoom() {
                this.listRoom = await fetch(
                    `http://127.0.0.1:8000/api/v1/reading_room/`
                ).then(response => response.json())
            },
            async loadReader() {
                this.reader = await fetch(
                    `http://127.0.0.1:8000/api/v1/reader/${this.id}/`
                ).then(response => response.json())
            },
            async loadListBook() {
                this.listBook = await fetch(
                    `http://127.0.0.1:8000/api/v1/book/`
                ).then(response => response.json())
            },
            async deleteReader() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/reader/${this.id}/delete`, {
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
                await alert('Данный читатель удален')
                await this.$router.push({name: "Читатели"})
            },
            ShowBooks() {
                this.isBookVisible = !this.isBookVisible
            },
            ShowBookAdd() {
                this.isBookAddVisible = !this.isBookAddVisible
            },
            ShowUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async UpdateReader() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/reader/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form)
                });
                await alert('Данные о читателе успешно изменены')
                this.isUpdateVisible = !this.isUpdateVisible
                await this.loadReader()
            },
            AddBook() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/taking_book/create",
                    type: "POST",
                    data: {
                        date_take: this.form_book.date_take,
                        date_back: this.form_book.date_back,
                        book: this.form_book.book,
                        reader: this.form_book.reader,
                    },
                    success: (response) => {
                        alert("Книга добавлена")
                        this.isBookAddVisible = !this.isBookAddVisible
                        this.loadReader()
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