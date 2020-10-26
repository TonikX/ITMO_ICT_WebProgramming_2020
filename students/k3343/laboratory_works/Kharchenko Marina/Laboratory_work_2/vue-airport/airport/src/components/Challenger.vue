<template>
  <main>
    <v-col cols="12">
      <form>
        <v-text-field v-model="last_name" label="Фамилия" required></v-text-field>
        <v-text-field v-model="first_name" label="Имя" required></v-text-field>
        <v-text-field v-model="middle_name" label="Отчество" required></v-text-field>
        <v-text-field v-model="age" label="Возраст" required></v-text-field>
        <v-text-field v-model="experience" label="Стаж работы" required></v-text-field>
        <v-text-field v-model="passport" label="Паспорт" required></v-text-field>
        <v-text-field v-model="position" label="Желаемая должность" required></v-text-field>
        <v-text-field v-model="email" label="Email" required></v-text-field>
        <v-select v-model="company" :items="companies" label="Компания" required></v-select>
        <v-btn class="mr-4" @click="submit">submit</v-btn>
        <v-btn @click="clear">clear</v-btn>
      </form>
    </v-col>
    <v-dialog
      v-model="success"
      max-width="290"
    >
      <v-card>
        <v-card-title class="headline">Спасибо!</v-card-title>

        <v-card-text>
          Как только мы рассмотрим Вашу заявку, мы свяжемся с Вами.
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
            @click="success = false"
          >
            Ок
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </main>
</template>
<script>
export default {
  name: 'Challenger',
  data () {
    return {
      url: 'http://127.0.0.1:8000/api/challengers',
      companies: [],
      companiesData: [],
      last_name: '',
      first_name: '',
      middle_name: '',
      age: '',
      experience: '',
      passport: '',
      position: '',
      email: '',
      company: '',
      success: false
    }
  },
  mounted () {
    this.axios
      .get('http://127.0.0.1:8000/api/companies')
      .then(response => { this.companiesData = response; this.updateCompanies() })
  },
  methods: {
    updateCompanies () {
      let data = this.companiesData.data.companies

      console.log(data)

      for (let company of data) {
        this.companies.push(company.name)
      }
    },
    submit () {
      this.axios
        .post(this.url, { challenger: {
          company: this.companies.indexOf(this.company) + 1,
          last_name: this.last_name,
          first_name: this.first_name,
          middle_name: this.middle_name,
          age: this.age,
          experience: this.experience,
          passport: this.passport,
          position: this.position,
          email: this.email
        }
        })
        .then(response => { this.clear(); this.success = true })
    },
    clear () {
      this.last_name = ''
      this.first_name = ''
      this.middle_name = ''
      this.age = ''
      this.experience = ''
      this.passport = ''
      this.position = ''
      this.email = ''
      this.company = ''
    }
  }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

</style>
