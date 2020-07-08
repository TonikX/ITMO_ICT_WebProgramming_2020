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

<mu-container >
    <br>
            <mu-tabs :value.sync="tab_active" color="indigo400"
                            indicator-color="indigo400">
                                <mu-tab>BUS TYPES</mu-tab>
                                <mu-tab>DRIVERS</mu-tab>
                                <mu-tab>ROUTES</mu-tab>
                              </mu-tabs>
            <mu-paper :z-depth="1" style="padding:10px" v-if="tab_active === 0">

                <mu-row style="background:#dbdbdb; border-radius:6px;
                                 padding:4px; margin:7px">
                    <mu-col span="3">Bus Types</mu-col>

                    <mu-col>Routes</mu-col>
                </mu-row>
                <mu-row v-for="line in queryReportfin.bus_types"
                style="background:#f5f5f5; border-radius:8px;
                                border-style:solid; border-width:2px;
                                border-color:#dbdbdb; margin:7px">
                 <mu-col span="3">
                   <mu-card style=" margin:8px" >
                        <mu-card-media>
                            Type: <b>{{type_names[line.type-1]}}</b>
                            <img v-bind:src="require('@/assets/images/bus_type'+line.type+'.png')"
                            >
                        </mu-card-media>
                       <mu-card-text style="background:#a7c8fa">
                           Total Number: <b>{{line.id__count}}</b>
                      </mu-card-text>
                   </mu-card>
                  </mu-col>

                <mu-col>
                  <mu-row v-for="route in r_for_t[line.type]" style="margin:10px; ">
                        <mu-row style="width:100%;">
                            <b>Route: {{routes.filter(r => r.id == route.route)[0].num}}</b>
                        </mu-row>
                        <mu-row gutter style="width:100%;">
                            <mu-col span="6"><mu-text-field full-width label="First stop" disabled
                            :placeholder="routes.filter(r => r.id == route.route)[0].loc_start">
                            </mu-text-field></mu-col>
                            <mu-col><mu-text-field full-width label="Last stop" disabled
                            :placeholder="routes.filter(r => r.id == route.route)[0].loc_end">
                            </mu-text-field></mu-col>
                        </mu-row>
                        <mu-row gutter>
                            <mu-col span="3"><mu-text-field full-width label="Buses start at" disabled
                            :placeholder="routes.filter(r => r.id == route.route)[0].time_start.slice(0,-3)">
                            </mu-text-field></mu-col>
                            <mu-col><mu-text-field full-width label="Buses stop at" disabled
                            :placeholder="routes.filter(r => r.id == route.route)[0].time_end.slice(0,-3)">
                            </mu-text-field></mu-col>
                            <mu-col><mu-text-field full-width label="Interval (minutes)" disabled
                            :placeholder="routes.filter(r => r.id == route.route)[0].interval_min">
                            </mu-text-field></mu-col>
                            <mu-col><mu-text-field full-width label="Circle (minutes)" disabled
                            :placeholder="routes.filter(r => r.id == route.route)[0].circle_time_min">
                            </mu-text-field></mu-col>
                        </mu-row>

                      <mu-row style="width:100%; margin:10px;" gutter>
                          <mu-col span="5" >
                            <mu-paper :z-depth="1" style="background:#e0ebff">
                                <b>Buses:</b>
                              <mu-col v-for="ThatBus in getBusDrOnRoute(route.route)">
                                  {{ThatBus}}
                              </mu-col>
                            </mu-paper>
                          </mu-col>
                          <mu-col>
                            <mu-paper :z-depth="1" style="background:#e0ebff">
                                <b>Drivers:</b>
                              <mu-col v-for="ThatDr in Object.values(drivers).filter(r => r.route.id == route.route)">
                                  {{ThatDr.name}} {{ThatDr.surname}} ({{ThatDr.passport}})
                              </mu-col>
                            </mu-paper>
                          </mu-col>
                      </mu-row>
                      <mu-divider></mu-divider><mu-divider></mu-divider>
                  </mu-row>

                </mu-col>
              </mu-row>
            </mu-paper>

        <mu-paper :z-depth="1" style="padding:10px" v-if="tab_active === 1">
            <mu-row style="width:70%;margin: auto">
                    <mu-data-table stripe
                               :columns="[{title:'Driver'},{title:'Age',sortable:true},
                                                {title:'Experience (years)'}]"
                               :data="queryReportfin.age_exp"  border
                               :sort.sync="sort" @sort-change="handleSortChange"
                                style="border-radius: 8px;width:100%">
                       <template slot-scope="scope" >
                        <td>
                            {{scope.row.name}} {{scope.row.surname}}
                            ({{scope.row.passport}})
                        </td>
                        <td>{{Math.floor(scope.row.age/365.25)}} </td>
                           <td>{{Math.floor(scope.row.exp_days/365.25)}} </td>
                        </td>
                      </template>
                    </mu-data-table>
                <mu-row style="width:100%;">
                    <mu-col span="4"></mu-col>
                    <mu-col >
                        <mu-paper :z-depth="2"
                                      style="border-radius:8px;
                                      background:#a7c8fa;margin:2px;
                                      padding:3px">
                            Average Age: <b>{{Math.floor(queryReportfin.avg_age_exp.age__avg/365.25)}}</b>
                        </mu-paper>
                    </mu-col>
                    <mu-col>
                        <mu-paper :z-depth="2"
                                      style="border-radius:8px;
                                      background:#a7c8fa;margin:2px;
                                      padding:3px">
                            Average Experience: <b>{{Math.floor(queryReportfin.avg_age_exp.exp_days__avg/365.25)}}</b>
                        </mu-paper>
                    </mu-col>

                </mu-row>
            </mu-row>

        </mu-paper>
    <mu-paper :z-depth="1" style="padding:10px; width:100%" v-if="tab_active === 2">
        <mu-row style="width:40%;margin: auto">
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

        <mu-row style="width:100%">
            <mu-col span="6"></mu-col>
            <mu-col>
                <mu-paper :z-depth="2"
                                      style="border-radius:8px;
                                      background:#a7c8fa;margin:2px;
                                      padding:3px">
                    Total Time: <b>{{total_time_routes}}</b>
                </mu-paper>
            </mu-col>
        </mu-row>
</mu-row>
    </mu-paper>
</mu-container>

    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
       name:"Report",
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
                    id:'',
                    info:'',
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

       created(){
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' +
                        sessionStorage.getItem('auth_token')}
            });
            this.FuncQueryReport();

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
                        url: "http://127.0.0.1:8000/api/v1/bus_info/all_drivers/",
                        type: "GET",
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
