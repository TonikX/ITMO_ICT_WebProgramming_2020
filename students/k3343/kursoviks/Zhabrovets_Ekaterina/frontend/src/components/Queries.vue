<template>
    <div>
        <mu-container>
            <mu-dialog title="Обработка актуальных заявок на участие в мастер-классах" width="800" max-width="90%"
                       :open.sync="openQueries">
                <mu-container>
                    <mu-data-table selectable select-all :selects.sync="selects" checkbox :columns="columns"
                                   :data="queries">
                    </mu-data-table>
                    <mu-flex align-items="center" style="padding: 8px;" wrap="wrap">
                        Выбранные заявки:
                        <mu-chip v-model="opt" delete v-for="selectIndex in selects" @delete="removeSelect(selectIndex)"
                                 style="margin: 8px;" color="primary" :key="selectIndex">
                            {{queries[selectIndex].id_query}}
                        </mu-chip>
                    </mu-flex>
                </mu-container>
                <mu-flex justify-content="center" align-items="center" wrap="wrap" class="icon-flex-wrap">
                    <mu-button color="primary" @click="final_approve">
                        ПОДТВЕРДИТЬ ВНЕСЕНИЕ ОПЛАТЫ
                        <mu-icon value="check_circle" right></mu-icon>
                    </mu-button>
                </mu-flex>
            </mu-dialog>
        </mu-container>
    </div>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "Queries",
        data() {
            return {
                openQueries: true,
                opt: '',
                queries: '',
                selects: [],
                columns: [{title: 'id Заявки', width: 90, name: 'id_query'},
                    {title: 'Имя клиента', width: 150, name: 'full_name'},
                    {title: 'Мастер-класс', width: 180, name: 'workshop_name'},
                    {title: 'Дата', width: 120, name: 'workshop_date'},
                    {title: 'Цена', width: 90, name: 'workshop_price'},
                    {title: 'Стиль', width: 120, name: 'workshop_style'},
                    {title: 'Место', width: 205, name: 'workshop_sсhool'},
                    {title: 'Хореографы', width: 200, name: 'workshop_choreographers'},

                ]
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadQueries()
        },
        methods: {
            loadQueries() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/quieries_to_approve2/",
                    type: "GET",
                    success: (response) => {
                        this.queries = response.data.data
                    }
                })
            },
            approveQuery(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/approve_query/",
                    type: "POST",
                    data: {
                        id_query: id,
                    },
                    success: (response) => {
                        alert("Заявки обработаны")
                    },
                    error: (response) => {
                        alert(this.selects[0])
                    }
                })
            },
            final_approve() {
                {
                    for (this.i = 0; this.i < this.selects.length; this.i++) {
                        var query = this.selects[this.i];
                        this.approveQuery(this.queries[query]['id_query'])
                    }
                }
            }

        }
    }
</script>

<style scoped>

</style>
