<template>
  <el-container id="app" >
    <el-header height="40px">Header</el-header>
    <el-container>
      <el-aside width="200px">
        <el-menu :router="true" :default-active="activeLink"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b">
          <template v-for="rule in $router.options.routes">
            <el-menu-item :index="rule.path">
                <i :class="rule.icon"></i>
                {{ rule.title }}
            </el-menu-item>
          </template>
        </el-menu>
      </el-aside>
      <router-view/>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: 'app',

  mounted() {
    const match = this.$route.matched.sort((a, b) => a - b)[0];
    // _.chain(this.$route.matched).sortBy(n => n.path.length).last().value();
    this.activeLink = match.path;
  },
  data() {
    return {
      activeLink: null,
    };
  },
};
</script>

<style>

</style>
