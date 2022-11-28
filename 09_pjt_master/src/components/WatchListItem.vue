<template>
    <div
    @click="deleteline(watch)"
    style="background-color:aliceblue"
    :class="{isdeletecolor:watch.is_delete}">
        <span :class="{isdeletetext:watch.is_delete}">{{watch.data}}</span>
    </div>
</template>

<script>
export default {
    name:'WatchListItem',
    props: {
        'watch':Object,
        "index":Number,
    },
    methods: {
        deleteline(watch) {
            watch.is_delete = !watch.is_delete
        }
    }
}
</script>

<style>

</style>