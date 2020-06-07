<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <mu-form :model="form" class="mu-demo-form"
                         :label-position="labelPosition" label-width="100">
                    <mu-form-item prop="select" label="Класс">
                        <mu-select v-model="form.klass">
                            <mu-option v-for="klass in listKlass" :key="klass.id"
                                       :label="klass.number+klass.litera"
                                       :value="klass.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
                <mu-button color="success" @click="Report"> Получить отчет по классу</mu-button>
            </mu-col>
        </mu-row>
        <mu-row v-if="isReportVis">
            <mu-col>
                <p>Количество человек в классе</p>
                <p>Классный руководитель</p>
            </mu-col>
            <mu-col>
                <p v-for="result in report">{{result}}</p>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "KlassReport",
        data() {
            return {
                isReportVis: false,
                listSubject: [],
                report: '',
                form: {
                    klass: '',
                }
            }
        },
        created() {
            this.loadListKlass()
        },
        methods: {
            async loadListKlass() {
                this.listKlass = await fetch(
                    `${this.$store.getters.getServerUrl}/klass`
                ).then(response => response.json())
            },
            Report() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/assessments_reports/",
                    type: "GET",
                    data: {
                        klass: this.form.klass,
                    },
                    success: (response) => {
                        this.report = response.data
                        this.isReportVis = !this.isReportVis
                        console.log(this.report)
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>