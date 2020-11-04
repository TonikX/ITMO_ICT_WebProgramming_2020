<template>
    <mu-row>
        <mu-form :model="form" class="book-form" :label-position="labelPosition" >
            <mu-flex>
                <mu-flex direction="column" class="flex-form" >
                    <mu-form-item prop="library_card" label="Номер шифра" label-width="400">
                        <mu-text-field v-model="form.cipher" ></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="name" label="Название" label-width="400">
                        <mu-text-field v-model="form.name"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="author" label="Автор" label-width="400">
                        <mu-text-field v-model="form.author"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="publisher" label="Издательство" label-width="400">
                        <mu-text-field v-model="form.publisher"></mu-text-field>
                    </mu-form-item>
                </mu-flex>
                <mu-flex direction="column" class="flex-form" >
                    <mu-form-item prop="year" label="Год издания" label-width="400">
                        <mu-text-field v-model="form.year"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="section" label="Раздел" label-width="400">
                        <mu-select v-model="form.section">
                            <mu-option v-for="option in section_options" :key="option"
                                       :label="option" :value="option"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-flex>
            </mu-flex>
            <mu-flex justify-content="end" class="flex-button">
                <mu-button color="primary" @click="addReader()">Добавить</mu-button>
            </mu-flex>
        </mu-form>
    </mu-row>
</template>

<script>
export default {
    name: "BookAdd",
    props: ['book'],
    data () {
        return {
            form: {
                name: '',
                author: '',
                publisher: '',
                year: '',
                section: '',
                cipher: '',
            },
            labelPosition: 'top',
            section_options: [
                'Художественная', 'Учебная', 'Психология', 'Детские'
            ]
        }
    },
    created () {
        $.ajaxSetup({
            headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
        })
    },
    methods: {
        addReader () {
            $.ajax({
                url: 'http://127.0.0.1:8000/api/v1/library/book_add/',
                type: 'POST',
                data: this.form,
                success: (response) => {
                    alert('Новая книга успешно добавлена')
                    this.form = []
                },
                error: (response) => {
                    alert('Error')
                }
            })
        },
    }
}
</script>

<style scoped>
    .flex-form {
        width: 50%;
    }
    .book-form {
        margin-top: 20px;
        margin-outside: 10px;
    }
    .flex-button {
        margin-right: 40px;
    }
</style>
