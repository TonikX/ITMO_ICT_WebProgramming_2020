<template>
    <div id="app">
        <mu-container>
            <mu-appbar color="#211f50">
                <p align="center">Автобусный парк</p>
                <mu-button flat slot="right" v-if="!auth" @click="goLogin">Войти</mu-button>
                <mu-button flat slot="right" v-else @click="logout">Выйти</mu-button>
                <mu-menu slot="left">
                    <mu-button flat> Меню
                    </mu-button>
                    <mu-list slot="content">
                        <mu-list-item button href="#/">
                            <mu-list-item-title>Главная страница</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/bus">
                            <mu-list-item-title>Автобусы</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/driver">
                            <mu-list-item-title>Водители</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/route">
                            <mu-list-item-title>Маршруты</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/schedule">
                            <mu-list-item-title>График работы водителей</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/query">
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
        font-family: Palatino, serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    a {
        cursor: pointer;
        color: #292cb3;
    }
    a:active {
        color: #2bd7ed;
    }
    a:visited {
        color: #7592f3;
    }
    table{
    border-radius: 3px;
    font-size: 12px;
    font-weight: normal;
    border: #201e7b;
    border-collapse: collapse;
    white-space: nowrap;
    background-color: #a9ceea;
}

td, th {
    text-align: center;
    padding: 8px;
}

td {
    border: 1px solid #101755;
    font-size: 12px;
}

thead th {
    color: #ffffff;
    background: #4a92c4;
}


tr:nth-child(odd) {
    background: #98b4c7;
}
tr:nth-child(even) {
    background: #c6e7f6;
}
</style>
