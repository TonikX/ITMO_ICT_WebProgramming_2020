<template>

</template>

<script>
    import $ from 'jquery'

    export default {
       name:"Buses",
       props: {
            id: ''
       },
       data(){
            return{
                bus: "",
                alphabet: 'abcdefghijklmnopqrstuvwxyz'.split(''),
                showDrivers:false,
            }
       },
       created(){
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' +
                        sessionStorage.getItem('auth_token')}
            }),
            this.loadBus()
       },
       methods: {
            showDriversVar(value) {
                this.showDrivers = value;
            },
            loadBus() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/bus_info/bus",
                    type: "GET",
                    data: {
                        driver: this.id
                    },
                    success: (response) => {
                        this.bus = response.data.data
                    }
                })
            }
       }
    };
</script>

<style scoped>
    .bus {
        border: 1px solid #000;
    }
</style>
