<template>
  <div class="grouping-rule-list-view">
    <div class="page-title">
      <el-button type="primary" @click="goGroupingRuleCreateView">新しいグループ分けルールの作成</el-button>
      <h1>グループ分けルール一覧</h1>
    </div>

    <el-row class="grouping-rule-list">
      <el-col :span="5" v-for="(rule, index) in groupList" :key="rule.id" :offset="index % 4 != 0 ? 1 : 0">
        <el-card class="grouping-rule" :body-style="{ padding: '0px' }">
          <div v-if="rule.active" class="el-badge__content">有効</div>
          <div class="grouping-rule-title">
            {{rule.name}}
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
export default {
  name: 'GroupingRuleListView',
  data() {
    return {
      groupList: [
        { id: 1, name: '単一グループ' },
        { id: 2, name: 'ランダムグループ分け', active: true },
        { id: 3, name: '取引量によるグループ分け' },
      ],
    };
  },

  methods: {
    goGroupingRuleCreateView() {
      this.$router.push({ name: 'GroupingRuleCreateView' });
    },
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
