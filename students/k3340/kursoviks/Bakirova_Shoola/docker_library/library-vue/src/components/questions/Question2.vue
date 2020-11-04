<template>
    <mu-row>
        <h3>Кто из читателей взял книгу более месяца тому назад?</h3>
        <mu-flex class="flex-list" direction="row" v-for="fix in fixes" v-bind:key="fixes.id">

                <mu-flex class="flex-readers" fill>
                    <h4>{{fix.reader.name}} (билет №{{fix.reader.library_card}}) -
                    "{{fix.book.name}}" {{fix.book.author}}
                    (шифр №{{fix.book.cipher}})
                    </h4>
                </mu-flex>
                <mu-flex class = "flex-date">
                    <h4>{{fix.date_fix}}</h4>
                </mu-flex>

        </mu-flex>
    </mu-row>
</template>

<script>
export default {
    name: "question1",
    data () {
        return {
            readers: [],
            fixes: []
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
                url: 'http://127.0.0.1:8000/api/v1/library/fix_filter/',
                type: 'GET',
                success: (response) => {
                    this.fixes = response.data.data
                }
            })

        },
    }
}
</script>

<style scoped>
    .flex-list {
        width: 100%;
        margin-top: 5px;
    }
    .flex-readers {
        width: 90%;
        text-align: left;
    }
    .flex-date {
        width: 10%;
        text-align: right;
    }
</style>
