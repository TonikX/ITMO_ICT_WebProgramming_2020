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
                                <td class="is-center">{{ dt.row.ascent_code }}</td>
                                <td class="is-center">{{dt.row.group.id}}</td>
                                <td class="is-center">{{dt.row.group.group_code}}</td>
                                <td class="is-center">{{dt.row.mountain.id}}</td>
                                <td class="is-center">{{dt.row.mountain.mountain_name}}</td>
                                <td class="is-center">{{ dt.row.duration }}</td>
                                <td class="is-center">{{ dt.row.complexity }}</td>
                                <td class="is-center">{{ dt.row.ascent_height }}</td>
                                <td class="is-center">{{ dt.row.start_date }}</td>
                                <td class="is-center">{{ dt.row.end_date }}</td>
                            </template>
                        </mu-data-table>
                    </mu-paper>
                </mu-col>
            </mu-row>
        </mu-container>
        <br/>
        <br/>

        <h3>Add new ascent</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="ascent_code" placeholder="Ascent code" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="duration" placeholder="Duration" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="complexity" placeholder="Complexity" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="ascent_height" placeholder="Ascent height" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="start_date" placeholder="Start date (yyyy-mm-dd)" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="end_date" placeholder="End date (yyyy-mm-dd)" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <h4>Select mountain for the ascent</h4>
                <mu-select v-model="mountain">
                    <mu-option v-for="mountain, index in mountain_list" :key="mountain.mountain_name"
                               :label="mountain.mountain_name"
                               :value="mountain.id"></mu-option>
                </mu-select>
                <h4>Select group for the ascent</h4>
                <mu-select v-model="group">
                    <mu-option v-for="group, index in group_list" :key="group.group_code" :label="group.group_code"
                               :value="group.id"></mu-option>
                </mu-select>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="addAscent">Add</mu-button>
        </mu-container>

        <h3>Delete an existing record</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="pk" placeholder="Ascent ID" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="deleteAscent">Delete</mu-button>
        </mu-container>

    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Ascents",
        data() {
            return {
                pk: '',
                ascent_code: '',
                group_id: '',
                group_code: '',
                mountain_id: '',
                mountain_name: '',
                duration: '',
                complexity: '',
                ascent_height: '',
                start_date: '',
                end_date: '',
                columns: [
                    { title: "Ascent ID", name: 'id', width: 60, align: 'center' },
                    { title: "Ascent Code", name: 'ascent_code', width: 130, align: 'center' },
                    { title: "Group ID", name: 'group_id', width: 60, align: 'center' },
                    { title: "Group Code", name: 'group_code', width: 150, align: 'center' },
                    { title: "Mountain ID", name: 'mountain_id', width: 150, align: 'center' },
                    { title: "Mountain Name", name: 'mountain_name', width: 150, align: 'center' },
                    { title: "Duration", name: 'duration', width: 150, align: 'center' },
                    { title: "Complexity", name: 'complexity', width: 70, align: 'center' },
                    { title: "Ascent height", name: 'ascent_height', width: 100, align: 'center' },
                    { title: "Start date", name: 'start_date', width: 140, align: 'center' },
                    { title: "End date", name: 'end_date', width: 140, align: 'center' }
                ],
                list: {},
                group_list: {},
                mountain_list: {},
                group: '',
                mountain: ''
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            })
            this.loadAscents()
            this.loadGroups()
            this.loadMountains()
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
                        this.group_list = response.data.data
                    }
                })
            },
            loadMountains() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/mountains/',
                    type: 'GET',
                    success: (response) => {
                        this.mountain_list = response.data.data
                    }
                })
            },
            loadAscents() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/ascents/',
                    type: 'GET',
                    success: (response) => {
                        this.list = response.data
                    }
                })
            },
            addAscent() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/ascents/',
                    type: 'POST',
                    data: {
                        ascent_code: this.ascent_code,
                        group: this.group,
                        mountain: this.mountain,
                        duration: this.duration,
                        complexity: this.complexity,
                        ascent_height: this.ascent_height,
                        start_date: this.start_date,
                        end_date: this.end_date,
                    },
                    success: (response) => {
                        alert('Ascent has been added'),
                        this.loadAscents()
                    },
                    error: (response) => {
                        alert('Ascent was not added. Input is not correct')
                    }
                })
            },
            deleteAscent() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/ascents/',
                    type: 'DELETE',
                    data: {
                        pk: this.pk,
                    },
                    success: (response) => {
                        this.loadAscents()
                    },
                    error: (response) => {
                        if (response.status === 404) {
                            alert('No ascent was found')
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
    }
</style>
