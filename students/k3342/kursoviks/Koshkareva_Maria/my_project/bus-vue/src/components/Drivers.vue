<template>
<body>
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
    <div style="position:relative;">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
        <mu-container>

            <mu-snackbar position="bottom" :open.sync="snackbar.open">
                <mu-icon value="done" left></mu-icon>
            The driver was deleted!
          </mu-snackbar>


            <mu-paper :z-depth=1
                      style="top:0;position:sticky;z-index:99;margin: 0% -5%">
                <mu-row>
                    <mu-col v-for="letter in alphabet" style="font-size:115%;">
                        <mu-col v-if="Object.values(drivers).filter(driver => driver.surname.startsWith(letter)).length >0"
                            style="cursor: pointer;" @click="">
                            <a v-bind:href="'#'+letter" style="color:#eb4f34">
                                <b>{{letter}}</b></a></mu-col>
                        <mu-col v-else style="color:silver">
                            {{letter}}</mu-col>
                    </mu-col>
                </mu-row>
            </mu-paper>

               <mu-button flat style="margin-top:2%; left:+40%;
                    background:lightGreen; border-radius:8px 8px 0 0;"
                    @click="addDriver">
                        add
               </mu-button>


            <mu-dialog :overlay-opacity="0.2"
                       :open.sync="openDialog"
                       :overlay-close="false"
                        >
                <mu-row gutter >
                    <mu-col >
                <mu-card raised style="max-width:400px">
                    <mu-card-header v-bind:title="form.name+' '+form.surname"
                                    :sub-title="form.passport">
                        <mu-avatar slot="avatar">
                          <img v-if="img_link" v-bind:src="require('@/assets/images/driver'
                     +max_id+'.jpg')" />
                          <img v-else src="@/assets/images/man0.png">
                        </mu-avatar>
                      </mu-card-header>
                      <mu-card-media>
                        <img v-if="img_link" v-bind:src="require('@/assets/images/driver'
                     +max_id+'.jpg')" />
                        <img v-else src="@/assets/images/man0.png">
                    </mu-card-media>
                </mu-card></mu-col>
                <mu-col>

                   <mu-form :model="form">
                       <mu-row gutter>
                           <mu-col>
                                <mu-form-item label="Surname" >
                                  <mu-text-field v-model="form.surname"></mu-text-field>
                                </mu-form-item></mu-col>
                           <mu-col>
                                <mu-form-item label="Name">
                                  <mu-text-field v-model="form.name"></mu-text-field>
                                </mu-form-item></mu-col>
                       </mu-row>
                       <mu-row>
                           <mu-col>
                               <mu-form-item label="Passport" >
                                  <mu-text-field v-model="form.passport"
                                            :max-length="10"></mu-text-field>
                               </mu-form-item>
                           </mu-col>
                       </mu-row>
                       <mu-row gutter>
                           <mu-col>
                               <mu-form-item label="Year" >
                                   <mu-date-input display-color="deepOrange"
                                                v-model="form.d_of_b"
                                                 type="date" :max-date="maxDate"
                                            :date-time-format="enDateFormat">
                                   </mu-date-input>
                               </mu-form-item>
                           </mu-col>

                       </mu-row>

                       <mu-row gutter>
                           <mu-col>
                                <mu-form-item label="Bus" >
                                    <mu-select v-model="form.bus">
                                        <mu-option v-for="option in buses" :key="option.id"
                                               :label="option.reg_plate.toString()" :value="option.id">
                                    </mu-option>
                                  </mu-select>
                                </mu-form-item></mu-col>
                           <mu-col>
                                <mu-form-item label="Route">
                                    <mu-select v-model="form.route">
                                        <mu-option v-for="option,index in routes" :key="option.id"
                                               :label="option.num.toString()" :value="option.id">
                                    </mu-option>
                                  </mu-select>
                                </mu-form-item></mu-col>
                       </mu-row>
                       <mu-row gutter>
                           <mu-col span="6">
                               <mu-form-item label="Started working" >
                                   <mu-date-input display-color="deepOrange"
                                                v-model="form.date_begin"
                                                 type="date"
                                            :date-time-format="enDateFormat">
                                   </mu-date-input>
                               </mu-form-item>
                           </mu-col>
                           <mu-col>
                                <mu-form-item prop="radio" label="Driver class">
                                  <mu-radio v-model="form.job_class" value="1" label="1"></mu-radio>
                                  <mu-radio v-model="form.job_class" value="2" label="2"></mu-radio>
                                  <mu-radio v-model="form.job_class" value="3" label="3"></mu-radio>
                                </mu-form-item>
                           </mu-col>
                       </mu-row>
                   </mu-form>
                </mu-col>
                </mu-row>
                <mu-row gutter style="width:100%">
                    <mu-col span="1" >
                        <mu-col >

                            <!--<input style="background:grey; padding:10%; border-radius:0 0 6px 6px"
                                   type="file" id="myFile"
                                   accept=".jpg" @change="onFileChange">-->
                            <mu-button color="grey" @click="showImage">
                                Show
                            </mu-button>
                        </mu-col>
                    </mu-col>
                    <mu-col span="1" offset="8">
                        <mu-button  @click="openDialog = !openDialog">close</mu-button>
                    </mu-col>
                    <mu-col span="1" offset="1">
                        <mu-button color="lightGreen" @click="submitDriver">submit</mu-button>
                    </mu-col>
                </mu-row>

            </mu-dialog>


            <mu-paper :z-depth=1 >
                <mu-list v-for="oneDriver in drivers" style="position:static;">
                        <div style="position:absolute; background:#a7c8fa;
                                    transform:translate(-100%); border-radius:8px 0 0 8px;"
                                v-if="uniqueLetter(oneDriver.surname.charAt(0))">
                            <mu-col><h1>{{oneDriver.surname.charAt(0)}}</h1></mu-col>
                        </div>
                    <mu-row class="anchor" :id="oneDriver.surname.charAt(0)"></mu-row>
                    <mu-list-item  avatar button :ripple="false">
                      <mu-list-item-action >
                        <mu-avatar>
                          <img v-bind:src="require('@/assets/images/driver'
                     +oneDriver.id+'.jpg')">
                        </mu-avatar>
                      </mu-list-item-action>
                      <mu-list-item-content>
                          <mu-list-item-title>
                              {{oneDriver.surname}} {{oneDriver.name}}
                          </mu-list-item-title>
                          <mu-list-item-sub-title>Passport: {{oneDriver.passport}}</mu-list-item-sub-title>
                      </mu-list-item-content>
                      <mu-list-item-action>
                          <mu-button icon color="red" @click="deleteDriver(oneDriver.id)">
                              <mu-icon value="clear"></mu-icon>
                          </mu-button>
                      </mu-list-item-action>
                    </mu-list-item>

                    <mu-paper style="padding:1% 3%">
                        <mu-row gutter>
                            <mu-col span="2">

                                <mu-date-input full-width v-bind:class="'driver'+oneDriver.id"
                                               display-color="deepOrange"
                                                disabled
                                                v-model="formDriver.d_of_b" type="date"
                                               label="Was born" :placeholder="oneDriver.d_of_b"
                                                :date-time-format="enDateFormat">
                                </mu-date-input>
                            </mu-col>
                            <mu-col>
                                <mu-text-field label="Bus" full-width disabled
                                               v-bind:class="'driver'+oneDriver.id"
                                                :placeholder="oneDriver.bus.reg_plate">
                                </mu-text-field>
                            </mu-col>
                            <mu-col>
                                <mu-text-field label="Route" full-width disabled
                                               v-bind:class="'driver'+oneDriver.id"
                                                :placeholder="oneDriver.route.num">
                                </mu-text-field>
                            </mu-col>
                            <mu-col span="2" >
                                <mu-text-field label="Started" full-width disabled
                                               v-bind:class="'driver'+oneDriver.id"
                                                :placeholder="oneDriver.date_begin">
                                </mu-text-field>
                            </mu-col>
                            <mu-col span="2" >
                                <mu-text-field label="Class" full-width v-bind:disabled="edit[oneDriver.id.toString()]"
                                               v-bind:class="'driver'+oneDriver.id"
                                                :placeholder="oneDriver.job_class">
                                </mu-text-field>
                            </mu-col>
                            <mu-col span="2" >
                                <mu-text-field label="Salary" full-width :disabled="edit[oneDriver.id.toString()]"
                                               v-bind:class="'driver'+oneDriver.id"
                                                :placeholder="oneDriver.salary">
                                </mu-text-field>
                            </mu-col>
                        </mu-row>
                    </mu-paper>
                    <mu-divider></mu-divider>
                </mu-list>

            </mu-paper>
        </mu-container>
    </div>
</body>
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
        name:"Drivers",
        data() {
            const maxDate = new Date();
            const minDate = new Date();

            maxDate.setFullYear(maxDate.getFullYear()-14);
            maxDate.setDate(0);
            return {
                max_id:'',
                snackbar: {
                    open: false,
                    timeout: 3000,
                  },
                img_link: false,
                maxDate,
                form: {
                    surname:'',
                    name:'',
                    passport:'',
                    d_of_b:maxDate,
                    bus:'',
                    route:'',
                    job_class:'',
                    date_begin:undefined,
                },
                buses:'',
                routes: '',
                openDialog:false,
                edit: {},
                enDateFormat,
                formDriver: {
                    d_of_b:'',
                },
                openDrawer: false,
                drivers: "",
                letters: [],
                driversLetter: "",
                alphabet: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split(''),
                showDrLValue: false,

            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' +
                        sessionStorage.getItem('auth_token')}
            }),
            this.loadDrivers()

        },
        computed: {
            auth(){
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            showImage(){
                this.img_link = true;
            },
            deleteDriver(the_id) {
                    $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/driver/"
                                + the_id + "/",
                        type: "DELETE",
                        success: (response) => {
                            this.loadDrivers();
                            if (this.snackbar.timer) clearTimeout(this.snackbar.timer);
                            this.snackbar.open = true;
                            this.snackbar.timer = setTimeout(() => {
                                    this.snackbar.open = false;
                                  },
                                  this.snackbar.timeout);
                        }
                    })
            },
            submitDriver() {
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/driver/",
                        type: "POST",
                        data: {
                            passport: this.form.passport,
                            name: this.form.name,
                            surname: this.form.surname,
                            d_of_b: this.form.d_of_b.toISOString().slice(0,10),
                            date_begin: this.form.date_begin.toISOString().slice(0,10),
                            job_class: this.form.job_class,
                            bus: this.form.bus,
                            route: this.form.route,

                        },
                        success: (response) => {
                            this.img_link = false;
                            this.loadDrivers();
                        }
                });
                this.openDialog = false;
            },
            onFileChange(e) {
              const file = e.target.files[0];
              this.img_link = URL.createObjectURL(file);
            },
            submit() {

            },
            addDriver() {
                this.openDialog = true;
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/bus/",
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
                $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/bus_info/route/",
                        type: "GET",
                        data: {},
                        success: (response) => {
                            this.routes = response.data.data;
                        }
                });

            },
            editDriver(driver_id) {

                this.edit[driver_id] = !this.edit[driver_id];
                var fields = document.getElementsByClassName('driver'+driver_id);
                for(let i = 0; i < fields.length; i++) {
                    fields[i].style.background='lightGreen';
                };


            },
            uniqueLetter(to_save){
                if (!this.letters.includes(to_save)){
                    this.letters.push(to_save);
                    return true;
                }
                else {
                    return false;
                }
            },
            showDriversLetter(letter){
                this.showDrLValue = true;
                this.driversLetter = this.drivers.filter(driver => driver.surname.startsWith(letter))
            },
            goLogin(){
                this.$router.push({name:"login"})
            },
            goLogout(){
                sessionStorage.removeItem("auth_token"),
                window.location = "/"
            },
            goHome(){
                this.$router.push({name:"home"})
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
            goBusMal(){
                this.$router.push({name:"busmals"})
            },
            goSchedReport(){
                this.$router.push({name:"schedreport"})
            },
            loadDrivers(){

                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/bus_info/all_drivers/",
                    type: "GET",
                    success:(response) => {
                        this.drivers = response.data.data;

                        for (let i = 0; i < this.drivers.length; i++){
                            this.edit[this.drivers[i].id.toString()] = true;

                        };
                        var ids = [];
                        for(let i = 0; i < this.drivers.length; i++) {
                            ids.push(this.drivers[i].id);
                        };
                        this.max_id = Math.max(...ids)+1;

                    }
                });


            },
        }
    }
</script>

<style scoped>
.anchor {
    display: block;
    position: relative;
    top: -2vw;
    visibility: hidden;
}

#driver9 {
    margin:5px;
    padding: 10px;
}
</style>

