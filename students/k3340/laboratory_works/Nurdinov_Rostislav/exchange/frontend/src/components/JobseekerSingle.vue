<template>
    <mu-container>
    <div id="app">
        <Navbar/>
        <router-view/>
        <div class="block1">
            <h3 align="center">Соискатель</h3>
        <mu-card style="width: 100%; max-width: 600px; margin: 0 auto;">
          <mu-card-header :title="jobseeker_single" :sub-title="jobseeker_single">
          </mu-card-header>
          <mu-card-title title="Описание" :sub-title="jobseeker_single.surname"></mu-card-title>
          <mu-card-text>
              <p>Фамилия: {{ jobseeker_single.surname }}</p>
              <p>Имя: {{ jobseeker_single.name }}</p>
              <p>Отчество: {{ jobseeker_single.second_name }}</p>
              <p>Дата рождения: {{ jobseeker_single.date_birth }}</p>
              <p>Адресс: {{ jobseeker_single.address }}</p>
              <p>Последняя зарплата: {{ jobseeker_single.last_salary }}</p>
          </mu-card-text>
        </mu-card>
    </div>
    <h1> {{ resume_single.education }} </h1>
    <div class="block3">
            <h3 align="center">Резюме</h3>
        <mu-card style="width: 100%; max-width: 600px; margin: 0 auto;">
          <mu-card-text>
              <p>Образование: {{ resume_single.education }}</p>
              <p>Описание: {{ resume_single.description }}</p>
          </mu-card-text>
        </mu-card>
    </div>

    <div class="block2">
        <h3 align="center">Опыт работы</h3>
        <table class="table_exp">
        <br/>
        <tr>
          <th>Профессия</th>
          <th>Организация</th>
          <th>Позиция</th>
          <th>Date start</th>
          <th>Date end</th>
        </tr>
        <tr v-for="experience in experiences">
          <td>{{experience.profession}}</td>
          <td>{{experience.name_org}}</td>
          <td>{{experience.position}}</td>
          <td>{{experience.date_start}}</td>
          <td>{{experience.date_end}}</td>
        </tr>
            </table>
    </div>
    </div>
    </mu-container>
</template>

<script>
import Navbar from '../components/Navbar';

export default {
    name: "JobseekerSingle",
    props: ['id'],
    data() {
        return {
            jobseeker_single: '',
            experiences: '',
            resume_single: '',
        }
    },

    components: {
        Navbar,
    },
    created() {
            this.auth();
            this.loadJobseeker();
            this.loadResume();
            this.loadExperience();
    },
    methods: {
        async loadJobseeker() {
            console.log();
            this.jobseeker_single = await fetch(
                `${this.$store.getters.getServerUrl}/jobseeker/detail/${this.id}`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + sessionStorage.getItem("access"),
                    },
                }
            ).then(response => response.json());

        },
        async loadExperience() {
            this.experiences = await fetch(
                `${this.$store.getters.getServerUrl}/experience/list/2`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + sessionStorage.getItem("access"),
                    },
                }
            ).then(response => response.json());
            console.log(this.experiences);
        },
    async loadResume() {
            console.log('!!!!');
            this.resume_single = await fetch(
                `${this.$store.getters.getServerUrl}/resume/list/?jobseeker=${this.id}`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + sessionStorage.getItem("access"),
                    },
                });
            console.log(this.resume_single);
        },
      auth() {
        if (sessionStorage.getItem("auth_token")) {
          console.log(sessionStorage)
        } else {
            console.log('NOOOO')
        }
    },
    },

}

</script>

<style>
   .block1 {
        margin-top: 5%; /* Отступ сверху */
   }
   .block2 {
        margin-top: 8%;
   }
    .table_exp {
font-size: 14px;
border-collapse: collapse;
text-align: center;
}
.table_exp th, td:first-child {
background: #AFCDE7;
color: white;
padding: 10px 20px;
}
.table_exp th, td {
border-style: solid;
border-width: 0 1px 1px 0;
border-color: white;
}
.table_exp td {
background: #D8E6F3;
}
.table_exp th:first-child, td:first-child {
text-align: left;
}

</style>