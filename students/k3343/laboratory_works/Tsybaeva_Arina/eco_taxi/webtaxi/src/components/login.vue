<template>
  <div class="text-md-center">
    <h2 align="center">Авторизация</h2>
    <v-layout>
      <v-flex xs6 offset-xs3>
        <v-card>
         <v-card-text>
              <v-text-field v-model="login.username" label="Логин"/>
              <v-text-field v-model="login.password"  type="password" label="Пароль"/>
         </v-card-text>
            <v-card-actions>
              <v-spacer><v-btn text color="green"  @click="setLogin()">Войти</v-btn></v-spacer>

            </v-card-actions>
        </v-card>

      </v-flex>
    </v-layout>


</div>
</template>

<script>
export default {
  name: 'Login',
  data(){
    return{
      login: {
        username: '',
        password: '',
      }
    }
  },
  methods:{

    setLogin() {
      this.$axios.post("http://127.0.0.1:8000/auth/token/login", this.login )
      .then(response =>{
        console.log(response.data.auth_token)
          let auth_token = response.data.auth_token;
          localStorage.setItem('auth_token', auth_token);
          alert("Спасибо, что с нами!");
        this.$router.push({name: "home"})})
    }
}}
</script>


<style scoped>
  div {padding: 10px}
</style>
