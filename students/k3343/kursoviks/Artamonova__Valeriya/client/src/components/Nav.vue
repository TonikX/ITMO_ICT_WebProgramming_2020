<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="success">
            <mu-menu slot="left">
                <mu-button flat> Menu
                </mu-button>
                <mu-list slot="content">
                    <mu-list-item button href="/">
                        <mu-list-item-title>Главная страница</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/teacher">
                        <mu-list-item-title>Учителя</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/klass">
                        <mu-list-item-title>Классы</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/pupils">
                        <mu-list-item-title>Ученики школы</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/subjects">
                        <mu-list-item-title>Дисциплины</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/cabinets">
                        <mu-list-item-title>Кабинеты</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/queries">
                        <mu-list-item-title>Запросы</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button href="/klass_report">
                        <mu-list-item-title>Отчет по классу</mu-list-item-title>
                    </mu-list-item>
                </mu-list>
            </mu-menu>
            SchoolWeb
            <mu-button flat slot="right" v-if="!auth" @click="goLogin">LOGIN</mu-button>
            <mu-button flat slot="right" v-else @click="logout">LOGOUT</mu-button>
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