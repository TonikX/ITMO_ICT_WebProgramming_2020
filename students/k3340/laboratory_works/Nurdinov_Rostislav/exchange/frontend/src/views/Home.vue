<template>
  <div>
    <table>
      <thead>
      <tr>
        <th>Имя</th>
        <th>Фамилия</th>
        <th>Отчество</th>
        <th>Дата рождения</th>
        <th>Адрес</th>
        <th>Статус работы</th>
        <th>Последняя зарплата</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="jobseeker in joobseekers" :key="jobseeker.id">
        <td>{{ jobseeker.name }}</td>
        <td>{{ jobseeker.surname }}</td>
        <td>{{ jobseeker.second_name }}</td>
        <td>{{ jobseeker.date_birth }}</td>
        <td>{{ jobseeker.address }}</td>
        <td>{{ jobseeker.status_work }}</td>
        <td>{{ jobseeker.last_salary }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Jobseekers',
  data() {
    return {
      joobseekers: [],
    };
  },

  async created() {
    const response = await fetch('http://127.0.0.1:8000/api/v1/jobseeker/');
    this.joobseekers = await response.json();
  },
};
</script>
