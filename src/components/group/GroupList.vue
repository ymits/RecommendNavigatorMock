<template>
  <div class="group-list-view">
    <div class="page-title">
      <el-button type="primary">新しいグループ分けルールの作成</el-button>
      <h1>グループ分けルール一覧</h1>
    </div>

    <el-row class="group-list">
      <el-col :span="5" v-for="(group, index) in groupList" :key="group" :offset="index % 4 != 0 ? 1 : 0">
        <el-card class="group-item" :body-style="{ padding: '0px' }">
          <div v-if="group.active" class="el-badge__content">有効</div>
          <div class="group-title">
            {{group.name}}
          </div>
          <div class="group-body">
            <el-button type="text">詳細</el-button>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      groupList: [
        { id: 1, name: '単一グループ' },
        { id: 2, name: 'ランダムグループ分け', active: true },
        { id: 3, name: '取引量によるグループ分け' },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
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

.group-list {

  .group-item {
    position: relative;
    margin-top: 10px;
    overflow: visible;

    .group-title {
      padding: 10px;
      height: 100px;
    }

    .group-body {
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
