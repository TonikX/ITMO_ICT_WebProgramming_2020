<template>
    <mu-container>
        <mu-row>
            <mu-col>
                Оценки из аттестата
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-form style="width: 50%" :model="form" class="mu-demo-form" :label-position="labelPosition"
                                 label-width="200">
                    <mu-form-item prop="select" label="Абитуриент">
                        <mu-select v-model="form.attestat">
                            <mu-option v-for="attestat in listAttestat" :key="attestat.id" :label="attestat.enrollee"
                                       :value="attestat.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                            <mu-form-item prop="input" label="Предмет">
                                <mu-text-field v-model="form.subject"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Оценка">
                                <mu-text-field v-model="form.mark"></mu-text-field>
                            </mu-form-item>
                </mu-form>
                <mu-button @click="CreateAttestatMark">Добавить оценку</mu-button>
                <br>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button href="#/docs">Вернуться к документам</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
    
</template>

<script>
    import $ from "jquery";

    export default {
        name: "Marks",
        props: ['id'],
        components: {},
        data() {
            return {
                listAttestat: [],
                form:{
                    subject:'',
                    mark:'',
                    attestat:''
                }
            }
            },
        created() {
            this.loadListAttestat()
        },
        methods: {
            async loadListAttestat() {
                this.listAttestat = await fetch(
                    `http://127.0.0.1:8000/api/v1/attestat/`
                ).then(response => response.json())
            },
            CreateAttestatMark() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/attestatsubject/create",
                    type: "POST",
                    data: {
                        attestat: this.form.attestat,
                        subject: this.form.subject,
                        mark: this.form.mark,
                    },
                    success: (response) => {
                        this.$router.push({name: "Оценки"})
                        alert("Оценка внесена")
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Данные введены неверно")
                        }
                    }

                })
            },
        }
    }
</script>

<style scoped>

</style>