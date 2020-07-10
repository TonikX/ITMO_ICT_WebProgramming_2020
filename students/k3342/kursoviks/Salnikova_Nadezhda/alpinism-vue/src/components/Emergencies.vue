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
                                <td class="is-center">{{ dt.row.participant.id }}</td>
                                <td class="is-center">{{ dt.row.participant.name }}</td>
                                <td class="is-center">{{dt.row.ascent.id}}</td>
                                <td class="is-center">{{dt.row.ascent.ascent_code}}</td>
                                <td class="is-center">{{ dt.row.date }}</td>
                                <td class="is-center">{{ dt.row.situation }}</td>
                                <td class="is-center">{{ dt.row.commentary }}</td>
                            </template>
                        </mu-data-table>
                    </mu-paper>
                </mu-col>
            </mu-row>
        </mu-container>
        <br/>
        <br/>

        <h3>Add new emergency</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <h4>Select participant</h4>
                <mu-select v-model="participant">
                    <mu-option v-for="participant, index in participant_list" :key="participant.name"
                               :label="participant.name" :value="participant.id"></mu-option>
                </mu-select>
                <h4>Select ascent</h4>
                <mu-select v-model="ascent">
                    <mu-option v-for="ascent, index in ascent_list" :key="ascent.ascent_code"
                               :label="ascent.ascent_code" :value="ascent.id"></mu-option>
                </mu-select>
                <h4>Fill in the fields below</h4>
                <mu-divider></mu-divider>
                <mu-text-field v-model="date" placeholder="Emergency Date (yyyy-mm-dd)" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="situation" placeholder="Injury/Gone/Death" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="commentary" placeholder="Commentary" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>

            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="addEmergency">Add</mu-button>
        </mu-container>

        <h3>Delete existing emergency</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="pk" placeholder="Emergency ID" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="deleteEmergency">Delete</mu-button>
        </mu-container>

    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Emergencies",
        data() {
            return {
                pk: '',
                id: '',
                participant_id: '',
                participant_name: '',
                ascent_id: '',
                ascent_code: '',
                date: '',
                situation: '',
                commentary: '',
                columns: [
                    { title: "Emergency ID", name: 'id', width: 85, align: 'center' },
                    { title: "Participant ID", name: 'participant_id', width: 85, align: 'center' },
                    { title: "Participant Name", name: 'participant_name', width: 155, align: 'center' },
                    { title: "Ascent ID", name: 'ascent_id', width: 85, align: 'center' },
                    { title: "Ascent Code", name: 'ascent_code', width: 174, align: 'center' },
                    { title: "Date", name: 'date', width: 140, align: 'center' },
                    { title: "Situation", name: 'situation', width: 100, align: 'center' },
                    { title: "Commentary", name: 'commentary', width: 300, align: 'center' },
                ],
                list: {},
                participant_list: {},
                ascent_list: {},
                participant: '',
                ascent: ''
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            })
            this.loadEmergencies()
            this.loadParticipants()
            this.loadAscents()
        },
        methods: {
            goHome() {
                this.$router.push({name: "main_page"})
            },
            loadEmergencies() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/emergencies/',
                    type: 'GET',
                    success: (response) => {
                        this.list = response.data
                    }
                })
            },
            loadAscents() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/ascents/',
                    type: 'GET',
                    success: (response) => {
                        this.ascent_list = response.data.data
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
            addEmergency() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/emergencies/',
                    type: 'POST',
                    data: {
                        id: this.id,
                        participant: this.participant,
                        ascent: this.ascent,
                        date: this.date,
                        situation: this.situation,
                        commentary: this.commentary,
                    },
                    success: (response) => {
                        alert('Emergency has been added'),
                        this.loadEmergencies()
                    },
                    error: (response) => {
                        alert('Emergency was not added. Input is not correct')
                    }
                })
            },
            deleteEmergency() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/emergencies/',
                    type: 'DELETE',
                    data: {
                        pk: this.pk,
                    },
                    success: (response) => {
                        this.loadEmergencies()
                    },
                    error: (response) => {
                        if (response.status === 404) {
                            alert('No emergency was found')
                        }
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
