<template>
    <mu-container>
        <mu-dialog title="Список участников" width="450" max-width="80%" :esc-press-close="false" :open.sync="open_part">
            <mu-list>
                <mu-list-item button :ripple="false" v-for="participant in participants">
                    <mu-list-item-action>
                        <mu-icon value="assignment_ind"></mu-icon>
                    </mu-list-item-action>
                    <mu-list-item-title>{{participant.full_name}}</mu-list-item-title>
                </mu-list-item>
            </mu-list>
        </mu-dialog>
    </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "ParticipantsForWSH",
        props: {
            id: ''
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadPart();
        },
        data() {
            return {
                participants: '',
                open_part: '',
            }
        },
        methods: {
            loadPart() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/participants/",
                    type: "GET",
                    data: {
                        wsh: this.id
                    },
                    success: (response) => {
                        this.participants = response.data.data
                    }
                })
            },
            // closeWriteFeedback() {
            //     this.$emit('closeWriteFeedback')
            // }
    }
    }
</script>

<style scoped>

</style>
