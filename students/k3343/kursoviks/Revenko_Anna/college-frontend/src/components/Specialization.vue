<template>
  <main>
    <div class="content container mt-5">
      <b-card :title="spec.name" sub-title="">
        <b-card-text>
          Количество свободных мест: {{ spec.freePositions }}
        </b-card-text>
        <b-card-text>
          Количество поданных заявлений: {{ spec.applicationsNum }}
        </b-card-text>
        <b-card-text>
          Проходной балл: {{ spec.minimalPoint }}
        </b-card-text>
      </b-card>
    </div>
  </main>
</template>
<script>
export default {
  name: 'Specialization',
  data () {
    return {
      specData: {},
      spec: {
        name: '',
        freePositions: 0,
        applicationsNum: 0,
        minimalPoint: 0,
      }
    }
  },
  mounted () {
    this.axios
      .get(`http://${window.location.hostname}:8005/api/specializations/${this.id}`)
      .then(response => { this.specData = response; this.getSpec() })
      .catch(err => { console.error('API', err) })    
  },
  props: ['id'],
  methods: {
    getSpec () {
      let s = this.specData.data
      let spec = {}

      spec.name = s.name
      // spec.department = s.department.name
      spec.freePositions = s.free_positions
      spec.applicationsNum = s.applications_num
      spec.minimalPoint = s.minimal_point

      console.log(spec)

      this.spec = spec
    }
  }
}

</script>
<style scoped>
</style>
