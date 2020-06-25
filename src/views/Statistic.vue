<template>
    <v-row align="start" justify="center">
        <v-col cols="12" sm="12" md="11" lg="10" xl="9">
            <v-card>
                <v-toolbar color="primary" dark flat>
                    <v-toolbar-title>Статистика квеста</v-toolbar-title>
                </v-toolbar>
                <v-data-table :headers="headers"
                              :items="statistic"
                              :page.sync="page"
                              :items-per-page="itemsPerPage"
                              @page-count="pageCount = $event"
                              hide-default-footer
                              :loading="is_loading"
                              loading-text="Loading... Please wait">
                </v-data-table>
            </v-card>
            <div class="text-center pt-2">
                <v-pagination v-model="page"
                              :length="pageCount"
                              prev-icon="keyboard_arrow_left"
                              next-icon="keyboard_arrow_right"
                              color="accent"
                              circle/>
            </div>
        </v-col>
    </v-row>
</template>

<script>
    import {httpClient} from "../api/httpClient";

    export default {
        name: "Statistic",
        data() {
            return {
                is_loading: false,
                page: 1,
                pageCount: 0,
                itemsPerPage: 15,
                headers: [
                    {
                        text: 'Команда',
                        sortable: false,
                        value: 'team',
                    }
                ],
                quest: {},
                statistic: [],
                rules: [
                    v => !!v || 'Это поле обязательно',
                    v => (v && v.length >= 8) || 'Пароль должен быть не менее 8 символов',
                ]
            }
        },
        methods: {
            loadTasks() {
                this.is_loading = false;
                const questId = this.$route.params.id;
                httpClient.get(`/quests/${questId}/`)
                    .then((response) => {
                        const start_time = new Date(response.data.start_time);
                        response.data.start_time = start_time.toISOString().substr(11, 5);
                        response.data.date = start_time.toISOString().substr(0, 10);
                        response.data.penalty_1 = response.data.penalty_1.substr(0, 5);
                        response.data.penalty_2 = response.data.penalty_2.substr(0, 5);
                        response.data.duration = response.data.duration.substr(0, 5);
                        this.quest = response.data;
                        this.quest.tasks.forEach((task, ind) => {
                            console.log(task);
                            this.headers.push({
                                text: `${ind + 1}. ${task.title}`,
                                sortable: false,
                                value: `task_${task.id}`,
                                align: 'center'
                            })
                        });
                        this.loadStatistic()
                    })
                    .catch((error) => {
                        this.is_loading = false;
                        console.log("Catch error when get quest: " + JSON.stringify(error))
                    })
            },
            loadStatistic() {
                this.is_loading = true;
                const questId = this.$route.params.id;
                httpClient.get(`/quests/${questId}/statistic`)
                    .then((response) => {
                        response.data['teams_statistic'].forEach((team_statistic) => {
                            let statistic = {};
                            statistic.team = team_statistic.team.username;
                            team_statistic['tasks_statistic'].forEach((task_statistic) => {
                                const tip_1_str = this.tip_str(task_statistic['tip_1_used']);
                                const tip_2_str = this.tip_str(task_statistic['tip_2_used']);
                                const lead_time_str = this.lead_time_str(task_statistic['lead_time']);
                                statistic[`task_${task_statistic.task}`] = `${lead_time_str}, ${tip_1_str} | ${tip_2_str}`
                            });
                            this.statistic.push(statistic)
                        });
                        this.is_loading = false;
                    })
                    .catch((error) => {
                        this.is_loading = false;
                        console.log("load teams error" + JSON.stringify(error))
                    })
            },
            lead_time_str(lead_time) {
                if (lead_time === null) {
                    return "Не закончен"
                }
                return lead_time.substr(0, 5);
            },
            tip_str(is_used) {
                if (is_used) {
                    return "+"
                }
                return "-"
            }
        },
        mounted() {
            this.loadTasks()
        }
    }
</script>
