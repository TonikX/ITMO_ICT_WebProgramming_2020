<template>
    <div>
        <mu-container>
            <mu-dialog title="Добавить участника" width="360" scrollable :open.sync="openScroll">
                <mu-list>
                    <mu-list-item :key="n.id" v-for="n in non_part">
                        <mu-list-item-content>
                            <mu-radio :label="n.fullname" :value="n.id" v-model="option"></mu-radio>
                        </mu-list-item-content>
                    </mu-list-item>
                    <mu-button @click="addPart">Add</mu-button>
                </mu-list>
            </mu-dialog>
        </mu-container>
    </div>

</template>

<script>
    import $ from 'jquery'

    export default {
        name: 'NonPart',
        props: {
            id: '',
        },
        data() {
            return {
                non_part: '',
                openScroll: true,
                option: '',
            }
        },
        created() {
            this.loadNon()
        },
        methods: {
            loadNon() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/not_incl/",
                    type: "GET",
                    data: {
                        workshop: this.id,
                    },
                    success: (response) => {
                        this.non_part = response.data.data
                    }
                })
            },

            addPart() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/add_part/",
                    type: "POST",
                    data: {
                        wsh: this.id,
                        partic: this.option,
                    },
                    success: (response) => {
                        alert("Пользователь добавлен")
                        window.location = '/'

                    },
                    error: (response) => {
                        alert("Ошибка при добавлении пользователя")
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
