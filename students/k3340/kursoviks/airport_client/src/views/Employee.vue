<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Сотрудники аэропорта</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <ul>
                    <li @click="showCrewCommander"> <a>Командиры экипажа</a></li>
                    <table v-if="isCrewCommanderVisible" class="paleBlueRows" width="70%">
                        <tr>
                            <th class="is-right">Фамилия</th>
                            <th class="is-right">Имя</th>
                            <th class="is-right">Отчество</th>
                        </tr>
                        <tr v-for="crewcommander in listCrewCommander" :key="crewcommander.id">
                            <td>{{crewcommander.last_name}}</td>
                            <td>{{crewcommander.first_name}}</td>
                            <td>{{crewcommander.second_name}}</td>
                            <td>
                                <mu-button color="primary" @click="goToCrewCommander(crewcommander.id)"> Подробнее
                                </mu-button>
                            </td>
                        </tr>
                    </table>
                    <br>
                    <mu-button @click="showCrewCommanderCreate">Добавить командира
                        экипажа
                    </mu-button>
                    <mu-container v-if="isCrewCommanderCreateVisible">
                        <mu-form :model="form_crewcommander" class="mu-demo-form" :label-position="labelPosition"
                                 label-width="200">
                            <mu-form-item prop="input" label="Фамилия">
                                <mu-text-field v-model="form_crewcommander.last_name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Имя">
                                <mu-text-field v-model="form_crewcommander.first_name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Отчество">
                                <mu-text-field v-model="form_crewcommander.second_name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Дата рождения гггг-мм-дд">
                                <mu-text-field v-model="form_crewcommander.date_of_birth"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Образование">
                                <mu-text-field v-model="form_crewcommander.education"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Опыт работы в годах">
                                <mu-text-field v-model="form_crewcommander.work_experience"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="radio" label="Допуск на рейс">
                                <mu-radio v-model="form_crewcommander.flight_admission" value="True"
                                          label="Есть"></mu-radio>
                                <mu-radio v-model="form_crewcommander.flight_admission" value="False"
                                          label="Нет"></mu-radio>
                            </mu-form-item>
                        </mu-form>
                        <mu-button color="primary" @click="addCrewCommander">Добавить</mu-button>
                    </mu-container>
                    <br>
                    <li @click="showSecondPilot"><a>Вторые пилоты</a></li>
                    <table v-if="isSecondPilotVisible" class="paleBlueRows" width="70%">
                        <tr>
                            <th class="is-right">Фамилия</th>
                            <th class="is-right">Имя</th>
                            <th class="is-right">Отчество</th>
                        </tr>
                        <tr v-for="secondpilot in listSecondPilot" :key="secondpilot.id">
                            <td>{{secondpilot.last_name}}</td>
                            <td>{{secondpilot.first_name}}</td>
                            <td>{{secondpilot.second_name}}</td>
                            <td>
                                <mu-button color="primary" @click="goToSecondPilot(secondpilot.id)"> Подробнее
                                </mu-button>
                            </td>
                        </tr>
                    </table>
                    <br>
                    <mu-button @click="showSecondPilotCreate">Добавить второго пилота
                    </mu-button>
                    <mu-container v-if="isSecondPilotCreateVisible">

                        <mu-form :model="form_secondpilot" class="mu-demo-form" :label-position="labelPosition"
                                 label-width="200">
                            <mu-form-item prop="input" label="Фамилия">
                                <mu-text-field v-model="form_secondpilot.last_name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Имя">
                                <mu-text-field v-model="form_secondpilot.first_name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Отчество">
                                <mu-text-field v-model="form_secondpilot.second_name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Дата рождения гггг-мм-дд">
                                <mu-text-field v-model="form_secondpilot.date_of_birth"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Образование">
                                <mu-text-field v-model="form_secondpilot.education"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Опыт работы в годах">
                                <mu-text-field v-model="form_secondpilot.work_experience"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="radio" label="Допуск на рейс">
                                <mu-radio v-model="form_secondpilot.flight_admission" value="True"
                                          label="Есть"></mu-radio>
                                <mu-radio v-model="form_secondpilot.flight_admission" value="False"
                                          label="Нет"></mu-radio>
                            </mu-form-item>
                        </mu-form>
                        <mu-button color="primary" @click="addSecondPilot">Добавить</mu-button>
                    </mu-container>
                    <li @click="showNavigator"><a>Штурманы</a></li>
                    <table v-if="isNavigatorVisible" class="paleBlueRows" width="70%">
                        <tr>
                            <th class="is-right">Фамилия</th>
                            <th class="is-right">Имя</th>
                            <th class="is-right">Отчество</th>
                        </tr>
                        <tr v-for="navigator in listNavigator" :key="navigator.id">
                            <td>{{navigator.last_name}}</td>
                            <td>{{navigator.first_name}}</td>
                            <td>{{navigator.second_name}}</td>
                            <td>
                                <mu-button color="primary" @click="goToNavigator(navigator.id)"> Подробнее</mu-button>
                            </td>
                        </tr>
                    </table>
                    <br>
                    <mu-button @click="showNavigatorCreate">Добавить штурмана
                    </mu-button>
                    <mu-container v-if="isNavigatorCreateVisible">
                        <mu-form :model="form_navigator" class="mu-demo-form" :label-position="labelPosition"
                                 label-width="200">
                            <mu-form-item prop="input" label="Фамилия">
                                <mu-text-field v-model="form_navigator.last_name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Имя">
                                <mu-text-field v-model="form_navigator.first_name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Отчество">
                                <mu-text-field v-model="form_navigator.second_name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Дата рождения гггг-мм-дд">
                                <mu-text-field v-model="form_navigator.date_of_birth"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Образование">
                                <mu-text-field v-model="form_navigator.education"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Опыт работы в годах">
                                <mu-text-field v-model="form_navigator.work_experience"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="radio" label="Допуск на рейс">
                                <mu-radio v-model="form_navigator.flight_admission" value="True"
                                          label="Есть"></mu-radio>
                                <mu-radio v-model="form_navigator.flight_admission" value="False"
                                          label="Нет"></mu-radio>
                            </mu-form-item>
                        </mu-form>
                        <mu-button color="primary" @click="addNavigator">Добавить</mu-button>
                    </mu-container>
                    <li @click="showSteward"><a>Бортпроводники</a></li>
                    <table v-if="isStewardVisible" class="paleBlueRows" width="70%">
                        <tr>
                            <th class="is-right">Фамилия</th>
                            <th class="is-right">Имя</th>
                            <th class="is-right">Отчество</th>
                        </tr>
                        <tr v-for="steward in listSteward" :key="steward.id">
                            <td>{{steward.last_name}}</td>
                            <td>{{steward.first_name}}</td>
                            <td>{{steward.second_name}}</td>
                            <td>
                                <mu-button color="primary" @click="goToSteward(steward.id)"> Подробнее</mu-button>
                            </td>
                        </tr>
                    </table>
                    <br>
                    <mu-button @click="showStewardCreate">Добавить бортпроводника
                    </mu-button>
                    <mu-container v-if="isStewardCreateVisible">
                        <mu-form :model="form_steward" class="mu-demo-form" :label-position="labelPosition"
                                 label-width="200">
                            <mu-form-item prop="input" label="Фамилия">
                                <mu-text-field v-model="form_steward.last_name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Имя">
                                <mu-text-field v-model="form_steward.first_name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Отчество">
                                <mu-text-field v-model="form_steward.second_name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Дата рождения гггг-мм-дд">
                                <mu-text-field v-model="form_steward.date_of_birth"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Образование">
                                <mu-text-field v-model="form_steward.education"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Опыт работы в годах">
                                <mu-text-field v-model="form_steward.work_experience"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="radio" label="Допуск на рейс">
                                <mu-radio v-model="form_steward.flight_admission" value="True"
                                          label="Есть"></mu-radio>
                                <mu-radio v-model="form_steward.flight_admission" value="False"
                                          label="Нет"></mu-radio>
                            </mu-form-item>
                            <mu-form-item prop="select" label="Экипаж">
                                <mu-select v-model="form_steward.crew">
                                    <mu-option v-for="crew in listCrew" :key="crew.id"
                                               :label="crew.id"
                                               :value="crew.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                                <mu-form-item prop="select" label="Экипаж">
                                <mu-select v-model="form_steward.crew">
                                    <mu-option v-for="crew in listCrew" :key="crew.id"
                                               :label="crew.id"
                                               :value="crew.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                        </mu-form>
                        <mu-button color="primary" @click="addSteward">Добавить</mu-button>
                    </mu-container>
                </ul>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Employee",
        props: ['id'],
        components: {},
        data() {
            return {
                isCrewCommanderVisible: false,
                isSecondPilotVisible: false,
                isNavigatorVisible: false,
                isStewardVisible: false,
                isCrewCommanderCreateVisible: false,
                isSecondPilotCreateVisible: false,
                isNavigatorCreateVisible: false,
                isStewardCreateVisible: false,
                listCrewCommander: [],
                listSecondPilot: [],
                listNavigator: [],
                listSteward: [],
                form_crewcommander: {
                    first_name: '',
                    last_name: '',
                    second_name: '',
                    date_of_birth: '',
                    education: '',
                    work_experience: '',
                    flight_admission: '',
                }, form_secondpilot: {
                    first_name: '',
                    last_name: '',
                    second_name: '',
                    date_of_birth: '',
                    education: '',
                    work_experience: '',
                    flight_admission: '',
                },
                form_navigator: {
                    first_name: '',
                    last_name: '',
                    second_name: '',
                    date_of_birth: '',
                    education: '',
                    work_experience: '',
                    flight_admission: '',
                },
                form_steward: {
                    first_name: '',
                    last_name: '',
                    second_name: '',
                    date_of_birth: '',
                    education: '',
                    work_experience: '',
                    flight_admission: '',
                    crew: '',
                },
                listCrew: '',
            }
        },
        created() {
            this.loadListCrewCommander()
            this.loadListSecondPilot()
            this.loadListNavigator()
            this.loadListSteward()
            this.loadListCrew()
        },
        methods: {
            async loadListCrew() {
                this.listCrew = await fetch(
                    `http://127.0.0.1:8000/api/v1/crew/`
                ).then(response => response.json())
            },
            async loadListCrewCommander() {
                this.listCrewCommander = await fetch(
                    `http://127.0.0.1:8000/api/v1/crewcommander/`
                ).then(response => response.json())
            },
            async loadListSecondPilot() {
                this.listSecondPilot = await fetch(
                    `http://127.0.0.1:8000/api/v1/secondpilot/`
                ).then(response => response.json())
            },
            async loadListNavigator() {
                this.listNavigator = await fetch(
                    `http://127.0.0.1:8000/api/v1/navigator`
                ).then(response => response.json())
            },
            async loadListSteward() {
                this.listSteward = await fetch(
                    `http://127.0.0.1:8000/api/v1/steward`
                ).then(response => response.json())
            },
            showCrewCommander() {
                this.isCrewCommanderVisible = !this.isCrewCommanderVisible
            },
            showSecondPilot() {
                this.isSecondPilotVisible = !this.isSecondPilotVisible
            },
            showNavigator() {
                this.isNavigatorVisible = !this.isNavigatorVisible
            },
            showSteward() {
                this.isStewardVisible = !this.isStewardVisible
            },
            showCrewCommanderCreate() {
                this.isCrewCommanderCreateVisible = !this.isCrewCommanderCreateVisible
            },
            showSecondPilotCreate() {
                this.isSecondPilotCreateVisible = !this.isSecondPilotCreateVisible
            },
            showNavigatorCreate() {
                this.isNavigatorCreateVisible = !this.isNavigatorCreateVisible
            },
            showStewardCreate() {
                this.isStewardCreateVisible = !this.isStewardCreateVisible
            },
            goToCrewCommander(id) {
                this.$router.push({name: 'Командир экипажа', params: {id: id}})
            },
            goToSecondPilot(id) {
                this.$router.push({name: 'Второй пилот', params: {id: id}})
            },
            goToNavigator(id) {
                this.$router.push({name: 'Штурман', params: {id: id}})
            },
            goToSteward(id) {
                this.$router.push({name: 'Бортпроводник', params: {id: id}})
            },
            addCrewCommander() {
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/crewcommander/create",
                        type: "POST",
                        data: {
                            last_name: this.form_crewcommander.last_name,
                            first_name: this.form_crewcommander.first_name,
                            second_name: this.form_crewcommander.second_name,
                            date_of_birth: this.form_crewcommander.date_of_birth,
                            education: this.form_crewcommander.education,
                            work_experience: this.form_crewcommander.work_experience,
                            flight_admission: this.form_crewcommander.flight_admission,
                        },
                        success: (response) => {
                            this.$router.push({name: "Сотрудники"})
                            alert("Вы успешно добавили нового командира экипажа")
                            this.isCrewCommanderCreateVisible = !this.isCrewCommanderCreateVisible
                            this.loadListCrewCommander()
                        },
                        error: (response) => {
                            if (response.status === 400) {
                                alert("Проверьте корректность введенных данных")
                            }
                        }
                    }
                )
            },
            addSecondPilot() {
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/secondpilot/create",
                        type: "POST",
                        data: {
                            last_name: this.form_secondpilot.last_name,
                            first_name: this.form_secondpilot.first_name,
                            second_name: this.form_secondpilot.second_name,
                            date_of_birth: this.form_secondpilot.date_of_birth,
                            education: this.form_secondpilot.education,
                            work_experience: this.form_secondpilot.work_experience,
                            flight_admission: this.form_secondpilot.flight_admission,
                        },
                        success: (response) => {
                            this.$router.push({name: "Сотрудники"})
                            alert("Вы успешно добавили нового второго пилота")
                            this.isSecondPilotCreateVisible = !this.isSecondPilotCreateVisible
                            this.loadListSecondPilot()
                        },
                        error: (response) => {
                            if (response.status === 400) {
                                alert("Проверьте корректность введенных данных")
                            }
                        }
                    }
                )
            },
            addNavigator() {
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/navigator/create",
                        type: "POST",
                        data: {
                            last_name: this.form_navigator.last_name,
                            first_name: this.form_navigator.first_name,
                            second_name: this.form_navigator.second_name,
                            date_of_birth: this.form_navigator.date_of_birth,
                            education: this.form_navigator.education,
                            work_experience: this.form_navigator.work_experience,
                            flight_admission: this.form_navigator.flight_admission,
                        },
                        success: (response) => {
                            this.$router.push({name: "Сотрудники"})
                            alert("Вы успешно добавили нового штурмана")
                            this.isNavigatorCreateVisible = !this.isNavigatorCreateVisible
                            this.loadListNavigator()
                        },
                        error: (response) => {
                            if (response.status === 400) {
                                alert("Проверьте корректность введенных данных")
                            }
                        }
                    }
                )
            },
            addSteward() {
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/steward/create",
                        type: "POST",
                        data: {
                            last_name: this.form_steward.last_name,
                            first_name: this.form_steward.first_name,
                            second_name: this.form_steward.second_name,
                            date_of_birth: this.form_steward.date_of_birth,
                            education: this.form_steward.education,
                            work_experience: this.form_steward.work_experience,
                            flight_admission: this.form_steward.flight_admission,
                            crew: this.form_steward.crew
                        },
                        success: (response) => {
                            this.$router.push({name: "Сотрудники"})
                            alert("Вы успешно добавили нового бортпроводника")
                            this.isStewardCreateVisible = !this.isStewardCreateVisible
                            this.loadListSteward()
                        },
                        error: (response) => {
                            if (response.status === 400) {
                                alert("Проверьте корректность введенных данных")
                            }
                        }
                    }
                )
            },

        }
    }
</script>

<style scoped>

</style>