<template>
        <mu-container>
        <mu-appbar style="width: 100%;" color="primary">
            <mu-menu slot="left">
                <mu-button flat> Меню
                </mu-button>
                <mu-list slot="content">
                    <mu-list-item button href="/">
                        <mu-list-item-title>Главная страница</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="#/route">
                        <mu-list-item-title>Маршруты</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="#/employee">
                        <mu-list-item-title>Сотрудники</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="#/flight">
                        <mu-list-item-title>Рейсы</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="#/queries">
                        <mu-list-item-title>Запросы</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="#/report">
                        <mu-list-item-title>Отчеты</mu-list-item-title>
                    </mu-list-item>
                </mu-list>
            </mu-menu>
            Администрирование аэропорта
            <mu-button flat slot="left" v-if="!auth" @click="goLogin">Войти</mu-button>
            <mu-button flat slot="left" v-else @click="logout">Выйти</mu-button>
        </mu-appbar>
    </mu-container>
</template>

<script>
    export default {
        name: "Navbar",
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

<style scoped>

</style>