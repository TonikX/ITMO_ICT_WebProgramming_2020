<template>
    <div id="app">
        <mu-container>
            <mu-appbar style="width: 100%;" color="#444140">
                
                <mu-button flat slot="left" v-if="!auth" @click="goLogin">Войти</mu-button>
                <mu-button flat slot="left" v-else @click="logout">Выйти</mu-button>
                <p align="right">Биржа труда</p>
                <mu-menu slot="left">
                    <mu-button flat> Меню
                    </mu-button>
                    <mu-list slot="content">
                        <mu-list-item button href="#/vacancy">
                            <mu-list-item-title>Вакансии</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/course">
                            <mu-list-item-title>Курсы</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/gratuity">
                            <mu-list-item-title>Пособие</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/employer">
                            <mu-list-item-title>Работодатели</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/applicant">
                            <mu-list-item-title>Соискатели</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/application">
                            <mu-list-item-title>Заявки</mu-list-item-title>
                        </mu-list-item>
                    </mu-list>
                </mu-menu>
                <mu-button flat slot="left" href="#/">Главная</mu-button>
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
        color: #2c3e50;
    }
    table{
    border-radius: 5px;
    font-size: 12px;
    font-weight: normal;
    border: dimgrey;
    border-collapse: collapse;
    white-space: nowrap;
    background-color: #b5bdc4;
}

td, th {
    text-align: center;
    padding: 10px;
}

td {
    border: 2px solid dimgrey;
    font-size: 14px;
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
