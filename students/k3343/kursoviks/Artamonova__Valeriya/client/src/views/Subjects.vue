<template>
    <mu-container>
        <mu-row align="center">
            <mu-col span="10" align-self="center">
                <h1>Список дисциплин, преподаваемых в школе</h1>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col span="10">
                <ol class="ball" v-for="subject in listSubject" :key="subject.id">
                    <li><a href="#">{{subject.subject}}</a></li>
                </ol>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "Subjects",
        data() {
            return {
                listSubject: []
            }
        },
        components: {},
        created() {
            this.loadListSubject()
        },
        methods: {
            async loadListSubject() {
                this.listSubject = await fetch(
                    `${this.$store.getters.getServerUrl}/subject`
                ).then(response => response.json())
            }
        }
    }
</script>

<style scoped>

</style>