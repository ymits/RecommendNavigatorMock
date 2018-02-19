<template>
  <div class="set-user">
    <div class="qa-area">
      <div class="section-title">
        <h2>
          ユーザ設定
        </h2>
      </div>
      <el-form label-position="top" label-width="100px" class="user-info">
        <el-form-item label="ユーザID">
          <el-input v-model="userId"></el-input>
        </el-form-item>
        例：80100001, 80200001
      </el-form>
    </div>
    <div class="action-btn">
      <el-button-group>
        <el-button disabled>-</el-button>
        <el-button type="primary" @click="goNext">質問の開始<i class="el-icon-arrow-right el-icon-right"></i></el-button>
      </el-button-group>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      userId: ''
    }
  },
  methods: {
    // 次へボタン押下時
    goNext() {
      this.$router.push({ name: 'Step1' });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.user-info {
  /deep/ label {
    padding: 0;
  }
}

</style>
