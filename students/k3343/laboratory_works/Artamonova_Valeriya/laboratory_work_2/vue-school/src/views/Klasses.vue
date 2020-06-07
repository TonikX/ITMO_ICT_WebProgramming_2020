<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>Список классов</h1>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col span="10">
                <ol class="ball" v-for="klass in listKlass" :key="klass.id">
                    <li><a href="#">{{klass.number}} "{{klass.litera}}"</a>
                        <mu-button round color="primary" @click="goToPupils(klass.id)">Показать учеников</mu-button>
                        <mu-button round color="secondary" @click="goToTimetable(klass.id)">Показать расписание</mu-button>
                    </li>
                </ol>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "Klasses",
        data() {
            return {
                listKlass: []
            }
        },
        components: {},
        created() {
            this.loadListKlass()
        },
        methods: {
            async loadListKlass() {
                this.listKlass = await fetch(
                    `${this.$store.getters.getServerUrl}/klass`
                ).then(response => response.json())
            },
            goToPupils(id) {
                this.$router.push({name: 'Ученики класса', params: {id: id}})
            },
            goToTimetable(id) {
                this.$router.push({name: 'Расписание класса', params: {id: id}})
            }
        }
    }
</script>

<style scoped>

</style>