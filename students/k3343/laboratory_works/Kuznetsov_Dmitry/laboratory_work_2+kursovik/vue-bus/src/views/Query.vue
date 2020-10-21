<template>
    <mu-container>
        <mu-row align="center">
            <mu-col>
                <h1>Запросы к курсовой работе</h1>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col>
                <h2>Запрос №1</h2>
                <h4>
                    Список водителей, работающих на определенном маршруте с указанием
                    графика их работы?
                </h4>
                <p>
                    Для выполнения этого запроса достаточно перейти на страницу <a href="#/schedule">График работы водителей</a> и указать в фильтре необходимый маршрут.
                </p>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col>
                <h2>Запрос №2</h2>
                <h4>
                    Когда начинается и заканчивается движение автобусов на каждом
                    маршруте?
                </h4>
                <p>
                    Для выполнения этого запроса достаточно перейти на страницу <a href="#/route">Маршруты</a>.
                </p>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col>
                <h2>Запрос №3</h2>
                <h4>
                    Какова общая протяженность маршрутов, обслуживаемых автопарком?
                </h4>
                <table>
                    <tr>
                        <td>Общая протяженность маршрутов в километрах</td>
                        <td>Общая протяженность маршрутов в минутах</td>
                    </tr>
                    <tr>
                        <td v-for="result in query3.result">
                            {{result.total_length}}
                        </td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col>
                <h2>Запрос №4</h2>
                <h4>
                    Какие автобусы не вышли на линию в заданный день и по какой причине
                    (неисправность, отсутствие водителя)?
                </h4>
                <p>
                    Для выполнения этого запроса достаточно перейти на страницу <a href="#/">Журнал автобусного парка</a> и указать в фильтре статус - "Не вышли на линию" и необходимую дату.
                </p>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col>
                <h2>Запрос №5</h2>
                <p>
                    Сколько водителей каждого класса работает в автопарке?
                </p>
                <table>
                    <tr>
                        <td>Водительский класс</td>
                        <td>Количество водителей</td>
                    </tr>
                    <tr v-for="result in query5.result">
                        <td>{{result.driver_class}}</td>
                        <td>{{result.fio__count}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Query",
        components: {},
        data() {
            return {
                query3: {
                    result: []
                },
                query5: {
                    result: []
                },
            }
        },
        created() {
            this.Query3()
            this.Query5()
        },
        methods: {
            async Query3() {
                this.query3 = await fetch(
                    `http://127.0.0.1:8000/api/v1/query3/`
                ).then(response => response.json())
            },
            async Query5() {
                this.query5 = await fetch(
                    `http://127.0.0.1:8000/api/v1/query5/`
                ).then(response => response.json())
            },
        }
    }
</script>

<style scoped>

</style>