<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>
                    Расписание классов
                </h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <table class="table-fill" v-for="timetable in listTimetable" :key="timetable.id">
                    <thead>
                    <tr v-for="nclass in timetable.nclass_name" :key="nclass.id">
                        <th colspan="4" class="text-left">{{timetable.nclass_name}} "{{nclass.letter}}"</th>
                    </tr>
                    </thead>
                    <tbody class="table-hover">

                    <tr>
                        <td class="text-left">{{timetable.day}}</td>
                        <td class="text-left">{{timetable.lesson}}</td>
                        <td class="text-left">Кабинет №{{timetable.room_number}}</td>
                        <td class="text-left">{{timetable.subject_name}}</td>
                        <td class="text-left">{{timetable.teacher_name}}</td>
                    </tr>
                    </tbody>
                </table>
            </mu-col>
        </mu-row>
        <button @click="filterTimetable()">Filter!</button>
        <button @click="addFilter()">+</button>
        <ul>
            <li v-for="filter in filters" :key="id">
                <input v-model="filter.key">
                <input v-model="filter.value">
                <button @click="dropFilter(filter)">-</button>
            </li>
        </ul>

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
                listTimetable: [],
                filters: [],
            }
        },
        components: {},
        created() {
            this.loadListTimetable();

        },
        methods: {
            async loadListTimetable(url = 'http://127.0.0.1:8000/api/v1/timetable/') {
                const response = await fetch(url);
                const results = await response.json();
                this.listTimetable = results;
            },
            addFilter() {
                this.filters.push({id: Math.random()});
            },
            dropFilter(filter) {
                this.filters = this.filters.filter(f => f.id !== filter.id);
            },
            async filterTimetable() {
                const filledFilters = this.filters.filter(({ key, value} ) => key && value);
                const url = new URL ("http://127.0.0.1:8000/api/v1/timetable/");
                filledFilters.forEach(({ key, value }) => url.searchParams.append(key, value));
                await this.loadListTimetable(url);
            },
        }
    }
</script>

<style scoped>
</style>
