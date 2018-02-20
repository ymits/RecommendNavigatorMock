import Vue from 'vue';
// ElementUI
import ElementUI from 'element-ui';
import locale from 'element-ui/lib/locale/lang/ja';
import 'element-ui/lib/theme-chalk/index.css';
import VeeValidate from 'vee-validate';
import 'chart.js'
import 'hchs-vue-charts'

import App from './App';
import router from './router';

Vue.use(ElementUI, { locale });
Vue.use(VeeValidate, { fieldsBagName: 'formFields' });
Vue.use(window.VueCharts)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
