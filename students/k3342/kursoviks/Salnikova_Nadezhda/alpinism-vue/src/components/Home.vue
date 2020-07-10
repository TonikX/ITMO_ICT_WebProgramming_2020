<template>
    <div>
        <h1>Welcome</h1>
        <h3>Please log in the system to proceed</h3>
        <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="goLogin">Sign in</mu-button>
        </mu-container>
        <h3>Don't have an account yet? Sign up</h3>
        <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="signUp">Sign up</mu-button>
        </mu-container>
    </div>
</template>

<script>
    export default {
        name: "Home",
        methods: {
            goLogin() {
                this.$router.push({name: "login"})
            },
            signUp() {
                this.$router.push({name: "register"})
            }
        }
    }
</script>

<style scoped>

</style>
