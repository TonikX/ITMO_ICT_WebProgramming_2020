<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Служащий</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table width="70%">
                    <tr>
                        <td>ID служащего</td>
                        <td>{{servant.id}}</td>
                    </tr>
                    <tr>
                        <td>ФИО</td>
                        <td>{{servant.fio}}

                <mu-form v-if="isUpdateVisible" style="width: 50%" :model="form_update" class="mu-demo-form" :label-position="labelPosition"
                         label-width="200">
                    <mu-form-item prop="input" label="ФИО">
                        <mu-text-field v-model="form_update.fio"></mu-text-field>
                    </mu-form-item>
                </mu-form>
                        </td>

                    </tr>
                </table>
<br>
            <mu-button color="primary" @click="ShowUpdate">Изменить данные</mu-button>
            <mu-button color="primary" @click="deleteServant">Уволить служащего</mu-button>
            <br>
                <br>
            <mu-button v-if="isUpdateVisible" color="black" @click="UpdateServant">Подтвердить изменения</mu-button>
        </mu-col>
        </mu-row>
    </mu-container>

</template>

<script>
    import $ from 'jquery'
    export default {
        name: "ServantSingle",
        props: ['id'],
        data() {
            return {
                servant: {},
                isUpdateVisible: false,
                form_update: {
                    fio: '',
                }
            }
        },
        created() {
            this.loadServant()
        },
        methods: {
            async loadServant() {
                this.servant = await fetch(
                    `http://127.0.0.1:8000/api/v1/servant/${this.id}/`
                ).then(response => response.json())
            },
            async deleteServant() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/servant/${this.id}/delete`, {
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
                await alert('Служащий уволен')
                await this.$router.push({name: "Служащие"})
            },
            ShowUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async UpdateServant() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/servant/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_update)
                });
                await alert('Данные о служащем успешно изменены')
                this.isUpdateVisible = !this.isUpdateVisible
                await this.loadServant()
            },
        }
    }
</script>

<style scoped>

</style>