<template>
    <div class="content-grid mdl-grid">
        <Quest v-for="(quest, index) in quests" :key="index" :quest="quest"/>
    </div>
</template>

<script>
    import Quest from "../components/Quest";

    export default {
        name: "quests",
        data() {
            return {
                quests: [
                    {
                        id: 0,
                        title: 'abacaba',
                        place: 'something',
                        start_time: '3:00',
                        duration: '12:00'
                    }
                ]
            }
        },
        components: {
            Quest
        }
    }
</script>
