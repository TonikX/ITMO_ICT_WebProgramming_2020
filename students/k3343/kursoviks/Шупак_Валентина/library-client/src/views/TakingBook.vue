<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Учет книг</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table>
                    <tr>
                        <th>Читатель</th>
                        <th>Книга</th>
                        <th>Дата взятия</th>
                        <th>Дата возврата</th>
                    </tr>
                    <tr v-for="taking_book in listTaking" :key="taking_book.id">
                        <td>{{taking_book.reader}}</td>
                        <td>{{taking_book.book}}</td>
                        <td>{{taking_book.date_take}}</td>
                        <td>{{taking_book.date_back}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-form v-if="isAddVisible" style="width: 80%; height: 20%" :model="form_book" class="mu-demo-form"
                         label-width="40">
                    <mu-form-item prop="select" label="Читатель">
                        <mu-select v-model="form.reader">
                            <mu-option v-for="reader in listReader" :key="reader.id" :label="reader.fio"
                                       :value="reader.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Книга">
                        <mu-select v-model="form.book">
                            <mu-option v-for="book in listBook" :key="book.id" :label="book.name"
                                       :value="book.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Дата взятия">
                        <mu-text-field v-model="form.date_take"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Дата возврата">
                        <mu-text-field v-model="form.date_back"></mu-text-field>
                    </mu-form-item>
                </mu-form>
                <mu-button v-if="isAddVisible" color="black" @click="AddBook">Добавить</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button color="indigo" @click="ShowAdd">Добавить запись</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "TakingBook",
        props: ['id'],
        data() {
            return {
                listTaking: [],
                listReader: [],
                listBook: [],
                isAddVisible: false,
                form: {
                    date_take: '',
                    date_back: '',
                    book: '',
                    reader: '',
                }
            }
        },
        created() {
            this.loadListTakingBook()
            this.loadListReader()
            this.loadListBook()
        },
        methods: {
            async loadListTakingBook() {
                this.listTaking = await fetch(
                    `http://127.0.0.1:8000/api/v1/taking_book/`
                ).then(response => response.json())
            },
            async loadListReader() {
                this.listReader = await fetch(
                    `http://127.0.0.1:8000/api/v1/reader/`
                ).then(response => response.json())
            },
            async loadListBook() {
                this.listBook = await fetch(
                    `http://127.0.0.1:8000/api/v1/book/`
                ).then(response => response.json())
            },
            ShowAdd(){
                this.isAddVisible = !this.isAddVisible
            },
            AddBook() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/taking_book/create",
                    type: "POST",
                    data: {
                        date_take: this.form.date_take,
                        date_back: this.form.date_back,
                        book: this.form.book,
                        reader: this.form.reader,
                    },
                    success: (response) => {
                        alert("Запись добавлена")
                        this.isAddVisible = !this.isAddVisible
                        this.loadListTakingBook()
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