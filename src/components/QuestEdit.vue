<template>
    <v-form v-model="valid">
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
                <v-btn text color="primary" @click="$refs.date_menu.save(quest.date)">OK</v-btn>
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
                              prepend-icon="access_time"
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
                    rows="2"
                    hint="Будет показан участникам во время ожидания старта"
                    required
                    :rules="rules"/>
        <v-textarea label="Прощальный текст"
                    v-model="quest.farewell_text"
                    rows="2"
                    hint="Будет показан участникам по окончанию квеста"
                    required
                    :rules="rules"/>
    </v-form>
</template>

<script>
    export default {
        name: "QuestEdit",
        data: () => ({
            valid: false,
            date_menu: false,
            start_time_menu: false,
            duration_menu: false,
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
                    10,
                    15
                ]
            },
            rules: [
                v => !!v || 'Это поле обязательно'
            ]
        }),
    }
</script>

<style scoped>

</style>