<template>
    <mu-container><h2>Classes</h2>
        <mu-container>
            <mu-paper>
                <mu-data-table border :columns="columns" :data="classes">
                    <template slot-scope="scope">
                        <td class="is-left">{{ scope.row.name }}</td>
                        <td class="is-left"><p v-if="scope.row.guiding_teacher">{{ scope.row.guiding_teacher }}</p><p v-else>None</p></td>
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
    name: 'Class',
    data() {
        return {
            classes: '',
            columns: [
                { title: 'Class', name: 'class', align: 'center', width: '491' },
                { title: 'Guiding teacher', name: 'teacher', align: 'center', width: '600' },
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
        this.loadClass()
    },
    methods: {
        returnHome() {
            window.location = '/'
        },
        loadClass() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/classes/",
                type: "GET",
                success: (response) => {
                    this.classes = response.data.data
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
