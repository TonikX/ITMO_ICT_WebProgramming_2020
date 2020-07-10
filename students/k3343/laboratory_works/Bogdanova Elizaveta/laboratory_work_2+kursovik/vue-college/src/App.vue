<template>
    <div id="app">
        <mu-container>
            <mu-appbar color="secondary">
                <mu-menu slot="left">
                    <mu-button flat> Меню
                    </mu-button>
                    <mu-list slot="content">
                        <mu-list-item button href="/">
                            <mu-list-item-title>Главная страница</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/faculty">
                            <mu-list-item-title>Факультеты и специальности</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/enrollee">
                            <mu-list-item-title>Абитуриенты</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/docs">
                            <mu-list-item-title>Документы</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/application">
                            <mu-list-item-title>Заявки</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/queries">
                            <mu-list-item-title>Запросы</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/report">
                            <mu-list-item-title>Отчеты</mu-list-item-title>
                        </mu-list-item>
                    </mu-list>
                </mu-menu>
                Петровский колледж
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
                if (localStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "Вход"})
            },
            logout() {
                localStorage.removeItem("auth_token")
                window.location = '/'
            },
        }
    }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        background-color: whitesmoke;
    }

    a {
        cursor: pointer;
    }

    table {
        border-radius: 5px;
        font-size: 12px;
        font-weight: normal;
        border: grey;
        border-collapse: collapse;
        white-space: nowrap;
        background-color: #fcbac8;
        max-width: 600px;
    }

    td, th {
        text-align: center;
        padding: 8px;
    }

    td {
        border-right: 1px solid gray;
        font-size: 12px;
    }

    thead th {
        color: #ffffff;
        background: lightpink;
    }


    thead th:nth-child(odd) {
        color: #ffffff;
        background: #324960;
    }

    tr:nth-child(even) {
        background: #F8F8F8;
    }
</style>
