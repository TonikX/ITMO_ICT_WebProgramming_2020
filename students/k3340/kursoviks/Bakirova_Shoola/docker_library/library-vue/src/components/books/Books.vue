<template>
    <mu-container>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <mu-appbar style="width: 100%;" color="deepPurpleA100">
            <mu-menu slot="left" v-if="auth">
                <mu-button flat icon>
                    <mu-icon value="menu"></mu-icon>
                </mu-button>
                <mu-list slot="content">
                    <mu-list-item button @click="goReaders()">
                        <mu-list-item-content>
                            <mu-list-item-title>Читатели</mu-list-item-title>
                        </mu-list-item-content>
                    </mu-list-item>
                    <mu-list-item button @click="goBooks()">
                        <mu-list-item-content>
                            <mu-list-item-title>Книги</mu-list-item-title>
                        </mu-list-item-content>
                    </mu-list-item>
                    <mu-list-item button @click="goHalls()">
                        <mu-list-item-content>
                            <mu-list-item-title>Залы</mu-list-item-title>
                        </mu-list-item-content>
                    </mu-list-item>
                </mu-list>
            </mu-menu>
            <h2 @click="goHome()">Библиотека</h2>
            <mu-button flat slot="right" v-if="auth" @click="logout">ВЫХОД</mu-button>
        </mu-appbar>
        <mu-row>
            <mu-col span="3" >
                <mu-flex justify-content="start" class="flex-wrapper">
                    <h2>Книги:</h2>
                </mu-flex>
                <mu-flex class="flex-wrapper">
                    <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="50">
                        <mu-text-field v-model="form.cipher" placeholder="Поиск по шифру" ></mu-text-field>
                    </mu-form>
                </mu-flex>
                <mu-flex justify-content="end" label-height="28px">
                    <mu-button color="deepPurpleA100" @click="openByCard()" small class="form-button">
                        Искать
                    </mu-button>
                </mu-flex>
                <mu-flex>
                    <mu-button class="button-reader" @click="openBookAdd()" >Добавить</mu-button>
                    <mu-dialog title="Добавление книги" :open.sync="showBookAdd" width="1200">
                        <book-add></book-add>
                        <mu-button slot="actions" flat color="deepPurpleA100" @click="closeBookAdd">Закрыть</mu-button>
                    </mu-dialog>
                </mu-flex>
                <div v-for="book in books" v-bind:key="book.id" >
                    <mu-flex class="flex-readers" fill>
                        <h3 @click="openFull(book.attributes.cipher)">
                            {{book.attributes.author}} "{{book.attributes.name}}"
                        </h3>
                    </mu-flex>
                    <mu-flex class="flex-card" justify-content="end">
                        <small>шифр №{{book.attributes.cipher}}</small>
                    </mu-flex>
                </div>
            </mu-col>
            <book v-if="book_full.show" :cipher="book_full.cipher" @reload="loadBooks"></book>
        </mu-row>
    </mu-container>
</template>

<script>
import BookAdd from "./BookAdd";
import Book from "./Book";

export default {
    name: "Books",
    components: {BookAdd, Book},
    created() {
        $.ajaxSetup({
            headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
        })
        this.loadBooks()
    },
    data () {
        return {
            books: [],
            form: {
                cipher: ''
            },
            labelPosition: 'left',
            book_full: {
                cipher: '',
                show: false
            },
            showBookAdd: false,
        }
    },
    computed: {
        auth() {
            if (sessionStorage.getItem("auth_token")) {
                return true
            }
        }
    },
    methods: {
        logout() {
            sessionStorage.removeItem("auth_token")
            window.location = '/'
        },
        goBooks() {
            this.$router.push({'name': 'books'})
        },
        goReaders() {
            this.$router.push({'name': 'readers'})
        },
        goHome() {
            this.$router.push({name: 'home'})
        },
        goHalls() {
            this.$router.push({name: 'halls'})
        },
        openByCard () {
            this.books.forEach(function (value) {
                if (value.attributes.cipher === this.form.cipher) {
                    this.openFull(value.attributes.cipher)
                }
            }.bind(this))
        },
        openFull: function (cipher) {
            //console.log(this.book_full.id)
            if (this.book_full.show === true) {
                let cipher2 = cipher
                this.book_full.show = false
                setTimeout(function (cipher) {
                    this.book_full.cipher = cipher
                    this.book_full.show = true
                }.bind(this), 10, cipher = cipher2)
            } else {
                this.book_full.cipher = cipher
                this.book_full.show = true
            }
        },
        loadBooks() {
            $.ajax({
                url: 'http://127.0.0.1:8000/api/v1/library/books/',
                type: 'GET',
                success: (response) => {
                    this.books = response.data
                }
            })
        },
        openBookAdd(){
            this.showBookAdd = true;
            this.loadBooks()
        },
        closeBookAdd(){
            this.showBookAdd = false;
            this.loadBooks()
        }
    },
}
</script>

<style scoped>
    h2 {
        cursor: pointer
    }
    .form-button {
        margin-top: -12px;
        margin-right: 10px;
    }
    .button-reader {
        width: 100%;
        margin-top: 16px;
    }
    h3 {
        cursor: pointer
    }
    .flex-readers {
        width: 100%;
        height: 36px;
        margin-top: 8px;
        text-align: start;
    }
    .flex-card {
        width: 100%;
        height: 30px;
        text-align: right;
        line-height: 32px;
        margin-top: 0;
    }
    .flex-card:first-child {
      margin-left: 0;
    }
    .flex-wrapper{
        width: 100%;
        height: 56px;
    }
    .mu-demo-form {
        width: 100%;
        max-width: 250px;
    }
</style>
