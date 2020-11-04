<template>
    <mu-container>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <mu-appbar style="width: 100%;" color="deepPurpleA100">
                <mu-menu slot="left" v-if="auth">
                    <mu-button flat icon>
                        <mu-icon value="menu"></mu-icon>
                    </mu-button>
                    <mu-list slot="content">
                        <mu-list-item button @click="goReaders()">
                            <mu-list-item-content>
                                <mu-list-item-title>Читатели</mu-list-item-title>
                            </mu-list-item-content>
                        </mu-list-item>
                        <mu-list-item button @click="goBooks()">
                            <mu-list-item-content>
                                <mu-list-item-title>Книги</mu-list-item-title>
                            </mu-list-item-content>
                        </mu-list-item>
                        <mu-list-item button @click="goHalls()">
                            <mu-list-item-content>
                                <mu-list-item-title>Залы</mu-list-item-title>
                            </mu-list-item-content>
                        </mu-list-item>
                    </mu-list>
                </mu-menu>
                <h2 @click="goHome()">Библиотека</h2>
                <mu-button flat slot="right" v-if="auth" @click="logout">ВЫХОД</mu-button>
            </mu-appbar>
        <mu-flex justify-content="start" class="flex-wrapper">
            <h2>Залы:</h2>
        </mu-flex>
        <mu-flex>
            <mu-flex direction="column" class="flex-col">
                <div v-for="hall in halls" v-bind:key="hall.id" >
                    <mu-flex class="flex-halls" fill>
                        <h3 @click="HallReaders(hall.id)">{{hall.name}}</h3>
                    </mu-flex>
                    <mu-flex class="flex-card" justify-content="end">
                        <small>Вместимостью {{hall.capacity}} читателей</small>
                    </mu-flex>
                </div>
            </mu-flex>
            <mu-flex v-if="hall_full" direction="column" >
                <mu-flex justify-content="start">
                    <h2>В зале {{hall_name}} находятся:</h2>
                </mu-flex >
                <mu-flex class="flex-halls-take"  direction="column" v-for="take in fixes "v-bind:key="take.id" >
                    <mu-flex class="flex-button" justify-content="start">
                        {{take.reader.name}} билет №{{take.reader.library_card}}) - "{{take.book.name}}" {{take.book.author}} (шифр №{{take.book.cipher}})
                    </mu-flex>
                </mu-flex>

            </mu-flex>
        </mu-flex>
    </mu-container>
</template>

<script>


    export default {
        name: "Halls",

        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        data () {
            return {
                hall: [],
                halls: [],
                fixes: [],
                hall_name: "",
                hall_full: false,
            }
        },
        created () {
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
            })
            this.loadHalls()
        },
        methods: {
            logout() {
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            },
            goBooks() {
                this.$router.push({'name': 'books'})
            },
            goReaders() {
                this.$router.push({'name': 'readers'})
            },
            goHome() {
                this.$router.push({name: 'home'})
            },
            goHalls() {
                this.$router.push({name: 'home'})
            },
            loadHalls() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/library/places/',
                    type: 'GET',
                    success: (response) => {
                        for (let j = 1; j < response.data.place.length; j++) {
                            this.halls.push(response.data.place[j])
                        }
                    }
                })
            },
            HallReaders(hall_id) {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/library/place/',
                    type: 'GET',
                    data: {
                        place: hall_id
                    },
                    success: (response) => {
                        this.fixes = response.data.fixes
                        this.hall_full = true
                    }
                })
            },
        },
    }
</script>

<style scoped>
    .flex-wrapper{
        width: 100%;
        height: 56px;
        margin-top: 20px;
        margin-left: 20px;
    }
    .flex-col {
        width: 30%;
        margin-top: 10px;
        margin-left: 50px;
    }
    .flex-card {
        width: 100%;
        height: 30px;
        text-align: right;
        line-height: 32px;
        margin-top: 0;
        margin-left: 50px;
    }
    .flex-halls {
        width: 100%;
        height: 36px;
        margin-top: 8px;
        text-align: start;
    }
    h3 {
        cursor: pointer
    }
    .flex-halls-take{
        width: 100%;
        margin-left: 28px;
        text-align: start;
        margin-top: 8px;
    }
    .flex-button{
        width: 100%;
    }
    h2 {
        cursor: pointer
    }
</style>
