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
              <p>Минимальный опыт работы: {{ vacancy_single.min_exp }}</p>
              <p>Зарплата: {{ vacancy_single.salary }}</p>
          </mu-card-text>
          <mu-card-text>
          </mu-card-text>
          <mu-card-actions>
            <mu-button color="success" v-on:click="createApplication(vacancy_single.id)">Подать заявку</mu-button>
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
            vac: '',
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
            this.vac = this.vacancy_single.id;
        },
        async createApplication(id) {
            console.log(id);
      const response = await fetch('http://127.0.0.1:8000/api/v1/application/create/', {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + sessionStorage.getItem("access")
        },
        method: "POST",
        body: JSON.stringify({vacancy_id: id})
      });
      // await this.$router.push({name: 'home'});
      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
    }
    }

}

</script>

<style>
   .block1 {
    margin-top: 5%; /* Отступ сверху */
   }
</style>