<template>
    <mu-container>
        <mu-row>
            <mu-col>
                Результаты ЕГЭ
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-form style="width: 50%" :model="form" class="mu-demo-form" :label-position="labelPosition"
                         label-width="200">
                    <mu-form-item prop="select" label="Абитуриент">
                        <mu-select v-model="form.ege">
                            <mu-option v-for="ege in listEge" :key="ege.id" :label="ege.enrollee"
                                       :value="ege.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Предмет">
                        <mu-text-field v-model="form.subject"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Балл">
                        <mu-text-field v-model="form.mark"></mu-text-field>
                    </mu-form-item>
                </mu-form>
                <mu-button @click="CreateEgeResult">Добавить</mu-button>
                <br>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button href="#/docs">Вернуться к документам</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from "jquery";
    export default {
        name: "EgeResults",
        props: ['id'],
        components: {},
        data() {
            return {
                listEge: [],
                form: {
                    subject: '',
                    mark: '',
                    ege: ''
                }
            }
        },
        created() {
            this.loadListEge()
        },
        methods: {
            async loadListEge() {
                this.listEge = await fetch(
                    `http://127.0.0.1:8000/api/v1/ege/`
                ).then(response => response.json())
            },
            CreateEgeResult() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/egesubject/create",
                    type: "POST",
                    data: {
                        ege: this.form.ege,
                        subject: this.form.subject,
                        mark: this.form.mark,
                    },
                    success: (response) => {
                        this.$router.push({name: "Результаты"})
                        alert("Результат внесен")
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Данные введены неверно")
                        }
                    }

                })
            },
        }
    }
</script>

<style scoped>

</style>