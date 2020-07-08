<template>
    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Информация о книге</h1>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <table>
                    <tr>
                        <td>Название</td>
                        <td>{{book.name}}</td>
                    </tr>
                    <tr>
                        <td>Автор</td>
                        <td>{{book.author}}</td>
                    </tr>
                    <tr>
                        <td>Издательство</td>
                        <td>{{book.publisher}}</td>
                    </tr>
                    <tr>
                        <td>Год</td>
                        <td>{{book.year}}</td>
                    </tr>
                    <tr>
                        <td>Секция</td>
                        <td>{{book.section}}</td>
                            <mu-select v-model="form_update.section" v-if="isUpdateVisible">
                                <mu-option label="Художественная литература"
                                           value="Художественная_литература"></mu-option>
                                <mu-option label="Учебная литература" value="Учебная_литература"></mu-option>
                                <mu-option label="Научная литература" value="Научная_литература"></mu-option>
                                <mu-option label="Докуентальна литература" value="Докуентальная_литература"></mu-option>
                            </mu-select>
                    </tr>
                    <tr>
                        <td>Шифр</td>
                        <td>{{book.cipher}}</td>
                            <mu-text-field v-model="form_update.cipher" v-if="isUpdateVisible"></mu-text-field>
                    </tr>
                </table>
            </mu-col>
            <mu-col v-if="isPlaceVisible">
                <table>
                    <tr>
                        <th>Читальный зал</th>
                        <th>Количество экземпляров</th>
                    </tr>
                    <tr v-for="place in book.places" :key="place.id">
                        <td>
                        <mu-radio v-if="isPlaceUpdateVisible" v-model="form_change.update_place" :value="place.id"></mu-radio>
                            {{place.reading_room}}</td>
                        <td>{{place.number}}</td>
                    </tr>
                </table>
                <br>
                <mu-button color="indigo" @click="ShowPlaceUpdate">Изменить количество экземпляров</mu-button>
                <br>
                            <mu-text-field v-model="form_update_place.number" v-if="isPlaceUpdateVisible"></mu-text-field>
                <br>
                <mu-button color="black" v-if="isPlaceUpdateVisible" @click="UpdatePlace">Изменить</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col v-if="isUpdateVisible">
                <mu-button color="black" @click="UpdateBook">Подтвердить</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <mu-button color="indigo" @click="ShowUpdate">Переклассификация</mu-button>
            </mu-col>
            <mu-col>
                <mu-button color="indigo" @click="ShowPlaces">Количество экземпляров</mu-button>
            </mu-col>
            <mu-col>
                <mu-button color="indigo" @click="deleteBook">Удалить книгу</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "BookSingle",
        props: ['id'],
        data() {
            return {
                book: {},
                form_update: {
                    section: '',
                    cipher: ''
                },
                form_change:{
                    update_place:''
                },
                form_update_place:{
                    number: '',
                },
                isUpdateVisible: false,
                isPlaceVisible: false,
                isPlaceUpdateVisible: false,
            }
        },
        created() {
            this.loadBook()
        },
        methods: {
            async loadBook() {
                this.book = await fetch(
                    `http://127.0.0.1:8000/api/v1/book/${this.id}/`
                ).then(response => response.json())
            },
            async deleteBook() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/book/${this.id}/delete`, {
                        method: 'DELETE',
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        }
                    }
                );
                if (response.status !== 204) {
                    alert(JSON.stringify(await response.json(), null, 2));
                }
                await alert('Данная книга удалена')
                await this.$router.push({name: "Книги"})
            },
            ShowPlaces() {
                this.isPlaceVisible = !this.isPlaceVisible
            },
            ShowPlaceUpdate() {
                this.isPlaceUpdateVisible = !this.isPlaceUpdateVisible
            },
            async UpdatePlace() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/book_place/${this.form_change.update_place}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_update_place)
                });
                await alert('Количество экземпляров изменено')
                this.isPlaceUpdateVisible = !this.isPlaceUpdateVisible
                await this.loadBook()
            },
            ShowUpdate() {
                this.isUpdateVisible = !this.isUpdateVisible
            },
            async UpdateBook() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/book/${this.id}/update`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_update)
                });
                await alert('Переклассификация прошла успешно')
                this.isUpdateVisible = !this.isUpdateVisible
                await this.loadBook()
            },
        }
    }
</script>

<style scoped>

</style>