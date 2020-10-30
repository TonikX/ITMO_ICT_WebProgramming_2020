<template>
    <div id="app">
        <Navbar/>
        <router-view/>
    </div>
</template>

<script>
    import $ from 'jquery'
    import Navbar from "./components/Navbar";

    export default {
        name: 'App',
        components: {Navbar},
        created() {
            if (localStorage.getItem("auth_token")) {
                $.ajaxSetup({
                    headers: {'Authorization': "Token " + localStorage.getItem('auth_token')},
                });
            }
        }
    }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        background-image: url("https://images.pexels.com/photos/19670/pexels-photo.jpg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260");
    }

    h1 {
        font-family: helvetica, serif;
        color: #1e2026;
        font-size: 20px;

    }

    table.paleBlueRows {
        font-family: "Times New Roman", Times, serif;
        border: 1px solid #FFFFFF;
        text-align: center;
        border-collapse: collapse;
    }

    table.paleBlueRows td, table.paleBlueRows th {
        border: 1px solid #FFFFFF;
        padding: 3px 2px;
    }

    table.paleBlueRows tbody td {
        font-size: 13px;
    }

    table.paleBlueRows tr:nth-child(even) {
        background: #D0E4F5;
    }

    table.paleBlueRows thead {
        background: #0B6FA4;
        border-bottom: 5px solid #FFFFFF;
    }

    table.paleBlueRows thead th {
        font-size: 17px;
        font-weight: bold;
        color: #FFFFFF;
        text-align: center;
        border-left: 2px solid #FFFFFF;
    }

    table.paleBlueRows thead th:first-child {
        border-left: none;
    }

    table.paleBlueRows tfoot {
        font-size: 14px;
        font-weight: bold;
        color: #333333;
        background: #D0E4F5;
        border-top: 3px solid #444444;
    }

    table.paleBlueRows tfoot td {
        font-size: 14px;
    }

    ul {
        list-style-type: circle;
        list-style-position: inherit;
    }

    li {
        padding: 0px;
        margin: 0px;
    }

    .mu-demo-form {
        width: 100%;
        max-width: 460px;
    }

    a {
        color: midnightblue;
        font-family: helvetica;
        text-decoration: none;
        cursor: pointer;
    }

    a:hover {
        text-decoration: underline;
    }

    a:active {
        color: midnightblue;
    }

    a:visited {
        color: royalblue;
    }
</style>
