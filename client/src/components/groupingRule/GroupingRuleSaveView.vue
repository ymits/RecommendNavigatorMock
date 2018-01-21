<template>
  <div class="grouping-rule-save-view">
    <div class="page-title">
      <div class="row">
        <div class="col fix">
          <el-button type="text" @click="back" icon="el-icon-arrow-left">戻る</el-button>
        </div>
        <div class="col title">
          <input type="text" class="title-text" name="title" v-model="rule.title" placeholder="ルール名称" v-validate="'required'">
        </div>
        <div class="col fix">
          <el-button type="primary" @click="saveGroupingRule">保存</el-button>
        </div>
      </div>
      <el-alert v-show="errors.has('title')" title="名称は必須だよ" type="error" show-icon :closable="false"></el-alert>
    </div>
    <el-form label-position="top" label-width="100px" class="program-info">
      <div class="active-badge" v-if="rule && rule.active">
        <el-tag type="danger">現在適用中のルール</el-tag>
      </div>
      <el-form-item label="ファイル名">
        <el-input v-model="rule.filename"></el-input>
      </el-form-item>
      <el-form-item label="実行パラメータ">
        <el-input type="textarea" :rows="5" v-model="rule.params"></el-input>
      </el-form-item>
      <el-form-item class="btn-row">
        <el-button @click="trialExecute">試し実行</el-button>
      </el-form-item>
    </el-form>
    <div class="group-info" v-if="showGroupInfo">
      <el-table
        :data="groups"
        style="width: 100%">
        <el-table-column
          label="No"
          width="50">
          <template slot-scope="scope">
            {{ scope.$index + 1 }}
          </template>
        </el-table-column>
        <el-table-column
          label="ユーザ数"
          width="80"
          align="right">
          <template slot-scope="scope">
            <el-popover
              placement="top-start"
              title="割り振り口座"
              width="200"
              trigger="hover"
              :content="scope.row.members.join(', ')">
              <el-button type="text" slot="reference">{{ scope.row.memberCount() }}</el-button>
            </el-popover>
            人
          </template>
        </el-table-column>
        <el-table-column
          label="推奨ルール"
          width="280">
          <template slot-scope="scope">
            <el-select v-model="scope.row.recommendRuleId" placeholder="推奨ルールの選択">
              <el-option
                v-for="rule in recommendRules"
                :key="rule.id"
                :label="rule.title"
                :value="rule.id">
              </el-option>
            </el-select>
          </template>
        </el-table-column>
        <el-table-column
          label="推奨ルールの評価">
          <template slot-scope="scope">
            <div class="">
              遷移率：{{ scope.row.viewRatio || '--' }}% 購入率：{{ scope.row.buyRatio || '--' }}%
            </div>
            <div class="">
              推薦回数：{{ scope.row.recommendCount || '--' }}回 遷移回数：{{ scope.row.viewCount || '--' }}回 購入回数：{{ scope.row.buyCount || '--' }}回
            </div>
          </template>
        </el-table-column>
      </el-table>
      <div class="adapt-btn-row">
        <el-button type="primary" @click="adaptRule">適用する</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import GroupingRule from '@/models/GroupingRule';
import RecommendRule from '@/models/RecommendRule';
import Group from '@/models/Group';

export default {
  name: 'GroupingRuleSaveView',
  data() {
    return {
      rule: null,
      showGroupInfo: false,
      groups: [],
      recommendRules: [],
    };
  },

  methods: {
    // 戻るボタン押下時
    back() {
      this.$router.back();
    },

    // 保存ボタン押下時
    saveGroupingRule() {
      this.$validator.validateAll().then((result) => {
        if (!result) {
          return;
        }
        this.$confirm('保存しますか?').then(() => {
          this.rule.save();
          this.$router.back();
        });
      });
    },

    // 試し実行ボタン押下時
    trialExecute() {
      this.rule.trialGrouping().then((groups) => {
        this.groups = groups;
        this.showGroupInfo = true;
      });
    },

    // 適用ボタン押下時
    adaptRule() {
      this.$validator.validateAll().then((result) => {
        if (!result) {
          return;
        }
        this.$confirm('適用しますか?').then(() => {
          // GroupingRuleのactiveフラグを付け替える
          GroupingRule.findAll().then((groups) => {
            groups.forEach((_rule) => {
              _rule.active = false;
              _rule.save();
            });
            this.rule.active = true;
            this.rule.save();
            return this.rule;
          }).then((rule) => {
            // Groupの保存
            Group.deleteByGroupingRuleId(rule.id);
            this.groups.forEach((group) => {
              group.save();
            });
            this.$router.back();
          });
        });
      });
    },
  },

  created() {
    this.rule = GroupingRule.of();
  },

  // 画面描画時
  mounted() {
    RecommendRule.findAll().then((rules) => {
      this.recommendRules = rules;
    });

    if (!this.$route.params.id) {
      return;
    }

    GroupingRule.findOne(this.$route.params.id).then((rule) => {
      this.rule = rule;
      return Group.findByGroupingRuleId(rule.id);
    }).then((groups) => {
      this.groups = groups;
      this.showGroupInfo = groups.length > 0;
    });
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

      &.title {
        padding-left: 20px;
        padding-right: 20px;
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

    &::placeholder-shown {
      color: #ddd;
    }
    &::-webkit-input-placeholder {
      color: #ddd;
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

// グループ情報
.group-info {
  .el-select {
    display: block;
  }

  .adapt-btn-row {
    margin-top: 22px;
    text-align: center;
  }
}

.active-badge {
  text-align: right;
}
</style>
