import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'bootstrap/dist/css/bootstrap.css';
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue' 
import VueCarousel from 'vue-carousel';

import "bootstrap-icons/font/bootstrap-icons.css"

Vue.use(BootstrapVue); 
Vue.use(BootstrapVueIcons);
Vue.use(VueCarousel);

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')


