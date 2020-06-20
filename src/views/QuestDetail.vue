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
                                <v-menu v-for="(penalty_time, index) in quest.penalty_times"
                                        :key="index"
                                        ref="penalty_time_menu"
                                        v-model="penalty_time_menu[index]"
                                        :close-on-content-click="false"
                                        :nudge-right="40"
                                        :return-value.sync="quest.penalty_times[index]"
                                        transition="scale-transition"
                                        offset-y
                                        max-width="290px"
                                        min-width="290px">
                                    <template v-slot:activator="{ on, attrs }">
                                        <v-text-field v-model="quest.penalty_times[index]"
                                                      :label="'Штрафное время за подсказку №' + (index + 1)"
                                                      prepend-icon="timer"
                                                      readonly
                                                      v-bind="attrs"
                                                      v-on="on"
                                                      required
                                                      :rules="rules"/>
                                    </template>
                                    <v-time-picker v-if="penalty_time_menu[index]"
                                                   v-model="quest.penalty_times[index]"
                                                   full-width
                                                   format="24hr"
                                                   @click:minute="$refs.penalty_time_menu[index].save(quest.penalty_times[index])">
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
                                            <v-icon color="primary">mdi-check</v-icon>
                                        </template>
                                    </v-expansion-panel-header>
                                    <v-expansion-panel-content>
                                        <v-text-field v-model="task.title"
                                                      label="Название"
                                                      prepend-icon="title"
                                                      required
                                                      hint="Используется только в админ панеле"
                                                      :rules="rules"/>
                                        <v-text-field v-model="task.question"
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
                                        <v-text-field v-for="(tip, index) in task.tips"
                                                      :key="index"
                                                      v-model="task.tips[index]"
                                                      :label="'Подсказка №' + (index + 1)"
                                                      prepend-icon="emoji_objects"
                                                      hint="Если поле пустое, то участник не увидит подсказку"/>
                                    </v-expansion-panel-content>
                                    <v-divider v-if="index + 1 < quest.tasks.length"/>
                                </v-expansion-panel>
                            </v-expansion-panels>
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
    export default {
        name: "QuestDetail",
        data: () => ({
            valid: false,
            date_menu: false,
            start_time_menu: false,
            duration_menu: false,
            penalty_time_menu: [false, false],
            quest: {
                id: 0,
                title: '',
                place: 'abacaba',
                date: new Date().toISOString().substr(0, 10),
                start_time: null,
                duration: null,
                welcome_text: 'welcome text',
                farewell_text: 'farewell text',
                penalty_times: [
                    '00:10',
                    '00:15'
                ],
                tasks: [
                    {
                        title: "title",
                        question: "It's question",
                        answers: ["ab", "abac", "qwerty"],
                        tips: ["tip1", "tip2"]
                    },
                    {
                        title: "title",
                        question: "It's question",
                        answers: ["ab", "abac", "qwerty"],
                        tips: ["tip1", "tip2"]
                    }
                ]
            },
            rules: [
                v => !!v || 'Это поле обязательно'
            ]
        }),
        methods: {
            remove() {
                console.log('remove ' + JSON.stringify(this.quest))
            },
            save() {
                console.log('save ' + JSON.stringify(this.quest))
            }
        }
    }
</script>
