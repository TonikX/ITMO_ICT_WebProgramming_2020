<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="darkslategray">
            <mu-menu slot="left">
                <mu-button flat> Меню
                </mu-button>
                <mu-list slot="content">
                    <mu-list-item button href="/">
                        <mu-list-item-title>Главная страница</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/teacher">
                        <mu-list-item-title>Учителя</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/subjects">
                        <mu-list-item-title>Предметы</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/nclass">
                        <mu-list-item-title>Классы</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/children">
                        <mu-list-item-title>Ученики</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/rooms">
                        <mu-list-item-title>Кабинеты</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/timetable">
                        <mu-list-item-title>Расписание</mu-list-item-title>
                    </mu-list-item>
                </mu-list>
            </mu-menu>
            <mu-row align="center">
            <mu-col span="11">
                    <h3>Школа номер 1</h3>
                </mu-col>
        </mu-row>
            <mu-button flat slot="right" v-if="!auth" @click="goLogin">Войти</mu-button>
            <mu-button flat slot="right" v-else @click="logout">Выйти</mu-button>
        </mu-appbar>
    </mu-container>
</template>

<script>
    export default {
        name: "Nav",
        computed: {
            auth() {
                if (localStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "login"})
            },
            logout() {
                localStorage.removeItem("auth_token")
                window.location = '/'
            },
        }
    }
</script>

<style scoped>
    #home {
        margin-top: 0;
        font-size: 20px;
    }
</style>
