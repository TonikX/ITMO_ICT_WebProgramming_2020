<template>
  <v-row cols="12" sm="10" offset-sm="1">
    <v-col cols="12" sm="10" offset-sm="1">
      <v-card>
        <v-list two-line>
          <v-btn class="my-2" @click="dialog_1 = true" color='primary' dark>Добавить группу</v-btn>
          <template v-for="group in items">
            <v-subheader v-if="group.header" :key="group.header">
              <v-row>
              </v-row>
            </v-subheader>
            <v-divider v-else-if="group.divider" :key="group.name" :inset="group.inset"></v-divider>
            <v-list-item v-else :key="group.id" :id="group.id" @click="set_group(group)">
              <v-list-item-avatar>
                <img :src="group.avatar">
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title v-html="group.name"></v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-icon>mdi-pencil</v-icon>
              </v-list-item-action>
            </v-list-item>
          </template>
        </v-list>
      </v-card>
    </v-col>
    <v-dialog v-model="dialog_1" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Добавить группу</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="6">
                <v-text-field label="Название группы *" required v-model="name"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-autocomplete :items="climbers" v-model="active_climbers" multiple label="Участники *" required></v-autocomplete>
              </v-col>
            </v-row>
          </v-container>
          <small>* Обязательные для заполнения поля</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog_1 = false">Закрыть</v-btn>
          <v-btn color="blue darken-1" text @click="submit()">Добавить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialog_2" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Изменить группу</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="6">
                <v-text-field label="Название группы *" required v-model="name"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-autocomplete :items="climbers" v-model="active_climbers" multiple label="Участники *" required></v-autocomplete>
              </v-col>
            </v-row>
          </v-container>
          <small>* Обязательные для заполнения поля</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="close_dialog_2()">Закрыть</v-btn>
          <v-btn color="blue darken-1" text @click="update_group()">Добавить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
export default {
  name: 'Groups',
  mounted() {
    this.get_climbers()
    this.get_groups()
  },
  data() {
    return {
      a: 200,
      dialog_1: false,
      dialog_2: false,
      name: '',
      active_climbers: [],
      climbers: [],
      country: '',
      height: '',
      is_climbed: false,
      group_id: '',
      items: []
    }
  },
  methods: {
    get_climbers() {
      this.axios
        .get('http://127.0.0.1:8000/api/climber/list')
        .then(response => {
          for (let i = 0; i < response.data.length; i++) {
            let climber = { value: response.data[i].id, text: `${response.data[i].first_name} ${response.data[i].last_name}` }
            this.climbers.push(climber)
          }
        })
        .catch(err => { console.error(err) })
    },
    get_groups() {
      this.axios
        .get(`http://127.0.0.1:8000/api/group/list`)
        .then(response => {
          this.items = response.data;
          for (let i = 0; i < this.items.length; i++) {
            let url = 'http://placekitten.com/350/350';
            this.items[i].avatar = url;
          }
        })
        .catch(err => { console.error(err) })
    },
    submit() {
      this.axios
        .post('http://127.0.0.1:8000/api/group/add', {
          name: this.name,
          climber: this.active_climbers
        })
        .then(response => { console.log(response) })
        .catch(err => { console.error(err) })

      this.clear()
      this.dialog_1 = false
      this.get_groups()
    },
    clear() {
      this.country = ''
      this.name = ''
      this.height = ''
      this.is_climbed = false
    },
    set_group(group) {
      this.name = group.name
      this.group_id = group.id
      this.active_climbers = group.climber

      this.dialog_2 = true
    },
    update_group() {
      let data = {
        name: this.name,
        climber: this.active_climbers
      }

      this.axios
        .patch(`http://127.0.0.1:8000/api/group/edit/${this.group_id}`, data)
        .then(response => {
          console.log(response);
          this.close_dialog_2();
          this.get_groups()
        })
        .catch(err => { console.error(err) })
    },
    close_dialog_2() {
      this.dialog_2 = false
      this.clear()
    }
  }
}

</script>
