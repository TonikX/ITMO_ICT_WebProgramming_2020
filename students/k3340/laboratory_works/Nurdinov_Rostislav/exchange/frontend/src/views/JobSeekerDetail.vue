<template>
  <div>
    <p>Имя: {{ jobseeker.name }}</p>
    <p>Фамилия: {{ jobseeker.surname }}</p>
    <p>Отчество: {{ jobseeker.second_name }}</p>
    <p>Дата рождения: {{ jobseeker.date_birth }}</p>
    <p>Адрес: {{ jobseeker.address }}</p>
    <p>Статус работы: {{ jobseeker.status_work }}</p>
    <p>Последняя зарплата: {{ jobseeker.last_salary }}</p>
    <p>Образование: {{ jobseeker.resume.education }}</p>
    <p>Описание: {{ jobseeker.resume.description }}</p>
  </div>
</template>

<script>
export default {
  name: 'Jobseeker',
  props: ['id'],
  data() {
    return {
      jobseeker: {},
    };
  },

  async created() {
    const response = await fetch('http://127.0.0.1:8000/api/v1/jobseeker/1/');
    this.joobseekers = await response.json();
  },
};
</script>
