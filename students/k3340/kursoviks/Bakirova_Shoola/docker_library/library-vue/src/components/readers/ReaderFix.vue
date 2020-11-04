<template>
    <mu-row>
        <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="150">
            <mu-form-item prop="input" label="Шифр книги">
                <mu-text-field v-model="form.book_cipher"></mu-text-field>
            </mu-form-item>
            <mu-form-item prop="date" label="Дата закрепления" help-text="гггг-мм-дд">
                <mu-text-field v-model="form.date"></mu-text-field>
            </mu-form-item>
            <div class="select-control-group">
                <mu-flex class="select-control-row" v-for="place in places" :key="place.id" >
                    <mu-radio :value="place.id" v-model="form.place"  :label="place.name"></mu-radio>
                </mu-flex>
            </div>
            <mu-form-item>
                <mu-button color="primary" @click="checkBook()">Добавить</mu-button>
            </mu-form-item>
        </mu-form>
    </mu-row>
</template>

<script>
export default {
    name: "ReaderFix",
    props: {
            id: ''
    },
    data () {
        return {
            labelPosition: 'left',
            book_id: '',
            form: {
                book_cipher: '',
                date: '',
                place: '',
            },
            places:[],
            book_check: true
        }
    },
    created () {
        $.ajaxSetup({
            headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
        })
        this.loadPlaces()
    },
    methods: {
        loadPlaces() {
            $.ajax({
                url: 'http://127.0.0.1:8000/api/v1/library/places/',
                type: 'GET',
                success: (response) => {
                    this.places = response.data.place
                }
            })
        },
        checkBook() {
            $.ajax({
                url: 'http://127.0.0.1:8000/api/v1/library/book/',
                type: 'GET',
                data: {
                  book: this.form.book_cipher
                },
                success: (response) => {
                    //console.log(response.data.book)
                    this.book_id = response.data.book[0].id
                    if (response.data.book.length !== 0) {
                        this.addFix()
                    }
                    else {
                        alert('Книга с введённым шифром отсутствует в библиотеке')
                    }

                }
            })
        },
        addFix () {
            //this.checkFix(this.form.book)
            $.ajax({
                url: 'http://127.0.0.1:8000/api/v1/library/fix/',
                type: 'GET',
                success: (response) => {
                    for (let j = 0; j < response.data.data.length; j++) {
                        //console.log(response.data.data[j].book)
                        if (response.data.data[j].book.cipher === this.form.book_cipher) {
                            this.book_check = false
                        }
                    }
                    if (this.book_check===true) {
                        console.log(this.book_id)
                        $.ajax({
                            url: 'http://127.0.0.1:8000/api/v1/library/fix_add/',
                            type: 'POST',
                            data: {
                                reader: this.id,
                                book: this.book_id,
                                date_fix: this.form.date,
                                place: this.form.place
                            },
                            success: (response) => {
                                alert('Закрепление добавлено')
                                this.form.book_cipher = ''
                                this.form.date = ''
                                this.form.place = ''
                            },
                            error: (response) => {
                                alert('Error')
                            }
                        })
                    } else {
                        alert('Книга с введённым шифром уже закреплена')
                    }
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
    .select-control-row{
      padding: 8px 0;
    }
    .select-control-group {
      margin: 16px 0;
    }
</style>
