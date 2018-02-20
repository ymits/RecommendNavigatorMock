import Vue from 'vue'
import Router from 'vue-router'
import SetUser from '@/components/SetUser'
import Step1 from '@/components/Step1'
import Step2 from '@/components/Step2'
import Step3 from '@/components/Step3'
import Step4 from '@/components/Step4'
import Step5 from '@/components/Step5'
import Result from '@/components/Result'

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
    },
    {
      path: '/step/step3',
      name: 'Step3',
      component: Step3
    },
    {
      path: '/step/step4',
      name: 'Step4',
      component: Step4
    },
    {
      path: '/step/step5',
      name: 'Step5',
      component: Step5
    },
    {
      path: '/step/result',
      name: 'Result',
      component: Result
    }
  ]
})
