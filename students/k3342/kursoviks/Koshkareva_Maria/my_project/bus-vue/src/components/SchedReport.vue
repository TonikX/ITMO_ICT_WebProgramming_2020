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
    <mu-paper style="background:lightGrey;border-radius:8px 8px 0 0; ">
            Next</mu-paper>
    <mu-paper :z-depth="1">

        <mu-paper v-if="schedRepNext == null" style="padding:1%; background:#ededed">
            No next schedules</mu-paper>


        <mu-paper v-else style="background:#ededed">
            <mu-row gutter>
                <mu-col span="1" style="padding-left:2%">
                    <mu-tooltip :content="schedRepNext.reason" placement="left">
                                <mu-button disabled icon >
                                    <mu-icon v-if="schedRepNext.reason == 'OK'"
                                        value="check_circle"
                                            color="green"></mu-icon>
                                    <mu-icon v-else
                                        :value="reasonsInfo[schedRepNext.reason]"
                                            color="deepOrange500"></mu-icon>
                                 </mu-button>
                        </mu-tooltip>
                </mu-col>
                <mu-col span="1" style="padding-top:1.2%;padding-left:1.5%;margin-right:-2.5%">
                    {{schedRepNext.schedule_line.bus.reg_plate}}
                </mu-col>
                <mu-col span="3" style="padding-top:1.2%;margin-right:-1.5%">
                    {{schedRepNext.schedule_line.driver.surname}}
                        ({{schedRepNext.schedule_line.driver.passport}})
                </mu-col>
                <mu-col span="2" style="padding-top:1.2%;margin-right:3.2%">
                    {{schedRepNext.schedule_line.route.num}}
                </mu-col>
                <mu-col span="1" style="padding-top:1.2%;padding-left:1.5%;margin-right:1.3%">
                    {{schedRepNext.schedule_line.work_day}}
                </mu-col>
                <mu-col span="2" style="padding-top:1.2%;margin-right:1.5%">
                    {{schedRepNext.schedule_line.work_start}}
                </mu-col>
                <mu-col span="1" style="padding-top:1.2%">
                    {{schedRepNext.schedule_line.work_end}}
                </mu-col>
            </mu-row>
     </mu-paper>
<!--
        <mu-data-table v-else stripe :columns="columns"
                       style="background:#ededed"
                               :data="[schedRepNext]"  border>
            <template slot-scope="scope_next" >
                    <td >
                        <mu-tooltip :content="scope_next.row.reason" placement="left">
                                <mu-button disabled icon >
                                    <mu-icon v-if="scope_next.row.reason == 'OK'"
                                        value="check_circle"
                                            color="green"></mu-icon>
                                    <mu-icon v-else
                                        :value="reasonsInfo[scope_next.row.reason]"
                                            color="deepOrange500"></mu-icon>
                                 </mu-button>
                        </mu-tooltip>

                    </td>
                    <td>{{scope_next.row.schedule_line.bus.reg_plate}}</td>
                    <td>
                        {{scope_next.row.schedule_line.driver.surname}}
                        ({{scope_next.row.schedule_line.driver.passport}})

                    </td>
                    <td>{{scope_next.row.schedule_line.route.num}}</td>
                    <td>{{scope_next.row.schedule_line.work_day}}</td>
                    <td>{{scope_next.row.schedule_line.work_start}}</td>
                    <td>{{scope_next.row.schedule_line.work_end}}</td>
            </template>
        </mu-data-table>-->

    </mu-paper>
    <br>

<mu-paper :z-depth="1">
    <mu-data-table stripe :columns="columns"
                               :data="schedReps"  border>
        <template slot-scope="scope" >

                    <td >
                        <mu-tooltip :content="scope.row.reason" placement="left">
                                <mu-button icon @click="openReport(scope.row)">
                                    <mu-icon v-if="scope.row.reason == 'OK'"
                                        value="check_circle"
                                            color="green"></mu-icon>
                                    <mu-icon v-else
                                        :value="reasonsInfo[scope.row.reason]"
                                            color="deepOrange500"></mu-icon>
                                 </mu-button>
                            </mu-menu>
                        </mu-tooltip>

                    </td>
                    <!--
                    <td v-else style="background:#ffd3bd">{{scope.row.reason}}</td>
                    -->
                    <td>{{scope.row.schedule_line.bus.reg_plate}}</td>
                    <td>
                        {{scope.row.schedule_line.driver.surname}}
                        ({{scope.row.schedule_line.driver.passport}})

                    </td>
                    <td>{{scope.row.schedule_line.route.num}}</td>
                    <td>{{scope.row.schedule_line.work_day}}</td>
                    <td>{{scope.row.schedule_line.work_start}}</td>
                    <td>{{scope.row.schedule_line.work_end}}</td>
        </template>
    </mu-data-table>
</mu-paper>

</mu-container>


<mu-dialog width="370"
                     :open.sync="ReportDialog">
            <mu-paper v-if="report" style="width: 100%;
                        max-width: 380px; margin:0 auto;
                        padding:3%" :z-depth="1">
                <mu-row gutter style="margin-bottom:-8%">
                    <mu-col span="6">
                         <mu-text-field full-width :placeholder="report.schedule_line.bus.reg_plate"
                               label="Bus" disabled>
                         </mu-text-field>
                    </mu-col>
                    <mu-col>
                        <mu-text-field full-width
                                       v-bind:placeholder="report.schedule_line.driver.name+' '
                                                            +report.schedule_line.driver.surname"
                               label="Driver" disabled>
                         </mu-text-field>
                    </mu-col>
                </mu-row >
                <mu-row gutter style="margin-bottom:-8%">
                    <mu-col span="6">
                         <mu-text-field full-width :placeholder="report.schedule_line.route.num"
                               label="Route" disabled>
                         </mu-text-field>
                    </mu-col>
                    <mu-col>
                        <mu-text-field full-width
                                       :placeholder="report.schedule_line.work_day"
                               label="Day" disabled>
                         </mu-text-field>
                    </mu-col>
                </mu-row>
                <mu-row gutter style="margin-bottom:-5%">
                    <mu-col span="6">
                         <mu-text-field full-width :placeholder="report.schedule_line.work_start"
                               label="Starts at" disabled>
                         </mu-text-field>
                    </mu-col>
                    <mu-col>
                        <mu-text-field full-width
                                       :placeholder="report.schedule_line.work_end"
                               label="Ends at" disabled>
                         </mu-text-field>
                    </mu-col>
                </mu-row>

                <mu-select style="margin-bottom:-2%"
                    full-width label="Reason" v-model="formEditRep.reason">
                    <mu-option v-for="option in reasons" :key="option[1]"
                               :label="option[0]" :value="option[1]">
                    </mu-option>
                </mu-select>


            </mu-paper><mu-flex justify-content="end">
               <mu-button flat color="deepOrange" @click="ReportDialog = !ReportDialog">Back</mu-button>
               <mu-button color="deepOrange" @click="EditReport">Edit</mu-button>
            </mu-flex>
</mu-dialog>

    </div>
</template>

<script>
    import $ from 'jquery'


    export default {
       name:"BusMals",
       props: {
            id: ''
       },
       data(){
            return{
                openScore: false,
                report:'',
                ReportDialog: false,
                driver: '',
                openDrawer: false,
                reasonsInfo: {
                    "Broken bus":"build",
                    "Sick driver":"hotel",
                    "No driver":"watch_later",
                    "Other":"help",
                },
                schedReps:'',
                schedRepNext:'',
                reasons:[
                    ['OK',0],['Broken bus',1],['Sick driver',2],
                    ['No driver',3],['Other',4]],
                formEditRep:{
                    reason:''
                },
                columns: [
                    { title:'Reason',width:90},
                    { title:'Bus',width:120},
                    { title:'Driver',width:270},
                    { title:'Route'},
                    { title: 'Day'},
                    { title:'Starts at'},
                    { title:'Ends at'},
                ],

            }
       },

       created(){
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' +
                        sessionStorage.getItem('auth_token')}
            });
            this.loadSchedReps();

       },
       computed: {
            auth(){
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
       methods: {
            EditReport(){
                 $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/schedule_report/"+
                        this.report.id+"/",
                        type: "PUT",
                        data: {
                            reason:this.formEditRep.reason,
                        },
                        success: (response) => {
                            this.loadSchedReps();
                            this.ReportDialog = false;
                        }
                 });
            },
            openReport(row){
                this.ReportDialog = true;
                this.report = row;
                this.formEditRep.reason = this.reasons.find(el => el[0] == row.reason)[1];
            },
            loadSchedReps(){
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/schedule_reports/",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            this.schedReps = response.data.available;
                            this.schedRepNext = response.data.next[0];
                        }
                });
            },
            viewScore(driver_id){
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/driver",
                        type: "GET",
                        data: {
                            id: driver_id
                        },
                        success: (response) => {
                            this.driver= response.data.data[0];
                        }
                });
                this.openScore = true;

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
