<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Приемная кампания 2020</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button color="secondary" @click="ShowCreate">Зарегистрировать абитуриента</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col v-if="isCreateVisible">
                <mu-form style="width: 90%" :model="form" class="mu-demo-form" :label-position="labelPosition"
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
                                    <mu-option label="Серебряная" value="Серебряная"></mu-option>
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
                <mu-button color="secondary" @click="CreateEnrollee">Зарегистрировать</mu-button>
            </mu-col>
            <mu-col align="left">
                <p>Санкт-Петербургское государственное бюджетное профессиональное образовательное учреждение «Петровский колледж» (сокращенно - СПб ГБПОУ «Петровский колледж») , создано на основании приказа начальника Главного управления трудовых резервов при СНК СССР и Комитета по делам высшей школы при СНК СССР от 12.05.1944 №873/93/Т.

Учредителем колледжа является город Санкт-Петербург  в лице Комитет имущественных отношений (КИО) и Комитета по науке и высшей школе (КНВШ).
                    Учреждение находится в ведении  КНВШ, осуществляющего координацию деятельности Учреждения.</p><br>

                <p>Информация об учредителях</p>

                <ul><li>Наименование учредителя: Комитет по науке и высшей школе (КНВШ)</li>
                    <li>Руководитель учредителя образовательной организации: председатель КНВШ Максимов Андрей Станиславович</li>
                    <li>Адрес электронной почты: knvsh@gov.spb.ru</li>
                    <li>Адрес сайта учредителя: http://knvsh.gov.spb.ru/</li>
                    <li>Юридический адрес учредителя: 191144, Санкт-Петербург, Новгородская улица, дом 20</li>
                    <li>Контактные телефоны: +7(812) 576 7160</li>
                </ul>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: 'Home',
        data() {
            return {
                isCreateVisible: false,
                isCreateVisible: false,
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
            }
        },
        created() {
        },
        methods: {
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
                        this.$router.push({name: "Документы"})
                        alert("Абитуриент добавлен")
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Данные введены неверно")
                        }
                    }

                })
            }
        },
        components: {}
    }
</script>
