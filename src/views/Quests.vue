<template>
    <v-row>
        <v-col cols="12"
               sm="6"
               md="4"
               lg="3"
               xl="2"
               v-for="(quest, index) in quests"
               :key="index">
            <quest :quest="quest"/>
        </v-col>
    </v-row>
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
                    },
                    {
                        id: 0,
                        title: 'abacaba',
                        place: 'something',
                        start_time: '3:00',
                        duration: '12:00'
                    },
                    {
                        id: 0,
                        title: 'abacaba',
                        place: 'something',
                        start_time: '3:00',
                        duration: '12:00'
                    },
                    {
                        id: 0,
                        title: 'abacaba',
                        place: 'something',
                        start_time: '3:00',
                        duration: '12:00'
                    },
                    {
                        id: 0,
                        title: 'abacaba',
                        place: 'something',
                        start_time: '3:00',
                        duration: '12:00'
                    },
                    {
                        id: 0,
                        title: 'abacaba',
                        place: 'something',
                        start_time: '3:00',
                        duration: '12:00'
                    },
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
