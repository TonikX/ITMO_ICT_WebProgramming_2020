<template>
        <mu-container>
        <mu-row align="left">
            <mu-col>
                <h1>Список соискателей</h1>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col>
                <ul>
                    <li v-for="applicant in listApplicant" :key="applicant.id">
                    <a @click="goTo(applicant.id)">{{applicant.fio}}</a>
                </li>
                </ul>
            </mu-col>
        </mu-row>
            <mu-row>
                <mu-col>
                    <mu-button href="#/applicant_reg">Зарегистрировать нового соискателя</mu-button>
                </mu-col>
            </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "Applicants",
        props: ['id'],
        components: {},
        data() {
            return {
                listApplicant: [],
            }
        },
        created() {
            this.loadListApplicant()
        },
        methods: {
            async loadListApplicant() {
                this.listApplicant = await fetch(
                    `http://127.0.0.1:8000/api/v1/applicant/`
                ).then(response => response.json())
            },
            goTo(id) {
                this.$router.push({name: 'Соискатель', params: {id: id}})
            },
        }
    }
</script>

<style scoped>

</style>