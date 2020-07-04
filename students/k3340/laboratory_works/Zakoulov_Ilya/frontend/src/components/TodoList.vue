<template>
    <ul id="app">
        <li v-for="(todo, index) in todos" :key="index" @click="deleteTodo(index)">{{ todo }}</li>
    </ul>
</template>

<script>
    export default {
        props : [
            'todos'
        ],
        name: 'TodoList',
        methods: {
            deleteTodo(index) {
                this.$emit('delete-todo', index);
            }
        }
    }
</script>

<style scoped>

</style>