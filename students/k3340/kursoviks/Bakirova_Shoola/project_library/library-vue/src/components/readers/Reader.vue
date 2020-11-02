<template>
    <mu-col span="9">
        <div v-for="person in person_books.reader" v-bind:key="person.id">
            <mu-flex justify-content="center" class="flex-wrapper">
                <h3>Читатель {{person.name}}</h3>
            </mu-flex>
            <mu-row class="flex-description">
                <mu-col span="6">
                    <mu-flex justify-content="start" wrap="column">
                        <mu-flex>Номер читательского билета: {{person.library_card}}</mu-flex>
                        <mu-flex>Паспортные данные: {{person.passport_number}}</mu-flex>
                        <mu-flex>Дата рождения: {{person.date_of_birth}}</mu-flex>
                        <mu-flex>Адрес: {{person.address}}</mu-flex>
                        <mu-flex>Контактный номер: {{person.phone}}</mu-flex>
                        <mu-flex>Образование: {{person.education}}</mu-flex>
                        <mu-flex v-if="person.academic">Имеется учёная степень</mu-flex>
                        <mu-flex v-else>Отсутствует учёная степень</mu-flex>
                        <mu-flex><br></mu-flex>
                    </mu-flex>
                    <mu-button color="deepPurpleA100" @click="openReaderUpdate()" small>
                        Изменить
                    </mu-button>
                    <mu-dialog title="Изменение данных" :open.sync="showReader" width="1300">
                        <reader-update :form_reader="person"></reader-update>
                        <mu-button slot="actions" flat color="deepPurpleA100" @click="closeReaderUpdate">Закрыть</mu-button>
                    </mu-dialog>
                    <mu-button color="deepPurpleA100" @click="deleteReader()" small>
                        Удалить
                    </mu-button>
                </mu-col>
                <mu-col span="6">
                    <mu-flex v-if="person_books_home.length !== 0"><h4>Закреплённые книги с собой:</h4></mu-flex>
                    <div v-for="book in person_books_home" v-bind:key="book.book.cipher">
                        <mu-flex justify-content="start" wrap="column">
                            <mu-flex>Шифр книги: {{book.book.cipher}}</mu-flex>
                            <mu-flex>Книга: {{book.book.name}}</mu-flex>
                            <mu-flex>Автор: {{book.book.author}}</mu-flex>
                            <mu-flex>Дата закрепления: {{book.date_fix}}</mu-flex>
                        </mu-flex>
                        <mu-flex><br></mu-flex>
                        <mu-button small color="deepPurpleA100"
                                   @click="delFix(idFix=book.id, idForm=book.book.id)">
                            Открепить
                        </mu-button>
                        <mu-flex><br></mu-flex>
                    </div>
                    <mu-flex v-if="person_books_hall.length !== 0"><h4>Закреплённые книги в зале библиотеки:</h4></mu-flex>
                    <div v-for="book in person_books_hall" :key="book.book.cipher">
                        <mu-flex justify-content="start" wrap="column">
                            <mu-flex>Шифр книги: {{book.book.cipher}}</mu-flex>
                            <mu-flex>Книга: {{book.book.name}}</mu-flex>
                            <mu-flex>Автор: {{book.book.author}}</mu-flex>
                            <mu-flex>Дата закрепления: {{book.date_fix}}</mu-flex>
                        </mu-flex>
                        <mu-flex><br></mu-flex>
                        <mu-button small color="deepPurpleA100"
                                   @click="delFix(idFix=book.id, idForm=book.book.id)">
                            Открепить
                        </mu-button>
                        <mu-flex><br></mu-flex>
                    </div>
                    <mu-flex justify-content="end">
                        <mu-button @click="openAddFix()">Закрепить книгу</mu-button>
                        <mu-dialog title="Закрепление книги" width="360" :open.sync="showFix">
                            <reader-fix :id="person.id"></reader-fix>
                            <mu-button slot="actions" flat color="deepPurpleA100" @click="closeAddFix">Закрыть</mu-button>
                        </mu-dialog>
                    </mu-flex>
                </mu-col>
            </mu-row>
        </div>
    </mu-col>
</template>

<script>
    import ReaderFix from './ReaderFix'
    import ReaderUpdate from "./ReaderUpdate";

    export default {
        name: 'Reader',
        components: {ReaderUpdate, ReaderFix},
        props: {
            id: ''
        },
        data () {
            return {
                person_books: {},
                person_books_home: [],
                person_books_hall: [],
                labelPosition: 'left',
                book_form: '',
                form: {
                    input: '',
                    date: ''
                },
                form_reader: {
                    name: '',
                    library_card: '',
                    passport_number: '',
                    date_of_birth: '',
                    address: '',
                    phone: '',
                    education: '',
                    academic: ''
                },
                del_fix_form: [],
                showFix: false,
                showReader: false,

            }
        },
        created () {
            $.ajaxSetup({
              headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
            })
            this.loadBooks()

        },
        methods: {
            loadBooks () {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/library/reader/',
                    type: 'GET',
                    data: {
                        reader: this.id
                    },
                    success: (response) => {
                        this.person_books = response.data
                        this.person_books_home = []
                        this.person_books_hall = []
                        //console.log(response.data)
                        let idList = []
                        for (let j = 0; j < this.person_books.books.length; j++) {
                            idList.push(this.person_books.books[j].book.id)
                        }
                        let maxNum = Math.max(...idList)
                        for (let i = 0; i < maxNum + 1; i++) {
                            this.del_fix_form.push({fix: '', handed: 'true'})
                        }
                        //console.log(this.del_fix_form)
                        for (let j = 0; j < this.person_books.books.length; j++) {
                            if (this.person_books.books[j].place===2){
                                this.person_books_home.push(this.person_books.books[j])
                            }
                            else{
                                this.person_books_hall.push(this.person_books.books[j])
                            }

                        }
                        //console.log(this.person_books_home)
                        //console.log(this.person_books_hall)

                    }
                })
            },
            delFix(idFix, idForm) {
                this.del_fix_form[idForm].fix = idFix
                let data = {
                    links: {
                        first: "http://127.0.0.1:8000/api/v1/library/fix_test/?page=1",
                        last: "http://127.0.0.1:8000/api/v1/library/fix_test/?page=1",
                        next: null,
                        prev: null
                    },
                    data: {
                        type: 'Fix',
                        id: idFix,
                        attributes: {
                            handed: 'true'
                          }
                    }
                }

                fetch(`http://127.0.0.1:8000/api/v1/library/fix_update/${this.del_fix_form[idForm].fix}/`,
                    {
                      method: 'PUT',
                      headers: {
                        'Authorization': 'Token ' + sessionStorage.getItem('auth_token'),
                        'Content-Type': 'application/vnd.api+json'
                      }, body: JSON.stringify(data)
                    }
                    ).then(response => {
                        alert('Книга успешно откреплена')
                        this.loadBooks()
                    })
            },
            deleteReader() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/library/reader/',
                    type: 'GET',
                    data: {
                      reader: this.id
                    },
                    success: (response) => {
                        if (response.data.books.length === 0) {
                            $.ajax({
                                url: 'http://127.0.0.1:8000/api/v1/library/reader_del/' + this.id + '/',
                                type: 'DELETE',
                                success: (response) => {
                                    alert('Читатель успешно удалён')
                                    this.$emit('reload')
                                    this.loadBooks()

                                }
                            })
                        } else {
                        alert('Невозможно удалить читателя, не возвращены все книги')
                        }
                    }
                })
            },
            openAddFix () {
                this.showFix = true;
            },
            closeAddFix () {
                this.showFix = false;
                this.person_books_home = [];
                this.person_books_hall = [];
                this.loadBooks()
            },
            openReaderUpdate () {
                this.showReader = true;
            },
            closeReaderUpdate () {
                this.showReader = false;
                this.person_books_home = [];
                this.person_books_hall = [];
                this.loadBooks()
            }
        }
    }
</script>

<style scoped>
    .mu-demo-form {
        width: 100%;
        max-width: 460px;
    }
    .title {
        text-align: justify;
    }
    .detachment-form {
        width: 400px;
        height: 50px;
    }
    .flex-wrapper{
        width: 100%;
        height: 44px;
        margin-top: 8px;
    }
    .flex-description {
        margin-top:10px;
        margin-left: 86px;
    }
    .mu-transition-row {
        margin-top: 16px;
        height: 100px;
    }
    .mu-transition-box {
        min-width: 200px;
        height: 100px;
        margin-right: 16px;
        border-radius: 4px;
        padding: 0 16px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
