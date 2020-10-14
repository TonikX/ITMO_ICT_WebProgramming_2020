<template>
    <mu-container>
        <mu-row align="left">
            <mu-col>
                <h1>Регистрация соискателя на бирже труда</h1>
                <p>Заполните все поля</p>
            </mu-col>
        </mu-row>
      <mu-row>
        <mu-col>
          <mu-form label-position="left">
            <mu-form-item prop="input" label="ФИО">
                        <mu-text-field v-model="form.fio"></mu-text-field>
                    </mu-form-item>
            <mu-form-item prop="input" label="Возраст">
                        <mu-text-field v-model="form.age"></mu-text-field>
                    </mu-form-item>
            <mu-form-item prop="input" label="Адрес">
                        <mu-text-field v-model="form.address"></mu-text-field>
                    </mu-form-item>
                    <mu-select v-model="form.education" label="Образование">
                        <mu-option v-for="education in listEducation" :key="education.id" :label="education.name"
                                   :value="education.id"></mu-option>
                    </mu-select>
            <mu-form-item prop="input" label="Трудовой стаж в годах">
                        <mu-text-field v-model="form.work_experience"></mu-text-field>
                    </mu-form-item>
          </mu-form>
        </mu-col>
      </mu-row>
      <mu-row>
        <mu-col>
          <mu-button @click="CreateApplicant">Зарегистрировать</mu-button>
        </mu-col>
      </mu-row>
    </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "ApplicantRegistration",
        props: ['id'],
        components: {},
        data() {
            return {
                listEducation: [],
              form: {
                fio: '',
                age: '',
                address: '',
                work_experience: '',
                education: '',
              },
            }
        },
        created() {
            this.loadListEducation()
        },
        methods: {
            async loadListEducation() {
                this.listEducation = await fetch(
                    `http://127.0.0.1:8000/api/v1/education/`
                ).then(response => response.json())
            },
            CreateApplicant() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/applicant/create",
                    type: "POST",
                    data: {
                        fio: this.form.fio,
                        address: this.form.address,
                        age: this.form.age,
                        work_experience: this.form.work_experience,
                        education: this.form.education,
                    },
                    success: (response) => {
                        this.$router.push({name: "Соискатели"})
                        alert("Соискатель успешно зарегистрирован")
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Данные введены неверно")
                        }
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>