<template>
    <mu-container>
        <mu-dialog title="Мой отзыв" width="500" max-width="80%" :esc-press-close="false"
                   :overlay-close="false" :open.sync="openWriteFed">
            <mu-select label="Оценка" v-model="rating" full-width label-float>
                <mu-option v-for="rat in ratings" :key="rat" :label="rat" :value="rat"></mu-option>
            </mu-select>
            <mu-form>
                <mu-form-item prop="textarea" label="Текст отзыва">
                    <mu-text-field multi-line :rows="1" :rows-max="6" v-model="textarea"></mu-text-field>
                </mu-form-item>
            </mu-form>
            <mu-button flat color="primary" @click="addFeedback">Отправить отзыв</mu-button>
            <mu-button flat color="primary" @click="closeWriteFeedback">Отмена</mu-button>
        </mu-dialog>
    </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "Feedback",
        props: {
            id: ''
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
        },
        data() {
            return {
                openWriteFed: true,
                textarea: '',
                rating: '',
                ratings: ['Отлично', 'Хорошо', 'Плохо']

            }
        },
        methods: {
            addFeedback() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/write_feedback/",
                    type: "POST",
                    data: {
                        wsh: this.id,
                        text: this.textarea,
                        rating: this.rating
                    },
                    success: (response) => {
                        alert("Отзыв сохранен")
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            closeWriteFeedback() {
                this.$emit('closeWriteFeedback')
            }
    }
    }
</script>

<style scoped>

</style>
