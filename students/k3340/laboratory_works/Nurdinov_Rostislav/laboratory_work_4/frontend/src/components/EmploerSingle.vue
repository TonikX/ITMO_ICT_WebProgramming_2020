<template>
    <mu-container>
    <div id="app">
        <Navbar/>
        <router-view/>
    </div>
    <div class="block1">
        <mu-card style="width: 100%; max-width: 600px; margin: 0 auto;">
<!--          <mu-card-header :title="vacancy_single.profession" :sub-title="vacancy_single.date_start">-->
<!--          </mu-card-header>-->
          <mu-card-title title="Описание" :sub-title="employer_single.firm"></mu-card-title>
          <mu-card-text>
              <p>Имя работодателя: {{ employer_single.surname }}</p>
              <p>Образование: {{ employer_single.name }}</p>
              <p>Необходимый разряд: {{ employer_single.second_name }}</p>
              <p>Минимальный опыт работы: {{ employer_single.email }}</p>
              <p>Зарплата: {{ employer_single.number }}</p>
          </mu-card-text>
        </mu-card>
    </div>
    </mu-container>
</template>

<script>
import Navbar from '../components/Navbar';

export default {
    name: "EmployerSingle",
    props: ['id'],
    data() {
        return {
            employer_single: '',
        }
    },
    components: {
        Navbar,
    },
    created() {
            this.loadVacancy()
    },
    methods: {
        async loadVacancy() {
            this.employer_single = await fetch(
                `${this.$store.getters.getServerUrl}/employer/detail/${this.id}`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form)
                }
            ).then(response => response.json());
            console.log('GGWP');
            console.log(this.employer_single);
        },
    },

}

</script>

<style>
   .block1 {
    margin-top: 5%; /* Отступ сверху */
   }
</style>