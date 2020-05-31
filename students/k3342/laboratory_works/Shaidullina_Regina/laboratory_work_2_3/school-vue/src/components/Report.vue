<template>
    <mu-container>
        <mu-container>
            <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                <mu-form-item prop="select" label="Class:">
                    <mu-select v-model="form.selectCls">
                        <mu-option v-for="option,index in this.classes" :key="option" :label="option" :value="option"></mu-option>
                    </mu-select>
                </mu-form-item>
            </mu-form>
        </mu-container>
        <mu-container class="button-wrapper2">
            <mu-button color="#5c6bc0" textColor="white" @click="loadR">Get</mu-button><br><br>
        </mu-container>
        <mu-container v-if="assessment">
            <mu-paper>
                <p>Academic performance of {{ form.selectCls }}</p>
                <p1>Class statistics</p1><br><br>
                <mu-container>
                    <span><b>Average grade per each subject:</b></span><br><span v-for="k in avg_sub_grades">{{ k.subject }}: {{ k.grade__avg }}<br></span><br>
                    <span><b>Average grade in class: </b>{{ results["Average grade in class"] }}</span><br>
                    <span><b>Total pupils in class: </b>{{ results["Total pupls in class"] }}</span><br>
                    <span><b>Guiding teacher: </b>{{ results["Guiding teacher"] }}</span>
                </mu-container>
                <br><br>
                <p1>All marks</p1><br><br>
                <mu-data-table border :columns="columns" :data="assessment">
                    <template slot-scope="scope">
                        <td class="is-left">{{ scope.row.term }}</td>
                        <td class="is-left">{{ scope.row.pupil }}</td>
                        <td class="is-left">{{ scope.row.subject }}</td>
                        <td class="is-left">{{ scope.row.grade }}</td>
                    </template>
                </mu-data-table>
            </mu-paper>
            <br><br>
        </mu-container>
    </mu-container>
</template>

<script>
/* eslint-disable */

export default {
    name: 'Report',
    data () {
        return {
            classes: '',
            assessment: '',
            results: '',
            avg_sub_grades: '',
            labelPosition: 'left',
            form: {
                selectCls: '',
            },
            columns: [
                { title: 'Term', name: 'term', align: 'center' },
                { title: 'Pupil', name: 'pupil', width: '370', align: 'center' },
                { title: 'Subject', name: 'subject', align: 'center' },
                { title: 'Grade', name: 'grade', align: 'center' },
            ]
        };
    },
    computed: {
        auth() {
            if (sessionStorage.getItem("auth_token")) {
                return true
            }
        }
    },
    created() {
        $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.loadClass()
    },
    methods: {
        loadClass() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/classes/",
                type: "GET",
                success: (response) => {
                    this.classes_list = response.data.data
                    this.classes = this.classes_list.map(function (item) { return item.name })
                }
            })
        },
        loadR() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/assessments_reports/",
                type: "GET",
                data: {
                    class: this.form.selectCls
                },
                success: (response) => {
                    this.assessment = response.data.data
                    this.avg_sub_grades = response.data.results["Average grade per each subject"]
                    this.results = response.data.results["results"]
                }
            })
        },
    }
}
</script>

<style scoped>
    p { font-size: 24px; font-weight: 400; },
    p1 { font-size: 16px; font-weight: 400; },
    .button-wrapper {
        text-align: right;
        .mu-button{
            margin: 8px;
        }
    },
    .button-wrapper2 {
        text-align: center;
        .mu-button{
            margin: 8px;
        }
    }
</style>