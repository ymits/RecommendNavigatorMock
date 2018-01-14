import Vue from 'vue';
import Router from 'vue-router';
import Index from '@/components/Index';
import HelloWorld from '@/components/HelloWorld';
import GroupingRuleListView from '@/components/groupingRule/GroupingRuleListView';
import GroupingRuleSaveView from '@/components/groupingRule/GroupingRuleSaveView';
import RecommendRuleListView from '@/components/recommendRule/RecommendRuleListView';
import RecommendRuleSaveView from '@/components/recommendRule/RecommendRuleSaveView';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/recommendRule',
      alias: '/',
      component: Index,
      icon: 'el-icon-share',
      title: '推奨ルール',
      children: [
        { path: '', name: 'RecommendRuleListView', component: RecommendRuleListView },
        { path: 'create', name: 'RecommendRuleCreateView', component: RecommendRuleSaveView },
        { path: 'update/:id', component: HelloWorld },
      ],
    },
    {
      path: '/groupingRule',

      component: Index,
      icon: 'el-icon-menu',
      title: 'グループ分けルール',
      children: [
        { path: '', component: GroupingRuleListView },
        { path: 'create', name: 'GroupingRuleCreateView', component: GroupingRuleSaveView },
        { path: 'update/:id', name: 'GroupingRuleUpdateView', component: GroupingRuleSaveView },
      ],
    },
  ],
});
