<template>
    <mu-row>
        <h3>Сколько читателей в процентном отношении имеют начальное образование,
            среднее, высшее, ученую степень?</h3>
        <mu-flex class="flex-test">
            <h4>Начальное образование: {{education.primary}}%</h4>
        </mu-flex>
        <mu-flex class="flex-test">
            <h4>Cреднее образование: {{education.secondary}}%</h4>
        </mu-flex>
        <mu-flex class="flex-test">
            <h4>Высшее образование: {{education.high}}%</h4>
        </mu-flex>
        <mu-flex class="flex-test">
            <h4>Ученую степень: {{education.academic}}%</h4>
        </mu-flex>
    </mu-row>
</template>

<script>
export default {
    name: "question5",
    data () {
        return {
            education: [],
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
                url: 'http://127.0.0.1:8000/api/v1/library/education/',
                type: 'GET',
                success: (response) => {
                    this.education = response.data
                    console.log(this.education)
                }
            })

        },
    }
}
</script>

<style scoped>
.flex-test {
    width: 100%;
    height: 36px;
    margin-left: 20px;
}
</style>
