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
                                <td class="is-center">{{ dt.row.mountain_name }}</td>
                                <td class="is-center">{{ dt.row.country.id }}</td>
                                <td class="is-center">{{ dt.row.country.country_name }}</td>
                                <td class="is-center">{{ dt.row.region }}</td>
                                <td class="is-center">{{ dt.row.height }}</td>
                            </template>
                        </mu-data-table>
                    </mu-paper>
                </mu-col>
            </mu-row>
        </mu-container>
        <br/>
        <br/>

        <h3>Add new mountain</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="mountain_name" placeholder="Mountain Name" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="region" placeholder="Region" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="height" placeholder="Height" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <h4>Select country of the mountain</h4>
                <mu-select v-model="country">
                <mu-option v-for="country, index in country_list" :key="country.country_name" :label="country.country_name"
                       :value="country.id"></mu-option>
                </mu-select>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="addMountain">Add</mu-button>
        </mu-container>

        <h3>Delete an existing record</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="pk" placeholder="Mountain ID" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="deleteMountain">Delete</mu-button>
        </mu-container>

        <h3>Edit group</h3>
        In order to edit a record of mountain, please, enter its id.
        <br/>
        <br/>
        <input v-model="id" type="text" placeholder=""/>
        <br/>
        <br/>
        <mu-container v-if="!options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="getMountain">Edit</mu-button>
        </mu-container>
        <mu-container v-if="options">
            <mu-paper :z-depth="1">
                <mu-text-field v-model="name_new" placeholder="Mountain name" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="country_new" placeholder="Country ID" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="region_new" placeholder="Region" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="height_new" placeholder="Height" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br v-if="options"/>
        <mu-container v-if="options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="editMountain">Choose</mu-button>
        </mu-container>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Mountains",
        data() {
            return {
                pk: '',
                id: '',
                mountain_name: '',
                country_id: '',
                country_name: '',
                region: '',
                height: '',
                columns: [
                    { title: "Mountain ID", name: 'id', width: 70, align: 'center' },
                    { title: "Mountain name", name: 'mountain_name', width: 150, align: 'center' },
                    { title: "Country ID", name: 'country_id', width: 70, align: 'center' },
                    { title: "Country Name", name: 'country_name', width: 150, align: 'center' },
                    { title: "Region", name: 'region', width: 200, align: 'center' },
                    { title: "Height", name: 'height', width: 100, align: 'center' }
                ],
                list: {},
                country_list: {},
                country: '',
                options: '',
                name_new: '',
                country_new: '',
                region_new: '',
                height_new: ''
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            })
            this.loadMountains()
            this.loadCountries()
        },
        methods: {
            goHome() {
                this.$router.push({name: "main_page"})
            },
            loadMountains() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/mountains/',
                    type: 'GET',
                    success: (response) => {
                        this.list = response.data
                    }
                })
            },
            loadCountries() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/countries/',
                    type: 'GET',
                    success: (response) => {
                        this.country_list = response.data.data
                    }
                })
            },
            addMountain() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/mountains/',
                    type: 'POST',
                    data: {
                        id: this.id,
                        mountain_name: this.mountain_name,
                        country: this.country,
                        region: this.region,
                        height: this.height,
                    },
                    success: (response) => {
                        alert('Mountain has been added'),
                        this.loadMountains()
                    },
                    error: (response) => {
                        alert('Mountain was not added. Input is not correct')
                    }
                })
            },
            deleteMountain() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/mountains/',
                    type: 'DELETE',
                    data: {
                        pk: this.pk,
                    },
                    success: (response) => {
                        this.loadMountains()
                    },
                    error: (response) => {
                        if (response.status === 404) {
                            alert('No mountain was found')
                        }
                    }
                })
            },
            getMountain() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/mountains/',
                    type: 'GET',
                    data: {
                        id: this.id
                    },
                    success: (response) => {
                        this.options = response.data,
                        this.name_new = response.data.mountain_name,
                        this.country_new = response.data.country.id,
                        this.region_new = response.data.region,
                        this.height_new = response.data.height,
                        console.log(response)
                    },
                    error: (response) => {
                        if (response.status === 404) {
                            alert('No mountain was found')
                        }
                        console.log(response)
                    }
                })
            },
            editMountain() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/mountains/',
                    type: 'PUT',
                    data: {
                        id: this.id,
                        mountain_name: this.name_new,
                        country: this.country_new,
                        region: this.region_new,
                        height: this.height_new
                    },
                    success: (response) => {
                        this.loadMountains()
                    },
                    error: (response) => {
                        if (response.status === 404) {
                            alert('Cannot update the mountain')
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
        width: 756px;
    }
</style>
