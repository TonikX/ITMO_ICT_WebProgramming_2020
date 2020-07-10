<template>
    <mu-container>
      <mu-appbar style="width: 100%;" color="primary">
        Регистрация нового пользователя
      <mu-button flat  @click="goHome">Назад</mu-button>
      </mu-appbar>
      <div class="registr">
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
     <mu-button class="btn-send" round @click="Register"> Зарегистрироваться </mu-button>
    </mu-form>
  </div>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Registration",
        data () {
          return {
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
          goHome() {
                this.$router.push({name: "Home"})
          },
          Register() {
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
                      alert('Пользователь зарегистрирован');
                      this.$router.push({name: "Home"})
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
