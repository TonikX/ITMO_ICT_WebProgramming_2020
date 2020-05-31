<template>
    <mu-container><br>
        <mu-container class="button-wrapper2">
            <mu-button v-if="auth" color="#5c6bc0" textColor="white" @click="upd">Update</mu-button>
            <mu-button v-if="auth" color="#5c6bc0" textColor="white" @click="add">Add</mu-button>
            <mu-button v-if="auth" color="#5c6bc0" textColor="white" @click="del">Delete</mu-button><br><br>
        </mu-container>
        <mu-container>
            <mu-paper>
                <mu-data-table border :columns="columns" :data="pupils">
                    <template slot-scope="scope">
                        <td class="is-left">{{ scope.row.name }}</td>
                        <td class="is-left">{{ scope.row.gender }}</td>
                        <td class="is-left"><p v-if="scope.row.study_class">{{ scope.row.study_class }}</p><p v-else>None</p></td>
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
    name: 'Pupil',
    data() {
        return {
            pupils: '',
            columns: [
                { title: 'Name', name: 'name', align: 'center', width: '401' },
                { title: 'Gender', name: 'gender', align: 'center', width: '350' },
                { title: 'Class', name: 'class', align: 'center', width: '340' },
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
        this.loadPupil()
    },
    methods: {
        returnHome() {
            window.location = '/'
        },
        add() {
            this.$router.push({name: "pupils_add"})
        },
        upd() {
            this.$router.push({name: "pupils_edit"})
        },
        del() {
            this.$router.push({name: "pupils_delete"})
        },
        loadPupil() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/pupils/",
                type: "GET",
                success: (response) => {
                    this.pupils = response.data.data
                }
            })
        }
    }
}
</script>

<style scoped>
    .button-wrapper2 {
        text-align: center;
        .mu-button{
            margin: 8px;
        }
    }
</style>
