import Vue from 'vue'
import Router from 'vue-router'
import SetUser from '@/components/SetUser'
import Step1 from '@/components/Step1'
import Step2 from '@/components/Step2'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SetUser',
      component: SetUser
    },
    {
      path: '/step/step1',
      name: 'Step1',
      component: Step1
    },
    {
      path: '/step/step2',
      name: 'Step2',
      component: Step2
    }
  ]
})
