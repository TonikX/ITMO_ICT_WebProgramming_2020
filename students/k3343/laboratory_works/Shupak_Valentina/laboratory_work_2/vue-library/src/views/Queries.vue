<template>
    <mu-container>
  <mu-row align="center">
    <mu-col>
        <h1>Запросы к курсовой работе</h1>
        <ul>
            <li>Запрос №1</li>
            <p>Какие книги закреплены за определенным читателем?</p>
            <mu-form :model="form_query1" class="mu-demo-form" label-width="100">
                        <mu-form-item prop="select" label="Читатель">
                                <mu-select v-model="form_query1.reader">
                                    <mu-option v-for="reader in listReader" :key="reader.id"
                                               :label="reader.fio"
                                               :value="reader.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                        </mu-form>
            <mu-button color="black" @click="Query1">Выполнить запрос</mu-button>
            <p v-for="q in query1">{{q.books}}</p>
            <li>Запрос №2</li>
            <p>Кто из читателей взял книгу более месяца тому назад?</p>
            <table>
                <tr>
                    <th>Читатель</th>
                    <th>Дата взятия книги</th>
                </tr>
                <tr v-for="taking in listTaking" :key="taking.id">
                    <td>{{taking.reader}}</td>
                    <td>{{taking.date_take}}</td>
                </tr>
            </table>
            <li>Запрос №3</li>
            <p>Сколько читателей в процентном отношении имеют начальное образование, среднее, высшее, ученую степень?</p>
            <table>
                <tr>
                    <th>Образование</th>
                    <th>Процент читателей</th>
                </tr>
                <tr>
                    <td>Начальное</td>
                    <td>{{query5.primary}}</td>
                </tr>
                <tr>
                    <td>Среднее неоконченное</td>
                    <td>{{query5.secondary_unfinished}}</td>
                </tr>
                <tr>
                    <td>Среднее</td>
                    <td>{{query5.secondary}}</td>
                </tr>
                <tr>
                    <td>Высшее неоконченное</td>
                    <td>{{query5.high_unfinished}}</td>
                </tr>
                <tr>
                    <td>Высшее</td>
                    <td>{{query5.high}}</td>
                </tr>
            </table>
            <table>
                <tr>
                    <td>Есть ученая степень</td>
                    <td>{{query5.academic}}</td>
                </tr>
                <tr>
                    <td>Ученой степени нет</td>
                    <td>{{query5.non_academic}}</td>
                </tr>
            </table>
        </ul>
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
                query1: {
                    result:[]
                },
                query5: {},
                listReader: [],
                listTaking: [],
                form_query1: {
                    reader: '',
                },
            }
        },
        created() {
            this.Query5()
            this.loadListReader()
            this.loadListTakingBook()
        },
        methods: {
            async Query5() {
                this.query5 = await fetch(
                    `http://127.0.0.1:8000/api/v1/query5/`
                ).then(response => response.json())
            },
            async loadListReader() {
                this.listReader = await fetch(
                    `http://127.0.0.1:8000/api/v1/reader/`
                ).then(response => response.json())
            },
            async loadListTakingBook() {
                this.listTaking = await fetch(
                    `http://127.0.0.1:8000/api/v1/taking_book/`
                ).then(response => response.json())
            },
            Query1() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/query1/",
                    type: "GET",
                    data: {
                        reader: this.form_query1.reader,
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