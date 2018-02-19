<template>
  <div class="grouping-rule-list-view">
    <div class="page-title">
      <el-button type="primary" @click="goGroupingRuleCreateView">新しいグループ分けルールの作成</el-button>
      <h1>グループ分けルール一覧</h1>
    </div>

    <el-row class="grouping-rule-list">
      <el-col :span="5" v-for="(rule, index) in rules" :key="rule.id" :offset="index % 4 != 0 ? 1 : 0">
        <el-card class="grouping-rule" :body-style="{ padding: '0px' }" @click.native="selectGroupingRule(rule.id)">
          <div v-if="rule.active" class="el-badge__content">有効</div>
          <div class="grouping-rule-title">
            {{rule.title}}
          </div>
          <div class="grouping-rule-body">
            <el-button type="text">詳細</el-button>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import GroupingRule from '@/models/GroupingRule';

export default {
  name: 'GroupingRuleListView',
  data() {
    return {
      rules: [],
    };
  },

  methods: {
    goGroupingRuleCreateView() {
      this.$router.push({ name: 'GroupingRuleCreateView' });
    },

    selectGroupingRule(id) {
      this.$router.push({ name: 'GroupingRuleUpdateView', params: { id } });
    },
  },

  mounted() {
    GroupingRule.findAll().then((rules) => {
      this.rules = rules;
    });
  },
};
</script>

<style lang="scss" scoped>
// タイトル
.page-title {
  border-bottom: solid 1px #E0E0E0;
  margin-bottom: 20px;

  h1 {
    margin-top: 0;
  }

  .el-button {
    float: right;
  }
}

// ルール一覧
.grouping-rule-list {

  .grouping-rule {
    position: relative;
    margin-top: 10px;
    overflow: visible;

    .grouping-rule-title {
      padding: 10px;
      height: 100px;
    }

    .grouping-rule-body {
      border-top: solid #EBEEF5 1px;
      text-align: center;
    }

    .el-badge__content{
      position: absolute;
      top: 0;
      right: 0;
      transform: translateY(-50%) translateX(30%);
    }

    &:hover {
      background-color: #ecf5ff;
    }
  }
}
</style>
