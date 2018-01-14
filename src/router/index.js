import Vue from 'vue';
import Router from 'vue-router';
import Index from '@/components/Index';
import HelloWorld from '@/components/HelloWorld';
import GroupingRuleListView from '@/components/groupingRule/GroupingRuleListView';
import GroupingRuleSaveView from '@/components/groupingRule/GroupingRuleSaveView';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/groupingRule',
      alias: '/',
      component: Index,
      icon: 'el-icon-menu',
      title: 'グループ分けルール',
      children: [
        { path: '', component: GroupingRuleListView },
        { path: 'create', name: 'GroupingRuleCreateView', component: GroupingRuleSaveView },
        { path: 'update/:id', name: 'GroupingRuleUpdateView', component: GroupingRuleSaveView },
      ],
    },
    {
      path: '/recommendRule',
      component: Index,
      icon: 'el-icon-share',
      title: '推奨ルール',
      children: [
        { path: '', component: HelloWorld },
        { path: 'create', component: HelloWorld },
        { path: 'update/:id', component: HelloWorld },
      ],
    },
  ],
});
