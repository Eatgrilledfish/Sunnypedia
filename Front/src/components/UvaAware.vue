<script setup>
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
</script>

<template>
<div class="UVAware">
  <div class="column" v-for="(item, index) in items" :key="index">
    <div class="content-wrapper">
      <img :src="item.image" :alt="`Image ${index + 1}`" class="image">
      <h2>{{ item.heading1 }}</h2>
      <p>{{ item.text1 }}</p>
    </div>
    <div class="subheading" v-if="item.heading2">
      <h3>{{ item.heading2 }}</h3>
    </div>
    <p>{{ item.text2 }}</p>
  </div>
</div>

</template>

<script>
import TemperatureAnomaly from '@/assets/Temperature Anomaly.png';
import OzoneHole from '@/assets/The ozone hole.png';
export default {
  name: 'ThreeColumns',
  data() {
    return {
      items: [
        {
          image: TemperatureAnomaly,
          heading1: "FIRST,THERE'S HEAT",
          text1: 'Global warming is a comparative measure with the pre-industrial (1850-1900s) average Earth temperatures as baseline.',
          heading2: 'Did you know?',
          text2: 'The Earth gets a little warmer everyday. The past 9 years have been the warmest since 1800s.'
        },
        {
          image: OzoneHole,
          heading1: "THEN, THERE'RE HOLES",
          text1: 'Stratospheric ozone that forms a layer above Earth absorbs UV-B and protects all life on Earth.',
          heading2: 'Did you know?',
          text2: 'In 2023, the ozone layer opened up aobce Antartica spanning 3 times the size of Australia.'
        },
        {
          image: 'path/to/your/image3.jpg',
          heading1: "FINALLY, THERE'S DISEASE",
          text1: 'UV damages your DNA, if your body cannot repair it, the cells grows uncontrollably and form a tumor.',
          heading2: 'Did you know?',
          text2: 'The Australian (ASR) rates of meanoma of skin (canser) increased by 2020-2022.'
        }
      ]
    }
  }
}
</script>

<style>
.UVAware {
  display: flex;
  justify-content: space-around;
  align-items: flex-start;
}

.column {
  flex: 1;
  margin: 10px;
  text-align: left;
  align-items: flex-start;
}
.content-wrapper, .subheading {
  width: 100%; /* 确保包裹元素占满列的宽度 */
}
.column h2 {
  text-align: center;
}
.image {
  max-width: 500px;
  height: 330px; /* 或你希望的固定高度 */

}
.column h3 {
  align-items: flex-start;
}
h2, h3 {
  margin: 10px 0;
}
</style>
