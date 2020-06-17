<template>
    <div class="mdl-grid">
        <div class="mdl-layout-spacer"></div>
        <div class="mdl-cell mdl-cell--5-col mdl-card mdl-shadow--6dp">
            <input id="input-file" type="file" style="display: none">
            <label id="input-file-holder" for="input-file" style="cursor:pointer">
                <span class="mdl-card__title" id="img-preview" style="color: #FFFFFF; height: 176px;"></span>
            </label>
            <div class="mdl-grid">
                <div class="mdl-cell mdl-cell--12-col">
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" style="width:100%;">
                        <input v-model="quest.title" class="mdl-textfield__input" type="text" id="name">
                        <label class="mdl-textfield__label" for="name">Название квеста</label>
                    </div>
                </div>
                <div class="mdl-cell mdl-cell--12-col">
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" style="width:100%;">
                        <input v-model="quest.place" class="mdl-textfield__input" type="text" id="place">
                        <label class="mdl-textfield__label" for="place">Место проведения</label>
                    </div>
                </div>
                <div class="mdl-cell mdl-cell--4-col">
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" style="width:100%;">
                        <input v-model="quest.date" type='date' class="mdl-textfield__input" id="date">
                        <label class="mdl-textfield__label" for="date">Дата проведения</label>
                    </div>
                </div>
                <div class="mdl-cell mdl-cell--4-col">
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" style="width:100%;">
                        <input v-model="quest.time" type='time' class="mdl-textfield__input" id="time">
                        <label class="mdl-textfield__label" for="time">Время проведения</label>
                    </div>
                </div>
                <div class="mdl-cell mdl-cell--4-col">
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" style="width:100%;">
                        <input v-model="quest.duration" type='time' class="mdl-textfield__input" id="duration">
                        <label class="mdl-textfield__label" for="duration">Продолжительность</label>
                    </div>
                </div>
                <div class="mdl-cell mdl-cell--12-col">
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" style="width:100%;">
                        <textarea v-model="quest.welcome_text" rows="3" class="mdl-textfield__input" id="start_text"></textarea>
                        <label class="mdl-textfield__label" for="start_text">Приветственный текст</label>
                    </div>
                </div>
                <div class="mdl-cell mdl-cell--12-col">
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" style="width:100%;">
                        <textarea v-model="quest.farewell_text" rows="3" class="mdl-textfield__input" id="final_text"></textarea>
                        <label class="mdl-textfield__label" for="final_text">Финальный текст</label>
                    </div>
                </div>
                <div v-for="(penalty, index) in quest.penalty_times" :key="index" class="mdl-cell mdl-cell--12-col">
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" style="width:100%;">
                        <input v-model="quest.penalty_times[index]" type='time' class="mdl-textfield__input" id="tip_1_time">
                        <label class="mdl-textfield__label" for="tip_1_time">Штраф за {{ index + 1 }}-ую подсказку</label>
                    </div>
                </div>
            </div>
            <div class="mdl-card__actions mdl-card--border" style="display: flex;">
                <button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--primary"
                        @click="save">
                    Сохранить
                </button>
                <div class="mdl-layout-spacer"></div>
                <button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
                        @click="remove">
                    Удалить
                </button>
            </div>
        </div>
        <div class="mdl-layout-spacer"></div>
    </div>

</template>

<script>
    export default {
        name: "QuestDetail",
        data() {
            return {
                quest: {
                    id: 0,
                    title: 'abacaba',
                    place: 'abacaba',
                    start_time: 'abacaba',
                    duration: 'abacaba',
                    welcome_text: 'welcome text',
                    farewell_text: 'farewell text',
                    penalty_times: [
                        10,
                        15
                    ]
                }
            }
        },
        methods: {
            remove() {
                console.log("remove")
            },
            save() {
                console.log("save")
            }
        }
    }
</script>
