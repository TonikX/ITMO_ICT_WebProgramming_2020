<template>
    <v-row align="start" justify="center">
        <v-col cols="12" sm="8" md="6" lg="5" xl="4">
            <v-card class="elevation-12">
                <v-img src="http://scipy-lectures.org/_images/face.png" :aspect-ratio="16/9"/>
                <v-form v-model="valid">

                    <v-tabs fixed-tabs>
                        <v-tab>Описание</v-tab>
                        <v-tab>Задания</v-tab>
                        <v-tab-item>
                            <v-card-text>
                                <v-text-field v-model="quest.title"
                                              label="Название"
                                              prepend-icon="title"
                                              required
                                              :rules="rules"/>
                                <v-text-field v-model="quest.place"
                                              label="Место проведения"
                                              prepend-icon="map"
                                              required
                                              :rules="rules"/>
                                <v-menu ref="date_menu"
                                        v-model="date_menu"
                                        :close-on-content-click="false"
                                        :return-value.sync="quest.date"
                                        transition="scale-transition"
                                        offset-y
                                        min-width="290px">
                                    <template v-slot:activator="{ on, attrs }">
                                        <v-text-field v-model="quest.date"
                                                      label="Время старта"
                                                      prepend-icon="event"
                                                      readonly
                                                      v-bind="attrs"
                                                      v-on="on"
                                                      required
                                                      :rules="rules"/>
                                    </template>
                                    <v-date-picker v-model="quest.date" no-title scrollable>
                                        <v-spacer></v-spacer>
                                        <v-btn text color="primary" @click="date_menu = false">Cancel</v-btn>
                                        <v-btn text color="primary" @click="$refs.date_menu.save(quest.date)">OK
                                        </v-btn>
                                    </v-date-picker>
                                </v-menu>
                                <v-menu ref="start_time_menu"
                                        v-model="start_time_menu"
                                        :close-on-content-click="false"
                                        :nudge-right="40"
                                        :return-value.sync="quest.start_time"
                                        transition="scale-transition"
                                        offset-y
                                        max-width="290px"
                                        min-width="290px">
                                    <template v-slot:activator="{ on, attrs }">
                                        <v-text-field v-model="quest.start_time"
                                                      label="Время начала"
                                                      prepend-icon="access_time"
                                                      readonly
                                                      v-bind="attrs"
                                                      v-on="on"
                                                      required
                                                      :rules="rules"/>
                                    </template>
                                    <v-time-picker v-if="start_time_menu"
                                                   v-model="quest.start_time"
                                                   full-width
                                                   format="24hr"
                                                   @click:minute="$refs.start_time_menu.save(quest.start_time)">
                                    </v-time-picker>
                                </v-menu>
                                <v-menu ref="duration_menu"
                                        v-model="duration_menu"
                                        :close-on-content-click="false"
                                        :nudge-right="40"
                                        :return-value.sync="quest.duration"
                                        transition="scale-transition"
                                        offset-y
                                        max-width="290px"
                                        min-width="290px">
                                    <template v-slot:activator="{ on, attrs }">
                                        <v-text-field v-model="quest.duration"
                                                      label="Предолжительность"
                                                      prepend-icon="timelapse"
                                                      readonly
                                                      v-bind="attrs"
                                                      v-on="on"
                                                      required
                                                      :rules="rules"/>
                                    </template>
                                    <v-time-picker v-if="duration_menu"
                                                   v-model="quest.duration"
                                                   full-width
                                                   format="24hr"
                                                   @click:minute="$refs.duration_menu.save(quest.duration)">
                                    </v-time-picker>
                                </v-menu>
                                <v-textarea label="Приветственный текст"
                                            v-model="quest.welcome_text"
                                            prepend-icon="emoji_people"
                                            rows="2"
                                            hint="Будет показан участникам во время ожидания старта"
                                            required
                                            :rules="rules"/>
                                <v-textarea label="Прощальный текст"
                                            v-model="quest.farewell_text"
                                            prepend-icon="emoji_people"
                                            rows="2"
                                            hint="Будет показан участникам по окончанию квеста"
                                            required
                                            :rules="rules"/>
                                <v-menu ref="penalty_time_menu_1"
                                        v-model="penalty_time_menu_1"
                                        :close-on-content-click="false"
                                        :nudge-right="40"
                                        :return-value.sync="quest.penalty_1"
                                        transition="scale-transition"
                                        offset-y
                                        max-width="290px"
                                        min-width="290px">
                                    <template v-slot:activator="{ on, attrs }">
                                        <v-text-field v-model="quest.penalty_1"
                                                      label="Штрафное время за подсказку №1"
                                                      prepend-icon="timer"
                                                      readonly
                                                      v-bind="attrs"
                                                      v-on="on"
                                                      required
                                                      :rules="rules"/>
                                    </template>
                                    <v-time-picker v-if="penalty_time_menu_1"
                                                   v-model="quest.penalty_1"
                                                   full-width
                                                   format="24hr"
                                                   @click:minute="$refs.penalty_time_menu_1.save(quest.penalty_1)">
                                    </v-time-picker>
                                </v-menu>
                                <v-menu ref="penalty_time_menu_2"
                                        v-model="penalty_time_menu_2"
                                        :close-on-content-click="false"
                                        :nudge-right="40"
                                        :return-value.sync="quest.penalty_2"
                                        transition="scale-transition"
                                        offset-y
                                        max-width="290px"
                                        min-width="290px">
                                    <template v-slot:activator="{ on, attrs }">
                                        <v-text-field v-model="quest.penalty_2"
                                                      label="Штрафное время за подсказку №1"
                                                      prepend-icon="timer"
                                                      readonly
                                                      v-bind="attrs"
                                                      v-on="on"
                                                      required
                                                      :rules="rules"/>
                                    </template>
                                    <v-time-picker v-if="penalty_time_menu_2"
                                                   v-model="quest.penalty_2"
                                                   full-width
                                                   format="24hr"
                                                   @click:minute="$refs.penalty_time_menu_2.save(quest.penalty_2)">
                                    </v-time-picker>
                                </v-menu>
                            </v-card-text>
                        </v-tab-item>
                        <v-tab-item>
                            <v-expansion-panels accordion flat>
                                <v-expansion-panel v-for="(task, index) in quest.tasks" :key="index">
                                    <v-expansion-panel-header>
                                        {{ index + 1 }}. {{ task.title }}
                                        <template v-slot:actions>
                                            <v-icon>keyboard_arrow_down</v-icon>
                                        </template>
                                    </v-expansion-panel-header>
                                    <v-expansion-panel-content>
                                        <v-text-field v-model="task.title"
                                                      label="Название"
                                                      prepend-icon="title"
                                                      required
                                                      hint="Используется только в админ панеле"
                                                      :rules="rules"/>
                                        <v-text-field v-model="task.content"
                                                      label="Вопрос"
                                                      prepend-icon="live_help"
                                                      required
                                                      :rules="rules"/>
                                        <v-combobox v-model="task.answers"
                                                    label="Ответы"
                                                    multiple
                                                    prepend-icon="spellcheck"
                                                    hide-selected
                                                    hint="Здесь необходимо перечислить все возможные варианты ответов"
                                                    chips/>
                                        <v-text-field v-model="task.tip_1"
                                                      label="Подсказка №1"
                                                      prepend-icon="emoji_objects"
                                                      hint="Если поле пустое, то участник не увидит подсказку"/>
                                        <v-text-field v-model="task.tip_2"
                                                      label="Подсказка №2"
                                                      prepend-icon="emoji_objects"
                                                      hint="Если поле пустое, то участник не увидит подсказку"/>
                                        <v-row class="justify-center">
                                            <v-btn text small color="error" @click="removeTask(index)">
                                                <v-icon small>delete_forever</v-icon>
                                                Удалить задание
                                            </v-btn>
                                        </v-row>
                                    </v-expansion-panel-content>
                                    <v-divider/>
                                </v-expansion-panel>
                            </v-expansion-panels>
                            <v-container>
                                <v-row class="justify-center">
                                    <v-btn rounded class="accent" @click="createNewTask()">
                                        <v-icon left>add</v-icon>
                                        Добавить
                                    </v-btn>
                                </v-row>
                            </v-container>
                        </v-tab-item>
                    </v-tabs>
                </v-form>

                <v-divider/>
                <v-card-actions>
                    <v-btn color="error" @click="remove()">
                        Удалить
                    </v-btn>
                    <v-spacer/>
                    <v-btn color="accent" @click="save()" :disabled="!valid">
                        Сохранить
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-col>
    </v-row>
</template>

<script>
    import {httpClient} from "../api/httpClient";

    export default {
        name: "QuestDetail",
        data: () => ({
            valid: false,
            date_menu: false,
            start_time_menu: false,
            duration_menu: false,
            penalty_time_menu_1: false,
            penalty_time_menu_2: false,
            quest: {
                title: '',
                place: '',
                date: new Date().toISOString().substr(0, 10),
                start_time: null,
                duration: null,
                welcome_text: '',
                farewell_text: '',
                penalty_1: '00:05',
                penalty_2: '00:15',
                tasks: []
            },
            rules: [
                v => !!v || 'Это поле обязательно'
            ]
        }),
        methods: {
            remove() {
                httpClient.delete('/quests/' + this.$route.params.id)
                    .then(() => {
                        this.$router.push({name: 'quests'})
                    });
            },
            save() {
                const questForSave = Object.assign({}, this.quest);
                const start_time = `${this.quest.date}T${this.quest.start_time}:00Z`;
                delete questForSave.date;
                questForSave.start_time = start_time;
                if (this.$route.params.id !== undefined) {
                    const questId = this.$route.params.id;
                    httpClient.put(`/quests/${questId}/`, questForSave)
                        .then((response) => {
                            console.log(`save quest by Id: response ${response}`)
                        })
                        .catch((error) => {
                            console.log(`save quest by Id: error ${error}`)
                        })
                } else {
                    httpClient.post(`/quests/`, questForSave)
                        .then((response) => {
                            console.log(`save quest: response ${response}`);
                            this.$router.push({name: 'editQuest', params: {id: response.data.id}})
                        })
                        .catch((error) => {
                            console.log(`save quest: error ${error}`)
                        })
                }
                console.log('save ' + JSON.stringify(questForSave))
            },
            createNewTask() {
                this.quest.tasks.push({
                    title: "Новое задание",
                    content: "",
                    answers: [],
                    tip_1: "",
                    tip_2: ""
                })
            },
            removeTask(index) {
                this.quest.tasks.splice(index, 1);
            },
        },
        mounted() {
            if (this.$route.params.id !== undefined) {
                const questId = this.$route.params.id;
                console.log("request quest " + questId);
                httpClient.get(`/quests/${questId}/`)
                    .then((response) => {
                        const start_time = new Date(response.data.start_time);
                        response.data.start_time = start_time.toISOString().substr(11, 5);
                        response.data.date = start_time.toISOString().substr(0, 10);
                        response.data.penalty_1 = response.data.penalty_1.substr(0, 5);
                        response.data.penalty_2 = response.data.penalty_2.substr(0, 5);
                        response.data.duration = response.data.duration.substr(0, 5);
                        this.quest = response.data
                    })
                    .catch((error) => {
                        console.log("Catch error when get quest: " + JSON.stringify(error))
                    })
            }
        }
    }
</script>
