<template>
    <div id="app">
        <mu-container>
            <mu-appbar color="#222222">
                <p align="left">Система для администратора гостиницы</p>
                <mu-button flat slot="right" v-if="!auth" @click="goLogin">Войти</mu-button>
                <mu-button flat slot="right" v-else @click="logout">Выйти</mu-button>
                <mu-menu slot="right">
                    <mu-button flat> Меню
                    </mu-button>
                    <mu-list slot="content">
                        <mu-list-item button href="/">
                            <mu-list-item-title>Главная страница</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/room">
                            <mu-list-item-title>Номера</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/resident">
                            <mu-list-item-title>Проживающие</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/servant">
                            <mu-list-item-title>Служащие</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/cleaning">
                            <mu-list-item-title>График уборки номеров</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/queries">
                            <mu-list-item-title>Запросы</mu-list-item-title>
                        </mu-list-item>
                    </mu-list>
                </mu-menu>
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
        font-family: Helvetica, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    a {
        cursor: pointer;
        color: royalblue;
    }
    a:active {
        color: dodgerblue;
    }

    a:visited {
        color: royalblue;
    }
    table{
    border-radius: 5px;
    font-size: 12px;
    font-weight: normal;
    border: dimgrey;
    border-collapse: collapse;
    white-space: nowrap;
    background-color: #a7d4fc;
}

td, th {
    text-align: center;
    padding: 8px;
}

td {
    border-right: 1px solid dimgrey;
    font-size: 12px;
}

thead th {
    color: #ffffff;
    background: #d0ebfc;
}


thead th:nth-child(odd) {
    color: #ffffff;
    background: #324960;
}
tr:nth-child(even) {
    background: #F8F8F8;
}
</style>
