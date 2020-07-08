<template>
    <div id="app">
        <mu-container>
            <mu-appbar color="indigo400">
                <p align="left">Web-сервис для работника библиотеки</p>
                <mu-menu slot="right">
                    <mu-button flat> Меню
                    </mu-button>
                    <mu-list slot="content">
                        <mu-list-item button href="/">
                            <mu-list-item-title>Главная страница</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/book">
                            <mu-list-item-title>Книги</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/reader">
                            <mu-list-item-title>Читатели</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/reading_room">
                            <mu-list-item-title>Читальные залы</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/taking_book">
                            <mu-list-item-title>Учет книг</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/queries">
                            <mu-list-item-title>Запросы</mu-list-item-title>
                        </mu-list-item>
                    </mu-list>
                </mu-menu>
                <mu-button flat slot="right" v-if="!auth" @click="goLogin">Войти</mu-button>
                <mu-button flat slot="right" v-else @click="logout">Выйти</mu-button>
            </mu-appbar>
        </mu-container>
        <router-view/>
    </div>
</template>


<script>
    export default {
        name: "App",
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "Вход"})
            },
            logout() {
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            },
        }
    }
</script>
<style>
#app {
  font-family: "Roboto Light", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

    a {
        cursor: pointer;
    }
    h1{
        font-family: "Roboto Thin";
    }
    p{
        font-family: "Roboto Light";
    }
    table {
        border-radius: 5px;
        font-family: "Roboto Light";
        font-size: 14px;
        font-weight: normal;
        border: black;
        border-collapse: initial;
        white-space: normal;
        background-color: #abbaed;
        width: 80%;
    }

    td, th {
        font-size: 16px;
        text-align: left;
        padding: 3px;
    }

    td {
        border-bottom: 1px solid black;
        font-size: 12px;
    }

    thead th {
        color: #ffffff;
        background: blanchedalmond;
    }


    thead th:nth-child(odd) {
        color: #ffffff;
        background: #324960;
    }

    tr:nth-child(even) {
        background: #dae5ff;
    }
</style>
