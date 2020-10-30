<template>
        <mu-container>
        <mu-row>
            <mu-col>
                <h1>Отчет по авиакомпаниям</h1>
            </mu-col>
        </mu-row>
            <mu-row>
                <mu-col>
                    <p>
                        Необходимо предусмотреть возможность получения отчета о бортах компании-владельца по маркам с характеристикой марки. Указать общее количество бортов и количество бортов по каждой марке.
                    </p>
                </mu-col>
            </mu-row>
            <mu-row>
                <mu-col>
                    <mu-form :model="form" class="mu-demo-form" label-width="100">
                    <mu-form-item prop="select" label="Авиакомпания">
                        <mu-select v-model="form.aircarrier">
                            <mu-option v-for="aircarrier in listAirCarrier" :key="aircarrier.id"
                                       :label="aircarrier.name"
                                       :value="aircarrier.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
                <mu-button color="primary" @click="Report"> Получить отчет </mu-button>
                </mu-col>
            </mu-row>
            <mu-row v-if="isReportVis">
            <mu-col>
                <table class="paleBlueRows" width="70%">
                <tr>
                    <td>Самолеты авиакомпании</td>
                    <td>Общее количество бортов</td>
                    <td>Количество бортов по каждой марке</td>
                </tr>
                    <tr>
                        <td>
                            <ul v-for="planes in report.planes">
                                <li>{{planes.number}} - {{planes.type}}
                                </li>
                            </ul>
                        </td>
                        <td>{{report.all_planes}}</td>
                        <td>
                            <ul v-for="planes_type in report.planes_by_type">
                                <li>{{planes_type.type}} - {{planes_type.type__count}}</li>
                            </ul>
                            </td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from "jquery";
    export default {
        name: "Report",
        data() {
            return {
                isReportVis: false,
                listAirCarrier: [],
                report: {
                    result:{
                    }
                },
                form: {
                    aircarrier: '',
                }
            }
        },
        created() {
            this.loadListAirCarrier()
        },
        methods: {
            async loadListAirCarrier() {
                this.listAirCarrier = await fetch(
                    `http://127.0.0.1:8000/api/v1/aircarrier`
                ).then(response => response.json())
            },
            Report() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/aircarrier_reports/",
                    type: "GET",
                    data: {
                        aircarrier: this.form.aircarrier,
                    },
                    success: (response) => {
                        this.report = response.result
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