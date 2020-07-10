<template>
    <div>
        <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="goHome">Home</mu-button>
        </mu-container>

        <mu-container class="table-wrapper">
            <mu-row gutter>
                <mu-col>
                    <mu-paper :z-depth="1">
                        <mu-data-table stripe :columns="columns" :data="list.data">
                            <template slot-scope="dt">
                                <td class="is-center">{{ dt.row.id }}</td>
                                <td class="is-center">{{ dt.row.group.id }}</td>
                                <td class="is-center">{{ dt.row.group.group_code }}</td>
                                <td class="is-center">{{ dt.row.participant.id }}</td>
                                <td class="is-center">{{ dt.row.participant.name }}</td>
                                <td class="is-center">{{ dt.row.individual_success }}</td>
                            </template>
                        </mu-data-table>
                    </mu-paper>
                </mu-col>
            </mu-row>
        </mu-container>
        <br/>
        <br/>

        <h3>Add new success</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <h4>Select group</h4>
                <mu-select v-model="group">
                    <mu-option v-for="group, index in group_list" :key="group.group_code"
                               :label="group.group_code" :value="group.id"></mu-option>
                </mu-select>
                <h4>Select participant</h4>
                <mu-select v-model="participant">
                    <mu-option v-for="participant, index in participant_list" :key="participant.name"
                               :label="participant.name" :value="participant.id"></mu-option>
                </mu-select>
                <mu-divider></mu-divider>
                <h4>Fill in the fields below</h4>
                <mu-text-field v-model="individual_success" placeholder="Finished/Injured/Not finished/Not started" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br/>

        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="addSuccess">Add</mu-button>
        </mu-container>

        <h3>Delete existing success</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="pk" placeholder="Success ID" solo full-width class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="deleteSuccess">Delete</mu-button>
        </mu-container>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Successes",
        data() {
            return {
                pk: '',
                id: '',
                group_id: '',
                group_code: '',
                participant_id: '',
                participant_name: '',
                individual_success: '',
                columns: [
                    { title: "Success ID", name: 'id', width: 85, align: 'center' },
                    { title: "Group ID", name: 'group_id', width: 85, align: 'center' },
                    { title: "Group Code", name: 'group_code', width: 155, align: 'center' },
                    { title: "Alpinist ID", name: 'participant_id', width: 85, align: 'center' },
                    { title: "Alpinist Name", name: 'participant_name', width: 174, align: 'center' },
                    { title: "Success", name: 'individual_success', width: 140, align: 'center' },
                ],
                list: {},
                group_list: {},
                group: '',
                participant_list: {},
                participant: ''
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            })
            this.loadSuccesses()
            this.loadGroups()
            this.loadParticipants()
        },
        methods: {
            goHome() {
                this.$router.push({name: "main_page"})
            },
            loadSuccesses() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/successes/',
                    type: 'GET',
                    success: (response) => {
                        this.list = response.data
                    }
                })
            },
            loadGroups() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/groups/',
                    type: 'GET',
                    success: (response) => {
                        this.group_list = response.data.data
                    }
                })
            },
            loadParticipants() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/alpinists/',
                    type: 'GET',
                    success: (response) => {
                        this.participant_list = response.data.data
                    }
                })
            },
            addSuccess() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/successes/',
                    type: 'POST',
                    data: {
                        id: this.id,
                        group: this.group,
                        participant: this.participant,
                        individual_success: this.individual_success,
                    },
                    success: (response) => {
                        alert('Success has been added'),
                        this.loadSuccesses()
                    },
                    error: (response) => {
                        alert('Success was not added. Input is not correct')
                    }
                })
            },
            deleteSuccess() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/successes/',
                    type: 'DELETE',
                    data: {
                        pk: this.pk,
                    },
                    success: (response) => {
                        this.loadSuccesses()
                    },
                    error: (response) => {
                        if (response.status === 404) {
                            alert('No success was found')
                        }
                    }
                })
            },
        }
    }
</script>

<style scoped>
    .table-wrapper {
        text-align: center;
        margin-left: auto;
        width: 740px;
    }
</style>
