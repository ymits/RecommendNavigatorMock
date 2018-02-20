<template>
  <div class="step2">
    <div class="qa-area">
      <div class="page-title">個別投信ロボ</div>
      <div class="section-title">
        <h2>
          質問２：どのような目的で投資信託を購入しますか？
        </h2>
      </div>
      <div class="select-btn">
        <el-button @click="select('1')" :class="{'is-active':value==='1'}">資産形成</el-button>
        <el-button @click="select('2')" :class="{'is-active':value==='2'}">使いながら運用</el-button>
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
  name: 'Step2',
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
      this.$router.push({ name: 'Step3' });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
