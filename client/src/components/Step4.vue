<template>
  <div class="step4">
    <div class="qa-area">
      <div class="page-title">個別投信ロボ</div>
      <div class="section-title">
        <h2>
          質問４：興味のある地域を教えてください
        </h2>
      </div>
      <div class="select-btn">
        <el-row :gutter="30">
          <el-col :span="6">
            <el-button @click="select('1')" :class="{'is-active':value.indexOf('1') >= 0}">欧州</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('2')" :class="{'is-active':value.indexOf('2') >= 0}">中近東</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('3')" :class="{'is-active':value.indexOf('3') >= 0}">日本</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('4')" :class="{'is-active':value.indexOf('4') >= 0}">北米</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('5')" :class="{'is-active':value.indexOf('5') >= 0}">アジア</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('6')" :class="{'is-active':value.indexOf('6') >= 0}">アフリカ</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('7')" :class="{'is-active':value.indexOf('7') >= 0}">オセアニア</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('8')" :class="{'is-active':value.indexOf('8') >= 0}">中南米</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('9')" :class="{'is-active':value.indexOf('9') >= 0}">グローバル</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('10')" :class="{'is-active':value.indexOf('10') >= 0}">エマージング</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('11')" :class="{'is-active':value.indexOf('11') >= 0}">おまかせ</el-button>
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="action-btn">
      <el-button-group>
        <el-button icon="el-icon-arrow-left" @click="goBack">前の質問へ</el-button>
        <el-button type="primary" @click="goNext">次の質問へ<i class="el-icon-arrow-right el-icon-right"></i></el-button>
      </el-button-group>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Step4',
  data () {
    return {
      value: []
    }
  },
  methods: {
    select(v) {
      let index = this.value.indexOf(v);
      if (index >= 0) {
        this.value.splice(index, 1);
      } else {
        this.value.push(v);
      }
    },
    // 前へボタン押下時
    goBack() {
      this.$router.go(-1);
    },
    // 次へボタン押下時
    goNext() {
      this.$router.push({ name: 'Step5' });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
