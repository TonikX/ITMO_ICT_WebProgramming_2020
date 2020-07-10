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
                                <td class="is-center">{{ dt.row.country_name }}</td>
                            </template>
                        </mu-data-table>
                    </mu-paper>
                </mu-col>
            </mu-row>
        </mu-container>
        <br/>
        <br/>

        <h3>Add new record</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="country_name" placeholder="Country Name" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="addCountry">Add</mu-button>
        </mu-container>

        <h3>Delete an existing record</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="pk" placeholder="Country ID" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="deleteCountry">Delete</mu-button>
        </mu-container>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Countries",
        data() {
            return {
                pk: '',
                id: '',
                country_name: '',
                columns: [
                    { title: "Country ID", name: 'id', width: 60, align: 'center' },
                    { title: "Country Name", name: 'country_name', width: 130, align: 'center' },
                ],
                list: {}
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            })
            this.loadCountries()
        },
        methods: {
            goHome() {
                this.$router.push({name: "main_page"})
            },
            loadCountries() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/countries/',
                    type: 'GET',
                    success: (response) => {
                        this.list = response.data
                    }
                })
            },
            addCountry() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/countries/',
                    type: 'POST',
                    data: {
                        id: this.id,
                        country_name: this.country_name
                    },
                    success: (response) => {
                        alert('Country has been added'),
                        this.loadCountries()
                    },
                    error: (response) => {
                        alert('Country was not added. Input is not correct')
                    }
                })
            },
            deleteCountry() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/countries/',
                    type: 'DELETE',
                    data: {
                        pk: this.pk,
                    },
                    success: (response) => {
                        this.loadCountries()
                    },
                    error: (response) => {
                        if (response.status === 404) {
                            alert('No country was found')
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
        width: 209px;
    }
</style>
