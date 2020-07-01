<template>
    <div id="app">
        <Nav/>
        <router-view/>
        <Footer/>
    </div>
</template>

<style>
    .ball {
        list-style: none;
        margin: 0;
    }
    .ball a {
        width: 100%;
        color: #22262e;
        text-decoration: none;
        display: inline-block;
        padding-left: 20px;
        height: 40px;
        line-height: 40px;
        font-size: 22px;
        position: relative;
        transition: .3s linear;
    }
    .ball a:before {
        content: "";
        width: 30px;
        height: 30px;
        border-radius: 10%;
        background: #22262e;
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
        background: #666B85;
        position: absolute;
        top: 15px;
        left: -30px;
        z-index: 2;
        transition: .4s ease-in-out;
    }
    .ball li:hover:before {
        left: -20px;
    }
    div.table-title {
        display: block;
        margin: auto;
        max-width: 600px;
        padding: 5px;
        width: 100%;
    }
    .table-title h1 {
        color: black;
        font-size: 30px;
        font-weight: 400;
        font-style: normal;
        font-family: "Roboto", helvetica, "Times New Roman", sans-serif;
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
        color: black;;
        background: slategray;
        font-size: 25px;
        font-weight: 100;
        padding: 10px;
        text-align: right;
        text-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
        vertical-align: middle;
    }
    th:first-child {
        border-top-left-radius: 1px;
    }
    th:last-child {
        border-top-right-radius: 1px;
        border-right: none;
    }
    tr {
        border-top: 2px solid chocolate;
        border-bottom-: 1px solid chocolate;
        color: black;
        font-size: 16px;
        font-weight: normal;
        text-shadow: 0 1px 1px rgba(256, 256, 256, 0.1);
    }
    tr:hover td {
        background: dimgray;
        color: whitesmoke;
        border-top: 5px solid coral;
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
        background: dimgray;
    }
    tr:last-child td:first-child {
        border-bottom-left-radius: 1px;
    }
    tr:last-child td:last-child {
        border-bottom-right-radius: 1px;
    }
    td {
        background: #FFFFFF;
        padding: 10px;
        text-align: left;
        vertical-align: middle;
        font-weight: 300;
        font-size: 18px;
        text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.1);
        border-right: 3px solid coral;
    }
    td:last-child {
        border-right: 5px;
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
    import Footer from "./components/Footer";
    export default {
        name: 'App',
        components: {Nav, Footer},
        created() {
            if (localStorage.getItem("auth_token")) {
                $.ajaxSetup({
                    headers: {'Authorization': "Token " + localStorage.getItem('auth_token')},
                });
            }
        }
    }
</script>

