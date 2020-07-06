<template>
    <mu-container>
    <div id="app">
        <Navbar/>
        <router-view/>
    </div>
    <div class="block1">
        <mu-card style="width: 100%; max-width: 600px; margin: 0 auto;">
          <mu-card-header :title="vacancy_single.profession" :sub-title="vacancy_single.date_start">
          </mu-card-header>
          <mu-card-title title="Описание" :sub-title="vacancy_single.description"></mu-card-title>
          <mu-card-text>
              <p>Имя работодателя: {{ vacancy_single.employer }}</p>
              <p>Образование: {{ vacancy_single.education }}</p>
              <p>Необходимый разряд: {{ vacancy_single.rank }}</p>
              <p>Минимальный опыт работы: {{ vacancy_single.employer }}</p>
              <p>Зарплата: {{ vacancy_single.salary }}</p>
          </mu-card-text>
          <mu-card-text>
          </mu-card-text>
          <mu-card-actions>
            <mu-button color="success">Подать заявку</mu-button>
          </mu-card-actions>
        </mu-card>
    </div>
    </mu-container>
</template>

<script>
import Navbar from '../components/Navbar';

export default {
    name: "VacancySingle",
    props: ['id'],
    data() {
        return {
            vacancy_single: '',
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
            console.log('11ппцз');
            this.vacancy_single = await fetch(
                `${this.$store.getters.getServerUrl}/vacancy/detail/${this.id}`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form)
                }
            ).then(response => response.json());
            console.log('GGWP');
            console.log(this.vacancy_single);
        },
    },

}

</script>

<style>
   .block1 {
    margin-top: 5%; /* Отступ сверху */
   }
</style>