<template>
    <v-row align="start" justify="center">
        <v-col cols="12" sm="8" md="6" lg="5" xl="4">
            <v-card>
                <v-toolbar color="primary" dark flat>
                    <v-toolbar-title>Команды</v-toolbar-title>
                    <v-spacer/>
                    <v-btn icon @click="createTeam()">
                        <v-icon>group_add</v-icon>
                    </v-btn>
                </v-toolbar>
                <v-data-table :headers="headers"
                              :items="teams"
                              :page.sync="page"
                              :items-per-page="itemsPerPage"
                              @page-count="pageCount = $event"
                              hide-default-footer
                              :loading="is_loading"
                              loading-text="Loading... Please wait">
                    <template v-slot:item.actions="{ item }">
                        <v-btn icon @click="editTeam(item)">
                            <v-icon>edit</v-icon>
                        </v-btn>
                        <v-btn icon @click="deleteTeam(item)">
                            <v-icon>delete</v-icon>
                        </v-btn>
                    </template>
                    <template v-slot:item.quest="{ item }">
                        <span v-if="item.quest !== null">
                            {{ item.quest.title }}
                            <v-tooltip top>
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn icon small @click="navigateToStatistic(item.quest.id)" v-bind="attrs" v-on="on">
                                    <v-icon small color="accent">
                                        open_in_new
                                    </v-icon>
                                </v-btn>
                            </template>
                            <span>Перейти к статистике</span>
                        </v-tooltip>
                        </span>
                        <span v-else>-</span>
                    </template>
                </v-data-table>
            </v-card>
            <v-dialog v-model="dialog" max-width="500px">
                <v-card>
                    <v-card-title>
                        <span class="headline">{{ formTitle }}</span>
                    </v-card-title>

                    <v-card-text>
                        <v-container>
                            <v-form v-model="valid">
                                <v-text-field v-model="password"
                                              :append-icon="showPassword ? 'visibility' : 'visibility_off'"
                                              :rules="rules"
                                              :type="showPassword ? 'text' : 'password'"
                                              :label="passwordTitle"
                                              required
                                              @click:append="showPassword = !showPassword"/>
                            </v-form>
                        </v-container>
                    </v-card-text>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                        <v-btn color="blue darken-1" text :disabled="!valid" @click="saveTeam()">Save</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <div class="text-center pt-2">
                <v-pagination v-model="page"
                              :length="pageCount"
                              prev-icon="keyboard_arrow_left"
                              next-icon="keyboard_arrow_right"
                              color="accent"
                              circle/>
            </div>
        </v-col>
    </v-row>
</template>

<script>
    import {httpClient} from "../api/httpClient";

    export default {
        data() {
            return {
                is_loading: false,
                valid: false,
                showPassword: false,
                editedTeamId: -1,
                editedTeamUsername: "",
                password: "",
                dialog: false,
                page: 1,
                pageCount: 0,
                itemsPerPage: 15,
                headers: [
                    {
                        text: 'Логин',
                        sortable: false,
                        value: 'username',
                    },
                    {
                        text: "Текущий квест",
                        sortable: false,
                        value: "quest",
                        align: 'center'
                    },
                    {
                        text: 'Действия',
                        sortable: false,
                        align: 'right',
                        value: 'actions'
                    }
                ],
                teams: [],
                rules: [
                    v => !!v || 'Это поле обязательно',
                    v => (v && v.length >= 8) || 'Пароль должен быть не менее 8 символов',
                ]
            }
        },
        computed: {
            formTitle() {
                return this.editedTeamId === -1 ? 'Создать команду' : `Изменить пароль для команды ${this.editedTeamUsername}`
            },
            passwordTitle() {
                return this.editedTeamId === -1 ? 'Пароль' : 'Новый пароль'
            }
        },
        methods: {
            createTeam() {
                this.dialog = true
            },
            editTeam(team) {
                this.editedTeamId = team.id;
                this.editedTeamUsername = team.username;
                this.dialog = true
            },
            deleteTeam(team) {
                if (confirm('Вы действительно хотите удалить команду ' + team.username + '?')) {
                    httpClient.delete(`/users/teams/${team.id}`)
                        .then((response) => {
                            console.log("delete team " + response);
                            this.loadTeams()
                        })
                        .catch((error) => {
                            console.log("delete team " + JSON.stringify(error))
                        })
                }
            },
            close() {
                this.dialog = false;
                this.$nextTick(() => {
                    this.editedTeamUsername = "";
                    this.editedTeamId = -1;
                    this.password = ""
                })
            },
            saveTeam() {
                if (this.editedTeamId > -1) {
                    httpClient.put(`/users/teams/${this.editedTeamId}`, {password: this.password})
                        .then((response) => {
                            console.log("update team " + response);
                            this.loadTeams()
                        })
                        .catch((error) => {
                            console.log("update team " + JSON.stringify(error))
                        })
                } else {
                    httpClient.post('/users/teams', {password: this.password})
                        .then((response) => {
                            console.log("create team " + response);
                            this.loadTeams()
                        })
                        .catch((error) => {
                            console.log("create team " + JSON.stringify(error))
                        })
                }
                this.close()
            },
            navigateToStatistic(id) {
                this.$router.push({name: "statistic", params: {id: id}})
            },
            loadTeams() {
                this.is_loading = true;
                httpClient.get('/users/teams')
                    .then((response) => {
                        this.is_loading = false;
                        this.teams = response.data
                        // console.log(response.data)
                    })
                    .catch((error) => {
                        this.is_loading = false;
                        console.log("load teams error" + JSON.stringify(error))
                    })
            }
        },
        mounted() {
            this.loadTeams()
        }
    }
</script>
