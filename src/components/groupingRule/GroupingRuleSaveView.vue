<template>
  <div class="grouping-rule-save-view">
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
      <el-form-item class="btn-row">
        <el-button @click="trialExecute">試し実行</el-button>
      </el-form-item>
    </el-form>
    <div class="execute-result" v-if="trialExecuted">
      <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column
          label="No"
          width="50">
          <template slot-scope="scope">
            {{ scope.row.id }}
          </template>
        </el-table-column>
        <el-table-column
          label="ユーザ数"
          width="80"
          align="right">
          <template slot-scope="scope">
            <el-button type="text">{{ scope.row.memberCount }}</el-button>
          </template>
        </el-table-column>
        <el-table-column
          label="推奨ルール"
          width="280">
          <template slot-scope="scope">
            <el-select v-model="recommendRule[scope.row.id]" placeholder="推奨ルールの選択">
              <el-option
                v-for="rule in recommendRules"
                :key="rule.value"
                :label="rule.label"
                :value="rule.value">
              </el-option>
            </el-select>
          </template>
        </el-table-column>
        <el-table-column
          label="ユーザ行動結果">
        </el-table-column>
      </el-table>
      <div class="adapt-btn-row">
        <el-button type="primary">適用する</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'underscore';

export default {
  name: 'HelloWorld',
  data() {
    return {
      title: '',
      filename: 'sample.ts',
      params: '{\n  "groupNum": 3\n}',
      trialExecuted: false,
      groupNum: 0,
      recommendRule: {},
    };
  },

  methods: {
    trialExecute() {
      const params = JSON.parse(this.params);
      this.groupNum = params.groupNum;
      this.trialExecuted = true;
    },
  },

  computed: {
    tableData() {
      return _.range(this.groupNum).map((index) => {
        return {
          id: index,
          memberCount: (Math.random() * 1000).toFixed(),
        };
      });
    },

    recommendRules() {
      return [
        { value: 1, label: 'ロイタースコアを利用した推奨' },
      ];
    },
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

// お試し実行結果
.execute-result {
  .el-select {
    display: block;
  }

  .adapt-btn-row {
    margin-top: 22px;
    text-align: center;
  }
}
</style>
