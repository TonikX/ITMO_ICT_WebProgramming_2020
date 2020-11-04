<template>
    <mu-row>
        <mu-form :model="form" class="reader-form" :label-position="labelPosition" >
            <mu-flex>
                <mu-flex direction="column" class="flex-form" >
                    <mu-form-item prop="library_card" label="Номер читательского билета" label-width="400">
                        <mu-text-field v-model="form.library_card" ></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="name" label="ФИО" label-width="400">
                        <mu-text-field v-model="form.name"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="passport_number" label="Паспортные данные" label-width="400">
                        <mu-text-field v-model="form.passport_number"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="date_of_birth" label="Дата рождения" help-text="гггг-мм-дд" label-width="400">
                        <mu-text-field v-model="form.date_of_birth"></mu-text-field>
                    </mu-form-item>
                </mu-flex>
                <mu-flex direction="column" class="flex-form" >
                    <mu-form-item  prop="address" label="Адрес" label-width="400">
                        <mu-text-field multi-line :rows="1" :rows-max="3" v-model="form.address"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="phone" label="Контактный номер" label-width="400">
                        <mu-text-field v-model="form.phone"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="education" label="Образование" label-width="400">
                        <mu-select v-model="form.education">
                            <mu-option v-for="option in education_options" :key="option"
                                       :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                    <mu-form-item prop="academic" label="Наличие учёной степени" label-width="400">
                        <mu-select v-model="form.academic">
                            <mu-option v-for="option in academic_options" :key="option"
                                       :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-flex>
            </mu-flex>
            <mu-flex justify-content="end" class="flex-button">
                <mu-button color="primary" @click="updateReader()">Изменить</mu-button>
            </mu-flex>
        </mu-form>
    </mu-row>
</template>

<script>
export default {
    name: "ReaderUpdate",
    props: {
        form_reader: {}
    },
    data () {
        return {
            form: {
                name: '',
                library_card: '',
                passport_number: '',
                date_of_birth: '',
                address: '',
                phone: '',
                education: '',
                academic: ''
            },
            labelPosition: 'top',
            education_options: [
                'Дошкольное', 'Начальное общее', 'Основное общее',
                'Среднее общее', 'Неполное высшее', 'Высшее'
            ],
            academic_options: ['есть', 'отсутствует']
        }
    },
    created () {
        $.ajaxSetup({
            headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
        })
        //console.log(this.form_reader)
    },
    methods: {
        updateReader() {
            let attributes = {}
            for (let key in this.form) {
                if (this.form[key]) {
                    if (attributes.academic) {
                        if (this.form.academic === 'есть') {
                            this.form_reader.academic = true
                        } else {
                            this.form_reader.academic = false
                        }
                    }
                    attributes[key] = this.form[key]
                }
                else {
                    attributes[key] = this.form_reader[key]
                }
            }
            console.log(attributes)
            let data = {
                data: {
                    type: 'Reader',
                    id: this.form_reader.id,
                    attributes: attributes
                }
            }
            //console.log(data)
            fetch(`http://127.0.0.1:8000/api/v1/library/reader_update/${this.form_reader.id}/`,
                {
                    method: 'POST',
                    headers: {
                        'Authorization': 'Token ' + sessionStorage.getItem('auth_token'),
                        'Content-Type': 'application/vnd.api+json'
                    }, body: JSON.stringify(data)
                }
            ).then(response => {
                alert('Данные читателя успешно изменены')
                this.form = []
            })
        }
    },


}
</script>

<style scoped>
    .flex-form {
        width: 50%;
    }
</style>
