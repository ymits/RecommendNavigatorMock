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
  padding: 15px;
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


.section-title {
  position: relative;

  h2 {
    font-weight: normal;
    padding: 7px 0 7px 15px;
    font-size: 1.5rem;
    line-height: 1.21;
    border-left: 7px solid #1c5546;

    &:after {
      width: 100%;
      position: absolute;
      left: 0;
      bottom: -8px;
      border-top: 2px solid #ccc;
      content: '';
    }
  }
}

.qa-area {
  height: 450px;
}

.action-btn {
  .el-button-group {
    display: block;
  }
  .el-button {
    width: 50%;
    border-radius: 0;
    font-size:40px;
    padding: 20px;

    &.el-button--primary {
      background-color: #195547;
      border-color: #195547;

      &.is-disabled {
        background-color: rgba(25,85,71,0.65);
      }
    }
  }
}
</style>
