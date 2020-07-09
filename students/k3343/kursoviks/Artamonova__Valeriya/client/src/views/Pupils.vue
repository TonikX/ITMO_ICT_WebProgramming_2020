<template>
    <mu-container>
        <mu-row align="center">
            <mu-col span="10">
                    <h1>Список учеников школы</h1>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col span="10">
                <ol class="ball" v-for="pupil in listPupil" :key="pupil.id">
                    <li><a href="#" @click="goTo(pupil.id)">{{pupil.last_name}} {{pupil.first_name}}
                            {{pupil.second_name}} </a></li>
                </ol>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col span="10">
                <br>
                    <mu-button color="primary" @click="showModal">Добавить ученика</mu-button>
                <modal
                        v-show="isModalVisible"
                        @close="closeModal"
                />
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import modal from '../components/Add_pupil.vue';

    export default {
        name: "Pupils",
        props: ['id'],
        data() {
            return {
                listPupil: [],
                isModalVisible: false,
            }
        },
        components: {
            modal
        },
        created() {
            this.loadListPupil()
        },
        methods: {
            async loadListPupil() {
                this.listPupil = await fetch(
                    `${this.$store.getters.getServerUrl}/pupil`
                ).then(response => response.json())
            },
            goTo(id) {
                this.$router.push({name: 'Досье ученика', params: {id: id}})
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

<style lang="less">
    .button-wrapper {
        text-align: center;

        .mu-button {
            margin: 8px;
        }
    }
</style>