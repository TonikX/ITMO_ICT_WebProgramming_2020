<template>
    <div>
        <mu-container>
            <mu-dialog title="Подтверждение записи на мастер-класс" width="400" :open.sync="openAlert">
                Вы уверены, что хотите записаться на данный мастер-класс?<br/>
                <mu-button style="margin-top: 10px" @click="queryPart">Да</mu-button>
                <mu-button @click="closeaddPart">Отмена</mu-button>
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
                openAlert: true,
                option: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
        },
        methods: {
            queryPart() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/query_for_part/",
                    type: "POST",
                    data: {
                        wsh: this.id,
                    },
                    success: (response) => {
                        alert("Ваш запрос отправлен на рассмотрение. Вас внесут в список участников после подтверждения оплаты администратором")
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            closeaddPart() {
                this.$emit('closeaddPart')
            }
        }
    }
</script>

<style scoped>

</style>
