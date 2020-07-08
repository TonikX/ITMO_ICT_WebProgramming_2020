<template>
    <div style="margin:auto;">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
<mu-paper :z-depth="2" style="padding:2%;width:100%">
        <mu-flex justify-content="center" style="background:#e0ebff;
            border-radius: 8px;
            margin:1px;
            padding:1px;
            ">
            <h3>Schedule</h3>
        </mu-flex>

              <mu-paper :z-depth=1>
                <mu-data-table
                    :selectable="sel_table.selectable_v"
                               :checkbox="sel_table.checkbox_v"
                               :selects.sync="selects"
                               :select-all="sel_table.select_all_v"
                               stripe :columns="columns"
                               :data="schedules"  border
                                :sort.sync="sort" @sort-change="handleSortChange">
                   <template slot-scope="scope" >
                    <td>
                        <mu-button flat @click="openSimpleDialog(scope.row.driver.id)">
                            {{scope.row.driver.surname}} ({{scope.row.driver.passport}})
                        </mu-button>
                    </td>
                    <td>{{scope.row.bus.reg_plate}}</td>
                    <td>{{scope.row.route.num}}</td>
                    <td>{{scope.row.work_day}}</td>
                    <td>{{scope.row.work_start}}</td>
                    <td>{{scope.row.work_end}}<br>
                    </td>
                  </template>
                </mu-data-table>
                  <mu-flex v-if="sel_table.selectable_v" justify-content="end">
                      <mu-button flat color="deepOrange" @click="delSch(false)">Back</mu-button>
                      <mu-button color="deepOrange" @click="delSchSubmit(selects)">Delete</mu-button>
                  </mu-flex>
                  <mu-flex v-else justify-content="end">
                      <mu-button flat color="deepOrange" @click="delSch(true)">Delete</mu-button>
                      <mu-button color="deepOrange" @click="addSch">Add</mu-button>
                  </mu-flex>
              </mu-paper>

        <mu-dialog :overlay-opacity="0.2" :open.sync="addSD">
            <mu-stepper :active-step="vactiveStep" orientation="vertical">
              <mu-step>
                <mu-step-label>
                  Driver
                </mu-step-label>
                <mu-step-content>
                  <p>
                      <mu-select v-model="form.select1">
                            <mu-option v-for="option,index in drivers"
                                       v-bind:label="option.surname +' ('+option.passport+')'" :value="option.id">
                            </mu-option>
                          </mu-select>
                  </p>
                  <mu-button @click="vhandleNext1(form.select1)" color="primary">Next</mu-button>
                </mu-step-content>
              </mu-step>
              <mu-step>
                <mu-step-label>
                  Bus and Route
                </mu-step-label>
                <mu-step-content>
                             <mu-col>
                                  <mu-select label="Bus" v-model="form.select2">
                                    <mu-option v-for="option,index in buses" :key="option.reg_plate"
                                               :label="option.reg_plate" :value="option.id">
                                    </mu-option>
                                  </mu-select>
                             </mu-col>
                             <mu-col>
                                  <mu-select label="Route" v-model="form.select3">
                                    <mu-option v-for="option,index in routes" :key="option.num"
                                               :label="option.num" :value="option.id">
                                    </mu-option>
                                  </mu-select>
                             </mu-col>
                  <mu-button @click="vhandleNext" color="primary">Next</mu-button>
                  <mu-button flat @click="vhandlePrev">Back</mu-button>
                </mu-step-content>
              </mu-step>
              <mu-step>
                <mu-step-label>
                  Date/Time
                </mu-step-label>
                <mu-step-content>
                            <mu-col>
                                 <mu-date-input label="Day" :min-date="minDate" display-color="deepOrange"
                                                v-model="form.value4"
                                                 type="date"
                                            :date-time-format="enDateFormat">
                                 </mu-date-input>

                            </mu-col>
                            <mu-col>
                                 <mu-date-input label="Start at" display-color="deepOrange" no-display
                                                v-model="form.value5" clock-type="24hr"
                                                 type="time" view-type="list"
                                            :date-time-format="enDateFormat">
                                 </mu-date-input>
                            </mu-col>
                            <mu-col>
                                 <mu-date-input label="Finish at" display-color="deepOrange" no-display
                                                v-model="form.value6" clock-type="24hr"
                                                 type="time" view-type="list"
                                            :date-time-format="enDateFormat">
                                 </mu-date-input>
                            </mu-col>
                  <mu-button @click="vhandleNext3" color="primary">Submit</mu-button>
                  <mu-button flat @click="vhandlePrev">Back</mu-button>
                </mu-step-content>
              </mu-step>
            </mu-stepper>
        </mu-dialog>

          <mu-dialog :overlay-opacity="0" width="370"
                     :open.sync="openSimple">
            <mu-card v-if="driver" style="width: 100%; max-width: 380px; margin:0 auto;">
              <mu-card-media>
                <img v-bind:src="require('@/assets/images/driver'
                     +driver.id+'.jpg')">

              </mu-card-media>
                <mu-card-title v-bind:title="driver.name+' '+driver.surname"
                               :sub-title="driver.passport">
                </mu-card-title>
              <mu-divider></mu-divider>
                <mu-expansion-panel :zDepth="0">
                    <div slot="header">
                        Information
                    </div>
                    <mu-container>
                      <mu-row gutter>
                        <mu-col span="4">
                            <mu-text-field style="width:100%;" label="Bus"
                                   disabled :placeholder="driver.bus.reg_plate">
                            </mu-text-field>
                        </mu-col>
                        <mu-col span="4">
                            <mu-text-field full-width label="Route"
                                   disabled :placeholder="driver.route.num">
                            </mu-text-field>
                        </mu-col>
                        <mu-col>
                            <mu-text-field full-width label="Salary"
                                   disabled :placeholder="driver.salary">
                            </mu-text-field>
                        </mu-col>
                    </mu-row>

                        </mu-container>
                </mu-expansion-panel>
            </mu-card>
          </mu-dialog>
</mu-paper>

    </div>
</template>

<script>
    import $ from 'jquery'

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


    export default {
        name: "Schedule",
        data() {
            const minDate = new Date();
            minDate.setDate(minDate.getDate());
            return {
                showSch: false,
                ShowRes: false,
                ImgError: false,
                link: '',
                minDate,
                enDateFormat,
                sel_table: {
                    selectable_v: false,
                    checkbox_v: false,
                    select_all_v: false,
                },
                vactiveStep: 0,
                selects: [],
                form: {
                    select1: '',
                    select2: '',
                    select3: '',
                    value4: undefined,
                    value5: undefined,
                    value6: undefined,
                 },
                schedules: [],
                openSimple: false,
                addSD: false,
                trigger: null,
                sch_driver: '',
                drivers: '',
                buses: '',
                routes:'',
                driver: '',
                columns: [
                    { title:'Driver', width:250},
                    { title:'Bus',width:110},
                    { title:'Route',width:80},
                    { title: 'Day', sortable: true},
                    { title:'Starts at'},
                    { title:'Ends at'},
                ],
                sort: {
                    name: '',
                    order: 'asc'
                  },
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' +
                        sessionStorage.getItem('auth_token')}
            }),
            this.loadSchedule()
        },
        computed: {
            vfinished () {
              return this.vactiveStep > 2;
            },
        },
        methods:{
            IsImgError () {
                this.src = "require('@/assets/images/shadow.png')"
            },
            showSchVar (value) {
                this.showSch = value;
            },
            handleSortChange ({name, order}) {
              this.schedules = this.schedules.sort(
                    (a, b) =>
                    order === 'asc' ? Date.parse(a.work_day) - Date.parse(b.work_day)
                    : Date.parse(b.work_day) - Date.parse(a.work_day)
                );
            },
            vhandleNext () {
              this.vactiveStep++;
            },
            vhandleNext3 () {
              this.addSD = false;
              var local_work_day = new Date(this.form.value4.getTime() -
                                    (this.form.value4.getTimezoneOffset()*60000))
                                    .toISOString().split("T")[0]
              $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/schedule/",
                        type: "POST",
                        data: {
                            driver: this.form.select1,
                            bus: this.form.select2,
                            route: this.form.select3,
                            work_day: local_work_day,
                            work_start: this.form.value5.toLocaleTimeString().slice(0,5)+':00',
                            work_end: this.form.value6.toLocaleTimeString().slice(0,5)+':00',

                        },
                        success: (response) => {
                            this.loadSchedule();
                            this.vactiveStep = 0;
                        }
                });
            },
            vhandleNext1 (dr_id) {
              this.vactiveStep++;
              $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/driver",
                        type: "GET",
                        data: {
                            id: dr_id
                        },
                        success: (response) => {
                            this.form.select2 = response.data.data[0].bus.id
                            this.form.select3 = response.data.data[0].route.id
                        }
              });
            },
            vhandlePrev () {
              this.vactiveStep--;
            },
            vreset () {
              this.vactiveStep = 0;
            },
            loadSchedule(){
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/bus_info/schedule/",
                    type: "GET",
                    success:(response) => {
                        this.schedules = response.data.data
                    }
                })
            },
            viewBus(id){
                this.$emit("viewBus", id)
            },
            openSimpleDialog (the_id) {
              this.openSimple = true;
              this.link =
                "../../assets/images/driver"+ the_id +".jpg"
              $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/driver",
                        type: "GET",
                        data: {
                            id: the_id
                        },
                        success: (response) => {
                            this.driver= response.data.data[0];
                        }
              });
            },
            closeSimpleDialog () {
              this.openSimple = false;
            },
            viewDriver(the_id){
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/driver",
                        type: "GET",
                        data: {
                            id: the_id
                        },
                        success: (response) => {
                            this.driver.passport = response.data.data.passport
                        }
                })
            },
            delSch(value){
                this.sel_table.selectable_v = value;
                this.sel_table.checkbox_v = value;
                this.sel_table.select_all_v = value;
            },
            delSchSubmit(s){
                for (let i = 0; i < s.length; ++i) {
                    $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/schedule/"
                                + this.schedules[s[i]].id + "/",
                        type: "DELETE",
                        success: (response) => {
                            this.loadSchedule();
                            this.delSch(false);
                        }
                    });
                }
            },
            addSch(){
                this.addSD = true;
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/all_drivers/",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            this.drivers = response.data.data;
                        }
                });
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/bus",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            this.buses = response.data.data;
                        }
                });
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/route/",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            this.routes = response.data.data;
                        }
                });
            }
        },
    }
</script>

<style scoped>
    h3 {
        cursor: pointer;
    }
</style>
