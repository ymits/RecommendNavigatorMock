import Vue from 'vue';
import Router from 'vue-router';
import Index from '@/components/Index';
import HelloWorld from '@/components/HelloWorld';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: Index,
      icon: 'el-icon-menu',
      title: 'グループ',
      children: [
        { path: '', component: HelloWorld },
        { path: 'create', component: HelloWorld },
        { path: 'edit', component: HelloWorld },
      ],
    },
    {
      path: '/recommend',
      name: 'HelloWorld',
      component: Index,
      icon: 'el-icon-share',
      title: '推奨エンジン',
      children: [
        { path: '', component: HelloWorld },
        { path: 'create', component: HelloWorld },
        { path: 'edit', component: HelloWorld },
      ],
    },
  ],
});
