<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Заявка №{{application.id}}</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col align="center">
                <table>
                    <tr>
                        <td>ФИО соискателя</td>
                        <td>{{application.resume.applicant}}</td>
                    </tr>
                    <tr>
                        <td>Профессия по резюме</td>
                        <td>{{application.resume.profession}}</td>
                    </tr>
                    <tr>
                        <td>Профессия по вакансии</td>
                        <td>{{application.vacancy.profession}}</td>
                    </tr>
                    <tr>
                        <td>Разряд по резюме</td>
                        <td>{{application.resume.rank}}</td>
                    </tr>
                    <tr>
                        <td>Разряд по вакансии</td>
                        <td>{{application.vacancy.rank}}</td>
                    </tr>
                    <tr>
                        <td>Запрашиваемая зарплата</td>
                        <td>{{application.resume.salary}}</td>
                    </tr>
                    <tr>
                        <td>Зарплата по вакансии</td>
                        <td>{{application.vacancy.salary}}</td>
                    </tr>
                    <tr>
                        <td>Требуемое образование</td>
                        <td>{{application.vacancy.education}}</td>
                    </tr>
                    <tr>
                        <td>Требуемый опыт работы</td>
                        <td>{{application.vacancy.work_experience}}</td>
                    </tr>
                    <tr>
                        <td>Тип работы</td>
                        <td>{{application.vacancy.type}}</td>
                    </tr>
                    <tr>
                        <td>Дата размещения вакансии</td>
                        <td>{{application.vacancy.date}}</td>
                    </tr>
                    <tr>
                        <td>Статус вакансии</td>
                        <td>{{application.vacancy.status}}</td>
                    </tr>
                    <tr>
                        <td>Статус заявки</td>
                        <td>{{application.status}}</td>
                    </tr>
                    <tr>
                        <td>Дата подачи заявки</td>
                        <td>{{application.date}}</td>
                    </tr>
                </table>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "ApplicationSingle",
        props: ['id'],
        data() {
            return {
                application: {},
            }
        },
        created() {
            this.loadApplication()
        },
        methods: {
            async loadApplication() {
                this.application = await fetch(
                    `http://127.0.0.1:8000/api/v1/application/${this.id}/`
                ).then(response => response.json())
            },
        }
    }
</script>

<style scoped>

</style>