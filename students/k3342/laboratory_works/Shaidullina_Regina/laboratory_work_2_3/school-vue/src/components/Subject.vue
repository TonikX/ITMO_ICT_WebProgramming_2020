<template>
    <mu-container><h2>Subjects</h2>
        <mu-container>
            <mu-paper>
                <mu-data-table border :columns="columns" :data="subjects">
                    <template slot-scope="scope">
                        <td class="is-left">{{ scope.row.name }}</td>
                        <td class="is-left">{{ scope.row.sub_type }}</td>
                    </template>
                </mu-data-table>
            </mu-paper>
            <br><br>
        </mu-container>
    </mu-container>
</template>

<script>
/* eslint-disable */

export default {
    name: 'Subject',
    data() {
        return {
            subjects: '',
            columns: [
                { title: 'Subject', name: 'subject', align: 'center', width: '491' },
                { title: 'Type', name: 'type', align: 'center', width: '600' },
            ]
        }
    },
    computed: {
        auth() {
            if (sessionStorage.getItem("auth_token")) {
                return true
            }
        }
    },
    created() {
        $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.loadSubject()
    },
    methods: {
        returnHome() {
            window.location = '/'
        },
        loadSubject() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/subjects/",
                type: "GET",
                success: (response) => {
                    this.subjects = response.data.data
                }
            })
        }
    }
}
</script>

<style scoped>
    h2 {
        font-size: 48px; 
        font-weight: 400;
        text-align: center;
        color: #1a237e;
    }
</style>
