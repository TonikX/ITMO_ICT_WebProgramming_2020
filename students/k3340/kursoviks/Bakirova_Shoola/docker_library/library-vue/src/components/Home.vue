<template>
    <mu-container>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <mu-appbar style="width: 100%;" color="deepPurpleA100">
            <mu-menu slot="left" v-if="auth">
                <mu-button flat icon>
                    <mu-icon value="menu"></mu-icon>
                </mu-button>
                <mu-list slot="content">
                    <mu-list-item button @click="goReaders()">
                        <mu-list-item-content>
                            <mu-list-item-title>Читатели</mu-list-item-title>
                        </mu-list-item-content>
                    </mu-list-item>
                    <mu-list-item button @click="goBooks()">
                        <mu-list-item-content>
                            <mu-list-item-title>Книги</mu-list-item-title>
                        </mu-list-item-content>
                    </mu-list-item>
                    <mu-list-item button @click="goHalls()">
                        <mu-list-item-content>
                            <mu-list-item-title>Залы</mu-list-item-title>
                        </mu-list-item-content>
                    </mu-list-item>
                </mu-list>
            </mu-menu>
            <h2>Библиотека</h2>
            <mu-button flat slot="right" v-if="!auth" @click="goLogin" >ВХОД</mu-button>
            <mu-button flat slot="right" v-else @click="logout">ВЫХОД</mu-button>
        </mu-appbar>
        <mu-row class="task-text" >
            <h3>Задание 2</h3>
            Создать программную систему, предназначенную для работников библиотеки.
            Такая система должна обеспечивать хранение сведений об имеющихся в библиотеке
            книгах, о читателях библиотеки и читальных залах.
            <br><br>
            Для каждой книги в БД должны храниться следующие сведения: название книги,
            автор (ы), издательство, год издания, раздел, число экземпляров этой книги в каждом зале
            библиотеки, а также шифр книги и дата закрепления книги за читателем. Сведения о
            читателях библиотеки должны включать номер читательского билета, ФИО читателя,
            номер паспорта, дату рождения, адрес, номер телефона, образование, наличие ученой
            степени.
            <br><br>
            Читатели закрепляются за определенным залом и могут записываться и
            выписываться из библиотеки. Библиотека имеет несколько читальных залов, которые
            характеризуются номером, названием и вместимостью, то есть количеством людей,
            которые могут одновременно работать в зале. Библиотека может получать новые книги и
            списывать старые. Шифр книги может измениться в результате переклассификации, а
            номер читательского билета в результате перерегистрации.
            <br><br>
            Библиотекарю могут потребоваться следующие сведения о текущем состоянии
            библиотеки:
            <ul class="value-list">
                <a @click="goReaders"><li>• Какие книги закреплены за определенным читателем?</li></a>
                <a @click="openDialog(2)"><li>• Кто из читателей взял книгу более месяца тому назад?</li></a>
                <a @click="openDialog(3)"><li>• За кем из читателей закреплены книги, количество экземпляров которых в библиотеке не превышает 2?</li></a>
                <a @click="openDialog(4)"><li>• Сколько в библиотеке читателей младше 20 лет?</li></a>
                <a @click="openDialog(5)"><li>• Сколько читателей в процентном отношении имеют начальное образование,
            среднее, высшее, ученую степень?</li></a>

            </ul>
            <br>
            Библиотекарь может выполнять следующие операции:
            <ul class="value-list">
                <a @click="goReaders"><li> • Записать в библиотеку нового читателя.</li></a>
                <a @click="goReaders"><li> • Исключить из списка читателей людей, записавшихся в библиотеку более года назад и не прошедших перерегистрацию.
                (Найти читателя можно как по читательскому билету, так и по паспортным данным)</li></a>
                <a @click="goBooks"><li> • Списать старую или потерянную книгу.</li></a>
                <a @click="goBooks"><li> • Принять книгу в фонд библиотеки.</li></a>
            </ul>
            <br>
            Необходимо предусмотреть возможность выдачи отчета о работе библиотеки в
            течение месяца. Отчет должен включать в себя следующую информацию: количество
            книг и читателей на каждый день в каждом из залов и в библиотеке в целом, количество
            читателей, записавшихся в библиотеку в каждый зал и в библиотеку за отчетный месяц.
        </mu-row>
        <mu-dialog width="1000" :open.sync="showDialog">
            <mu-flex v-if="ques===2">
                <question2></question2>
            </mu-flex>
            <mu-flex v-if="ques===3">
                <question3></question3>
            </mu-flex>
            <mu-flex v-if="ques===4">
                <question4></question4>
            </mu-flex>
            <mu-flex v-if="ques===5">
                <question5></question5>
            </mu-flex>
            <mu-button slot="actions" flat color="deepPurpleA100" @click="closeDialog">Закрыть</mu-button>
        </mu-dialog>
    </mu-container>
</template>

<script>
import Question2 from "./questions/Question2";
import Question3 from "./questions/Question3";
import Question4 from "./questions/Question4";
import Question5 from "./questions/Question5";

    export default {
        components: {Question2, Question3, Question4, Question5},
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        name: "Home",
         data () {
            return {
                showDialog: false,
                ques: ''
            }
         },
        methods: {
            goLogin() {
                this.$router.push({name: "login"})
            },
            logout() {
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            },
            goBooks() {
                this.$router.push({name: 'books'})
            },
            goReaders() {
              this.$router.push({name: 'readers'})
            },
            goHalls() {
              this.$router.push({name: 'halls'})
            },
            openDialog(number) {
                this.showDialog = true;
                this.ques = number
            },
            closeDialog() {
                this.showDialog = false;
            }
        },
    }
</script>

<style scoped>

    .grid-cell {
        border-radius: 4px;
        height: 150px;
        margin-top: 70px;

    }
    .task-text {
        width: 70%;
        margin-left: 100px;
        margin-top: 20px;
        text-align: left;
    }
    .value-list {
        list-style: none;
        margin-top: 10px;
    }
    li {
        position: relative;
        background-color: #FAFCFD;
        display: flex;
        align-items: center;
        cursor: pointer;
        opacity: 1;
    }
    a {
    color: darkred;
    }

    a:hover {
    color: red;
    }


</style>
