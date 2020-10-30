<template>
    <mu-container>
        <mu-row align="left">
            <mu-col>
                <h1>Список поданных заявок</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <ul>
                    <li v-for="application in listApplication" :key="application.id">
                    <a @click="goTo(application.id)">Заявка №{{application.id}}</a>
                </li>
                </ul>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "Application",
        props: ['id'],
        components: {},
        data() {
            return {
                listApplication: [],
            }
        },
        created() {
            this.loadListApplication()
        },
        methods: {
            async loadListApplication() {
                this.listApplication = await fetch(
                    `http://127.0.0.1:8000/api/v1/application/`
                ).then(response => response.json())
            },
            goTo(id) {
                this.$router.push({name: 'Заявка', params: {id: id}})
            },
    }
    }
</script>

<style scoped>

</style>