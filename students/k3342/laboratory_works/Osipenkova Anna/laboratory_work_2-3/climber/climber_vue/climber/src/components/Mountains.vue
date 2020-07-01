<template>
  <v-row cols="12" sm="10" offset-sm="1">
    <v-col cols="12" sm="10" offset-sm="1">
      <v-card>
        <v-list two-line>
          <v-btn class="my-2" @click="dialog_1 = true" color='primary' dark>Добавить вершину</v-btn>
          <template v-for="mountain in items">
            <v-subheader v-if="mountain.header" :key="mountain.header">
              <v-row>
              </v-row>
            </v-subheader>
            <v-divider v-else-if="mountain.divider" :key="mountain.name" :inset="mountain.inset"></v-divider>
            <v-list-item v-else :key="mountain.id" :id="mountain.id" @click="set_mountain(mountain)">
              <v-list-item-avatar>
                <img :src="mountain.avatar">
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title v-html="mountain.name + ', ' + mountain.country"></v-list-item-title>
                <v-list-item-subtitle v-html="mountain.height + 'м'"></v-list-item-subtitle>
                <span v-if="mountain.is_climbed">Вершина покорена</span>
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
          <span class="headline">Добавить вершину</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="6">
                <v-text-field label="Название вершины *" required v-model="name"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-text-field v-model="country" label="Страна *" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-text-field v-model="height" label="Высота *" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-checkbox v-model="is_climbed" label="Вершина была покорена *" required></v-checkbox>
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
          <span class="headline">Добавить вершину</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="6">
                <v-text-field label="Название вершины *" required v-model="name"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-text-field v-model="country" label="Страна *" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-text-field v-model="height" label="Высота *" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-checkbox v-model="is_climbed" label="Вершина была покорена *" required></v-checkbox>
              </v-col>
            </v-row>
          </v-container>
          <small>* Обязательные для заполнения поля</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="close_dialog_2()">Закрыть</v-btn>
          <v-btn color="blue darken-1" text @click="update_mountain()">Сохранить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
export default {
  name: 'Mountain',
  mounted() { this.get_mountains() },
  data() {
    return {
      a: 200,
      dialog_1: false,
      dialog_2: false,
      name: '',
      country: '',
      height: '',
      is_climbed: false,
      mountain_id: '',
      items: []
    }
  },
  methods: {
    get_mountains() {
      this.axios
        .get(`http://127.0.0.1:8000/api/mountain/list`)
        .then(response => {
          console.log(response.data);
          this.items = response.data;
          console.log(this.items)
          for (let i = 0; i < this.items.length; i++) {
            let url = 'http://placekitten.com/350/350';
            this.items[i].avatar = url;
          }
        })
        .catch(err => { console.error(err) })
    },
    submit() {
      this.axios
        .post('http://127.0.0.1:8000/api/mountain/add', {
          country: this.country,
          height: this.height,
          name: this.name,
          is_climbed: this.is_climbed
        })
        .then(response => { console.log(response) })
        .catch(err => { console.error(err) })

      this.clear()
      this.dialog_1 = false
      this.get_mountains()
    },
    clear() {
      this.country = ''
      this.name = ''
      this.height = ''
      this.is_climbed = false
    },
    set_mountain(mountain) {
      this.country = mountain.country
      this.name = mountain.name
      this.height = mountain.height
      this.is_climbed = mountain.is_climbed
      this.mountain_id = mountain.id

      this.dialog_2 = true
    },
    update_mountain() {
      let data = {
        country: this.country,
        height: this.height,
        name: this.name,
        is_climbed: this.is_climbed
      }

      this.axios
        .patch(`http://127.0.0.1:8000/api/mountain/edit/${this.mountain_id}`, data)
        .then(response => {
          console.log(response);
          this.close_dialog_2();
          this.get_mountains()
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
