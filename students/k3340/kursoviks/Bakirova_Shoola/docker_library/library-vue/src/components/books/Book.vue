<template>
    <mu-col span="9">
        <div v-for="bk in book_one.book" v-bind:key="bk.id">
            <mu-row class="flex-description">

                    <mu-flex fill direction="column">
                        <mu-flex>Шифр книнги: {{bk.cipher}}</mu-flex>
                        <mu-flex>Название: {{bk.name}}</mu-flex>
                        <mu-flex>Автор: {{bk.author}}</mu-flex>
                        <mu-flex>Издательство: {{bk.publisher}}</mu-flex>
                        <mu-flex>Год издания: {{bk.year}}</mu-flex>
                        <mu-flex>Раздел: {{bk.section}}</mu-flex>
                        <mu-flex><br></mu-flex>
                    </mu-flex>
                    <mu-flex fill direction="column">
                        <mu-button color="deepPurpleA100" @click="openBookUpdate()" small>
                            Изменить
                        </mu-button>
                        <mu-dialog title="Изменение данных" :open.sync="showBook" width="1200">
                            <book-update :form_book="bk"></book-update>
                            <mu-button slot="actions" flat color="deepPurpleA100" @click="closeBookUpdate">Закрыть</mu-button>
                        </mu-dialog>
                        <mu-button color="deepPurpleA100" @click="deleteBook()" small class="flex-button">
                            Удалить
                        </mu-button>
                    </mu-flex>

            </mu-row>
        </div>
    </mu-col>
</template>

<script>
import BookUpdate from "./BookUpdate";

    export default {
        name: 'Book',
        components: {BookUpdate},
        props: {
            cipher: ''
        },
        data () {
            return {
                book_one: '',
                labelPosition: 'left',
                book_form: '',
                form: {
                    input: '',
                    date: ''
                },
                del_fix_form: [],
                showBook: false,
                book_id: '',
            }
        },
        created () {
            $.ajaxSetup({
              headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
            })
            this.loadBooks()

        },
        methods: {
            loadBooks () {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/library/book/',
                    type: 'GET',
                    data: {
                        book: this.cipher
                    },
                    success: (response) => {
                        this.book_one = response.data
                        this.book_id = response.data.book[0].id
                        //console.log(this.book_id)
                    }
                })
            },
            deleteBook() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/library/book_del/' + this.book_id + '/',
                    type: 'DELETE',
                    success: (response) => {
                        alert('Книга успешно удалёна')
                        this.$emit('reload')
                        this.loadBooks()
                    }
                })
            },
            openBookUpdate () {
                  this.showBook = true;
            },
            closeBookUpdate () {
                  this.showBook = false;
                  this.loadBooks()
            }
        }
    }
</script>

<style scoped>
    .detachment-form {
        width: 400px;
        height: 50px;
    }
    .flex-wrapper{
        width: 100%;
        height: 44px;
        margin-top: 8px;
    }
    .flex-button {
        margin-top: 8px;
    }
    .flex-description {
        width: 100%;
        margin-top: 56px;
        margin-left: 86px;
    }
    .mu-transition-row {
        margin-top: 16px;
        height: 100px;
    }
    .mu-transition-box {
        min-width: 200px;
        height: 100px;
        margin-right: 16px;
        border-radius: 4px;
        padding: 0 16px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
