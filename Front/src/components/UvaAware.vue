<script setup>
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
    <div class="wrap-column">
      <div class="echart-container" ref="echartDom"></div>
      <div class="chart-description">
        <h2>{{ chartDescription.heading }}</h2>
        <p>{{ chartDescription.text }}</p>
        <h3>{{ chartDescription.heading2 }}</h3>
        <p>{{ chartDescription.text2 }}</p>
      </div>
  </div>
</div>

</template>

<script>
import * as echarts from 'echarts';
import TemperatureAnomaly from '@/assets/Temperature Anomaly.png';
import OzoneHole from '@/assets/The ozone hole.png';
export default {
  name: 'ThreeColumns',
  data() {
    return {
      // 你原始的数据
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
        }
      ],
      // 添加一个用于图表的引用对象
      echartRef: null,
      chartDescription: {
        heading: "FINALLY, THERE'S DISEASE",
        heading2: "Did you know?",
        text: "UV damages your DNA, if your body cannot repair it, the cells grows uncontrollably and form a tumor.",
        text2: "In 2023, the ozone layer opened up aobce Antartica spanning 3 times the size of Australia."
      }
    }
  },
  mounted() {
    // 初始化图表
    this.fetchDataAndInitChart();
  },
  methods: {
    fetchDataAndInitChart() {
      fetch('http://127.0.0.1:5000/data/graph')
        .then(response => response.json())
        .then(data => {
          // 假设返回的数据是data对象中的一部分，根据你的实际数据结构调整
          console.log(data)
          this.initChart(data);
        })
        .catch(error => console.error('Error fetching data:', error));
    },
    initChart(data) {
      this.echartRef = echarts.init(this.$refs.echartDom);
      const option = {
        // 更新ECharts配置项以匹配新的图表样式
        title: {
          text: "Trend rate (per 100k unit of pop) of mortality/incidences of skin ",
          textStyle: { fontSize: 14  }
        },
        legend: {
          data:['Mortality Rates','Incidence Rates'],
          top: 'bottom',
          textStyle: {color: '#000'}
        },
        xAxis: {
          type: 'category',
          data: data.years
        },
        yAxis: {
          type: 'value'
        },
        series: [
        {
          name: 'Mortality Rates',
          data: data.mortality_rates_per_100000,
          type: 'line',
          smooth: true // 这确保了线条平滑
        },
        {
          name: 'Incidence Rates',
          data: data.incidence_rates_per_100000,
          type: 'line',
          smooth: true // 这确保了线条平滑
        }
      ]
      };
      this.echartRef.setOption(option);
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

.chart-description h2 {
  text-align: center;
  /* 更多样式 */
}

.wrap-column {
  display: flex;
  flex-direction: column;
  align-items: center; /* 这会使图表和文本居中对齐 */
  margin: 20px;
  text-align: left;
}

.echart-container {
  width: 500px;
  height:330px;

}
</style>