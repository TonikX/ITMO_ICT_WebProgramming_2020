<template>
    <div style="margin:auto" >
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">

        <mu-appbar color="deepOrange300">
            <h2 @click="goHome"style="cursor:pointer">The Company</h2>
            <mu-button flat slot="right" v-if="!auth" @click="goLogin">To log in</mu-button>
            <mu-button flat slot="right" v-else @click="goLogout">To log out</mu-button>
            <mu-button  slot="left" @click="openDrawer = !openDrawer" icon><mu-icon value="menu"></mu-icon></mu-button>
            <mu-drawer slot="left" :open.sync="openDrawer" :docked="false">
                <mu-list v-if="auth" >
                    <mu-list-item button @click="goDrivers">
                              <mu-list-item-action>
                                    <mu-icon value="person_search"></mu-icon>
                                </mu-list-item-action>
                                <mu-list-item-title>
                                    Drivers
                                </mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goQueries">
                              <mu-list-item-action>
                                    <mu-icon value="assignment"></mu-icon>
                                </mu-list-item-action>
                                <mu-list-item-title>
                                    Information
                                </mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goBusMal">
                              <mu-list-item-action>
                                    <mu-icon value="build"></mu-icon>
                                </mu-list-item-action>
                                <mu-list-item-title>
                                    Bus Malfunctions
                                </mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goSchedReport">
                              <mu-list-item-action>
                                    <mu-icon value="fact_check"></mu-icon>
                                </mu-list-item-action>
                                <mu-list-item-title>
                                    Schedule Reports
                                </mu-list-item-title>
                    </mu-list-item>

                    <mu-divider></mu-divider>

                    <mu-list-item button @click="goReport">
                              <mu-list-item-action>
                                    <mu-icon value="book"></mu-icon>
                                </mu-list-item-action>
                                <mu-list-item-title>
                                    Report
                                </mu-list-item-title>
                      </mu-list-item>

                </mu-list>
                <mu-list v-else >
                    <mu-list-item button @click="goLogin">
                              <mu-list-item-action>
                                    <mu-icon value="account_box"></mu-icon>
                                </mu-list-item-action>
                                <mu-list-item-title>
                                    Please, Log In
                                </mu-list-item-title>
                      </mu-list-item>
                </mu-list>
            </mu-drawer>
        </mu-appbar>
            <br>


<mu-container>
            <mu-row>
                <mu-button ref="button"  @click="openQs = !openQs" >
                    Get info
                </mu-button>
                <mu-col >
                <mu-button v-if="query.id" @click="query.id='';"
                        style="position: absolute;right: 0;">
                    Close
                </mu-button>
                </mu-col>
                <mu-popover cover :open.sync="openQs" :trigger="trigger">
                   <mu-list>
                    <mu-tooltip content="List of Drivers on a Route
                                                and their Schedules"
                                placement="right">
                        <mu-list-item button @click="FuncQuery1">
                            <mu-list-item-action>
                                <mu-icon value="person_search"></mu-icon>
                            </mu-list-item-action>
                            <mu-list-item-title>Drivers on a Route</mu-list-item-title>
                        </mu-list-item>
                    </mu-tooltip>
                    <mu-tooltip content="Time when Buses start and stop on each Route"
                                placement="right">
                            <mu-list-item button @click="FuncQuery2">
                                <mu-list-item-action>
                                    <mu-icon value="directions_bus"></mu-icon>
                                </mu-list-item-action>                              <mu-list-item-title>Buses on Routes</mu-list-item-title>
                            </mu-list-item>
                    </mu-tooltip>
                    <mu-tooltip content="Total time of all Routes"
                                placement="right">
                            <mu-list-item button @click="FuncQuery3">
                            <mu-list-item-action>
                                <mu-icon value="more_time"></mu-icon>
                            </mu-list-item-action>
                                <mu-list-item-title>Routes total time</mu-list-item-title>
                            </mu-list-item>
                       </mu-tooltip>
                       </mu-tooltip>
                       <mu-tooltip content="Buses, which missed schedule, and reasons for it"
                                placement="right">
                            <mu-list-item button @click="FuncQuery4">
                            <mu-list-item-action>
                                <mu-icon value="departure_board"></mu-icon>
                            </mu-list-item-action>
                                <mu-list-item-title>Buses missed days</mu-list-item-title>
                            </mu-list-item>
                       </mu-tooltip>
                       </mu-tooltip>
                       <mu-tooltip content="Number of drivers for each job class"
                                placement="right">
                            <mu-list-item button @click="FuncQuery5">
                                <mu-list-item-action>
                                    <mu-icon value="group"></mu-icon>
                                </mu-list-item-action>
                                <mu-list-item-title>Drivers JobClasses</mu-list-item-title>
                            </mu-list-item>
                       </mu-tooltip>
                   </mu-list>
                </mu-popover>
            </mu-row>

<mu-container v-if="query.id==1"><br>
            <mu-paper :z-depth="1" style="padding:10px">
                <mu-flex justify-content="center" class="query_title">
                    <h3>{{query.info}}</h3>
                </mu-flex>
                <mu-select icon="gps_fixed" full-width label="Route"
                           v-model="formQuery.select1">
                    <mu-option v-for="option,index in routes" :key="option.num"
                            :label="option.num.toString()" :value="option.id">
                    </mu-option>
                </mu-select>
                <mu-button full-width @click="CompQuery1(formQuery.select1)">Search</mu-button>
            </mu-paper>

        <mu-paper :z-depth="1" v-if="queryRes" >

            <mu-tabs :value.sync="tab_active_q1" color="indigo400"
                            indicator-color="indigo400">
                <mu-col v-for="one_driver in queryfin.drivers">
                    <mu-tab>{{one_driver.surname}} ({{one_driver.passport.slice(0,4)}}...)</mu-tab>
                </mu-col>
            </mu-tabs>
            <mu-row style="width:100%;">
                <mu-row v-if="queryfin.scheds.filter(sch => sch.driver.id == queryfin.drivers[tab_active_q1].id).length > 0"
                    style="width:80%;margin:auto;padding:5px;">
                    <mu-col>
                    <mu-data-table

                        stripe :columns="columns1"
                        :data="queryfin.scheds.filter(sch => sch.driver.id == queryfin.drivers[tab_active_q1].id)"  border>
                   <template slot-scope="scope" >

                    <td>{{scope.row.bus.reg_plate}}</td>
                    <td>{{scope.row.route.num}}</td>
                    <td>{{scope.row.work_day}}</td>
                    <td>{{scope.row.work_start}}</td>
                    <td>{{scope.row.work_end}}<br>
                    </td>
                  </template>
                </mu-data-table></mu-col>
                </mu-row>

                <mu-row style="width:100%" v-else>

                    <mu-alert color="info">
                        <mu-icon left value="info"></mu-icon>
                        Nothing was found.
                    </mu-alert>

                </mu-row>

            </mu-row>
    </mu-paper>
</mu-container>

<mu-container v-if="query.id==2">
    <br>
            <mu-paper :z-depth="1" style="padding:10px">
                <mu-flex justify-content="center" class="query_title">
                    <h3>{{query.info}}</h3>
                </mu-flex>
                <mu-data-table stripe :columns="columns2"
                               :data="queryfin"  border
                                style="border-radius: 8px;">
                       <template slot-scope="scope" >
                        <td>
                            {{scope.row.route__num}}
                        </td>
                        <td>{{scope.row.work_start__min}}</td>
                        <td>{{scope.row.work_end__max}}</td>
                        </td>
                      </template>
                    </mu-data-table>
            </mu-paper>
</mu-container>

<mu-container v-if="query.id==3">
    <br>
            <mu-paper :z-depth="1" style="padding:10px">
                <mu-flex justify-content="center" class="query_title">
                    <h3>{{query.info}}</h3>
                </mu-flex>
                <mu-row>
               <mu-col span="8">
                <mu-data-table stripe :columns="[{title:'Route'},{title:'Time (minutes)'}]"
                               :data="routes"  border
                                style="border-radius: 8px">
                   <template slot-scope="scope" >
                    <td>
                        {{scope.row.num}}
                    </td>
                    <td>{{scope.row.circle_time_min}}</td>
                    </td>
                  </template>
                </mu-data-table>
               </mu-col>
                <mu-col style="margin: auto;">
                <h1>{{queryfin}}</h1>
                </mu-col>
                    </mu-row>
            </mu-paper>
</mu-container>

<mu-container v-if="query.id==4">
    <br>
            <mu-paper :z-depth="1" style="padding:10px">
                <mu-flex justify-content="center" class="query_title">
                    <h3>{{query.info}}</h3>
                </mu-flex>
                   <mu-date-input style="width:100%" icon="today" display-color="deepOrange"
                        v-model="formQuery.date1" type="date" label="Day to check"
                                  :date-time-format="enDateFormat">
                   </mu-date-input>
                <mu-button full-width @click="CompQuery4">Search</mu-button>
            </mu-paper>
            <mu-paper :z-depth="1" v-if="queryRes && !queryError">
                <mu-row style="margin-bottom:1%; padding:1%; background:grey">
                <mu-col v-for="bus in queryfin.buses">
                    <mu-chip>{{bus.schedule_line__bus__reg_plate}}</mu-chip>
                </mu-col></mu-row>


                <mu-data-table stripe :columns="columns4"
                               :data="queryfin.data"  border>
                   <template slot-scope="scope" >

                    <td style="background:#e6eeff">{{scope.row.reason}}</td>
                    <td>{{scope.row.schedule_line.bus.reg_plate}}</td>
                    <td>
                        {{scope.row.schedule_line.driver.surname}}<br>
                        ({{scope.row.schedule_line.driver.passport}})
                    </td>
                    <td>{{scope.row.schedule_line.route.num}}</td>
                    <td>{{scope.row.schedule_line.work_day}}</td>
                    <td>{{scope.row.schedule_line.work_start}}</td>
                    <td>{{scope.row.schedule_line.work_end}}<br>
                    </td>
                  </template>
                </mu-data-table>
            </mu-paper>
            <mu-alert transition="mu-scale-transition" color="info"
                      v-if="queryError">
                <mu-icon left value="info"></mu-icon>
                Nothing was found.
            </mu-alert>
</mu-container>

<mu-container v-if="query.id==5">
    <br>
            <mu-paper :z-depth="1" style="padding:10px">
                <mu-flex justify-content="center" class="query_title">
                    <h3>{{query.info}}</h3>
                </mu-flex>

                <mu-paper :z-depth="1" style="padding:8px"
                          >
                    <mu-row style="background:#f5f5f5; border-radius:8px;
                                border-style:solid; border-width:2px;
                                border-color:#dbdbdb; margin:7px"
                            v-for="item in queryfin.data">
                        <mu-col span="6" style="margin:auto">
                            <h3>Job Class: {{item.job_class}}</h3>
                        </mu-col>
                        <mu-col style="padding:5px;">
                            <mu-row v-if="item.job_class == 1"
                                    v-for="dr in queryfin.dr_1"
                                    style="padding:5px;">
                                {{dr.name}} {{dr.surname}} ({{dr.passport}})
                                <mu-divider></mu-divider>
                            </mu-row>
                            <mu-row v-if="item.job_class == 2"
                                    v-for="dr in queryfin.dr_2"
                                    style="padding:5px;">
                                {{dr.name}} {{dr.surname}} ({{dr.passport}})
                                <mu-divider></mu-divider>
                            </mu-row>
                            <mu-row v-if="item.job_class == 3"
                                    v-for="dr in queryfin.dr_3"
                                    style="padding:5px;">
                                {{dr.name}} {{dr.surname}} ({{dr.passport}})
                                <mu-divider></mu-divider>
                            </mu-row>
                            <mu-paper :z-depth="2"
                                      style="border-radius:8px;
                                      background:#a7c8fa;margin:2px;
                                      padding:3px">
                                Total Number: <b>{{item.job_class__count}}</b></mu-paper>
                        </mu-col>

                    </mu-row>
                </mu-paper>

            </mu-paper>
</mu-container></mu-container>
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
       name:"Queries",
       props: {
            id: ''
       },
       data(){
            return{
                                openDrawer: false,
                sort: {
                    name: '',
                    order: 'asc'
                },
                tab_active:0,
                tab_active_q1:0,
                enDateFormat,
                one_route:'',
                total_time_routes:'',
                trigger: null,
                drivers: '',
                routes:[],
                type_names:[
                    'very little','little',
                    'average','big','articulated'
                ],
                openQs: false,
                routes:'',
                query: {
                    id:'1',
                    info:'List of Drivers on a Route and their Schedules',
                },
                r_for_t: [],
                queryRes: false,
                queryError: false,
                queryfin: '',
                queryReportfin:'',
                columns1: [

                    { title:'Bus'},
                    { title:'Route'},
                    { title: 'Day'},
                    { title:'Starts at'},
                    { title:'Ends at'},
                ],
                columns2: [
                    { title:'Route'},
                    { title: 'Earliest start'},
                    { title:'Latest end'},
                ],
                columns4: [
                    { title:'Reason'},
                    { title:'Bus'},
                    { title:'Driver'},
                    { title:'Route'},
                    { title: 'Day'},
                    { title:'Starts at'},
                    { title:'Ends at'},
                ],
                formQuery: {
                    select1:'',
                    date1:undefined,
                },
                bus: {
                    id: '',
                    show: false
                }

            }
       },
       mounted() {
            this.trigger = this.$refs.button.$el;
        },
       created(){
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' +
                        sessionStorage.getItem('auth_token')}
            });
            this.FuncQuery1();
       },
       computed: {
            auth(){
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
       methods: {
                        handleSortChange ({name, order}) {
              this.queryReportfin.age_exp = this.queryReportfin.age_exp.sort(
                            (a, b) => order === 'asc' ? a.age - b.age : b.age - a.age);
            },
            getBusDrOnRoute(this_id){
                var dr_on_route = Object.values(this.drivers).filter(r => r.route.id == this_id);
                var buses_dr = [];
                for (let i = 0; i < dr_on_route.length; i++){
                    buses_dr.push(dr_on_route[i].bus.reg_plate);
                };
                return [...new Set(buses_dr)]
            },

            getRoute(id){
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/route/",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            this.routes = response.data.data;
                        }
                });
            },
            FuncQuery1(){
                this.queryError=false;
                this.query.id=1;
                this.queryRes='';
                this.query.info="List of Drivers on a Route and their Schedules";
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/route/",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            this.routes = response.data.data;
                        }
                });
            },
            CompQuery1(id){
                console.log(this.tab_active_q1);
                this.tab_active_q1 = 0;
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/dr_on_r/",
                        type: "GET",
                        data: {route: id},
                        success: (response) => {
                            this.queryfin = response.data;
                            if (response.data.drivers.length > 0){
                                this.queryRes = true;
                                this.queryError = false;
                            }else {
                                this.queryError = true;
                            };
                        }
                });
            },
            FuncQuery2 (){
                this.queryError=false;
                this.queryRes='';
                this.query.id=2;
                this.query.info="Time when Buses start and stop on each Route";
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/bus_on_r/",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            this.queryfin = response.data.data;
                        }
                });
            },
            FuncQuery3 (){
                this.queryError=false;
                this.queryRes='';
                this.query.id=3;
                this.query.info="Total time of all Routes";
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/routes_time/",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            var to_change = response.data.data.circle_time_min__sum
                            var hours = Math.floor(to_change / 60)
                            this.queryfin =
                                `${hours}h.${to_change-hours*60}m.`
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
            },
            FuncQuery4() {
                this.queryError=false;
                this.queryRes='';
                this.query.id=4;
                this.query.info="Buses, which missed schedule, and reasons for it";

            },
            CompQuery4(){
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/bad_report/",
                        type: "GET",
                        data: {work_day: this.formQuery.date1.toISOString().slice(0,10)},
                        success: (response) => {
                            this.queryfin = response.data;
                            if (response.data.data.length > 0){
                                this.queryRes = true;
                                this.queryError = false;
                            } else {
                                this.queryError = true;
                            };
                        }
                });
            },
            FuncQuery5() {
                this.queryRes='';
                this.query.id=5;
                this.query.info="Number of drivers for each job class";
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/dr_class/",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            this.queryfin = response.data;
                            if (response.data.length > 0){
                                this.queryRes = true;
                                this.queryError = false;
                            } else {
                                this.queryError = true;
                            };
                        }
                });

            },
            FuncQueryReport (){
                this.queryRes='';
                this.query.id=6;
                this.getRoute();
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/report_buses/",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            this.queryReportfin = response.data;
                            this.r_for_t = [response.data.r_for_t1,
                                            response.data.r_for_t2,
                                            response.data.r_for_t3,
                                            response.data.r_for_t4,
                                            response.data.r_for_t5];

                        }
                });

                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/driver/",
                        type: "POST",
                        data: {},
                        success: (response) => {
                            this.drivers = response.data.data;
                        }
                });

                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/routes_time/",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            var to_change = response.data.data.circle_time_min__sum
                            var hours = Math.floor(to_change / 60)
                            this.total_time_routes =
                                `${hours}h.${to_change-hours*60}m.`
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

            },
            goLogin(){
                this.$router.push({name:"login"})
            },
            goLogout(){
                sessionStorage.removeItem("auth_token"),
                window.location = "/"
            },
            viewBus(id){
                this.bus.id = id
                this.bus.show = true
            },
            goDrivers() {
                this.$router.push({name:"drivers"})
            },
            goQueries() {
                this.$router.push({name:"queries"})
            },
            goReport() {
                this.$router.push({name:"report"})
            },
            goHome(){
                this.$router.push({name:"home"})
            },
            goBusMal(){
                this.$router.push({name:"busmals"})
            },
            goSchedReport(){
                this.$router.push({name:"schedreport"})
            },

       }
    };
</script>

<style scoped>

    .query_title {
            background:#e0ebff;
            border-radius: 8px;
            margin:1px;
            padding-left:10px
    }
</style>
