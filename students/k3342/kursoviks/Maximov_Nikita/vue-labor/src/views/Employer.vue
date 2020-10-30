<template>
    <mu-container>
        <mu-row align="left">
            <mu-col>
                <h1>Список работодателей</h1>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col>
                <ul>
                    <li v-for="employer in listEmployer" :key="employer.id">
                    <a @click="goTo(employer.id)">{{employer.name}}</a>
                </li>
                </ul>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "Employer",
        props: ['id'],
        components: {},
        data() {
            return {
                listEmployer: [],
            }
        },
        created() {
            this.loadListEmployer()
        },
        methods: {
            async loadListEmployer() {
                this.listEmployer = await fetch(
                    `http://127.0.0.1:8000/api/v1/employer/`
                ).then(response => response.json())
            },
            goTo(id) {
                this.$router.push({name: 'Работодатель', params: {id: id}})
            },
        }
    }
</script>

<style scoped>

</style>