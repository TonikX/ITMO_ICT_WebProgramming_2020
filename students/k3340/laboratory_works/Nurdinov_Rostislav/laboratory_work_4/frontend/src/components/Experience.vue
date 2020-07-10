<template>
    <mu-container>
        <table>
        <br/>
        <tr>
          <th>Профессия</th>
          <th>Организация</th>
          <th>Позиция</th>
          <th>Date start</th>
          <th>Date end</th>
<!--          <th></th>-->
<!--          <th></th>-->
        </tr>
        <tr v-for="experience in experiences">
          <td>{{experience.profession}}</td>
          <td>{{experience.name_org}}</td>
          <td>{{experience.position}}</td>
          <td>{{experience.date_start}}</td>
          <td>{{experience.date_end}}</td>
        </tr>
<!--          <td><mu-button style="margin-right: 3px; margin-left: 3px;" @click="DeleteStudents(student.id)" >удалить</mu-button></td>-->
<!--           <td>-->
<!--            <mu-button @click="openAlertDialog">Редактировать</mu-button>-->
<!--          </td>-->
<!--          <mu-dialog title="Редактировать пользователя" width="600" max-width="80%" :esc-press-close="false"-->
<!--                     :overlay-close="false" :open.sync="openAlert">-->
<!--            <mu-form class="mu-demo-form">-->

<!--        <mu-form-item prop="input">-->
<!--          <mu-text-field placeholder="Имя" v-model="student_update.name"></mu-text-field>-->
<!--        </mu-form-item>-->
<!--        <mu-form-item prop="input">-->
<!--          <mu-text-field placeholder="Фамилия" v-model="student_update.surname"></mu-text-field>-->
<!--        </mu-form-item>-->
<!--         <mu-select v-model="student_update.group" label="Номер группы" style="width: 200px" >-->
<!--      <mu-option v-for="group in groups" :value=group.id :label="group.group">{{group.group}} </mu-option>-->
<!--      </mu-select>-->

<!--      </mu-form>-->
<!--            <mu-button slot="actions" flat color="primary" @click="updateStudent(student.id)">Редактировать</mu-button>-->
<!--            <mu-button slot="actions" flat color="primary" @click="closeAlertDialog">Закрыть</mu-button>-->
<!--          </mu-dialog>-->
<!--        </tr>-->

      </table>
    </mu-container>
</template>

<script>

export default {
    name: "Experience",
    props: ['id'],
    data() {
        return {
            experiences: '',
        }
    },
    created() {
            this.loadExperience()
    },
    methods: {
        async loadExperience() {
            console.log('???');
            // console.log(${this.id});
            this.experiences = await fetch(
                `${this.$store.getters.getServerUrl}/experience/list/2`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form)
                }
            ).then(response => response.json());
            console.log('!!!!');
            console.log(this.experiences);
        },
    },

}

</script>

<style>
   .block1 {
    margin-top: 5%; /* Отступ сверху */
   }
</style>