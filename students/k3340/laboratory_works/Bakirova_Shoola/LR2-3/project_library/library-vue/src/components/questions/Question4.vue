<template>
    <mu-row>
        <h2>Сколько в библиотеке читателей младше 20 лет?</h2>
        <mu-flex class="flex-title">
            <h3>Всего {{this.amount}}: </h3>
        </mu-flex>
        <mu-flex class="flex-list" v-for="reader in readers" v-bind:key="reader.id">
            <h4>{{reader.name}} (билет №{{reader.library_card}}) - дата рождения {{reader.date_of_birth}}</h4>
        </mu-flex>
    </mu-row>
</template>

<script>
export default {
    name: "question4",
    data () {
        return {
            readers: [],
            amount: ''
        }
    },
    created () {
        $.ajaxSetup({
            headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
        })
        this.loadReaders()
    },
    methods: {
        loadReaders() {
            $.ajax({
                url: 'http://127.0.0.1:8000/api/v1/library/readers_filter/',
                type: 'GET',
                success: (response) => {
                    this.readers = response.data.data
                    this.amount = this.readers.length
                }
            })

        },
    }
}
</script>

<style scoped>
.flex-list {
    width: 100%;
    margin-left: 30px;
    height: 36px;
}
.flex-title {
    width: 100%;
    height: 36px;
}
</style>
