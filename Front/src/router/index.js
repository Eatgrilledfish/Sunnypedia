// router/index.js 或者 router.js，取决于你的项目结构
import { createRouter, createWebHistory } from 'vue-router'

// 导入页面组件
import SunscreenCalculator from '../components/SunscreenCalculator.vue';
import UvaAware from '../components/UvaAware.vue';
import Home from '../components/Home.vue';
import Uvmap from '../components/UvMap.vue';
import clothing from '../components/clothing.vue';


// 可以继续导入其他页面组件

const routes = [
  {
        path: '/',
        name: 'Home',
        component: Home
  },
  {
    path: '/sunscreen-calculator',
    name: 'SunscreenCalculator',
    component: SunscreenCalculator
  },
  {
    path: '/uva-aware',
    name: 'UvaAware',
    component: UvaAware
  },
  {
    path: '/uv-map',
    name: 'Uvmap',
    component: Uvmap
  },
  {
    path: '/clothing',
    name: 'clothing',
    component: clothing
  },
  // 定义其他路由
]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})

export default router
