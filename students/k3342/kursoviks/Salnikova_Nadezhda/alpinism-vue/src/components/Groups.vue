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
                                <td class="is-center">{{ dt.row.group_code }}</td>
                                <td class="is-center"><ul><li v-for="person in dt.row.participant">{{person.id}}</li></ul></td>
                                <td class="is-center"><ul><li v-for="person in dt.row.participant">{{person.name}}</li></ul></td>
                                <td class="is-center">{{ dt.row.contact_person }}</td>
                                <td class="is-center">{{ dt.row.email }}</td>
                                <td class="is-center">{{ dt.row.telephone }}</td>
                                <td class="is-center">{{ dt.row.group_success }}</td>
                            </template>
                        </mu-data-table>
                    </mu-paper>
                </mu-col>
            </mu-row>
        </mu-container>
        <br/>
        <br/>

        <h3>Add new group</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="group_code" placeholder="Group Code" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="participant_id" placeholder="Participant ID" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="contact_person" placeholder="Contact Person" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="email" placeholder="E-mail" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="telephone" placeholder="Telephone" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="group_success" placeholder="Group Success (Finished/Not finished/Not started)" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="addGroup">Add</mu-button>
        </mu-container>


        <h3>Delete existing group</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="pk" placeholder="Group ID" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="deleteGroup">Delete</mu-button>
        </mu-container>

        <h3>Edit group</h3>
        In order to edit a record of group, please, enter its id.
        <br/>
        <br/>
        <input v-model="id" type="text" placeholder=""/>
        <br/>
        <br/>
        <mu-container v-if="!options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="getGroup">Edit</mu-button>
        </mu-container>
        <mu-container v-if="options">
            <mu-paper :z-depth="1">
                <mu-text-field v-model="code" placeholder="Group Code" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="part" placeholder="Participants ID" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="contact" placeholder="Contact person" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="mail" placeholder="Email" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="phone" placeholder="Telephone" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="success" placeholder="Group Success" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br v-if="options"/>
        <mu-container v-if="options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="editGroup">Choose</mu-button>
        </mu-container>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: 'Groups',
        data() {
            return {
                pk: '',
                id: '',
                group_code: '',
                participant_id: '',
                participant_name: '',
                contact_person: '',
                email: '',
                telephone: '',
                group_success: '',
                columns: [
                    { title: "Group ID", name: 'id', width: 70, align: 'center' },
                    { title: "Group code", name: 'group_code', width: 150, align: 'center' },
                    { title: "Participants id", name: 'participant_id', width: 100, align: 'center' },
                    { title: "Participants names", name: 'participant_name', width: 200, align: 'center' },
                    { title: "Contact person", name: 'contact_person', width: 145, align: 'center' },
                    { title: "Email", name: 'email', width: 220, align: 'center' },
                    { title: "Phone number", name: 'telephone', width: 135, align: 'center' },
                    { title: "Success", name: 'group_success', width: 100, align: 'center' }
                ],
                list: {},
                options: '',
                code: '',
                part: '',
                contact: '',
                mail: '',
                phone: '',
                success: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            })
                this.loadGroups()
        },
        methods: {
            goHome() {
                this.$router.push({name: "main_page"})
            },
            loadGroups() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/groups/',
                    type: 'GET',
                    success: (response) => {
                        this.list = response.data
                    }
                })
            },
            addGroup() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/groups/',
                    type: 'POST',
                    data: {
                        id: this.id,
                        group_code: this.group_code,
                        participant: this.participant_id,
                        contact_person: this.contact_person,
                        email: this.email,
                        telephone: this.telephone,
                        group_success: this.group_success
                    },
                    success: (response) => {
                        alert('Group has been added'),
                        this.loadGroups()
                    },
                    error: (response) => {
                        alert('Group was not added. Input is not correct')
                        console.log(response)
                    }
                })
            },
            toggle (panel) {
                this.panel = panel === this.panel ? '' : panel;
            },
            deleteGroup() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/groups/',
                    type: 'DELETE',
                    data: {
                        pk: this.pk,
                    },
                    success: (response) => {
                        this.loadGroups()
                    },
                    error: (response) => {
                        if (response.status === 404) {
                            alert('No group was found')
                        }
                    }
                })
            },
            getGroup() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/groups/',
                    type: 'GET',
                    data: {
                        id: this.id
                    },
                    success: (response) => {
                        this.options = response.data
                        this.code = response.data.attributes.group_code
                        this.part = response.data.attributes.participant
                        this.contact = response.data.attributes.contact_person
                        this.mail = response.data.attributes.email
                        this.phone = response.data.attributes.telephone
                        this.success = response.data.attributes.group_success
                    },
                    error: (response) => {
                        if (response.status === 404) {
                            alert('No group was found')
                        }
                    }
                })
            },
            editGroup() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/groups/',
                    type: 'PUT',
                    data: {
                        id: this.id,
                        group_code: this.code,
                        participants: this.part,
                        contact_person: this.contact,
                        email: this.mail,
                        telephone: this.phone,
                        group_success: this.success
                    },
                    success: (response) => {
                        this.loadGroups()
                        this.options = ''
                        alert('Group was edited')
                    },
                    error: (response) => {
                        alert('Something is wrong')
                        console.log(response)
                    }
                })
            },
        }
    }
</script>

<style>
    body {
        background-color: #ffffff;
    }

    .demo-divider-form {
        font-size: 90%;
        padding: 0 16px;
        height: 30px;
    }

    .table-wrapper {
        text-align: center;
        margin-left: auto;
        width: 1300px;
    }

    .panel-wrapper {
        width: 640px;
    }

    .button-wrapper4 {
        text-align: center;
    }

    .mu-button {
        margin: 8px;
    }
</style>
