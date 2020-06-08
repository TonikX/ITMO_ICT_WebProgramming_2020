<template>
    <div class="root">
        <div class="header">
            <mu-tabs :value.sync="active">
                <router-link to="/" exact>
                    <mu-tab exact>
                        Главная
                    </mu-tab>
                </router-link>
                <router-link to="/dogs" exact>
                    <mu-tab exact>
                        Мои собаки
                    </mu-tab>
                </router-link>
                <router-link to="/clubs" exact>
                    <mu-tab exact>
                        Клубы
                    </mu-tab>
                </router-link>
            </mu-tabs>
        </div>
        <router-view></router-view>
    </div>
</template>

<script>
const tabs = ['home', 'dogs', 'clubs']

export default {
    name: "IndexPage",
    mounted() {
        this.$store.dispatch("show/getShows");
        this.$store.dispatch("user/getProfileInfo");
        this.$store.dispatch("club/getClubs");
        this.$store.dispatch("user/getDogs");
    },
    data() {
        return {
            $active: undefined,
        };
    },
    computed: {
        active: {
            get() {
                const actualTab = this.$active || this.$route.name || 'home';

                return tabs.indexOf(actualTab);
            },
            set(newActive) {
                this.$active = tabs[newActive];
            },
        }
    },
}
</script>

<style scoped>
.mu-tab {
    color: hsla(0,0%,100%,.7);
}
.mu-tab-active {
    color: #fff;
}
.root {
    width: 800px;
    margin: 0 auto;
}
</style>