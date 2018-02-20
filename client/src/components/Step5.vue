<template>
  <div class="step5">
    <div class="qa-area">
      <div class="page-title">個別投信ロボ</div>
      <div class="section-title">
        <h2>
          質問５：この先日本経済はどうなると思いますか？
        </h2>
      </div>
      <div class="select-btn">
        <el-button @click="select('1')" :class="{'is-active':value==='1'}">景気の見通しは明るい</el-button>
        <el-button @click="select('2')" :class="{'is-active':value==='2'}">景気の見通しは暗い</el-button>
        <el-button @click="select('3')" :class="{'is-active':value==='3'}">変わらない、わからない</el-button>
      </div>
    </div>
    <div class="action-btn">
      <el-button-group>
        <el-button icon="el-icon-arrow-left" @click="goBack">前の質問へ</el-button>
        <el-button type="primary" @click="goNext">診断結果へ<i class="el-icon-arrow-right el-icon-right"></i></el-button>
      </el-button-group>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Step5',
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
      this.$router.push({ name: 'Result' });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
