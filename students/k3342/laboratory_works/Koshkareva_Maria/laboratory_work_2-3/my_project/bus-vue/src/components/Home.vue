<template>
        <div>
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
            <br>

     <mu-row>
            <Schedule v-if="auth" @viewBus="viewBus"></Schedule>
            <mu-container v-else>
                    <mu-card class="card" style="width:55%; max-width:375px; margin:0 auto;">
                         <mu-card-header class="card_head">
                             <h1>No Strangers</h1>
                             Please, log in!
                         </mu-card-header>
                        <br>
                        <mu-flex justify-content="center">

                            <br></mu-flex>
                    </mu-card>
            </mu-container>
         <Buses v-if="auth" :id="bus.id"></Buses>
        </mu-row>



</mu-container>
</div>

</template>

<script>
    import Schedule from "@/components/Buses/Schedule.vue"
    import Buses from "@/components/Buses/Buses.vue"
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
        name: "Home",
        components: {
            Schedule,
            Buses
        },
        data() {
            return {
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
