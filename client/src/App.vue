<template>
  <div id="app">
    <header></header>
    <div class="main">
      <transition :name="transitionName">
        <router-view class="child-view"/>
      </transition>
    </div>
    <footer>Copyright © 2018 Simplex Inc.</footer>
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
footer {
  background: #195547;
  height: 25px;

  position: absolute;
  bottom:0;
  left:0;
  right:0;
  text-align: center;
  color: #fff;
  font-size: 16px;
  padding: 15px;

}
.child-view {
  position: absolute;
  width: 1200px;
  // margin-left: auto;
  // margin-right: auto;
  left: 50%;
  margin-left: -600px;
  top:60px;
  bottom:25px;
  transition: all .5s cubic-bezier(.55,0,.1,1);
  padding: 15px;

  background: url(/static/image/profileQA_back.png);
  overflow: scroll;
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

.page-title {
  background-color: #fff;
  color: #333;
  font-weight: bold;
  display: inline-block;
  margin-left: 0px;
  padding: 15px 0px;
  border-radius: 4px;
  font-size: 18px;
  &:before {
    content: " ";
    display: inline-block;
    border: 10px solid transparent;
    border-left: 10px solid #195547;
    margin-top: 1px;
    margin-left: 0;
    float: left;
  }
}
.section-title {
  color: #fff;
  background-color: #195547;
  h2 {
    padding: 10px 0 7px 15px;
  }

}
/*
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
*/

.qa-area {
  height: 600px;
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

.el-button{
  &.el-button--default {
    &.is-active {
    background-color: #457;
    border-color: #457;
    color: #fff;
    }
  }
}

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
