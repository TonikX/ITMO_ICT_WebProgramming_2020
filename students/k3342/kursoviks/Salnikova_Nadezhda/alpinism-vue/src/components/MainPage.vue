<template>
    <div>
        <h1>Welcome to the alpinist club service</h1>
        <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="goAscents">Ascents</mu-button>
            <mu-button color="#2c3e50" textColor="white" @click="goAlpinists">Alpinists</mu-button>
            <mu-button color="#2c3e50" textColor="white" @click="goGroups">Groups</mu-button>
            <mu-button color="#2c3e50" textColor="white" @click="goMountains">Mountains</mu-button>
            <mu-button color="#2c3e50" textColor="white" @click="goClubs">Clubs</mu-button>
            <mu-button color="#2c3e50" textColor="white" @click="goCountries">Countries</mu-button>
            <mu-button color="#2c3e50" textColor="white" @click="goEmergencies">Emergencies</mu-button>
            <mu-button color="#2c3e50" textColor="white" @click="goSuccesses">Successes</mu-button>
        </mu-container>
        </br>
        <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
            <mu-button color="grey" textColor="white" @click="goRequest1">Ascents by mountain</mu-button>
        </mu-container>
        <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
            <mu-button color="grey" textColor="white" @click="logout">logout</mu-button>
        </mu-container>

    </div>
</template>

<script>
    export default {
        name: "MainPage",
        methods: {
            logout() {
            sessionStorage.removeItem("auth_token")
            window.location = '/'
            },
            goGroups() {
                this.$router.push({name: "groups"})
            },
            goAlpinists() {
                this.$router.push({name: "alpinists"})
            },
            goMountains() {
                this.$router.push({name: "mountains"})
            },
            goClubs() {
                this.$router.push({name: "clubs"})
            },
            goCountries() {
                this.$router.push({name: "countries"})
            },
            goAscents() {
                this.$router.push({name: "ascents"})
            },
            goEmergencies() {
                this.$router.push({name: "emergencies"})
            },
            goSuccesses() {
                this.$router.push({name: "successes"})
            },
            goRequest1() {
                this.$router.push({name: "request1"})
            }
        }
    }
</script>

<style scoped>
    .button-wrapper4 {
        text-align: center;
        color: grey;
    }

    h1 {
        font-size: 180%;
        line-height: 100px;
        color: #000000;
        text-align: center;
    }
</style>
