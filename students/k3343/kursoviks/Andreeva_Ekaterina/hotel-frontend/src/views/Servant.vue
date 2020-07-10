<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Служащие</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <ul>
                    <li v-for="servant in listServant" :key="servant.id">
                        <a @click="goTo(servant.id)">{{servant.fio}}</a>
                    <mu-radio v-if="isDeleteVisible" v-model="form_delete" :value="servant.id"
                                      label=""></mu-radio>

                    </li>
                </ul>
                <mu-button color="primary" @click="ShowCreate">Нанять сотрудника</mu-button>
                <mu-button color="primary" @click="ShowDelete">Уволить сотрудника</mu-button>
            </mu-col>
            <mu-col v-if="isCreateVisible">
                <mu-form style="width: 50%" :model="form" class="mu-demo-form" :label-position="labelPosition"
                         label-width="200">
                    <mu-form-item prop="input" label="ФИО">
                        <mu-text-field v-model="form.fio"></mu-text-field>
                    </mu-form-item>
                </mu-form>
                <mu-button @click="CreateServant">Нанять</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <br>
                <mu-button v-if="isDeleteVisible" color="black" @click="deleteServant">Подтвердить удаление</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Servant",
        props: ['id'],
        components: {},
        data() {
            return {
                listServant: [],
                isCreateVisible: false,
                isDeleteVisible: false,
                form: {
                    fio: '',
                },
                form_delete: {},
            }
        },
        created() {
            this.loadListServant()
        },
        methods: {
            async loadListServant() {
                this.listServant = await fetch(
                    `http://127.0.0.1:8000/api/v1/servant/`
                ).then(response => response.json())
            },
            goTo(id) {
                this.$router.push({name: 'Служащий', params: {id: id}})
            },
            ShowDelete() {
                this.isDeleteVisible = !this.isDeleteVisible
            },
            async deleteServant() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/servant/${this.form_delete}/delete`, {
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
                await alert('Сотрудник уволен')

                this.isDeleteVisible = !this.isDeleteVisible
                await this.loadListServant()
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            CreateServant() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/servant/create",
                    type: "POST",
                    data: {
                        fio: this.form.fio,
                    },
                    success: (response) => {
                        this.$router.push({name: "Служащие"})
                        alert("Сотрудник нанят")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListServant()
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