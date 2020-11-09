<template>
    <div>
        <mu-container>
        <mu-list>
            <mu-header><h3>Рейтинг пользователей по количеству посещенных мастер-классов</h3></mu-header>
            <mu-list-item button :ripple="false" v-for="user in users">
                <mu-list-item-action v-if="users.indexOf(user)===0">
                    <mu-icon value="star" color="yellow"></mu-icon>
                </mu-list-item-action>
                <mu-list-item-action v-else-if="users.indexOf(user)===1">
                    <mu-icon value="star" color="grey"></mu-icon>
                </mu-list-item-action>
                <mu-list-item-action v-else-if="users.indexOf(user)===2">
                    <mu-icon value="star" color="brown"></mu-icon>
                </mu-list-item-action>
                <mu-list-item-action v-else>
                    <mu-icon></mu-icon>
                </mu-list-item-action>
                <mu-list-item-title>{{user.full_name}}</mu-list-item-title>
                <mu-list-item-action>
<!--                    <mu-tooltip content="Количество посещенных мастер-классов">-->
                        {{user.wsh_count}}
<!--                    </mu-tooltip>-->
                </mu-list-item-action>
            </mu-list-item>
        </mu-list>
        </mu-container>
    </div>
</template>

<script>
    import $ from "jquery";


    export default {
        name: "Choreographers",
        props:{
            id_login_user:'',
        },
        data() {
            return {
                users: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadRating();
        },
        methods: {
            loadRating() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/dance/rating/",
                    type: "GET",
                    success: (response) => {
                        this.users = response.data.data
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
