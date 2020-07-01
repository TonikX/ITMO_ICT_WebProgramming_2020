<template>
    <mu-container>
  <mu-row>
    <mu-col>
        <h1>Список всех абитуриентов</h1>
    </mu-col>
  </mu-row>
        <mu-row align="center">
            <mu-col>
                <ul v-for="enrollee in listEnrollee" :key="enrollee.id">
                    <li><a @click="goTo(enrollee.id)">{{enrollee.fio}}</a></li>
                    <mu-radio v-if="isDeleteVisible" v-model="form_delete" :value="enrollee.id"
                                      label="Удалить"></mu-radio>
                </ul>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button @click="ShowCreate">Абитуриент принес документы</mu-button>
                <mu-button @click="showDelete">Абитуриент забрал документы</mu-button>
            </mu-col>
        </mu-row>
                <mu-row v-if="isCreateVisible">
            <mu-col>
                <mu-form style="width: 50%" :model="form" class="mu-demo-form" :label-position="labelPosition"
                                 label-width="200">
                            <mu-form-item prop="input" label="ФИО">
                                <mu-text-field v-model="form.fio"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Оконченное учебное заведение">
                                <mu-text-field v-model="form.school"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Дата окончания учебного заведения">
                                <mu-text-field v-model="form.finish_school"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="select" label="Медаль">
                                <mu-select v-model="form.medal">
                                    <mu-option label="Золотая" value="Золотая"></mu-option>
                                    <mu-option label="Серебрна" value="Серебряная"></mu-option>
                                    <mu-option label="Отсутствует" value="Отсутствует"></mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Номер паспорта">
                                <mu-text-field v-model="form.passport_number"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Адрес">
                                <mu-text-field v-model="form.address"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="select" label="Льготы">
                                <mu-select v-model="form.privileges">
                                    <mu-option label="Инвалид" value="Инвалид"></mu-option>
                                    <mu-option label="Сирота" value="Сирота"></mu-option>
                                    <mu-option label="Нет" value="Нет"></mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="radio" label="Целевой прием">
                                <mu-radio v-model="form.target" value="True"
                                          label="Да"></mu-radio>
                                <mu-radio v-model="form.target" value="False"
                                          label="Нет"></mu-radio>
                            </mu-form-item>
                </mu-form>
                <br>
                <mu-button color="secondary" @click="CreateEnrollee">Зарегистрировать</mu-button>
            </mu-col>
        </mu-row>
        <mu-row v-if="isDeleteVisible">
            <mu-col>
                <br>
                <mu-button color="error" @click="deleteEnrollee">Подтвердить удаление</mu-button>
            </mu-col>
        </mu-row>
</mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "Enrollee",
        props: ['id'],
        components: {},
        data() {
            return {
                listEnrollee: [],
                isDeleteVisible: false,
                isCreateVisible: false,
                form: {
                    fio: '',
                    school: '',
                    finish_school: '',
                    medal: '',
                    passport_number: '',
                    address: '',
                    privileges: '',
                    target: '',
                },
                form_delete:{},
            }
        },
        created() {
            this.loadListEnrollee()
        },
        methods: {
            async loadListEnrollee() {
                this.listEnrollee = await fetch(
                    `http://127.0.0.1:8000/api/v1/enrollee/`
                ).then(response => response.json())
            },
            goTo(id) {
                this.$router.push({name: 'Абитуриент', params: {id: id}})
            },
            showDelete() {
                this.isDeleteVisible = !this.isDeleteVisible
            },
            async deleteEnrollee() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/enrollee/${this.form_delete}/delete`, {
                        method: 'DELETE',
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        }
                    }
                );
                if (response.status !== 204) {
                    alert(JSON.stringify(await response.json(), null, 2));
                }
                await alert('Абитуриент удален')

                this.isDeleteVisible = !this.isDeleteVisible
                await this.loadListEnrollee()
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            CreateEnrollee() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/enrollee/create",
                    type: "POST",
                    data: {
                        fio: this.form.fio,
                        school: this.form.school,
                        finish_school: this.form.finish_school,
                        medal: this.form.medal,
                        passport_number: this.form.passport_number,
                        address: this.form.address,
                        privileges: this.form.privileges,
                        target: this.form.target,
                    },
                    success: (response) => {
                        this.$router.push({name: "Абитуриенты"})
                        alert("Абитуриент добавлен")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListEnrollee()
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