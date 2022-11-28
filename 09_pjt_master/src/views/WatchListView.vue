<template>
    <div class="card m-auto" style="width: 90%;">
        <div class="card-header" style="background-color: #e3f2fd;">
            <form @submit.prevent="">
                <h1 ><b>보고싶은 영화</b></h1>
                <input type="text" v-model="watchdata">&nbsp;
                <button @click="addMovie(watchdata)" class="btn btn-outline-dark">Add</button>
            </form>
        </div>
            <ul class="list-group list-group-flush">
                <WatchListItem
                v-for="watch in watchlist"
                :key="watch.id"
                :watch="watch"
                class="list-group-item"
                />
            </ul>
    </div>
</template>

<script>
import WatchListItem from '@/components/WatchListItem'

export default {
    name: 'WatchListView',
    components: {
        WatchListItem
    },
    data() {
        return {
            watchdata:null,
            watchlist:[],
            addid:1,
        }
    },
    methods: {
        addMovie(watchdata) {
            if (watchdata != null) {
                this.watchdata = watchdata
                this.watchlist.push({data:this.watchdata, id:this.addid,is_delete:false})
                this.watchdata = null
                this.addid += 1
            }
        },
    },
}
</script>

<style>

.isdeletecolor {
    background-color:gainsboro !important;
}

.isdeletetext {
    color:gray;
    text-decoration: line-through;  
}


</style>