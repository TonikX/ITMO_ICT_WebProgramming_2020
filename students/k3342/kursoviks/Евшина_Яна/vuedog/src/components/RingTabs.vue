<template>
  <div>
    <mu-tabs
            :value.sync="activeRing"
            inverse color="secondary"
            text-color="rgba(0, 0, 0, .54)"
            center
    >
      <mu-tab v-for="(ring, index) in rings.list" :key="index">
        Ринг {{ ring.id }}
      </mu-tab>
    </mu-tabs>
    <div v-for="(ring, index) in rings.list" :key="index">
      <div class="demo-text" v-if="activeRing === index">
        <p><b>Упражнение 1: </b> {{ ring.ex1 }}</p>
        <p><b>Упражнение 2: </b> {{ ring.ex2 }}</p>
        <p><b>Упражнение 3: </b> {{ ring.ex3 }}</p>
      </div>
    </div>
    <h4>Результаты</h4>
    <template v-if="grades !== undefined">
      <mu-data-table :columns="columns" :data="grades">
        <template slot-scope="scope">
          <td>{{scope.row.dog_name}}</td>
          <td>{{scope.row.points1}}</td>
          <td>{{scope.row.points2}}</td>
          <td>{{scope.row.points3}}</td>
          <td>{{scope.row.total}}</td>
        </template>
      </mu-data-table>
    </template>
  </div>
</template>

<script>
export default {
    name: "RingTabs",
    mounted() {
      const showId = parseInt(this.$route.params.id);

      this.$store
          .dispatch("show/getShowRings", showId)
          .then(() => {
              this.activeRing = 0;
          })
    },
    data() {
        return {
            activeRing: undefined,
            grades: undefined,
            columns: [
                { title: 'Кличка', name: 'dog_name' },
                { title: '1 упр', name: 'points1' },
                { title: '2 упр', name: 'points2' },
                { title: '3 упр', name: 'points3' },
                { title: 'Итого', name: 'total' },
            ],
        };
    },
    watch: {
        activeRing(newActiveRing) {
            const showId = this.$route.params.id;
            const rings = this.$store.state.show.rings[showId];
            const newRingId = rings[newActiveRing].id;

            this.grades = undefined;

            this.$store
              .dispatch("show/getRingGrades", { showId, ringId: newRingId })
              .then(() => {
                  const grades = this.$store.state.show.grades[showId][newRingId];

                  const gradesByDog = grades.reduce((acc, grade) => {
                      if (!acc[grade.dog_id]) {
                          acc[grade.dog_id] = {
                              dog_name: grade.dog,
                              ex1Sum: 0,
                              ex2Sum: 0,
                              ex3Sum: 0,
                              count: 0,
                          }
                      }

                      const dogObj = acc[grade.dog_id];

                      dogObj.ex1Sum += grade.points1;
                      dogObj.ex2Sum += grade.points2;
                      dogObj.ex3Sum += grade.points3;
                      dogObj.count += 1;

                      return acc;
                  }, {});

                  this.grades = Object.values(gradesByDog).map(dogGrades => {
                      const count = dogGrades.count;
                      return {
                          dog_name: dogGrades.dog_name,
                          points1: dogGrades.ex1Sum / count,
                          points2: dogGrades.ex2Sum / count,
                          points3: dogGrades.ex3Sum / count,
                          total: (dogGrades.ex1Sum + dogGrades.ex2Sum + dogGrades.ex3Sum) / 3 / count,
                      }
                  }).sort((a, b) => b.total - a.total);
              });
        }
    },
    computed: {
        rings() {
            const showId = parseInt(this.$route.params.id);
            const result = {
                list: this.$store.state.show.rings[showId] || [],
            };

            return result;
        },
    }
}
</script>

<style scoped>

</style>