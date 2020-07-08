<template>
  <div>
    <h3>{{ show.show_name }}</h3>
    <mu-container>
      <mu-paper class="show-page" :z-depth="2">
        <template v-if="Boolean(show.allowed_dogs) === false">
          <h4>Подать заявку на участие в шоу</h4>
            <mu-form :model="form" class="mu-demo-form" label-position="left" label-width="100" ref="form">
              <mu-flex class="flex-wrapper" align-items="start">
                <mu-flex class="flex-demo" justify-content="start">
                  <mu-form-item prop="dog" label="Собака" :rules="dogRules">
                    <mu-select prop="dog" v-model="form.dog" full-width>
                      <mu-option v-for="dog in dogs" :key="dog.id" :label="dog.dog_name" :value="dog.id"></mu-option>
                    </mu-select>
                  </mu-form-item>
                </mu-flex>
                <mu-flex class="flex-demo" justify-content="start">
                  <mu-form-item>
                    <mu-button color="primary" @click="submit">Подать заявку</mu-button>
                  </mu-form-item>
                </mu-flex>
              </mu-flex>
            </mu-form>
        </template>
        <template v-else>
          <h4>Информация о шоу</h4>
          <div class="show__info">
            <p><b>Город</b>: {{ show.show_town }}</p>
              <p><b>Тип выставки</b>: {{ show.type === '1' ? 'одна порода' : 'много пород' }}</p>
              <p><b>Дата начала</b>: {{ show.start_date.split('-').join('.') }}</p>
              <p><b>Дата конца</b>: {{ show.end_date.split('-').join('.') }}</p>
          </div>
          <mu-divider></mu-divider>
          <h4>Ринги</h4>
          <RingTabs />
        </template>
      </mu-paper>
    </mu-container>
  </div>
</template>

<script>
import RingTabs from "../components/RingTabs";

export default {
    name: "ShowPage",
    components: {
        RingTabs,
    },
    data() {
        return {
            form: {
              dog: undefined,
            },
            dogRules: [{ validate: (val) => !!val, message: 'Нужно заполнить'}],
        }
    },
    computed: {
        show() {
            const showId = parseInt(this.$route.params.id);
            const show = (this.$store.state.show.list || []).find(show => show.id === showId);

            return show || {};
        },
        dogs() {
            return this.$store.state.user.dogs;
        }
    },
    methods: {
        submit() {
            this.$refs.form.validate().then((result) => {
                if (result === false) {
                    return;
                }

                const payload = {
                    dog: this.$refs.form.model.dog,
                    show: this.$route.params.id,
                }

                this.$store
                    .dispatch("user/makeRegistrationRequest", payload)
                    .then(result => {
                        console.log(result);
                        this.$refs.form.clear();
                        this.form = { dog: undefined };
                    })
            });
        }
    }
}
</script>

<style scoped>
.show-page {
  padding: 20px;
}
.show__info {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}
.show__info p {
  width: 50%;
}
</style>
