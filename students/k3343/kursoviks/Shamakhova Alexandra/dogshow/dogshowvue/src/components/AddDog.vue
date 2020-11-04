<template>
  <main>
    <v-col cols="8" class="mx-auto">
      <h2>Добавить питомца</h2>
      <form>
        <v-text-field v-model="dog_club" label="Клуб" required></v-text-field>
        <v-text-field v-model="dog_name" label="Кличка" required></v-text-field>
        <v-text-field v-model="dog_breed" label="Порода" required></v-text-field>
        <v-text-field v-model="dog_age" label="Возраст" required></v-text-field>
        <v-text-field v-model="dog_class" label="Классность" required></v-text-field>
        <v-text-field v-model="dog_document" label="Номер документа" required></v-text-field>
        <v-text-field v-model="dog_mother" label="Кличка матери" required></v-text-field>
        <v-text-field v-model="dog_father" label="Кличка отца" required></v-text-field>
        <v-text-field v-model="dog_vaccination" label="Дата последней прививки yyyy-mm-dd" required></v-text-field>
        <v-btn class="mr-4" @click="addDog" color="light-green darken-4" dark>Добавить собаку</v-btn>
      </form>
    </v-col>
  </main>
</template>

<script>
export default {
  name: 'AddDog',
  created () {
    if (sessionStorage.getItem('token') === null || sessionStorage.getItem('user') === null) {
      this.$router.push('/login')
    }
  },
  data () {
    return {
      dog_club: '',
      dog_name: '',
      dog_breed: '',
      dog_age: '',
      dog_class: '',
      dog_document: '',
      dog_mother: '',
      dog_father: '',
      dog_vaccination: '',
      dow_owner: '',
      check: ''
    }
  },
  mounted () {
    this.axios
      .get(`http://127.0.0.1:8000/api/human/all?user=${sessionStorage.getItem('user')}`)
      .then(response => { console.log(response); this.ifClient(response.data) })
      .catch(err => { console.error(err) })
  },
  methods: {
    ifClient (data) {
      this.dog_owner = data[0].id
    },
    addDog () {
      let dogdata = {
        dog_owner: this.dog_owner,
        dog_club: this.dog_club,
        dog_name: this.dog_name,
        dog_breed: this.dog_breed,
        dog_age: this.dog_age,
        dog_class: this.dog_class,
        dog_document: this.dog_document,
        dog_mother: this.dog_mother,
        dog_father: this.dog_father,
        dog_vaccination: this.dog_vaccination
      }

      this.axios
        .post(`http://127.0.0.1:8000/api/dogs/new`, dogdata)
        .then(response => { console.log(response); this.clearRequest() })
        .catch(err => { console.error(err) })
    },
    clearRequest () {
      this.dog_club = ''
      this.dog_name = ''
      this.dog_breed = ''
      this.dog_age = ''
      this.dog_class = ''
      this.dog_document = ''
      this.dog_mother = ''
      this.dog_father = ''
      this.dog_vaccination = ''
      this.dow_owner = ''
      this.$router.push('/partcab')
    }
  }
}
</script>

<style scoped>
h2 {
  font-weight: normal;
}
</style>
