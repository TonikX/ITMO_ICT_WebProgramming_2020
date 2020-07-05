<template>
  <div>
    <mu-container>
      <mu-paper class="show-page" :z-depth="2">
        <h3>Добавить собаку</h3>
        <mu-form :model="form" class="mu-demo-form" label-position="right" label-width="100" ref="form">
          <mu-flex class="flex-wrapper" align-items="start">
            <mu-flex class="flex-demo" justify-content="start" fill>
              <mu-form-item prop="dog_name" label="Кличка" :rules="rules.dogNameRules">
                <mu-text-field prop="dog_name" v-model="form.dog_name"></mu-text-field>
              </mu-form-item>
            </mu-flex>
            <mu-flex class="flex-demo" justify-content="start" fill>
              <mu-form-item prop="breed" label="Порода" :rules="rules.breedRules">
                <mu-text-field prop="breed" v-model="form.breed"></mu-text-field>
              </mu-form-item>
            </mu-flex>
          </mu-flex>
          <mu-form-item prop="age" label="Возраст">
            <mu-slider prop="age" v-model="form.age" :step="1" :max="20"></mu-slider>
          </mu-form-item>
          <mu-flex class="flex-wrapper" align-items="start">
            <mu-flex class="flex-demo" justify-content="start" fill>
              <mu-form-item prop="date_of_medicine" label="Дата прививки" :rules="rules.dateOfMedicineRules">
                <mu-date-input
                    v-model="form.date_of_medicine"
                    label-float
                    full-width
                    :date-time-format="enDateFormat"
                    prop="date_of_medicine"
                  />
              </mu-form-item>
            </mu-flex>
            <mu-flex class="flex-demo" justify-content="start" fill>
              <mu-form-item prop="gender" label="Пол">
                <mu-radio v-model="form.gender" prop="gender" value="M" label="М"></mu-radio>
                <mu-radio v-model="form.gender" prop="gender" value="F" label="Ж"></mu-radio>
              </mu-form-item>
            </mu-flex>
          </mu-flex>
          <mu-flex class="flex-wrapper" align-items="start">
            <mu-flex class="flex-demo" justify-content="start" fill>
              <mu-form-item prop="club" label="Клуб" :rules="rules.clubRules">
                <mu-select prop="club" v-model="form.club" full-width>
                  <mu-option v-for="club in clubs" :key="club.id" :label="club.club_name" :value="club.id"></mu-option>
                </mu-select>
              </mu-form-item>
            </mu-flex>
            <mu-flex class="flex-demo" justify-content="start" fill>
              <mu-form-item prop="inspection" label="Мед. осмотр">
                <mu-radio prop="inspection" v-model="form.inspection" value="yes" label="Да"></mu-radio>
                <mu-radio prop="inspection" v-model="form.inspection" value="no" label="Нет"></mu-radio>
              </mu-form-item>
            </mu-flex>
          </mu-flex>
          <mu-form-item>
            <mu-button color="primary" @click="submit">Добавить</mu-button>
          </mu-form-item>
        </mu-form>
        <mu-divider></mu-divider>
        <h3>Список моих собак</h3>
        <mu-list>
          <template v-for="dog in dogs">
            <mu-list-item button :ripple="false" :key="dog.id">
              <mu-list-item-title>{{ dog.dog_name }}</mu-list-item-title>
            </mu-list-item>
          </template>
         </mu-list>
      </mu-paper>
    </mu-container>
  </div>
</template>

<script>
const dayAbbreviation = ['S', 'M', 'T', 'W', 'T', 'F', 'S'];
const dayList = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
const monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
  'Oct', 'Nov', 'Dec'];
const monthLongList = ['January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December'];

const enDateFormat = {
  formatDisplay (date) {
    return `${dayList[date.getDay()]}, ${monthList[date.getMonth()]} ${date.getDate()}`;
  },
  formatMonth (date) {
    return `${monthLongList[date.getMonth()]} ${date.getFullYear()}`;
  },
  getWeekDayArray (firstDayOfWeek) {
    let beforeArray = [];
    let afterArray = [];
    for (let i = 0; i < dayAbbreviation.length; i++) {
      if (i < firstDayOfWeek) {
        afterArray.push(dayAbbreviation[i]);
      } else {
        beforeArray.push(dayAbbreviation[i]);
      }
    }
    return beforeArray.concat(afterArray);
  },
  getMonthList () {
    return monthList;
  }
};

function formatDate(date) {
  let dd = date.getDate();

  if (dd < 10) {
      dd = '0' + dd;
  }

  let mm = date.getMonth() + 1;
  if (mm < 10) {
      mm = '0' + mm;
  }

  let yyyy = date.getFullYear();

  return yyyy + '-' + mm + '-' + dd;
}

const formInitialState = {
  dog_name: '',
  breed: '',
  age: 5,
  gender: 'M',
  date_of_medicine: undefined,
  inspection: 'yes',
  club: undefined,
}

export default {
    name: "DogsPage",
    computed: {
        dogs() {
            return this.$store.state.user.dogs;
        },
        clubs() {
            return this.$store.state.club.list.map(({ id, club_name }) => ({ id, club_name }));
        },
    },
    data() {
        return {
            rules: {
                dogNameRules: [{ validate: (val) => !!val, message: 'Нужно заполнить'}],
                breedRules: [{ validate: (val) => !!val, message: 'Нужно заполнить'}],
                dateOfMedicineRules: [{ validate: (val) => !!val, message: 'Нужно заполнить'}],
                clubRules: [{ validate: (val) => !!val, message: 'Нужно заполнить'}],
            },
            form: { ...formInitialState },
            enDateFormat,
        }
    },
    methods: {
      submit () {
        this.$refs.form.validate().then((result) => {
          if (result === false) {
              return;
          }

          const { dog_name, breed, age, gender, date_of_medicine, inspection, club } = this.$refs.form.model;
          const dateObj = new Date(date_of_medicine);
          const formattedDate = formatDate(dateObj);

          const payload = {
              dog_name,
              breed,
              age,
              gender,
              date_of_medicine: formattedDate,
              inspection: inspection === 'yes',
              club,
              owner: this.$store.state.user.id,
          }

          this.$store
              .dispatch('user/createDog', payload)
              .then(() => {
                  console.log('HERE')
                  this.$refs.form.clear();
                  this.form = { ...formInitialState };
              });
        });
      },
    }
};
</script>

<style scoped>
.show-page {
  padding: 20px;
}
</style>