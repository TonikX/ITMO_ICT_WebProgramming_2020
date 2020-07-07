<template>
    <div>
        <mu-container>
            <mu-dialog title="Редактировать информацию об участнике" width="360" scrollable :open.sync="openScroll">
                <mu-form>
                    <mu-form-item prop="input" label="Имя"><mu-text-field v-model="name"></mu-text-field></mu-form-item>
                    <mu-form-item prop="input" label="Электронная почта"><mu-text-field v-model="email"></mu-text-field></mu-form-item>
                    <mu-form-item prop="input" label="Телефон"><mu-text-field v-model="telephone"></mu-text-field></mu-form-item>
                </mu-form>
                    <mu-button @click="editPers">Редактировать</mu-button>
            </mu-dialog>
        </mu-container>
    </div>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "EditPart",
        data() {
            return {
                openScroll: true,
                name: '',
                email: '',
                telephone: '',
            }
        },
        created() {
            this.loadInfoPart()
        },
        methods: {
            loadInfoPart() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/one_part/",
                    type: "GET",
                    success: (response) => {
                        this.name = response.data.data.full_name;
                        this.telephone = response.data.data.telephone;
                        this.email = response.data.data.email
                        this.birth_date = response.data.data.birth_date
                        this.country = response.data.data.country
                        this.biography = response.data.data.biography
                    }
                })
            },
            editPers() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/dance/wsh_upd/' + this.id +'/',
                    type: "POST",
                    data: {
                        fullname: this.name,
                        email: this.email,
                        telephone: this.telephone,
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
