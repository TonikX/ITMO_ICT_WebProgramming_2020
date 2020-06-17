<template>
    <div class="mdl-cell mdl-cell--4-col mdl-card mdl-shadow--6dp" :id="quest.index">
        <div class="mdl-card__title" style="color: #FFFFFF; height: 176px; padding: 0px;">
            <a class="mdl-card__title-text blur-label">{{ quest.title }}</a>
        </div>
        <div class="mdl-card__supporting-text">
            <b>Количество КП:</b> {{ quest.title }}
            <br>
            <b>Место проведения:</b> {{ quest.place }}
            <br>
            <b>Время старта:</b> {{ quest.start_time }}
            <br>
            <b>Продолжительность:</b> {{ quest.duration }}
        </div>
        <div class="mdl-card__actions mdl-card--border" style="display: flex;">
            <form method="GET" :action="'statistic/' + quest.index">
                <button class="remove_button mdl-button mdl-button--raised mdl-button--primary mdl-js-button mdl-js-ripple-effect">Статистика</button>
            </form>
            <div class="mdl-layout-spacer"></div>
            <button
                @click="edit(quest.id)"
                class="remove_button mdl-button mdl-button--raised mdl-button--accent mdl-js-button mdl-js-ripple-effect">
                Редактрировать
            </button>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Quest',
        props: ['quest'],
        methods: {
            edit(id) {
                this.$router.push({ path: `quests/${id}` })
            }
        }
    }
</script>
