<template>
    <div>
        <mu-header><h3>Изменить данные профиля</h3></mu-header>
        <mu-container>
        <mu-row>
            <mu-col span="10" lg="4" sm="5"/>
            <mu-col span="10" lg="4" sm="7">
                <mu-form align="left" style="text-align: left;">
                    <mu-form-item prop="input" label="Фамилия-Имя"><mu-text-field v-model="full_name"></mu-text-field></mu-form-item>
                    <mu-form-item prop="input" label="Электронная почта"><mu-text-field v-model="email"></mu-text-field></mu-form-item>
                    <mu-form-item prop="input" label="Телефон"><mu-text-field v-model="telephone"></mu-text-field></mu-form-item>
<!--                    <mu-form-item prop="input" label="Дата Рождения"><mu-text-field v-model="birth_date"></mu-text-field></mu-form-item>-->
                    <mu-form-item prop="input" label="Cтрана"><mu-text-field v-model="country"></mu-text-field></mu-form-item>
                    <mu-form-item prop="input" label="Биография"><mu-text-field v-model="biography"></mu-text-field></mu-form-item>
                </mu-form>
                    <mu-button @click="editProfile">Редактировать</mu-button>
            </mu-col>
        </mu-row>
        </mu-container>
    </div>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "AboutMe",
        created() {
            this.loadInfoPart()
        },
        data() {
            return {
                openScroll: true,
                id: '',
                full_name: '',
                email: '',
                telephone: '',
                birth_date: '',
                country: '',
                biography: '',
                style: '',
                is_teacher: ''
            }
        },
        methods: {
            loadInfoPart() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/user_info/",
                    type: "GET",
                    success: (response) => {
                        this.id = response.data.data.id;
                        this.full_name = response.data.data.full_name;
                        this.telephone = response.data.data.telephone;
                        this.email = response.data.data.email;
                        this.birth_date = response.data.data.birth_date;
                        this.country = response.data.data.country;
                        this.biography = response.data.data.biography;
                        this.style = response.data.data.style;
                        this.is_teacher = response.data.data.is_teacher
                    }
                })},
            editProfile() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/dance/profile_upd/' + this.id + '/',
                    type: "POST",
                    data: {
                        full_name: this.full_name,
                        telephone: this.telephone,
                        email: this.email,
                        country: this.country,
                        biography: this.biography
                    },
                    success: (response) => {
                        alert("Получилось, проверь")
                    },
                    error: (response) => {
                        alert("Не получилось")
                        console.log(this.id)
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
