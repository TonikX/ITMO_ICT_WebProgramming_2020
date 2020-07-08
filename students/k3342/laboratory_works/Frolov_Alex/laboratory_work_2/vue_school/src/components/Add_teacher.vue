<template>
    <transition name="modal-fade">
        <div class="modal-backdrop">
            <div class="modal" role="dialog" aria-labelledby="modalTitle" aria-describedby="modalDescription">
                <header class="modal-header" id="modalTitle">
                    <slot name="header">
                        Добавление учителя
                        <button type="button" class="btn-close" @click="close" aria-label="Close modal">
                            x
                        </button>
                    </slot>
                </header>
                <section class="modal-body" id="modalDescription">
                    <slot name="body">
                        <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                            <mu-form-item prop="input" label="Фамилия">
                                <mu-text-field v-model="form.surname"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Имя">
                                <mu-text-field v-model="form.name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Отчество">
                                <mu-text-field v-model="form.second_name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Предмет">
                                <mu-select v-model="form.subject">
                                    <mu-option v-for="subject in listSubject" :key="subject.id" :label="subject.subject"
                                               :value="subject.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="date" label="Преподает до Год-Месяц-День">
                                <mu-text-field v-model="form.teaching_period" ></mu-text-field>
                            </mu-form-item>
                        </mu-form>
                    </slot>
                </section>
                <footer class="modal-footer">
                    <slot name="footer">
                        <button
                                type="button"
                                class="btn-green"
                                @click="addTeacher"
                                aria-label="Close modal">
                            <p @click="close">Добавить</p>
                        </button>
                    </slot>
                </footer>
            </div>
        </div>
    </transition>
</template>
<script>
    import $ from 'jquery'
    export default {
        name: 'AddTeacher',
        data() {
            return {
                labelPosition: 'right',
                listSubject: [],
                form: {
                    name: '',
                    surname: '',
                    second_name: '',
                    subject: '',
                    teaching_period: '',
                }
            }
        },
        created() {
            this.loadListSubject()
        },
        methods: {
            close() {
                this.$emit('close');
            },
            async loadListSubject() {
                this.listSubject = await fetch(
                    `${this.$store.getters.getServerUrl}/subject`
                ).then(response => response.json())
            },
            addTeacher() {
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/teacher/add",
                        type: "POST",
                        data: {
                            surname: this.form.surname,
                            name: this.form.name,
                            second_name: this.form.second_name,
                            teaching_period: this.form.teaching_period,
                            subject: this.form.subject
                        },
                        success: (response) => {
                            this.close()
                            alert("Учитель добавлен")
                            this.$router.push({name: "Учителя"})
                        },
                        error: (response) => {
                            if (response.status === 400) {
                                alert("Введите все данные")
                            }
                        }
                    }
                )
            },
        }
    }
</script>
<style scoped>
    .modal-backdrop {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: rgba(0, 0, 0, 0.3);
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .modal {
        background: #FFFFFF;
        box-shadow: 2px 2px 20px 1px;
        overflow-x: auto;
        display: flex;
        flex-direction: column;
    }
    .modal-header,
    .modal-footer {
        padding: 30px;
        display: flex;
    }
    .modal-header {
        border-bottom: 1px solid #0b0aff;
        color: #22262e;
        justify-content: space-between;
    }
    .modal-footer {
        border-top: 1px solid #0b0aff;
        justify-content: flex-end;
    }
    .modal-body {
        position: relative;
        padding: 10px 10px;
    }
    .btn-close {
        border: none;
        font-size: 20px;
        padding: 20px;
        cursor: pointer;
        font-weight: bold;
        color: red;
        background: transparent;
    }
    .btn-green {
        color: black;
        background: limegreen;
        border: 1px solid limegreen;
        border-radius: 10px;
    }
</style>