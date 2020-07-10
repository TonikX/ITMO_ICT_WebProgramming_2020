<template>
  <body :style="{'background-color' : backgroundcolor}" >
  <div id="app">
    <router-view/>
  </div>
  </body>
</template>

<script>
    export default {
        name: 'App',
        data(){
            return{
              backgroundcolor:"#FFFFFF",
           }
         }
    }
</script>

<style>
</style>