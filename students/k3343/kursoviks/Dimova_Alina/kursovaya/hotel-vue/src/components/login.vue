<template>
  <mu-container>
  <div class="title">
    <h2> Войдите в свой аккаунт </h2>
  </div>
    <div class="login">
      <mu-text-field v-model="username" label="Логин"></mu-text-field>
      <mu-text-field v-model="password" type="password" label="Пароль"></mu-text-field>
        <button @click="isWorker">Войти</button>
    </div>
    <div v-if="!show">
    <button @click="Show">Регистрация</button>
    </div>
  <div v-if="show">
    <h4> Либо заполните форму для регистрации </h4>
  </div>
  <div class="registr" v-if="show">
    <mu-form :model="form">
      <mu-form-item label="Ваше ФИО">
        <mu-text-field v-model="form.name"></mu-text-field>
      </mu-form-item>
      <mu-form-item label="Вы являетесь уборщиком?">
        <mu-select v-model="form.is_worker">
              <mu-option label="Да" value="1"></mu-option>
              <mu-option label="Нет" value="0"></mu-option>
          </mu-select>
      </mu-form-item>
      <mu-form-item label="Имя пользователя">
        <mu-text-field v-model="form.username"></mu-text-field>
      </mu-form-item>

      <mu-form-item label="Ваш email">
        <label>
           <mu-text-field v-model="form.email"></mu-text-field>
        </label>
      </mu-form-item>
      <mu-form-item label="Пароль">
        <label>
           <mu-text-field type="password" v-model="form.password"></mu-text-field>
        </label>
      </mu-form-item>
     <mu-button class="btn-send" round @click="Registr"> Зарегистрироваться </mu-button>
    </mu-form>
  </div>
  </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Login",
        data() {
            return {
                show: false,
                is_w: true,
                username: '',
                password: '',
                workers: '',
                user_id: '',
                form: {
                  name: '',
                  username: '',
                  email: '',
                  password: '',
                  is_worker: '',
                }
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login/",
                    type: "POST",
                    data: {
                        username: this.username,
                        password: this.password
                    },
                    success: (response) => {
                      sessionStorage.setItem("auth_token", response.data.attributes.auth_token);
                      alert('Вы вошли');
                      this.$router.push({name: "Home"});
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Логин или пароль не верен")
                        }
                    }
                })
            },
            isWorker() {
              $.ajax({
                    url: "http://127.0.0.1:8000/app/hotel/users/1",
                    type: "GET",
                      success: (response) => {
                      console.log(response);
                      this.workers = response.data.data;
                      for (let i = 0; i < this.workers.length; i++) {
                        if (this.workers[i].username === this.username) {
                          alert('У вас нет доступа');
                          this.$router.push({name: "Home"});
                          return true
                        }
                      }
                      this.setLogin();
                      return false
                    }
                  })
            },
            Show() {
              this.show = true
            },
            Registr() {
              $.ajax({
                    url: "http://127.0.0.1:8000/auth/users/",
                    type: "POST",
                    data: {
                        username: this.form.username,
                        email: this.form.email,
                        password: this.form.password,
                    },
                    success: (response) => {
                        this.show = false;
                        this.user_id = response.data.id;
                        this.addInfo();
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Пароль не соответствует требованиям! (В нем меньше 8 знаков либо он похож на имя пользователя)")
                        }
                    }
                })
            },
            addInfo() {
              $.ajax({
                    url: "http://127.0.0.1:8000/app/hotel/users/" + this.user_id,
                    type: "POST",
                    data: {
                        is_worker: this.form.is_worker,
                        full_name: this.form.name,
                    },
                    success: (response) => {
                      console.log(response);
                      this.$router.push({name: "login"})
                    },
                      error: (response) => {
                        if (response.status === 400) {
                          console.log(response);
                          }
                    }
              })
            }
        }
    }
</script>

<style scoped>
</style>
