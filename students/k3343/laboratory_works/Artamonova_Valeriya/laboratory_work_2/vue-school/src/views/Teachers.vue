<template>
    <mu-container>
        <mu-row align="center">
            <mu-col span="10" align-self="center">
                <h1>Список учителей школы</h1>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col span="10">
                <ol class="ball" v-for="teacher in listTeacher" :key="teacher.id">
                    <li><a href="#" @click="goTo(teacher.id)">{{teacher.last_name}} {{teacher.first_name}}
                        {{teacher.second_name}}</a></li>
                </ol>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col span="10" align-self="center">
                <mu-button color="primary" @click="showModal">Добавить учителя</mu-button>
                <modal
                        v-show="isModalVisible"
                        @close="closeModal"
                />
            </mu-col>
        </mu-row>
<mu-row>
    <mu-col>

    </mu-col>
</mu-row>

    </mu-container>
</template>

<script>
    import modal from '../components/Add_teacher.vue';

    export default {
        name: "Teachers",
        data() {
            return {
                listTeacher: [],
                isModalVisible: false,
            }
        },
        components: {
            modal
        },
        created() {
            this.loadListTeacher()
        },
        methods: {
            async loadListTeacher() {
                this.listTeacher = await fetch(
                    `${this.$store.getters.getServerUrl}/teacher/`
                ).then(response => response.json())
            },
            goTo(id) {
                this.$router.push({name: 'Досье учителя', params: {id: id}})
            },
            showModal() {
                this.isModalVisible = true;
            },
            closeModal() {
                this.isModalVisible = false;
            }
        }
    }
</script>

<style scoped>

</style>