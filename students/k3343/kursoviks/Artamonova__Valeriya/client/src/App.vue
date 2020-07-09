<template>
    <div id="app">
        <Nav/>
        <router-view/>

    </div>
</template>

<style>
    .ball {
        list-style: none;
        margin: 0;
    }

    .ball a {
        width: 100%;
        color: #808285;
        text-decoration: none;
        display: inline-block;
        padding-left: 25px;
        height: 44px;
        line-height: 44px;
        font-size: 20px;
        position: relative;
        transition: .3s linear;
    }

    .ball a:before {
        content: "";
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background: #425273;
        position: absolute;
        left: -30px;
        top: 7px;
    }

    .ball li {
        position: relative;
    }

    .ball li:before {
        content: "";
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: #EC351D;
        position: absolute;
        top: 12px;
        left: -30px;
        z-index: 2;
        transition: .4s ease-in-out;
    }

    .ball li:hover:before {
        left: -20px;
    }

    @import url(https://fonts.googleapis.com/css?family=Roboto:400,500,700,300,100);


    div.table-title {
        display: block;
        margin: auto;
        max-width: 600px;
        padding: 5px;
        width: 100%;
    }

    .table-title h3 {
        color: #fafafa;
        font-size: 30px;
        font-weight: 400;
        font-style: normal;
        font-family: "Roboto", helvetica, arial, sans-serif;
        text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.1);
        text-transform: uppercase;
    }


    /*** Table Styles **/

    .table-fill {
        background: white;
        border-radius: 3px;
        border-collapse: collapse;
        height: 40px;
        margin: auto;
        max-width: 600px;
        padding: 5px;
        width: 100%;
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
        animation: float 5s infinite;
    }

    th {
        color: whitesmoke;;
        background: #2f4858;
        border-bottom: 4px solid #9ea7af;
        border-right: 1px solid #343a45;
        font-size: 20px;
        font-weight: 100;
        padding: 5px;
        text-align: left;
        text-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
        vertical-align: middle;
    }

    th:first-child {
        border-top-left-radius: 3px;
    }

    th:last-child {
        border-top-right-radius: 3px;
        border-right: none;
    }

    tr {
        border-top: 1px solid #C1C3D1;
        border-bottom-: 1px solid #C1C3D1;
        color: #666B85;
        font-size: 16px;
        font-weight: normal;
        text-shadow: 0 1px 1px rgba(256, 256, 256, 0.1);
    }

    tr:hover td {
        background: #4E5066;
        color: #FFFFFF;
        border-top: 1px solid #22262e;
    }

    tr:first-child {
        border-top: none;
    }

    tr:last-child {
        border-bottom: none;
    }

    tr:nth-child(odd) td {
        background: #EBEBEB;
    }

    tr:nth-child(odd):hover td {
        background: #4E5066;
    }

    tr:last-child td:first-child {
        border-bottom-left-radius: 3px;
    }

    tr:last-child td:last-child {
        border-bottom-right-radius: 3px;
    }

    td {
        background: #FFFFFF;
        padding: 10px;
        text-align: left;
        vertical-align: middle;
        font-weight: 300;
        font-size: 18px;
        text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.1);
        border-right: 1px solid #C1C3D1;
    }

    td:last-child {
        border-right: 0px;
    }

    th.text-left {
        text-align: left;
    }

    th.text-center {
        text-align: center;
    }

    th.text-right {
        text-align: right;
    }

    td.text-left {
        text-align: left;
    }

    td.text-center {
        text-align: center;
    }

    td.text-right {
        text-align: right;
    }

    .mu-demo-form {
        width: 100%;
        max-width: 460px;
    }
</style>
<script>
    import $ from 'jquery'
    import Nav from "./components/Nav";

    export default {
        name: 'App',
        components: {Nav},
        created() {
            if (localStorage.getItem("auth_token")) {
                $.ajaxSetup({
                    headers: {'Authorization': "Token " + localStorage.getItem('auth_token')},
                });
            }
        }
    }
</script>