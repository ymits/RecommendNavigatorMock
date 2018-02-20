<template>
  <div class="step3">
    <div class="qa-area">
      <div class="section-title">
        <h2>
          質問３：興味のある資産を教えてください
        </h2>
      </div>
      <div class="select-btn">
        <el-row :gutter="30">
          <el-col :span="8">
            <el-button @click="select('1')" :class="{'is-active':value.indexOf('1') >= 0}">株式</el-button>
          </el-col>
          <el-col :span="8">
            <el-button @click="select('2')" :class="{'is-active':value.indexOf('2') >= 0}">債券</el-button>
          </el-col>
          <el-col :span="8">
            <el-button @click="select('3')" :class="{'is-active':value.indexOf('3') >= 0}">不動産</el-button>
          </el-col>
          <el-col :span="8">
            <el-button @click="select('4')" :class="{'is-active':value.indexOf('4') >= 0}">おまかせ</el-button>
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
  name: 'Step3',
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
      this.$router.push({ name: 'Step4' });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
