<template>
  <v-row cols="12" sm="10" offset-sm="1">
    <v-col cols="12" sm="10" offset-sm="1">
      <v-card>
        <v-list two-line>
          <v-btn class="my-2" @click="dialog_1 = true" color='primary' dark>Добавить альпиниста</v-btn>
          <template v-for="climber in items">
            <v-subheader v-if="climber.header" :key="climber.header">
              <v-row>
              </v-row>
            </v-subheader>
            <v-divider v-else-if="climber.divider" :key="climber.header" :inset="climber.inset"></v-divider>
            <v-list-item v-else :key="climber.id" :id="climber.id" @click="set_climber(climber)">
              <v-list-item-avatar>
                <img :src="climber.avatar">
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title v-html="climber.first_name + ' ' + climber.last_name + ', ' + interests[parseInt(climber.interest) - 1].text"></v-list-item-title>
                <v-list-item-subtitle v-html="climber.address"></v-list-item-subtitle>
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
          <span class="headline">Добавить альпиниста</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="6">
                <v-text-field label="Имя*" required v-model="first_name"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-text-field v-model="last_name" label="Фамилия *" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-text-field v-model="username" label="Имя пользователя *" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-text-field v-model="address" label="Адрес *" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-text-field v-model="email" label="Email *" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-text-field v-model="password" type="password" label="Пароль *" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-text-field v-model="age" label="Возраст *" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-autocomplete v-model="interest" :items="interests" label="Интересы *"></v-autocomplete>
              </v-col>
            </v-row>
          </v-container>
          <small>* Обязательные для заполнения поля</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog_1 = false">Закрыть</v-btn>
          <v-btn color="blue darken-1" text @click="submit">Добавить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialog_2" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Изменить информацию по альпинисту</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6">
                <v-text-field label="Legal first name *" v-model="first_name" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-text-field label="Legal last name *" v-model="last_name" hint="example of persistent helper text" persistent-hint required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="Address *" required v-model="address"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-text-field v-model="age" label="Age *" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-autocomplete :items="interests" label="Interests" v-model="interest"></v-autocomplete>
              </v-col>
            </v-row>
          </v-container>
          <small>* indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="close_dialog_2()">Close</v-btn>
          <v-btn color="blue darken-1" text @click="update_climber()">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
export default {
  name: 'Climber',
  mounted() { this.get_climbers() },
  data() {
    return {
      a: 200,
      dialog_1: false,
      dialog_2: false,
      first_name: '',
      last_name: '',
      age: '',
      address: '',
      email: '',
      password: '',
      username: '',
      radios: 1,
      interest: '',
      climber_id: '',
      items: [],
      interests: [{ value: '1', text: 'Skiing' }, { value: '2', text: 'Ice hockey' }, { value: '3', text: 'Soccer' }, { value: '4', text: 'Basketball' }, { value: '5', text: 'Hockey' }, { value: '6', text: 'Reading' }, { value: '7', text: 'Writing' }, { value: '8', text: 'oding' }, { value: '9', text: 'Basejump' }]
    }
  },
  methods: {
    get_climbers() {
      this.axios
        .get(`http://127.0.0.1:8000/api/climber/list`)
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
        .post('http://127.0.0.1:8000/api/auth/users/', {
          email: this.email,
          password: this.password,
          username: this.username
        })
        .then(response => { this.add_climber(response.data.id) })
        .catch(err => { console.error(err) })
    },
    add_climber(user_id) {
      this.axios
        .post('http://127.0.0.1:8000/api/climber/add', {
          first_name: this.first_name,
          last_name: this.last_name,
          age: this.age,
          address: this.address,
          user: user_id,
          interest: this.interest
        })
        .then(response => { console.log(response.data) })
        .catch(err => { console.error(err) })

      this.dialog_1 = false;
      this.clear()        
    },
    clear() {
      this.last_name = ''
      this.first_name = ''
      this.age = 0
      this.address = ''
      this.interest = ''
      this.username = ''
      this.password = ''
      this.email = ''
    },
    set_climber(climber) {
      this.dialog_2 = true
      this.first_name = climber.first_name
      this.last_name = climber.last_name
      this.age = climber.age
      this.address = climber.address
      this.interest = climber.interest
      this.climber_id = climber.id
    },
    update_climber() {
      let data = {
        first_name: this.first_name,
        last_name: this.last_name,
        age: this.age,
        interest: this.interest,
        address: this.address
      }

      this.axios
        .patch(`http://127.0.0.1:8000/api/climber/edit/${this.climber_id}`, data)
        .then(response => {
          console.log(response);
          this.close_dialog_2();
          this.get_climbers()
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
