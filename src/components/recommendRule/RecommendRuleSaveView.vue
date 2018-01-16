<template>
  <div class="recommend-rule-save-view">
    <div class="page-title">
      <div class="row">
        <div class="col fix">
          <el-button type="text" @click="back" icon="el-icon-arrow-left">戻る</el-button>
        </div>
        <div class="col title">
          <input type="text" class="title-text" name="title" v-model="title" placeholder="ルール名称" v-validate="'required'">
        </div>
        <div class="col fix">
          <el-button type="primary" @click="saveRecommendRule">保存</el-button>
        </div>
      </div>
      <el-alert v-show="errors.has('title')" title="名称は必須だよ" type="error" show-icon :closable="false"></el-alert>
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
import RecommendRule from '@/models/RecommendRule';

export default {
  name: 'RecommendRuleSaveView',
  data() {
    return {
      title: null,
      filename: null,
      params: null,
    };
  },

  methods: {
    // 戻るボタン押下時
    back() {
      this.$router.back();
    },

    // 保存ボタン押下時
    saveRecommendRule() {
      this.$validator.validateAll().then((result) => {
        if (!result) {
          return;
        }
        this.$confirm('保存しますか?').then(() => {
          let rule;
          if (this.$rule) {
            rule = this.$rule;
          } else {
            rule = RecommendRule.of(this.title, this.filename, this.params);
          }
          rule.title = this.title;
          rule.filename = this.filename;
          rule.params = this.params;

          rule.save();

          this.$router.back();
        });
      });
    },
  },

  // 画面描画時
  mounted() {
    if (!this.$route.params.id) {
      return;
    }
    this.$rule = RecommendRule.findOne(this.$route.params.id);
    this.title = this.$rule.title;
    this.filename = this.$rule.filename;
    this.params = this.$rule.params;
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
</style>
