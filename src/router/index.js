import Vue from 'vue';
import Router from 'vue-router';
import Index from '@/components/Index';
import HelloWorld from '@/components/HelloWorld';
import GroupList from '@/components/group/GroupList';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      component: Index,
      icon: 'el-icon-menu',
      title: 'グループ分けルール',
      children: [
        { path: '', component: GroupList },
        { path: 'create', component: HelloWorld },
        { path: 'edit', component: HelloWorld },
      ],
    },
    {
      path: '/recommend',
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
