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
                                <td class="is-center">{{ dt.row.name }}</td>
                                <td class="is-center">{{ dt.row.birth_date }}</td>
                                <td class="is-center">{{ dt.row.club_name.id }}</td>
                                <td class="is-center">{{ dt.row.club_name.club_name}}</td>
                                <td class="is-center">{{ dt.row.telephone }}</td>
                                <td class="is-center">{{ dt.row.email }}</td>
                                <td class="is-center">{{ dt.row.address }}</td>
                            </template>
                        </mu-data-table>
                    </mu-paper>
                </mu-col>
            </mu-row>
        </mu-container>
        <br/>
        <br/>

        <h3>Add new alpinist</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="name" placeholder="Alpinist Name" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="birth_date" placeholder="Birth date (yyyy-mm-dd)" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="telephone" placeholder="Telephone number" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="email" placeholder="E-mail" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="address" placeholder="Address (city, street, house, flat)" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <h4>Select club of the alpinist</h4>
                <mu-select v-model="club">
                <mu-option v-for="club, index in club_list" :key="club.club_name" :label="club.club_name"
                       :value="club.id"></mu-option>
                </mu-select>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="addAlpinist">Add</mu-button>
        </mu-container>

        <h3>Delete a record</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="pk" placeholder="Alpinist ID" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="deleteAlpinist">Delete</mu-button>
        </mu-container>

        <h3>Edit alpinist</h3>
        In order to edit a record of an alpinist, please, enter its id.
        <br/>
        <br/>
        <input v-model="id" type="text" placeholder=""/>
        <br/>
        <br/>
        <mu-container v-if="!options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="getAlpinist">Edit</mu-button>
        </mu-container>
        <mu-container v-if="options">
            <mu-paper :z-depth="1">
                <mu-text-field v-model="new_name" placeholder="Name" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="new_birth" placeholder="Birth date (yyyy-mm-dd)" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="new_phone" placeholder="Telephone" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="new_mail" placeholder="E-mail" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="new_address" placeholder="Address" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <h4>Select club of the alpinist</h4>
                <mu-select v-model="new_club">
                <mu-option v-for="new_club, index in club_list" :key="new_club.club_name" :label="new_club.club_name"
                       :value="new_club.id"></mu-option>
                </mu-select>
            </mu-paper>
        </mu-container>
        <br v-if="options"/>
        <mu-container v-if="options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="editAlpinist">Edit</mu-button>
        </mu-container>

    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Alpinists",
        data() {
            return {
                pk: '',
                id: '',
                name: '',
                birth_date: '',
                club_name_id: '',
                club_name: '',
                telephone: '',
                email: '',
                address: '',
                columns: [
                    { title: "Alpinist ID", name: 'id', width: 70, align: 'center' },
                    { title: "Name", name: 'name', width: 170, align: 'center' },
                    { title: "Birth date", name: 'birth_date', width: 150, align: 'center' },
                    { title: "Club ID", name: 'club_name_id', width: 70, align: 'center' },
                    { title: "Club Name", name: 'club_name', width: 120, align: 'center' },
                    { title: "Telephone", name: 'telephone', width: 140, align: 'center' },
                    { title: "Email", name: 'email', width: 170, align: 'center' },
                    { title: "Address", name: 'address', width: 234, align: 'center' }
                ],
                list: {},
                club_list: {},
                options: '',
                club: '',
                new_name: '',
                new_birth: '',
                new_club: '',
                new_phone: '',
                new_mail: '',
                new_address: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            })
            this.loadAlpinists()
            this.loadClubs()
        },
        methods: {
            goHome() {
                this.$router.push({name: "main_page"})
            },
            loadAlpinists() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/alpinists/',
                    type: 'GET',
                    success: (response) => {
                        this.list = response.data
                    }
                })
            },
            loadClubs() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/clubs/',
                    type: 'GET',
                    success: (response) => {
                        this.club_list = response.data.data
                    }
                })
            },
            addAlpinist() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/alpinists/',
                    type: 'POST',
                    data: {
                        id: this.id,
                        name: this.name,
                        birth_date: this.birth_date,
                        club_name: this.club,
                        telephone: this.telephone,
                        email: this.email,
                        address: this.address,
                    },
                    success: (response) => {
                        alert('Alpinist has been added'),
                        this.loadAlpinists()
                    },
                    error: (response) => {
                        alert('Alpinist was not added. Input is not correct')
                    }
                })
            },
            deleteAlpinist() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/alpinists/',
                    type: 'DELETE',
                    data: {
                        pk: this.pk,
                    },
                    success: (response) => {
                        this.loadAlpinists()
                    },
                    error: (response) => {
                        if (response.status === 404) {
                            alert('No alpinist was found')
                        }
                    }
                })
            },
            getAlpinist() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/alpinists/',
                    type: 'GET',
                    data: {
                        id: this.id
                    },
                    success: (response) => {
                        this.options = response.data
                        this.new_name = response.data.attributes.name
                        this.new_birth = response.data.attributes.birth_date
                        this.new_club = response.data.attributes.club_name
                        this.new_phone = response.data.attributes.telephone
                        this.new_mail = response.data.attributes.email
                        this.new_address = response.data.attributes.address
                    },
                    error: (response) => {
                        if (response.status === 404) {
                            alert('No alpinist was found')
                        }
                    }
                })
            },
            editAlpinist() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/alpinists/',
                    type: 'PUT',
                    data: {
                        id: this.id,
                        name: this.new_name,
                        birth_date: this.new_birth,
                        club_name: this.new_club,
                        telephone: this.new_phone,
                        email: this.new_mail,
                        address: this.new_address
                    },
                    success: (response) => {
                        this.loadAlpinists()
                        this.options = ''
                        alert('Alpinist was edited')
                    },
                    error: (response) => {
                        alert('Something went wrong')
                    }
                })
            },
        }
    }

</script>

<style scoped>

</style>
