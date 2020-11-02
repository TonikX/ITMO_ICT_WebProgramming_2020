<template>
    <mu-row>
        <h3>За кем из читателей закреплены книги, количество экземпляров которых в библиотеке не превышает 2?</h3>
        <mu-flex v-for="reader in filter_reader" :key="reader.id" class="reader-list" direction="column">
            <mu-flex class="reader-list">
                <h4>{{ reader.name }} (билет №{{reader.library_card}}):</h4>
            </mu-flex>
            <mu-flex v-for="book in reader.books" :key="book.id" class="books-list">
                <li>
                    "{{book.name}}" (шифр №{{book.cipher}})
                </li>
            </mu-flex>
        </mu-flex>
    </mu-row>
</template>

<script>
export default {
    name: "question3",
    data () {
        return {
            readers: [],
            reader_books: [],
            books: [],
            cipher_filter: [],
            filter_reader: [],
        }
    },
    created () {
        $.ajaxSetup({
            headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
        })
        this.loadBooks()
    },
    methods: {
        loadBooks() {
            $.ajax({
                url: 'http://127.0.0.1:8000/api/v1/library/books/',
                type: 'GET',
                success: (response) => {
                    this.books = response.data
                    let cipher_test
                    let cipher_split = []
                    for (let i = 0; i < this.books.length; i++) {
                        cipher_test = this.books[i].attributes.cipher
                        cipher_split = cipher_test.split("-")
                        //console.log(cipher_split)
                        let find = this.cipher_filter.indexOf(cipher_split[0])
                        if (cipher_split[1] > 2 && find === -1) {
                            this.cipher_filter.push(cipher_split[0])
                        }
                    }
                     //console.log(this.cipher_filter)
                    this.loadReaders()
                }
            })
        },
        loadReaders() {
            $.ajax({
                url: 'http://127.0.0.1:8000/api/v1/library/readers/',
                type: 'GET',
                success: (response) => {
                    this.readers = response.data
                    //console.log(this.readers)

                    for (let j = 0; j < this.readers.length; j++) {
                         $.ajax({
                            url: 'http://127.0.0.1:8000/api/v1/library/reader/',
                            type: 'GET',
                            data: {
                                reader: this.readers[j].id
                            },
                            success: (response) => {
                                this.reader_books = response.data
                                let cipher_test
                                let cipher_split = []
                                let books_test = []
                                for(let i = 0; i < this.reader_books.books.length; i++) {
                                    cipher_test = this.reader_books.books[i].book.cipher
                                    cipher_split = cipher_test.split("-")
                                    //console.log(cipher_split)
                                    if(this.cipher_filter.indexOf(cipher_split[0]) == -1) {
                                        let book_test = {
                                            id: this.reader_books.books[i].book.id,
                                            name: this.reader_books.books[i].book.name,
                                            cipher: this.reader_books.books[i].book.cipher,
                                        }
                                        books_test.push(book_test)
                                    }
                                }
                                //console.log(this.reader_books)
                                if (books_test.length !== 0){
                                    let reader_test = {
                                        id: this.reader_books.reader[0].id,
                                        name: this.reader_books.reader[0].name,
                                        library_card: this.reader_books.reader[0].library_card,
                                        books: books_test
                                    }
                                    this.filter_reader.push(reader_test)
                                }
                            }
                        })
                    }
                    //console.log(this.filter_reader)
                }
            })

        },
    }
}
</script>

<style scoped>
.reader-list{
    width: 100%;
    margin-left: 20px;
}
.books-list{
    width: 100%;
    margin-left: 40px;
}
</style>
