<template>
  <mu-row>
    <div v-for="client in clients">
    <p v-if="client.name == 'Алексей'">{{client.name}}</p>
    </div>
    <h1>Запрос 1</h1>
    <p>Вывести по алфавиту список всех пациентов заданного врача с датами и
      стоимостью приемов. (для примера врач Иванов)</p>
    <div v-for="transaction in transactions">
      <p v-if="transaction.doctor == 'Иванов'">Врач: {{transaction.doctor}}, Пациент: {{transaction.patients}}. Цена:{{transaction.price}}, Дата: {{transaction.date}}</p>
    </div>

  </mu-row>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "Requests",
        data() {
          return {
            clients: "",
            transactions: "",
          }
        },
      created() {
        this.firstRequest()
        this.secondRequest()
      },
      methods: {
          firstRequest() {
            $.ajax({
              url: "http://127.0.0.1:8000/client/",
              type: "GET",
              success: (response) => {
                this.clients = response

            },

          })
      }, secondRequest() {
          $.ajax({
            url: "http://127.0.0.1:8000/transaction/",
            type: "GET",
            success: (response) => {
              this.transactions = response

            },

          })
        }
    }
    }
</script>

<style scoped>

</style>
