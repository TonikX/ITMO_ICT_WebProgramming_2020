<template>
    <transition name="modal-fade">
        <div class="modal-backdrop">
            <div class="modal" role="dialog" aria-labelledby="modalTitle" aria-describedby="modalDescription">
                <header class="modal-header" id="modalTitle">
                    <slot name="header">
                        Добавление новой четвертной оценки
                        <button type="button" class="btn-close" @click="close" aria-label="Close modal">
                            x
                        </button>
                    </slot>
                </header>
                <section class="modal-body" id="modalDescription">
                    <slot name="body">
                        <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                            <mu-form-item prop="input" label="Ученик">
                                <mu-select v-model="form.pupil">
                                    <mu-option v-for="pupil in listPupil" :key="pupil.id" :label="pupil.last_name"
                                               :value="pupil.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="radio" label="Оценка">
                                <mu-radio v-model="form.grade" value="5" label="5"></mu-radio>
                                <mu-radio v-model="form.grade" value="4" label="4"></mu-radio>
                                <mu-radio v-model="form.grade" value="3" label="3"></mu-radio>
                                <mu-radio v-model="form.grade" value="2" label="2"></mu-radio>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Предмет">
                                <mu-select v-model="form.subject">
                                    <mu-option v-for="subject in listSubject" :key="subject.id" :label="subject.subject"
                                               :value="subject.id"></mu-option>
                                </mu-select>
                            </mu-form-item>
                        </mu-form>
                    </slot>
                </section>
                <footer class="modal-footer">
                    <slot name="footer">
                        <button
                                type="button"
                                class="btn-green"
                                @click="addGrade"
                                aria-label="Close modal">
                            Submit
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
        name: 'AddGrade',
        props: ['id'],
        data() {
            return {
                labelPosition: 'right',
                listSubject: [],
                listPupil: [],
                form: {
                    pupil: this.id,
                    grade: '',
                    subject: '',
                }
            }
        },
        created() {
            this.loadListSubject()
            this.loadListPupil()
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
            async loadListPupil() {
                this.listPupil = await fetch(
                    `${this.$store.getters.getServerUrl}/pupil`
                ).then(response => response.json())
            },
            addGrade() {
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/grade/",
                        type: "POST",
                        data: {
                            student: this.form.pupil,
                            grade: this.form.grade,
                            subject: this.form.subject
                        },

                        success: (response) => {
                            alert("Оценка добавлена")
                            this.close()
                            this.$router.push({name: "Досье ученика"})
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
        padding: 15px;
        display: flex;
    }

    .modal-header {
        border-bottom: 1px solid #eeeeee;
        color: #4AAE9B;
        justify-content: space-between;
    }

    .modal-footer {
        border-top: 1px solid #eeeeee;
        justify-content: flex-end;
    }

    .modal-body {
        position: relative;
        padding: 20px 10px;
    }

    .btn-close {
        border: none;
        font-size: 20px;
        padding: 20px;
        cursor: pointer;
        font-weight: bold;
        color: #4AAE9B;
        background: transparent;
    }

    .btn-green {
        color: white;
        background: #4AAE9B;
        border: 1px solid #4AAE9B;
        border-radius: 2px;
    }
</style>