<template>
    <mu-container>
        <mu-row align="center">
            <mu-col span="10">
                    <h1>Список учеников школы</h1>
            </mu-col>
        </mu-row>
        <mu-row align="left">
            <mu-col span="10">
                <ol class="ball" v-for="children in listChildren" :key="children.id">
                    <li><a href="#" @click="goTo(children.id)">{{children.surname}} {{children.name}}
                            {{children.second_name}} </a></li>
                </ol>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col span="10" align-self="center">
                <br>
                    <mu-button color="darkgray" style: text-color="black" @click="showModal">Добавить ученика</mu-button>
                <modal
                        v-show="isModalVisible"
                        @close="closeModal"
                />
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import modal from '../components/Add_children.vue';
    export default {
        name: "Childrens",
        props: ['id'],
        data() {
            return {
                listChildren: [],
                isModalVisible: false,
            }
        },
        components: {
            modal
        },
        created() {
            this.loadListChildren()
        },
        methods: {
            async loadListChildren() {
                this.listChildren = await fetch(
                    `${this.$store.getters.getServerUrl}/children`
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
        text-align: left;
        .mu-button {
            margin: 8px;
        }
    }
</style>