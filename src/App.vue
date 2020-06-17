<template>
    <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
        <header class="mdl-layout__header">
            <div class="mdl-layout__header-row">
                <span class="mdl-layout-title">
                    Неизвестный Питер
                </span>
                <div class="mdl-layout-spacer"></div>
                <div class="mdl-layout-spacer"></div>
            </div>
        </header>
        <div class="mdl-layout__drawer">
            <span class="mdl-layout-title">Настройки</span>
            <nav class="mdl-navigation" id="nav">
                <router-link class="mdl-navigation__link" to="/quests">
                    <i class="material-icons" style="margin: 0px 10px 5px 0px">extension</i>
                    Квесты
                </router-link>
                <router-link class="mdl-navigation__link" to="/teams">
                    <i class="material-icons" style="margin: 0px 10px 5px 0px">people</i>
                    Команды
                </router-link>
            </nav>
        </div>
        <main class="mdl-layout__content" id="content_holder">
            <router-view></router-view>
        </main>
    </div>
</template>

<script></script>