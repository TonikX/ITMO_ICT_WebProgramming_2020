<template>
<mu-container>
  <mu-form :model="jobseek" class="mu-demo-form" :label-position="value" label-width="100">
    <mu-form-item prop="name" label="Имя">
      <mu-text-field v-model="jobseek.name"></mu-text-field>
    </mu-form-item>
    <mu-form-item prop="surname" label="Фамилия">
      <mu-text-field v-model="jobseek.surname"></mu-text-field>
    </mu-form-item>
    <mu-form-item prop="second_name" label="Отчество">
      <mu-text-field v-model="jobseek.second_name"></mu-text-field>
    </mu-form-item>
    <mu-form-item prop="address" label="Адрес">
      <mu-text-field v-model="jobseek.address"></mu-text-field>
    </mu-form-item>
    <mu-form-item prop="last_salary" label="Последняя зарплата">
      <mu-text-field v-model="jobseek.last_salary"></mu-text-field>
    </mu-form-item>
    <mu-form-item prop="date_birth" label="Дата рождения">
      <mu-text-field v-model="jobseek.date_birth"></mu-text-field>
    </mu-form-item>
    <mu-form-item prop="status_work" label="Работаете?">
      <mu-switch v-model="jobseek.status_work"></mu-switch>
    </mu-form-item>
    <mu-form-item prop="education" label="Select">
      <mu-select v-model="resume.education">
        <mu-option v-for="option,index in options" :key="index" :label="option" :value="index"></mu-option>
      </mu-select>
    </mu-form-item>
    <mu-form-item prop="description" label="Описание">
      <mu-text-field multi-line :rows="3" :rows-max="6" v-model="resume.description"></mu-text-field>
    </mu-form-item>
  </mu-form>
  <h2 align="center"><mu-button v-on:click="createJobseeker" color="success">Зарегистрироваться</mu-button></h2>
</mu-container>
</template>

<script>
export default {
  name: 'ResumeReg',
  data () {
    return {
      value: 'right',
      options: {
        '1': 'Среднее', '2': 'Профессиональное', '3': 'Высшее (бакалавр)', '4': 'Высшее (магистратура)',
      },
      labelPosition: 'top',
      jobseek: {
        name: '',
        surname: '',
        second_name: '',
        address: '',
        last_salary: '',
        date_birth: '',
        radio: '',
        status_work: false,
      },
      resume: {
        education: '',
        description: '',
      }
    }
  },
  created() {
    auth();
  },
  methods : {
    async createJobseeker() {
      const response = await fetch('http://127.0.0.1:8000/api/v1/jobseeker/create/', {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + sessionStorage.getItem("access"),
        },
        method: "POST",
        body: JSON.stringify(this.jobseek)
      });
      this.createResume();
      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      await this.$router.push({name: 'home'});
      }
    },
    async createResume() {
      const response = await fetch('http://127.0.0.1:8000/api/v1/resume/create/', {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + sessionStorage.getItem("access")
        },
        method: "POST",
        body: JSON.stringify(this.resume)
      });
      await this.$router.push({name: 'home'});
      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
    },
    auth() {
        if (sessionStorage.getItem("auth_token")) {
          console.log(sessionStorage);
        } else {
            console.log('NOOOO');
        }
  },
  }
};
</script>
<style>
.mu-demo-form {
  width: 100%;
  max-width: 460px;
}
</style>