<template>
  <div class="recommend-rule-list-view">
    <div class="page-title">
      <el-button type="primary" @click="goRecommendRuleCreateView">新しい推奨ルールの作成</el-button>
      <h1>推奨ルール一覧</h1>
    </div>

    <el-row class="recommend-rule-list">
      <el-col :span="5" v-for="(rule, index) in groupList" :key="rule.id" :offset="index % 4 != 0 ? 1 : 0">
        <el-card class="recommend-rule" :body-style="{ padding: '0px' }" @click.native="selectRecommendRule(rule.id)">
          <div class="recommend-rule-title">
            {{rule.title}}
          </div>
          <div class="recommend-rule-body">
            <el-button type="text">詳細</el-button>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import RecommendRule from '@/models/RecommendRule';

export default {
  name: 'RecommendRuleListView',
  data() {
    return {
      groupList: [],
    };
  },

  methods: {
    goRecommendRuleCreateView() {
      this.$router.push({ name: 'RecommendRuleCreateView' });
    },

    selectRecommendRule(id) {
      this.$router.push({ name: 'RecommendRuleUpdateView', params: { id } });
    },
  },

  mounted() {
    this.groupList = RecommendRule.findAll();
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
.recommend-rule-list {

  .recommend-rule {
    position: relative;
    margin-top: 10px;
    overflow: visible;

    .recommend-rule-title {
      padding: 10px;
      height: 100px;
    }

    .recommend-rule-body {
      border-top: solid #EBEEF5 1px;
      text-align: center;
    }

    &:hover {
      background-color: #ecf5ff;
    }
  }
}
</style>
