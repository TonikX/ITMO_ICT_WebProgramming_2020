<template>
    <mu-container>
  <mu-row>
    <mu-col>
        <h1>Атобус №{{bus.id}}</h1>
    </mu-col>
  </mu-row>
  <mu-row align="center">
    <mu-col>
    <table>
        <tr>
            <td>Государственный номер</td>
            <td>Тип автобуса</td>
            <td>Вместимость</td>
        </tr>
        <tr>
            <td>{{bus.number}}</td>
            <td>{{bus.bus_type.bus_type}}</td>
            <td>{{bus.bus_type.capacity}} человек</td>
        </tr>
    </table>
    </mu-col>
  </mu-row>
  <mu-row>
    <mu-col>
        <mu-button @click="DeleteBus">Удалить автобус</mu-button>
    </mu-col>
  </mu-row>
</mu-container>
</template>

<script>
    export default {
        name: "BusSingle",
        props: ['id'],
        components: {},
        data() {
          return {
            bus: {},
          }
        },
      created() {
          this.loadBus()
      },
      methods: {
            async loadBus() {
                this.bus = await fetch(
                    `http://127.0.0.1:8000/api/v1/bus/${this.id}/`
                ).then(response => response.json())
            },
            async DeleteBus() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/bus/${this.id}/delete`, {
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
                await alert('Автобус удален')
                await this.$router.push({name: "Автобусы"})
            },

      }
    }
</script>

<style scoped>

</style>