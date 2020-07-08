<template>
  <mu-container>
    <mu-form ref="form" :model="validateForm" class="mu-demo-form">
      <h1>Регистрация</h1>
      <mu-form-item label="username" help-text="help text" prop="username" :rules="usernameRules">
        <mu-text-field v-model="validateForm.username" prop="username"></mu-text-field>
      </mu-form-item>
      <mu-form-item label="last name" help-text="help text" prop="last_name">
        <mu-text-field v-model="validateForm.lastName" prop="last_name"></mu-text-field>
      </mu-form-item>
      <mu-form-item label="password" prop="password" :rules="passwordRules">
          <mu-text-field type="password" v-model="validateForm.password" prop="password"></mu-text-field>
      </mu-form-item>
      <mu-form-item label="password 2" prop="repeatedPassword" :rules="repeatedPasswordRules">
          <mu-text-field type="password" v-model="validateForm.repeatedPassword" prop="password"></mu-text-field>
      </mu-form-item>
      <mu-form-item>
        <mu-button color="primary" @click="submit">submit</mu-button>
        <mu-button @click="clear">reset</mu-button>
      </mu-form-item>
    </mu-form>
  </mu-container>
</template>

<script>
export default {
  data () {
    return {
      usernameRules: [
        { validate: (val) => !!val, message: 'Username must be filled in'},
        { validate: (val) => val.length >= 3, message: 'Username length greater than 3'}
      ],
      passwordRules: [
        { validate: (val) => !!val, message: 'Password must be filled in'},
        { validate: (val) => val.length >= 3 && val.length <= 10, message: 'Password length must be greater than 3 and less than 10'}
      ],
      repeatedPasswordRules: [
        {
          validate: (val) => {
            const { password } = this.$refs.form.model;

            console.log(password, val)

            return val === password;
          },
          message: 'Passwords must be equal'
        },
      ],
      argeeRules: [{ validate: (val) => !!val, message: 'Must agree with user agreement'}],
      validateForm: {
        username: '',
        password: '',
        repeatedPassword: '',
        lastName: '',
      }
    }
  },
  methods: {
    submit () {
      this.$refs.form.validate().then((result) => {
        if (result === false) {
          return;
        }

        const { password, username, lastName } = this.$refs.form.model;

        this.$store
          .dispatch('user/register', { password, username, lastName })
            .then(() => {
              this.$router.push('/login');
            })
          .catch(err => {
            console.log(err);
          })
      });
    },
    clear () {
      this.$refs.form.clear();
      this.validateForm = {
        username: '',
        password: '',
        isAgree: false
      };
    }
  }
};
</script>

<style scoped>
.mu-demo-form {
  width: 100%;
  max-width: 460px;
  margin: 0 auto;
}
</style>