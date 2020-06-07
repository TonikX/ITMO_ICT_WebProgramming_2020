<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>
                    Расписание класса
                </h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <table>
                    <thead>
                    <tr>
                        <th colspan="4" class="text-left">{{timetable.day}}</th>
                    </tr>
                    </thead>
                    <tbody class="table-hover">
                    <tr>
                        <td class="text-left">{{timetable.lesson}}</td>
                        <td class="text-left">Кабинет №{{timetable.cabinet_number}}</td>
                        <td class="text-left">{{timetable.subject_name}}</td>
                        <td class="text-left">{{timetable.teacher_name}}</td>
                    </tr>
                    </tbody>
                </table>
                <br>
            </mu-col>
        </mu-row>

        <mu-row align="center">
            <mu-col>
                <mu-button color="success">Добавить запись в расписание</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>



<script>
    export default {
        name: "Timetable",
        data() {
            return {
                listTimetable: []
            }
        },
        components: {},
        created() {
            this.loadListTimetable()
        },
        methods: {
            async loadListTimetable() {
                this.listTimetable = await fetch(
                    `${this.$store.getters.getServerUrl}/timetable`
                ).then(response => response.json())
            },
        }
    }
</script>

<style scoped>

</style>