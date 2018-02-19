<template>
  <div id="app">
    <header></header>
    <transition :name="transitionName">
      <router-view class="child-view"/>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      transitionName: 'slide-left'
    }
  },
  watch: {
    '$route' (to, from) {
      const toDepth = to.path.split('/').length
      const fromDepth = from.path.split('/').length
      if (toDepth < fromDepth) {
        this.transitionName = 'slide-right';
      } else if (toDepth > fromDepth) {
        this.transitionName = 'slide-left';
      } else {
        var toStepNum = Number(to.path.slice(-1));
        var fromStepNum = Number(from.path.slice(-1));
        this.transitionName = toStepNum < fromStepNum ? 'slide-right' : 'slide-left'
      }
    }
  }

}
</script>

<style lang="scss">
header {
  background: #195547;
  height: 60px;
}
.child-view {
  position: absolute;
  left:0;
  right:0;
  top:60px;
  bottom:0;
  transition: all .5s cubic-bezier(.55,0,.1,1);
}
.slide-left-enter, .slide-right-leave-active {
  //opacity: 0;
  -webkit-transform: translate(100%, 0);
  transform: translate(100%, 0);
}
.slide-left-leave-active, .slide-right-enter {
  //opacity: 0;
  -webkit-transform: translate(-100%, 0);
  transform: translate(-100%, 0);
}
</style>
