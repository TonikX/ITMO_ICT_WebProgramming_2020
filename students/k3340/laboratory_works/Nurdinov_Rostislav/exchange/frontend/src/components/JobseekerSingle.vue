<template>
    <mu-container>
    <div id="app">
        <Navbar/>
        <router-view/>
        <div class="block1">
        <mu-card style="width: 100%; max-width: 600px; margin: 0 auto;">
          <mu-card-header :title="jobseeker_single" :sub-title="jobseeker_single">
          </mu-card-header>
          <mu-card-title title="Описание" :sub-title="jobseeker_single.surname"></mu-card-title>
          <mu-card-text>
<!--              <p>Имя работодателя: {{ vacancy_single.employer }}</p>-->
<!--              <p>Образование: {{ vacancy_single.education }}</p>-->
<!--              <p>Необходимый разряд: {{ vacancy_single.rank }}</p>-->
<!--              <p>Минимальный опыт работы: {{ vacancy_single.employer }}</p>-->
<!--              <p>Зарплата: {{ vacancy_single.salary }}</p>-->
          </mu-card-text>
          <mu-card-text>
          </mu-card-text>
          <mu-card-actions>
            <mu-button color="success">Подать заявку</mu-button>
          </mu-card-actions>
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
<!--          <th></th>-->
<!--          <th></th>-->
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
        }
    },
    components: {
        Navbar,
    },
    created() {
            this.loadJobseeker();
            this.loadExperience();
    },
    methods: {
        async loadJobseeker() {
            console.log('11ппцз');
            this.jobseeker_single = await fetch(
                `${this.$store.getters.getServerUrl}/jobseeker/detail/${this.id}`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form)
                }
            ).then(response => response.json());
            console.log('GGWP');
            console.log(this.jobseeker_single);
        },
        async loadExperience() {
            console.log('???');
            // console.log(${this.id});
            this.experiences = await fetch(
                `${this.$store.getters.getServerUrl}/experience/list/${this.id}`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form)
                }
            ).then(response => response.json());
            console.log('!!!!');
            console.log(this.experiences);
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