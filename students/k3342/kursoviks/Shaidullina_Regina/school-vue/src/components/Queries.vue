<template>
    <mu-container class="panel-wrapper">

        <mu-expansion-panel :expand="panel === 'panel1'" @change="toggle('panel1')">
            <div slot="header" style="color: #1a237e">What subject will be teached in a specified class on a given weekday during a given lesson?</div>
                <mu-container>
                    <mu-row>
                        <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                            <mu-form-item prop="select" label="Weekday:">
                                <mu-select v-model="form.weekday">
                                    <mu-option v-for="option,index in this.all_weekdays" :key="option" :label="option" :value="option"></mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="select" label="Class:">
                                <mu-select v-model="form.class">
                                    <mu-option v-for="option,index in this.all_classes" :key="option" :label="option" :value="option"></mu-option>
                                </mu-select>
                            </mu-form-item>
                            <mu-form-item prop="select" label="Lesson num:">
                                <mu-select v-model="form.lesson">
                                    <mu-option v-for="option,index in this.all_lesson_nums" :key="option" :label="option" :value="option"></mu-option>
                                </mu-select>
                            </mu-form-item>
                        </mu-form>
                    </mu-row>
                    <mu-button color="#5c6bc0" textColor="white" @click="getQuery1">Output</mu-button>
                </mu-container>
                <mu-container><br><p>{{timetable.subject}}</p></mu-container>
        </mu-expansion-panel>

        <mu-expansion-panel :expand="panel === 'panel2'" @change="toggle('panel2')">
            <div slot="header" style="color: #1a237e">How many teachers teach each of the subjects in the school?</div>
            <mu-container><span><b>Teachers:</b></span><br><span v-for="k,v in subs">{{v}}: {{k}}<br></span></mu-container>
        </mu-expansion-panel>

        <mu-expansion-panel :expand="panel === 'panel3'" @change="toggle('panel3')">
            <div slot="header" style="color: #1a237e">A list of teachers who teach the same subjects as the informatics teacher in a given class.</div>
                <mu-container>
                    <mu-row>
                        <mu-form :model="form1" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                            <mu-form-item prop="select" label="Class:">
                                <mu-select v-model="form1.class">
                                    <mu-option v-for="option,index in this.all_classes" :key="option" :label="option" :value="option"></mu-option>
                                </mu-select>
                            </mu-form-item>
                        </mu-form>
                    </mu-row>
                    <mu-button color="#5c6bc0" textColor="white" @click="getQuery3">Output</mu-button>
                </mu-container>
                <mu-container><br><span v-for="t in teachers_list">{{t}}<br></span></mu-container>
        </mu-expansion-panel>

        <mu-expansion-panel :expand="panel === 'panel4'" @change="toggle('panel4')">
            <div slot="header" style="color: #1a237e">How many boys and girls are there in each class?</div>
            <mu-container><span><b>Class - gender: number of pupils:</b><br></span><span v-for="c in genders">{{c.study_class}} - {{c.gender}}: {{c.gender__count}}<br></span></mu-container>
        </mu-expansion-panel>

        <mu-expansion-panel :expand="panel === 'panel5'" @change="toggle('panel5')">
            <div slot="header" style="color: #1a237e">How many classrooms are there in the school for minor and major subjects?</div>
            <mu-container><span v-for="k,v in rooms">{{v}}: {{k}} rooms<br></span></mu-container>
        </mu-expansion-panel>

        <br><br>

    </mu-container>
</template>

<script>
/* eslint-disable */

export default {
    name: 'Queries',
    data () {
        return {
            panel: '',

            // 1
            timetables: '',
            all_weekdays: '',
            all_classes: '',
            all_lesson_nums: '',
            labelPosition: 'left',
            form: {
                weekday: '',
                class: '',
                lesson: '',
            },
            timetable: '',

            // 2
            subs: '',

            // 3
            form1: {
                class: '',
            },
            teachers_list: '',

            // 4
            genders: '',
            
            // 5
            rooms: '',
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
        this.loadT()
        this.getQuery2()
        this.getQuery4()
        this.getQuery5()
    },
    methods: {
        toggle (panel) {
            this.panel = panel === this.panel ? '' : panel;
        },
        loadT() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/timetable/",
                type: "GET",
                success: (response) => {
                    this.timetables = response.data.data
                    this.all_weekdays = new Set(this.timetables.map(function (item) { return item.day_of_week }))
                    this.all_classes = new Set(this.timetables.map(function (item) { return item.study_class }))
                    this.all_lesson_nums = new Set(this.timetables.map(function (item) { return item.lesson_num }))
                    // this.all_subjects = new Set(this.timetables.map(function (item) { return item.subject }))
                }
            })
        },
        getQuery1() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/query1/",
                type: "GET",
                data: {
                    day_of_week: this.form.weekday,
                    study_class: this.form.class,
                    lesson_num: this.form.lesson
                },
                success: (response) => {
                    this.timetable = response.data.data
                }
            })
        },
        getQuery2() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/query2/",
                type: "GET",
                success: (response) => {
                    this.subs = response.data.data
                }
            })
        },
        getQuery3() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/query3/",
                type: "GET",
                data: {
                    study_class: this.form1.class,
                },
                success: (response) => {
                    this.teachers_list = response.data.data
                }
            })
        },
        getQuery4() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/query4/",
                type: "GET",
                success: (response) => {
                    this.genders = response.data.data
                }
            })
        },
        getQuery5() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/query5/",
                type: "GET",
                success: (response) => {
                    this.rooms = response.data.data
                }
            })
        },
    }
}
</script>

<style scoped>
    p { font-size: 24px; font-weight: 400; }
</style>