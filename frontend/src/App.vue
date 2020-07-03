<template>
    <v-app id="inspire">
        <router-view name="header"/>
        <v-main>
            <v-container fluid>
                <router-view/>
            </v-container>
        </v-main>
    </v-app>
</template>
