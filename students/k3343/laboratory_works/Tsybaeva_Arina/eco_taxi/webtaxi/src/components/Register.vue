<template>
  <div class="text-md-center">
    <h2 align="center">Регистрация</h2>
    <v-layout>
      <v-flex xs6 offset-xs3>
        <v-card>
         <v-card-text>
              <v-text-field v-model="register.username" label="Логин"/>
              <v-text-field v-model="register.password"  type="password" label="Пароль"/>
         </v-card-text>
            <v-card-actions>
              <v-spacer><v-btn text color="green"  @click="goInfo()">Зарегистрироваться</v-btn></v-spacer>

            </v-card-actions>
        </v-card>

      </v-flex>
    </v-layout>


</div>
</template>

<script>
    export default {
        name: "Register",
      data () {
          return {
            register:{
              username:"",
              password:""
            }
          }
      },
      methods : {
        goInfo() {
          this.$axios.post("http://127.0.0.1:8000/auth/users/", this.register);
          this.$router.push({name: "Info"})}
          }}

</script>

<style scoped>

</style>
