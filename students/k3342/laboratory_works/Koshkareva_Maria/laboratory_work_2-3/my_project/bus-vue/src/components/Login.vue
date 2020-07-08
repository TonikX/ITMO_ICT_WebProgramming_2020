<template>
<body>
    <mu-container>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
    <mu-card class="card" style="width:55%; max-width:375px; margin:0 auto;">
         <mu-card-header class="card_head">
             <h1>User Login</h1>
         </mu-card-header>
        <br>
        <mu-flex justify-content="center">
        <mu-text-field class="cell" color="black" icon="face" v-model="login" type="text"
        placeholder="username"/>
        </mu-flex>
        <mu-flex justify-content="center">
        <mu-text-field class="cell" color="black" icon="lock" v-model="password" type="password"
        placeholder="password"/></mu-flex>
        <br>
        <mu-button color="deepOrange400" full-width @click="setLogin">
            Log in
        </mu-button>
    </mu-card>
    </mu-container>
</body>
</template>

<script>
    import $ from 'jquery'

    export default {
        name:"Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            setLogin(){
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login/",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        sessionStorage.setItem("auth_token",response.data.attributes.auth_token)
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status == 400){
                            alert("Your login or password is incorrect")
                        }
                    }
                })
            }
        }
    }
</script>

<style scoped>
     .cell {
        border-radius: 15px;
        background: #fff;
      }
      .card {
        background: #e0ebff;
      }
      .card_head {
        background: #fff;
      }
</style>

