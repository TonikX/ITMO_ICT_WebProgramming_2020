<template>
    <v-card class="elevation-8">
        <v-img src="http://scipy-lectures.org/_images/face.png"
               class="white--text align-end"
               gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0.5)"
               :aspect-ratio="16/9">
            <v-card-title v-text="quest.title"/>
        </v-img>
        <v-card-text>
            <v-list>
                <v-list-item>
                    <v-list-item-icon>
                        <v-icon>map</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>{{ quest.place }}</v-list-item-title>
                        <v-list-item-subtitle>Место проведения</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item>
                    <v-list-item-icon>
                        <v-icon>not_listed_location</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>{{ quest.place }}</v-list-item-title>
                        <v-list-item-subtitle>Количество КП</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item>
                    <v-list-item-icon>
                        <v-icon>event</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>{{ dateStart }}</v-list-item-title>
                        <v-list-item-subtitle>Дата проведения</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item>
                    <v-list-item-icon>
                        <v-icon>timelapse</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>{{ duration }}</v-list-item-title>
                        <v-list-item-subtitle>Продолжительность</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-card-text>
        <v-divider/>
        <v-card-actions md-alignment="space-between">
            <v-btn color="primary" @click="navigateToStatistic(quest.id)">Статистика</v-btn>
            <v-spacer/>
            <v-btn color="accent" @click="edit(quest.id)">Редактировать</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        name: 'Quest',
        props: ['quest'],
        methods: {
            edit(id) {
                this.$router.push({name: 'editQuest', params: {id: id}})
            },
            navigateToStatistic(id) {
                this.$router.push({name: 'statistic', params: {id: id}})
            }
        },
        computed: {
            dateStart: function () {
                console.log(`start time ${this.quest.start_time}`);
                const start_time = new Date(this.quest.start_time).toISOString();
                return start_time.substr(0, 10) + ", " + start_time.substr(11, 5)
            },
            duration: function () {
                return new Date('1970-01-01T' + this.quest.duration + 'Z').toISOString().substr(11, 5)
            }
        }
    }
</script>
