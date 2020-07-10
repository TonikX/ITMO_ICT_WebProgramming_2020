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



<mu-container >

    <mu-flex justify-content="end">
        <mu-button flat style="margin-top:2%; ;
                    background:lightGreen; border-radius:8px 8px 0 0;"
                    @click="openAddDial">
                        add
               </mu-button>
    </mu-flex>

    <mu-paper style="border-style: solid; border-width: 2px;
                        border-radius:10px; border-color: silver;
                         padding: 2%; margin:0 -5%"
                :z-depth="5">
    <mu-row gutter >
        <mu-col v-for="line in busmals_open" span="3" style="padding-bottom: 1%">
            <mu-flex style="background:#e0ebff;
                    border-radius:10px 10px 0 0;
                    padding:3%;">
                <mu-row>
                <mu-col span="2" >{{line.bus.reg_plate}}</mu-col>
                <mu-col span="2" offset="8" style="margin:-10%;left:+230%">
                    <mu-button v-if="Object.values(schedules).filter(s => s.bus.id == line.bus.id).length > 0"
                               icon
                               style="margin:-20%" color="red500"
                        @click="openScheds(line)">
                      <mu-icon value="error"></mu-icon>
                    </mu-button>
                </mu-col>
                </mu-row>
            </mu-flex>

            <mu-paper :z-depth="2" style="padding:0 4% 4% 4%">
                <mu-row gutter >
                    <mu-col>
                        <mu-date-input full-width
                                       disabled v-model="formBusMal.date_start" type="date"
                                       label="First day" :placeholder="line.date_start">
                        </mu-date-input>
                    </mu-col>
                    <mu-col>
                        <mu-date-input full-width
                                       disabled v-model="formBusMal.date_close" type="date"
                                       label="Last day" :placeholder="line.date_close">
                        </mu-date-input>
                    </mu-col>
                </mu-row>
                <mu-row>
                    <mu-text-field v-model="formBusMal.piece" style="min-height: 10px; "
                                   :placeholder="line.piece" multi-line
                                   :rows-max="3" :rows="3"
                                     label="Pieces">
                    </mu-text-field>
                </mu-row>
                <mu-row>
                    <!--
                    <mu-chip style="margin:1%"
                             class="demo-chip" v-for="chip, index in line.piece_now"
                             :key="chip" @delete="remove(line.id,chip)"
                             delete>
                        {{piece_list[chip]}}
                    </mu-chip>-->

                    <mu-chip style="margin:1%"
                             class="demo-chip"
                             v-for="one_piece in line.piece_now.split(', ').filter(p => p !== '')"
                             :key="one_piece" @delete="remove(busmals_open, line.id,one_piece)"
                             delete>
                        {{one_piece}}
                    </mu-chip>

                </mu-row>

            </mu-paper>
        </mu-col>
    </mu-row>
    </mu-paper>

    <mu-row gutter style="padding-top:3%">
        <mu-col v-for="line in busmals_closed" span="3" style="padding-bottom:1.5%">
            <mu-flex style="background:silver;
                    border-radius:10px 10px 0 0;
                    padding:3% 3% 3% 5%;">
                {{line.bus.reg_plate}}</mu-flex>
            <mu-paper :z-depth="1" style="padding:0 4% 4% 4%">
                <mu-row gutter >
                    <mu-col>
                        <mu-date-input full-width
                                       disabled v-model="formBusMal.date_start" type="date"
                                       label="First day" :placeholder="line.date_start">
                        </mu-date-input>
                    </mu-col>
                    <mu-col>
                        <mu-date-input full-width
                                       disabled v-model="formBusMal.date_close" type="date"
                                       label="Last day" :placeholder="line.date_close">
                        </mu-date-input>
                    </mu-col>
                </mu-row>
                <mu-row>
                    <mu-text-field v-model="formBusMal.piece" style="min-height: 10px; "
                                   :placeholder="line.piece" multi-line
                                   :rows-max="3" :rows="3"
                                     label="Pieces">
                    </mu-text-field>
                </mu-row>
                <mu-row>
                    <!--
                    <mu-chip style="margin:1%"
                             class="demo-chip" v-for="chip, index in line.piece_now"
                             :key="chip" @delete="remove(line.id,chip)"
                             delete>
                        {{piece_list[chip]}}
                    </mu-chip>-->

                    <mu-chip style="margin:1%"
                             class="demo-chip"
                             v-for="one_piece in line.piece_now.split(', ').filter(p => p !== '')"
                             :key="one_piece" @delete="remove(busmals_closed,line.id,one_piece)"
                             delete>
                        {{one_piece}}
                    </mu-chip>
                </mu-row>

            </mu-paper>
        </mu-col>
    </mu-row>
</mu-container>


<mu-dialog :open.sync="openDT" :overlay-close="false">
    <mu-paper>

        <mu-data-table
                    :selectable="sel_table.selectable_v"
                               :checkbox="sel_table.checkbox_v"
                               :selects.sync="selects"
                               :select-all="sel_table.select_all_v"
                               stripe :columns="columnsSched"
                               :data="filtered_scheds"  border>
                   <template slot-scope="scope" >
                    <td>
                        {{scope.row.driver.surname}}
                        ({{scope.row.driver.passport}})
                    </td>
                    <td>{{scope.row.bus.reg_plate}}</td>
                    <td>{{scope.row.route.num}}</td>
                    <td>{{scope.row.work_day}}</td>
                    <td>{{scope.row.work_start}}</td>
                    <td>{{scope.row.work_end}}<br>
                    </td>
                  </template>
                </mu-data-table>
    </mu-paper>

    <mu-flex v-if="sel_table.selectable_v" justify-content="end">
                      <mu-button flat color="deepOrange" @click="chooseSch(false)">Back</mu-button>
                      <mu-button color="deepOrange300" @click="delSchSubmit(selects)">Delete</mu-button>
                      <mu-button color="deepOrange" @click="askEditSched(selects)">Edit</mu-button>

                  </mu-flex>
                  <mu-flex v-else justify-content="end">
                      <mu-button flat color="deepOrange" @click="chooseSch(false)">Back</mu-button>
                      <mu-button color="deepOrange" @click="chooseSch(true)">Choose</mu-button>
                  </mu-flex>
</mu-dialog>


<mu-dialog :open.sync="openEdit" :overlay-close="false" v-if="toEdit.driver">
    <mu-paper>
        <mu-row gutter style="margin-bottom:-5%">
            <mu-col span="4">
                <mu-text-field full-width :placeholder="toEdit.driver.passport"
                               label="Driver" disabled>
                </mu-text-field>
            </mu-col>
            <mu-col span="4">
            <mu-text-field full-width :placeholder="toEdit.route.num"
                           label="Route" disabled>
            </mu-text-field>
            </mu-col>
        </mu-row>
        <mu-row gutter style="margin-bottom:-5%">
            <mu-col span="4">
                <mu-select full-width label="Bus" v-model="formEditSch.bus">
                    <mu-option v-for="option,index in workingBuses" :key="option.reg_plate"
                               :label="option.reg_plate" :value="option.id"
                                >
                    </mu-option>
                </mu-select>
            </mu-col>
                <mu-col span="4">
                    <mu-date-input full-width label="Day" :min-date="minDate"
                                   v-model="formEditSch.work_day"
                                   type="date" display-color="deepOrange"
                                   :date-time-format="enDateFormat">
                    </mu-date-input>
                </mu-col>
        </mu-row>
        <mu-row gutter>
            <mu-col span="4">
                <mu-text-field full-width :placeholder="toEdit.work_start"
                           label="Start at" disabled>
            </mu-text-field>
            </mu-col>
                <mu-col span="4">
                   <mu-text-field full-width :placeholder="toEdit.work_end"
                           label="Finish at" disabled>
            </mu-text-field>
                </mu-col>
        </mu-row>
        <mu-flex justify-content="end">
           <mu-button flat color="deepOrange" @click="openEdit = !openEdit">Back</mu-button>
           <mu-button color="deepOrange" @click="editSched">Edit</mu-button>
        </mu-flex>
    </mu-paper>
</mu-dialog>




<mu-dialog :open.sync="openAdd" width="350"
           :overlay-close="false" >
    <mu-paper :z-depth="1" >

            <mu-flex style="background:#e0ebff;
                    border-radius:10px 10px 0 0;
                    padding-left:3%;margin-bottom:-7%">
                <mu-row>
                    <mu-col>
                        <mu-select  label="Bus" v-model="formAdd.bus">
                            <mu-option v-for="option,index in workingBuses" :key="option.reg_plate"
                                       :label="option.reg_plate" :value="option.id"
                                        >
                            </mu-option>
                        </mu-select>
                    </mu-col>
                </mu-row>
            </mu-flex>

            <mu-paper :z-depth="2" style="padding:0 4% 4% 4%">
                <mu-row gutter >
                    <mu-col>
                        <mu-date-input full-width :date-time-format="enDateFormat"
                                       v-model="formAdd.date_start" type="date"
                                       label="First day" display-color="deepOrange">
                        </mu-date-input>
                    </mu-col>

                </mu-row>
                <mu-row>
                </mu-row>
                <mu-row>

                    <mu-select label="Pieces" multiple chips
                               v-model="formAdd.piece" full-width>
                        <mu-option v-for="name,index in 'engine, tyres, oil filter, lights, turn signals, steering wheel, other'.split(', ')"
                                   :key="name" :label="name" :value="name">
                        </mu-option>
                      </mu-select>

                </mu-row>

                <mu-flex justify-content="end">
                   <mu-button flat color="deepOrange" @click="openAdd = !openAdd">Back</mu-button>
                   <mu-button color="deepOrange" @click="addMalBus">Add</mu-button>
                </mu-flex>
            </mu-paper>
    </mu-paper>
</mu-dialog>


<mu-snackbar position="bottom" :open.sync="snackbar.open">
    <mu-icon value="done" left></mu-icon>
    The schedule line was deleted!
</mu-snackbar>

<mu-snackbar position="bottom" :open.sync="snackbarEdit.open">
    <mu-icon value="done" left></mu-icon>
    The schedule line was edited!
</mu-snackbar>

<mu-snackbar position="bottom" :open.sync="snackbarAdd.open">
    <mu-icon value="done" left></mu-icon>
    The mulfunction line was added!
</mu-snackbar>

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
       name:"BusMals",
       props: {
            id: ''
       },
       data(){
            const minDate = new Date();
            minDate.setDate(minDate.getDate());
            return{

                openAdd: false,
                enDateFormat,
                minDate,
                toEdit:[],
                snackbar: {
                    open: false,
                    timeout: 3000,
                },
                snackbarEdit: {
                    open: false,
                    timeout: 3000,
                },
                snackbarAdd: {
                    open: false,
                    timeout: 3000,
                },
                workingBuses:'',
                brokenBuses:'',
                buses:'',
                schedules:'',
                filtered_scheds:'',
                openDT: false,
                openEdit: false,
                sel_table: {
                    selectable_v: false,
                    checkbox_v: false,
                    select_all_v: false,
                },
                selects: [],
                piece_list: {
                    1:'engine',
                    2:'tyres',
                    3:'oil filter',
                    4:'lights',
                    5:'turn signals',
                    6:'steering wheel',
                    7:'rear-view mirrors',
                    8:'other',
                },
                columnsSched: [
                    { title:'Driver', width:250},
                    { title:'Bus',width:110},
                    { title:'Route',width:80},
                    { title: 'Day'},
                    { title:'Starts at'},
                    { title:'Ends at'},
                ],
                openDrawer: false,
                busmals_open: '',
                busmals_closed: '',
                columns: [
                    { title:'Bus'},
                    { title:'First day'},
                    { title:'Final day'},
                    { title:'Pieces'},
                ],
                formBusMal: {
                    date_start:'',
                    date_close:'',
                    piece:[],
                    piece_now:[],
                },
                formEditSch: {
                    bus:'',
                    work_day:'',
                },
                formAdd: {
                    date_start:'',
                    bus:'',
                    piece:[],
                },
            }
       },

       created(){
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' +
                        sessionStorage.getItem('auth_token')}
            });
            this.loadBusMals();
            this.loadSchedule();

       },
       computed: {
            auth(){
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
       methods: {
            addMalBus(){
                console.log(this.formAdd.bus)
                var local_date_start = new Date(this.formAdd.date_start.getTime() -
                                    (this.formAdd.date_start.getTimezoneOffset()*60000))
                                    .toISOString().split("T")[0];
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/malfunction/",
                        type: "POST",
                        data: {
                            bus:this.formAdd.bus,
                            date_start:local_date_start,
                            piece:this.formAdd.piece.join(', '),
                        },
                        success: (response) => {
                            this.openAdd = false;
                            this.loadSchedule();
                            this.loadBusMals();
                            if (this.snackbarAdd.timer) clearTimeout(this.snackbarAdd.timer);
                            this.snackbarAdd.open = true;
                            this.snackbarAdd.timer = setTimeout(() => {
                                    this.snackbarAdd.open = false;
                                  },
                                  this.snackbarAdd.timeout);
                        }
                });

            },
            openAddDial(){
                this.openAdd = true;
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/buses_status",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            this.workingBuses = response.data.working;
                        }
                });
            },
            askEditSched(s){
                 $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/buses_status",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            this.workingBuses = response.data.working;
                        }
                });
                this.openEdit = true;
                this.formEditSch.bus = this.filtered_scheds[s[0]].bus.id
                var local_date = new Date(new Date(this.filtered_scheds[s[0]].work_day).getTime()
                                    -(new Date(this.filtered_scheds[s[0]].work_day).getTimezoneOffset()*60000));
                this.formEditSch.work_day = local_date;
                this.toEdit = this.filtered_scheds[s[0]];

            },
            editSched(){
                var local_work_day = new Date(this.formEditSch.work_day.getTime() -
                                    (this.formEditSch.work_day.getTimezoneOffset()*60000))
                                    .toISOString().split("T")[0]

                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/bus_info/schedule/"
                        + this.filtered_scheds[0].id + "/",
                    type: "PUT",
                    data: {
                        bus:this.formEditSch.bus,
                        work_day:local_work_day,
                    },
                    success: (response) => {
                        this.loadSchedule();
                        this.loadBusMals();
                        this.chooseSch(false);
                        this.openEdit = false;
                        if (this.snackbarEdit.timer) clearTimeout(this.snackbarEdit.timer);
                            this.snackbarEdit.open = true;
                            this.snackbarEdit.timer = setTimeout(() => {
                                    this.snackbarEdit.open = false;
                                  },
                                  this.snackbarEdit.timeout);
                    }
                });
            },
            delSchSubmit(s){
                for (let i = 0; i < s.length; ++i) {
                    $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/schedule/"
                                + this.schedules[s[i]].id + "/",
                        type: "DELETE",
                        success: (response) => {
                            this.loadSchedule();
                            this.chooseSch(false);
                            if (this.snackbar.timer) clearTimeout(this.snackbar.timer);
                            this.snackbar.open = true;
                            this.snackbar.timer = setTimeout(() => {
                                    this.snackbar.open = false;
                                  },
                                  this.snackbar.timeout);
                        }
                    });
                }
            },
            chooseSch(value){
                this.sel_table.selectable_v = value;
                this.sel_table.checkbox_v = value;
                this.sel_table.select_all_v = value;
                this.openDT = value;
            },
            openScheds(the_busmal){
                this.filtered_scheds = Object.values(this.schedules).filter(s => s.bus.id == the_busmal.bus.id)
                this.openDT = true;
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
            remove(open_closed,busmal_id,piece_name){
                var the_busmal = Object.values(open_closed).filter(mal => mal.id == busmal_id);
                var changed_piece_now = the_busmal[0].piece_now.split(', ').filter(mal => mal !== piece_name);
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/malfunction/"+busmal_id+"/",
                        type: "PUT",
                        data: {
                            piece_now: changed_piece_now.join(', ')
                        },
                        success: (response) => {
                            this.loadBusMals();
                        }
                });
            },
            loadBusMals(){
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/malfunction/",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            this.busmals_open = response.data.open;
                            this.busmals_closed = response.data.closed;
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
