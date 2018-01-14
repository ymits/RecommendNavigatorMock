<template>
  <div class="recommend-rule-save-view">
    <div class="page-title">
      <div class="row">
        <div class="col">
          <input type="text" class="title-text" v-model="title" placeholder="ルール名称">
        </div>
        <div class="col fix">
          <el-button type="primary">保存</el-button>
        </div>
      </div>
    </div>
    <el-form label-position="top" label-width="100px" class="program-info">
      <el-form-item label="ファイル名">
        <el-input v-model="filename"></el-input>
      </el-form-item>
      <el-form-item label="実行パラメータ">
        <el-input type="textarea" :rows="5" v-model="params"></el-input>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'RecommendRuleSaveView',
  data() {
    return {
      title: '',
      filename: 'sample.ts',
      params: '{\n  "groupNum": 3\n}',
    };
  },

  methods: {
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
// タイトル
.page-title {
  border-bottom: solid 1px #E0E0E0;
  margin-bottom: 20px;

  .row {
    display: table;
    width: 100%;
    margin: -5px 0 5px 0;

    .col {
      display: table-cell;
      vertical-align: middle;

      &.fix {
        width: 1%;
      }
    }
  }

  .title-text {
    width: 100%;
    font-weight: 400;
    font-size: 24px;
    line-height: 36px;
    height: 40px;

    border-color: transparent;
    border-width: 0 0 2px;
    outline: 0;

    &:focus {
      border-color: #46A0FC;
    }
  }
}

// プログラム情報
.program-info {
  /deep/ label {
    padding: 0;
  }

  .btn-row {
    text-align: center;
  }
}
</style>
