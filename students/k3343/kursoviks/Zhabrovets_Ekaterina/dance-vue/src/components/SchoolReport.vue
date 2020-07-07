<template>
    <div>
        <mu-container>
            <h3>Отчет о выручке по школам</h3>
            <mu-data-table :columns="cols"
                           :data="reports">
            </mu-data-table>
        </mu-container>
    </div>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "SchoolReport",
        data() {
            return {
                reports: '',
                cols: [{title: 'Название школы', width: 220, name: 'name'}, {
                    title: 'Количество прошедших мастер-классов',
                    width: 200,
                    name: 'number_prev',
                    align: 'center'
                }, {title: 'Выручка(руб.)', width: 250, name: 'gained_profit', align: 'center'}, {
                    title: 'Количество грядущих мастер-классов',
                    width: 200,
                    name: 'number_fut',
                    align: 'center'
                }, {title: 'Ожид. прибыль(руб.)', width: 250, name: 'fut_profit', align: 'center'}]
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadRep()
        },
        methods: {
            loadRep() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/report/",
                    type: "GET",
                    success: (response) => {
                        this.reports = response.data.data
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
