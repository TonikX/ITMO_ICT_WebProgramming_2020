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
                                <td class="is-center">{{ dt.row.club_name }}</td>
                                <td class="is-center">{{ dt.row.country.id }}</td>
                                <td class="is-center">{{ dt.row.country.country_name }}</td>
                                <td class="is-center">{{ dt.row.city }}</td>
                                <td class="is-center">{{ dt.row.contact_person }}</td>
                                <td class="is-center">{{ dt.row.email }}</td>
                                <td class="is-center">{{ dt.row.telephone }}</td>
                            </template>
                        </mu-data-table>
                    </mu-paper>
                </mu-col>
            </mu-row>
        </mu-container>
        <br/>
        <br/>

        <h3>Add new club</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="club_name" placeholder="Club Name" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="city" placeholder="City" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="contact_person" placeholder="Contact Person" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="email" placeholder="E-mail" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="telephone" placeholder="Telephone number" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <h4>Select country of the club</h4>
                <mu-select v-model="country">
                <mu-option v-for="country, index in countries_list" :key="country.country_name" :label="country.country_name"
                       :value="country.id"></mu-option>
                </mu-select>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="addClub">Add</mu-button>
        </mu-container>

        <h3>Delete an existing club</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="pk" placeholder="Club ID" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="deleteClub">Delete</mu-button>
        </mu-container>

    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Clubs",
        data() {
            return {
                pk: '',
                club_name: '',
                country_id: '',
                country_name: '',
                city: '',
                contact_person: '',
                email: '',
                telephone: '',
                columns: [
                    { title: "Club ID", name: 'id', width: 70, align: 'center' },
                    { title: "Club name", name: 'club_name', width: 150, align: 'center' },
                    { title: "Country ID", name: 'country_id', width: 70, align: 'center' },
                    { title: "Country Name", name: 'country_name', width: 150, align: 'center' },
                    { title: "City", name: 'city', width: 120, align: 'center' },
                    { title: "Contact Person", name: 'contact_person', width: 150, align: 'center' },
                    { title: "Email", name: 'email', width: 250, align: 'center' },
                    { title: "Telephone", name: 'telephone', width: 150, align: 'center' }
                ],
                list: {},
                country: '',
                options: '',
                countries_list: {}
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            })
            this.loadClubs()
            this.loadCountries()
        },
        methods: {
            goHome() {
                this.$router.push({name: "main_page"})
            },
            loadClubs() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/clubs/',
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
                        this.countries_list = response.data.data,
                        options = response.data.data
                    }
                })
            },
            addClub() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/clubs/',
                    type: 'POST',
                    data: {
                        id: this.id,
                        club_name: this.club_name,
                        country: this.country,
                        city: this.city,
                        contact_person: this.contact_person,
                        email: this.email,
                        telephone: this.telephone
                    },
                    success: (response) => {
                        alert('Club has been added'),
                        this.loadClubs()
                    },
                    error: (response) => {
                        alert('Club was not added. Input is not correct')
                    }
                })
            },
            deleteClub() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/clubs/',
                    type: 'DELETE',
                    data: {
                        pk: this.pk,
                    },
                    success: (response) => {
                        this.loadClubs()
                    },
                    error: (response) => {
                        if (response.status === 404) {
                            alert('No club was found')
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
        width: 1126px;
    }
</style>
