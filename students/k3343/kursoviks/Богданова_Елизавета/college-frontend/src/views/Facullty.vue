<template>
    <mu-container>
  <mu-row>
    <mu-col>
        <h1>Факультеты и специальности</h1>
    </mu-col>
  </mu-row >
        <mu-row align="left">
            <mu-col>
        <ul v-for="faculty in listFaculty" :key="faculty.id">
            <li>{{faculty.name}}
            <ul v-for="specialty in faculty.specialties" :key="specialty.id">
                <li> {{specialty.name}}</li>
                <table>
                    <th colspan="2">
                        Приемная кампания 2020
                    </th>
                    <tr>
                        <td>Количество бюджетных мест</td>
                        <td>{{specialty.budget}}</td>
                    </tr>
                    <tr>
                        <td>Количество контрактных мест</td>
                        <td>{{specialty.contract}}</td>
                    </tr>
                </table>
            </ul></li>
        </ul>
            </mu-col>
        </mu-row>
</mu-container>
</template>

<script>
    export default {
        name: "Facullty",
        props: ['id'],
        components: {},
        data() {
            return {
                listFaculty: []
            }
        },
        created() {
            this.loadListFaculty()
        },
        methods: {
            async loadListFaculty() {
                this.listFaculty = await fetch(
                    `http://127.0.0.1:8000/api/v1/faculty/`
                ).then(response => response.json())
            },

        }
    }
</script>

<style scoped>

</style>