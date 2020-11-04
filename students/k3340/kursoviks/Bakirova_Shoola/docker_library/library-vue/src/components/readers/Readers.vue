<template>
    <mu-container>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500">
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
                    <h2 >Читатели:</h2>
                </mu-flex>
                <mu-flex class="flex-wrapper">
                    <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="50">
                        <mu-text-field v-model="form.search" placeholder="Поиск по билету и паспорту" ></mu-text-field>
                    </mu-form>
                </mu-flex>
                <mu-flex justify-content="end" label-height="28px">
                    <mu-button color="deepPurpleA100" @click="openByCard()" small class="form-button">
                        Искать
                    </mu-button>
                </mu-flex>
                <mu-flex>
                    <mu-button class="button-reader" @click="openReaderAdd()" >Добавить</mu-button>
                    <mu-dialog title="Добавление читателя" :open.sync="showReaderAdd" width="1200">
                        <reader-add></reader-add>
                        <mu-button slot="actions" flat color="deepPurpleA100" @click="closeReaderAdd">Закрыть</mu-button>
                    </mu-dialog>
                </mu-flex>
                <div v-for="reader in readers" v-bind:key="reader.id" >
                    <mu-flex class="flex-readers" fill>
                        <h3 @click="openFull(reader.id)">{{reader.attributes.name}}</h3>
                    </mu-flex>
                    <mu-flex class="flex-card" justify-content="end">
                        <small>билет №{{reader.attributes.library_card}}</small>
                    </mu-flex>
                </div>
            </mu-col>
            <reader v-if="reader_full.show" :id="reader_full.id" @reload="loadReader"></reader>
        </mu-row>
    </mu-container>
</template>

<script>

import Reader from './Reader'
import ReaderAdd from "./ReaderAdd";

export default {
    name: "Readers",
    components: {
        ReaderAdd,
        Reader
    },
    computed: {
        auth() {
            if (sessionStorage.getItem("auth_token")) {
                return true
            }
        }
    },
    data () {
        return {
            readers: [],
            form: {
                search: ''
            },
            labelPosition: 'left',
            reader_full: {
                id: '',
                show: false
            },
            showReaderAdd: false,
        }
    },
    methods: {
        logout() {
            sessionStorage.removeItem("auth_token")
            window.location = '/'
        },
        goBooks () {
            this.$router.push({'name': 'books'})
        },
        goReaders () {
            this.$router.push({'name': 'readers'})
        },
        goHome() {
            this.$router.push({name: 'home'})
        },
        goHalls() {
            this.$router.push({name: 'halls'})
        },
        openByCard () {
            this.readers.forEach(function (value) {
                if (value.attributes.library_card === this.form.search || value.attributes.passport_number === this.form.search) {
                    let reader = value.id
                    this.form.search = ''
                    this.openFull(reader)
                }
            }.bind(this))
        },
        loadReader() {
            $.ajax({
                url: 'http://127.0.0.1:8000/api/v1/library/readers/',
                type: 'GET',
                success: (response) => {
                    this.readers = response.data
                }
            })
        },
        openFull: function (id) {
            if (this.reader_full.show === true) {
                let id2 = id
                this.reader_full.show = false
                setTimeout(function (id) {
                    this.reader_full.id = id
                    this.reader_full.show = true
                }.bind(this), 10, id = id2)
            } else {
                this.reader_full.id = id
                this.reader_full.show = true
            }
        },
        openReaderAdd(){
            this.showReaderAdd = true;
        },
        closeReaderAdd(){
            this.showReaderAdd = false;
            this.loadReader()
        }
    },
    created () {
        $.ajaxSetup({
            headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
        })
        this.loadReader()
    }
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
