<template>
    <v-app-bar dark color="primary" fixed app>
        <v-toolbar-title>
            <span>Неизвестный питер</span>
        </v-toolbar-title>
        <v-spacer/>
        <v-btn text @click="navigateToQuests()">Квесты</v-btn>
        <v-btn text @click="navigateToTeams()">Команды</v-btn>
    </v-app-bar>
</template>

<script>
    export default {
        name: "MainNavbar",
        methods: {
            navigateToQuests() {
                this.$router.push({name: 'quests'})
            },
            navigateToTeams() {
                this.$router.push({name: 'teams'})
            }
        }
    }
</script>

<style scoped>

</style>