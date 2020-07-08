<template>
  <v-stepper v-model="e1">
    <v-stepper-header>
      <v-stepper-step :complete="e1 > 1" step="1">Состояние</v-stepper-step>
      <v-divider></v-divider>
      <v-stepper-step :complete="e1 > 2" step="2">Тип восхождения</v-stepper-step>
      <v-divider></v-divider>
      <v-stepper-step :complete="e1 > 3" step="3">Период восхождения</v-stepper-step>
      <v-divider></v-divider>
      <v-stepper-step step="4">Статистика</v-stepper-step>
    </v-stepper-header>
    <v-stepper-items>
      <v-stepper-content step="1">
        <v-row>
          <v-col cols="12" sm="6" offset-sm="3">
            <v-card>
              <v-container fluid>
                <v-row>
                  <v-col class="d-flex child-flex" cols="4">
                    <v-card flat tile class="d-flex">
                      <v-img :src="`https://images.unsplash.com/photo-1503503330041-4cd943d2b61f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2204&q=80`" :lazy-src="`https://images.unsplash.com/photo-1503503330041-4cd943d2b61f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2204&q=80`" aspect-ratio="1" class="grey lighten-2">
                        <template v-slot:placeholder>
                          <v-row class="fill-height ma-0" align="center" justify="center">
                            <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                          </v-row>
                        </template>
                      </v-img>
                    </v-card>
                  </v-col>
                  <v-col class="d-flex child-flex" cols="4">
                    <v-card flat tile class="d-flex">
                      <v-img :src="`https://images.unsplash.com/photo-1532339142463-fd0a8979791a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80`" :lazy-src="`https://images.unsplash.com/photo-1532339142463-fd0a8979791a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80`" aspect-ratio="1" class="grey lighten-2">
                        <template v-slot:placeholder>
                          <v-row class="fill-height ma-0" align="center" justify="center">
                            <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                          </v-row>
                        </template>
                      </v-img>
                    </v-card>
                  </v-col>
                  <v-col class="d-flex child-flex" cols="4">
                    <v-card flat tile class="d-flex">
                      <v-img :src="`https://images.unsplash.com/photo-1531683944026-e56b930467ad?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1300&q=80`" :lazy-src="`https://images.unsplash.com/photo-1531683944026-e56b930467ad?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1300&q=80`" aspect-ratio="1" class="grey lighten-2">
                        <template v-slot:placeholder>
                          <v-row class="fill-height ma-0" align="center" justify="center">
                            <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                          </v-row>
                        </template>
                      </v-img>
                    </v-card>
                  </v-col>
                  <v-col cols="4" class="d-flex child-flex">
                    <v-checkbox v-model="is_planned" label="Запланировано" required></v-checkbox>
                  </v-col>
                  <v-col cols="4" class="d-flex child-flex">
                    <v-checkbox v-model="is_in_progress" label="В процессе" required></v-checkbox>
                  </v-col>
                  <v-col cols="4" class="d-flex child-flex">
                    <v-checkbox v-model="is_finished" label="Завершено" required></v-checkbox>
                  </v-col>
                </v-row>
              </v-container>
            </v-card>
          </v-col>
        </v-row>
        <v-btn color="primary" @click="e1 = 2">
          Продолжить
        </v-btn>
      </v-stepper-content>
      <v-stepper-content step="2">
        <v-row>
          <v-col cols="12" sm="6" offset-sm="3">
            <v-card>
              <v-container fluid>
                <v-row>
                  <v-col class="d-flex child-flex" cols="6">
                    <v-card flat tile class="d-flex">
                      <v-img :src="`https://images.unsplash.com/photo-1469026140142-cb239ea68152?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80`" :lazy-src="`https://images.unsplash.com/photo-1469026140142-cb239ea68152?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80`" aspect-ratio="1" class="grey lighten-2">
                        <template v-slot:placeholder>
                          <v-row class="fill-height ma-0" align="center" justify="center">
                            <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                          </v-row>
                        </template>
                      </v-img>
                    </v-card>
                  </v-col>
                  <v-col class="d-flex child-flex" cols="6">
                    <v-card flat tile class="d-flex">
                      <v-img :src="`https://images.unsplash.com/photo-1458442310124-dde6edb43d10?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80`" :lazy-src="`https://images.unsplash.com/photo-1458442310124-dde6edb43d10?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80`" aspect-ratio="1" class="grey lighten-2">
                        <template v-slot:placeholder>
                          <v-row class="fill-height ma-0" align="center" justify="center">
                            <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                          </v-row>
                        </template>
                      </v-img>
                    </v-card>
                  </v-col>
                  <v-col cols="6" class="d-flex child-flex">
                    <v-checkbox v-model="is_group" label="Групповое" required></v-checkbox>
                  </v-col>
                  <v-col cols="6" class="d-flex child-flex">
                    <v-checkbox v-model="is_solo" label="Одиночное" required></v-checkbox>
                  </v-col>
                </v-row>
              </v-container>
            </v-card>
          </v-col>
        </v-row>
        <v-btn color="primary" @click="e1 = 3">
          Продолжить
        </v-btn>
        <v-btn @click="e1 -= 1">
          Назад
        </v-btn>
      </v-stepper-content>
      <v-stepper-content step="3">
        <v-row>
          <v-col cols="12" sm="6" offset-sm="3">
            <v-card>
              <v-container fluid>
                <v-row>
                  <v-col class="d-flex child-flex" cols="6">
                    <v-card flat tile class="d-flex">
                      <v-date-picker v-model="date_1" :show-current="true"></v-date-picker>
                    </v-card>
                  </v-col>
                  <v-col class="d-flex child-flex" cols="6">
                    <v-card flat tile class="d-flex">
                      <v-date-picker v-model="date_2" show-current="2020-06-01"></v-date-picker>
                    </v-card>
                  </v-col>
                  <v-col cols="12" class="d-flex child-flex">
                    <v-checkbox v-model="is_dated" label="Учитывать дату начала и конца восхождения" required></v-checkbox>
                  </v-col>
                </v-row>
              </v-container>
            </v-card>
          </v-col>
        </v-row>
        <v-btn color="primary" @click="get_climbing()">
          Продолжить
        </v-btn>
        <v-btn @click="e1 -= 1">
          Назад
        </v-btn>
      </v-stepper-content>
      <v-stepper-content step="4">
        <v-container fluid>
          <v-col cols="12">
            <h4 class="headline" v-if="!climbings.length">Ничего не найдено :(</h4>
            <v-card color="primary lighten-2" dark v-if="climbings.length" class="my-2" v-for="climbing in climbings" :key="climbing.name">
              <v-card-title>
                {{ climbing.name }}
              </v-card-title>
              <v-card-subtitle>
                {{ climbing.status }}, {{ climbing.date_start }} - {{ climbing.date_end }}
              </v-card-subtitle>
              <v-card-text>Тип: {{ climbing.type }}</v-card-text>
            </v-card>
          </v-col>
        </v-container>
        <v-btn color="primary" @click="clear()">
          Вернуться в начало
        </v-btn>
        <v-btn @click="e1 -= 1">
          Назад
        </v-btn>
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
</template>
<script>
export default {
  name: 'AllClimbings',
  data() {
    return {
      e1: 1,
      date_1: new Date().toISOString().substr(0, 10),
      date_2: '2020-07-04',
      is_planned: false,
      is_in_progress: false,
      is_finished: false,
      is_group: false,
      is_solo: false,
      is_dated: false,
      climbings: []
    }
  },
  methods: {
    clear() {
      this.e1 = 1
      this.date_1 = new Date().toISOString().substr(0, 10)
      this.date_2 = '2020-07-04'
      this.is_planned = false
      this.is_in_progress = false
      this.is_finished = false
      this.is_group = false
      this.is_solo = false
      this.is_dated = false
    },
    get_climbing() {
      this.e1 = 4
      let date_1 = ''
      let date_2 = ''

      if (this.is_dated) {
        date_1 = this.date_1
        date_2 = this.date_2
      }

      let is_group = ''
      let is_solo = ''

      if (this.is_group) {
        is_group = this.is_group
      }

      if (this.is_solo) {
        is_solo = this.is_solo
      }

      let is_planned = ''
      let is_in_progress = ''
      let is_finished = ''

      if (this.is_planned) {
        is_planned = this.is_planned
      }

      if (this.is_in_progress) {
        is_in_progress = this.is_in_progress
      }

      if (this.is_finished) {
        is_finished = this.is_finished
      }

      this.axios
        .get(`http://localhost:8000/api/climbing/list?is_planned=${is_planned}&is_in_progress=${is_in_progress}&is_finished=${is_finished}&is_group=${is_group}&is_solo=${is_solo}&date_start=${date_1}&date_end=${date_2}`)
        .then(response => {
          console.log(response);
          this.show_climbing(response.data)
        })
        .catch(err => { console.error(err) })
    },
    show_climbing(data) {
      this.climbings = []

      for (let i = 0; i < data.length; i++) {
        let types = ['Одиночное', 'Групповое']
        let is_group = data[i].group ? true : false
        let type = types[0]

        if (is_group) {
          type = types[1]
        }

        let statuses = ['Запланировано', 'В процессе', 'Завершено']
        let status = statuses[parseInt(data[i].status) - 1]

        let climbing = {
          name: `${data[i].mountain.name}, ${data[i].mountain.country}, ${data[i].mountain.height} м`,
          type: type,
          date_start: data[i].climbing_date_start,
          date_end: data[i].climbing_date_end,
          status: status
        }

        this.climbings.push(climbing)
      }
    }
  }
}

</script>
