<template>
  <mu-col>
              <mu-form :model="change_form" class="book-change-form" :label-position="labelPosition" label-width="0">
                <mu-form-item prop="cipher" label="">
                  <mu-text-field v-model="change_form.cipher"></mu-text-field>
                </mu-form-item>
                <mu-form-item prop="title" label="">
                  <mu-text-field multi-line :rows="3" :rows-max="4" v-model="change_form.title"></mu-text-field>
                </mu-form-item>
                <mu-form-item  prop="author" label="">
                  <mu-text-field v-model="change_form.author"></mu-text-field>
                </mu-form-item>
                <mu-form-item prop="publisher" label="">
                  <mu-text-field v-model="change_form.publisher"></mu-text-field>
                </mu-form-item>
                <mu-form-item prop="edition_year" label="">
                  <mu-text-field v-model="change_form.edition_year"></mu-text-field>
                </mu-form-item>
                <mu-form-item prop="sphere" label="">
                  <mu-text-field v-model="change_form.sphere"></mu-text-field>
                </mu-form-item>
                <mu-form-item prop="receipt_date" label="" help-text="В формате: год(4 цифры)-месяц-день">
                  <mu-text-field v-model="change_form.receipt_date"></mu-text-field>
                </mu-form-item>
                <mu-form-item prop="hall" label="">
                  <mu-select v-model="change_form.hall">
                    <mu-option v-for="option in h_options" :key="option[0]"
                               :label="option[1]" :value="option[0]"></mu-option>
                  </mu-select>
                </mu-form-item>
              </mu-form>
            </mu-col>
</template>

<script>
export default {
  name: 'BookChange',
  data () {
    return {
      change_form: {
        cipher: '',
        title: '',
        author: '',
        publisher: '',
        edition_year: '',
        sphere: '',
        receipt_date: '',
        hall: ''
      }
    }
  }
}
</script>

<style scoped>
  .book-change-form {
    width: 500px;
    height: 560px;
  }
</style>
