import { createRouter, createWebHistory } from 'vue-router'

// import components
import SunscreenCalculator from '../components/SunscreenCalculator.vue';
import UvaAware from '../components/UvaAware.vue';
import Home from '../components/Home.vue';
import Uvmap from '../components/UvMap.vue';
import Clothing from '../components/clothing.vue';


// import routes

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
    component: Clothing
  },
]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})

export default router
