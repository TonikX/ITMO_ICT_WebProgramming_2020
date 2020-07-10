<template>

    <mu-container>
        <mu-row>
            <mu-col>
                <h1>Проживающие</h1>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <ul>
                    <li v-for="resident in listResident" :key="resident.id">
                        <a @click="goTo(resident.id)">{{resident.fio}}</a>
                        <mu-radio v-if="isDeleteVisible" v-model="form_delete" :value="resident.id"
                                      label=""></mu-radio>
                    </li>
                </ul>
                <mu-button color="primary" @click="ShowCreate">Добавить проживающего</mu-button>
                <mu-button color="primary" @click="ShowDelete">Удалить проживающего</mu-button>
            </mu-col>
            <mu-col v-if="isCreateVisible">
                <mu-form style="width: 50%" :model="form" class="mu-demo-form" :label-position="labelPosition"
                         label-width="200">
                    <mu-form-item prop="input" label="ФИО">
                        <mu-text-field v-model="form.fio"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Номер паспорта">
                        <mu-text-field v-model="form.passport_number"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Прибыл(а) из города">
                        <mu-text-field v-model="form.from_town"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Дата заселения гггг-мм-дд">
                        <mu-text-field v-model="form.check_in"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="input" label="Дата выселения гггг-мм-дд">
                        <mu-text-field v-model="form.check_out"></mu-text-field>
                    </mu-form-item>
                    <mu-form-item prop="select" label="Номер">
                        <mu-select v-model="form.room">
                            <mu-option v-for="room in listRoom" :key="room.id" :label="room.room_number+room.room_type"
                                       :value="room.id"></mu-option>
                        </mu-select>
                    </mu-form-item>
                </mu-form>
                <mu-button color="black" @click="CreateResident">Заселить</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col>
                <br>
                <mu-button v-if="isDeleteVisible" color="black" @click="deleteResident">Подтвердить удаление</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Resident",
        props: ['id'],
        components: {},
        data() {
            return {
                listResident: [],
                listRoom: [],
                isCreateVisible: false,
                isDeleteVisible: false,
                form: {
                    room: '',
                    fio: '',
                    passport_number: '',
                    from_town: '',
                    check_in: '',
                    check_out: '',
                },
                form_delete: {},
            }
        },
        created() {
            this.loadListResident()
            this.loadListRoom()
        },
        methods: {
            async loadListResident() {
                this.listResident = await fetch(
                    `http://127.0.0.1:8000/api/v1/resident/`
                ).then(response => response.json())
            },
            goTo(id) {
                this.$router.push({name: 'Проживающий', params: {id: id}})
            },
            ShowDelete() {
                this.isDeleteVisible = !this.isDeleteVisible
            },
            async deleteResident() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/resident/${this.form_delete}/delete`, {
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
                await alert('Проживающий удален')

                this.isDeleteVisible = !this.isDeleteVisible
                await this.loadListResident()
            },
            ShowCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            async loadListRoom() {
                this.listRoom = await fetch(
                    `http://127.0.0.1:8000/api/v1/room/`
                ).then(response => response.json())
            },
            CreateResident() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/resident/create",
                    type: "POST",
                    data: {

                        room: this.form.room,
                        fio: this.form.fio,
                        passport_number: this.form.passport_number,
                        from_town: this.form.from_town,
                        check_in: this.form.check_in,
                        check_out: this.form.check_out,
                    },
                    success: (response) => {
                        this.$router.push({name: "Проживающие"})
                        alert("Проживающий заселен")
                        this.isCreateVisible = !this.isCreateVisible
                        this.loadListResident()
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Данные введены неверно")
                        }
                    }

                })
            }

        }
    }
</script>

<style scoped>

</style>