<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Список книг, которые имеются в библиотеке</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col v-if="isCreateVisible">
                <mu-form style="width: 80%; height: 20%" :model="form" class="mu-demo-form" label-width="40">
                            <mu-form-item prop="input" label="Название">
                                <mu-text-field v-model="form.name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Автор(ы)">
                                <mu-text-field v-model="form.author"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Издательство">
                                <mu-text-field v-model="form.publisher"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Год издания">
                                <mu-text-field v-model="form.year"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="select" label="Секция">
                                <mu-select v-model="form.section">
                                    <mu-option label="Художественная литература" value="Художественная_литература"></mu-option>
                                    <mu-option label="Учебная литература" value="Учебная_литература"></mu-option>
                                    <mu-option label="Научная литература" value="Научная_литература"></mu-option>
                                    <mu-option label="Докуентальна литература" value="Докуентальная_литература"></mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Шифр">
                                <mu-text-field v-model="form.cipher"></mu-text-field>
                            </mu-form-item>
                </mu-form>
                <br>
                <mu-button color="black" @click="CreateBook">Подтвердить</mu-button>
            </mu-col>
            <mu-col>
                <ul>
                    <li v-for="book in listBook" :key="book.id">
                        <mu-radio v-if="isDeleteVisible" v-model="form_delete" :value="book.id"
                                      :label="book.name"></mu-radio>
                        <a @click="goTo(book.id)" v-if="!isDeleteVisible">{{book.name}}</a>

                    </li>
                </ul>
            </mu-col>
        </mu-row>
        <mu-row v-if="isDeleteVisible" align="center">
            <mu-col>
                <br>
                <mu-button color="error" @click="deleteBook">Подтвердить удаление</mu-button>
            <br>
            </mu-col>
        </mu-row>
        <mu-row align="center">
                <br>
            <mu-col>
                <br>
                <mu-button color="indigo" @click="ShowCreate">Принять книгу в фонд библиотеки</mu-button>
            </mu-col>
            <mu-col>
                <br>
                <mu-button color="indigo" @click="ShowDelete">Списать книгу</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Book",
        props: ['id'],
        components: {},
        data() {
            return {
                listBook: [],
                isCreateVisible: false,
                isDeleteVisible: false,
                form: {
                    name: '',
                    author: '',
                    publisher: '',
                    year: '',
                    section: '',
                    cipher: '',
                },
                form_delete: {},
            }
        },
        created() {
            this.loadListBook()
        },
        methods: {
            async loadListBook() {
                this.listBook = await fetch(
                    `http://127.0.0.1:8000/api/v1/book/`
                ).then(response => response.json())
            },
            goTo(id) {
                this.$router.push({name: 'Книга', params: {id: id}})
            },
            ShowDelete() {
                this.isDeleteVisible = !this.isDeleteVisible
            },
            async deleteBook() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/book/${this.form_delete}/delete`, {
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
                await alert('Книга удалена')

                this.isDeleteVisible = !this.isDeleteVisible
                await this.loadListBook()
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            CreateBook() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/book/create",
                    type: "POST",
                    data: {
                        name: this.form.name,
                        author: this.form.author,
                        publisher: this.form.publisher,
                        year: this.form.year,
                        section: this.form.section,
                        cipher: this.form.cipher,
                    },
                    success: (response) => {
                        this.$router.push({name: "Книги"})
                        alert("Книга добавлена")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListBook()
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