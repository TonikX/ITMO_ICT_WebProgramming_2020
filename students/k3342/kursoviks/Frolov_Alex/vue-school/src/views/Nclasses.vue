<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>Список классов</h1>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col span="9">
                <ol class="ball" v-for="nclass in listNclass" :key="nclass.id">
                    <li><a href="#">{{nclass.number}} "{{nclass.letter}}"</a>
                        <mu-button round color="success" style: text-color="black" @click="goToChildrens(nclass.id)">Показать учеников</mu-button>
                        <mu-button round color="blue" style: text-color="black" @click="goToTimetable(nclass.id)">Показать расписание</mu-button>
                    </li>
                </ol>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "Nclasses",
        data() {
            return {
                listNclass: []
            }
        },
        components: {},
        created() {
            this.loadListNclass()
        },
        methods: {
            async loadListNclass() {
                this.listNclass = await fetch(
                    `${this.$store.getters.getServerUrl}/nclass`
                ).then(response => response.json())
            },
            goToChildrens(id) {
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