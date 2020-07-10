<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Запросы к курсовой работе</h1>
                <p>Секретарю приемной комиссии могут потребоваться следующие сведения:</p>
                <mu-container align="left">
                    <ul>
                        <li>Запрос №1</li>
                        <p>Список абитуриентов, подавших заявление на заданную специальность</p>
                        <mu-form :model="form_query1" class="mu-demo-form" label-width="100">
                        <mu-form-item prop="select" label="Специальность">
                                <mu-select v-model="form_query1.specialty">
                                    <mu-option v-for="specialty in query5" :key="specialty.id"
                                               :label="specialty.name"
                                               :value="specialty.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                        </mu-form>
                        <mu-button color="secondary" @click="Query1">Выполнить запрос</mu-button>
                        <p v-if="isQueryVis">Результат выполнения запроса</p>
                        <table v-if="isQueryVis">
                        <tr v-for="query_1 in query1">
                            <td>{{query_1.enrollee}}</td>
                        </tr>
                        </table>
                        <li>Запрос №2</li>
                        <p>Количество абитуриентов, подавших заявления на каждую специальность по каждой форме обучения
                            на бюджет (или контракт)</p>
                        <mu-container>
                            <mu-row>
                                <mu-col>
                                    <table>
                                        <tr>
                                            <th>Код специальности</th>
                                            <th>Основа обучения</th>
                                            <th>Количество абитуриентов</th>
                                        </tr>
                                        <tr v-for="query_2 in query2.result" :key="query_2.id">
                                            <td>{{query_2.specialty}}</td>
                                            <td>{{query_2.form}}</td>
                                            <td>{{query_2.enrollee__count}}</td>
                                        </tr>
                                    </table>
                                    <br>
                                </mu-col>
                                <mu-col>
                                    <table>
                                        <tr>
                                            <th>Код специальности</th>
                                            <th>Название специальности</th>
                                        </tr>
                                        <tr v-for="specialty in query5" :key="specialty.id">
                                            <td>{{specialty.id}}</td>
                                            <td>{{specialty.name}}</td>
                                        </tr>
                                    </table>
                                </mu-col>
                            </mu-row>
                        </mu-container>
                        <li>Запрос №3</li>
                        <p>Количество абитуриентов на базе 9 и 11 классов, поступающих на бюджет (или контракт).</p>
                        <table>
                            <tr>
                                <th>Основа обучения</th>
                                <th>Количество абитуриентов</th>
                            </tr>
                            <tr v-for="query_3 in query3.result">
                                <td>{{query_3.form}}</td>
                                <td>{{query_3.enrollee__count}}</td>
                            </tr>
                        </table>
                        <li>Запрос №4</li>
                        <p>Общее количество поданных заявлений ежедневно</p>
                        <table>
                            <tr>
                                <th>Дата</th>
                                <th>Количество заявлений</th>
                            </tr>
                            <tr v-for="query_4 in query4.result">
                                <td>{{query_4.date}}</td>
                                <td>{{query_4.enrollee__count}}</td>
                            </tr>
                        </table>
                        <li>Запрос №5</li>
                        <p>Конкурс на каждую специальность по каждой форме обучения на бюджет</p>
                        <table>
                            <tr>
                                <th>Специальность</th>
                                <th>Количество бюджетных мест</th>
                            </tr>
                            <tr v-for="query_5 in query5" :key="query_5.id">
                                <td>{{query_5.name}}</td>
                                <td>{{query_5.budget}}</td>
                            </tr>
                        </table>
                    </ul>
                </mu-container>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Queries",
        data() {
            return {
                query1: '',
                query2: {
                    result: []
                },
                query3: {
                    result: []
                },
                query4: {
                    result: []
                },
                query5: [],
                form_query1: {
                    specialty: '',
                },
                isQueryVis: false,
            }
        },
        created() {
            this.Query1()
            this.Query2()
            this.Query4()
            this.Query3()
            this.Query5()
        },
        methods: {
            async Query5() {
                this.query5 = await fetch(
                    `http://127.0.0.1:8000/api/v1/specialty/`
                ).then(response => response.json())
            },
            async Query4() {
                this.query4 = await fetch(
                    `http://127.0.0.1:8000/api/v1/query4/`
                ).then(response => response.json())
            },
            async Query3() {
                this.query3 = await fetch(
                    `http://127.0.0.1:8000/api/v1/query3/`
                ).then(response => response.json())
            },
            async Query2() {
                this.query2 = await fetch(
                    `http://127.0.0.1:8000/api/v1/query2/`
                ).then(response => response.json())
            },
            Query1() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/query1/",
                    type: "GET",
                    data: {
                        specialty: this.form_query1.specialty,
                    },
                    success: (response) => {
                        this.query1 = response.result
                        this.isQueryVis = true
                        console.log(this.query1)
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>