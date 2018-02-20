<template>
  <div class="step1">
    <div class="qa-area">
      <div class="section-title">
        <h2>
          質問１：どのような投資信託をお探しですか？
        </h2>
      </div>
      <div class="select-btn">
        <el-button @click="select('1')" :class="{'is-active':value==='1'}">自分の好みに合った投資信託を探す</el-button>
        <el-button @click="select('2')" :class="{'is-active':value==='2'}">現在持っている投資信託より、条件の良い投資信託を探す</el-button>
        <el-button @click="select('3')" :class="{'is-active':value==='3'}">自分に最適な投資信託の組み合わせを探す</el-button>
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
  name: 'Step1',
  data () {
    return {
      value: ''
    }
  },
  methods: {
    select(v) {
      this.value = v;
    },
    // 前へボタン押下時
    goBack() {
      this.$router.go(-1);
    },
    // 次へボタン押下時
    goNext() {
      this.$router.push({ name: 'Step2' });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.select-btn {
  width: 1000px;
  margin-left: auto;
  margin-right: auto;

  .el-button {
    display: block;
    width: 100%;
    margin: 0;
    font-size: 30px;
    padding: 20px;
    margin-top: 50px;
  }
}
</style>
