<template>
    <mu-container>
  <mu-row>
    <mu-col>
        <h1>Отчет по результатам приемной кампании</h1>
    </mu-col>
  </mu-row>
        <mu-row>
            <mu-col>
                <table>
                    <tr>
                        <th>Факультет</th>
                        <th>Специальность</th>
                        <th>Основа обучения</th>
                        <th>Абитуриент</th>
                        <th>Статус</th>
                    </tr>
                    <tr v-for="app in listApp" :key="app.id">
                        <td>{{app.faculty}}</td>
                        <td>{{app.specialty}}</td>
                        <td>{{app.form}}</td>
                        <td>{{app.enrollee}}</td>
                        <td>{{app.status}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
</mu-container>
</template>

<script>
    export default {
        name: "Report",
        props: ['id'],
        components: {},
        data() {
            return {
                listApp: []
            }
        },
        created() {
            this.loadListApp()
        },
        methods: {
            async loadListApp() {
                this.listApp = await fetch(
                    `http://127.0.0.1:8000/api/v1/application/`
                ).then(response => response.json())
            },

        }
    }
</script>

<style scoped>

</style>