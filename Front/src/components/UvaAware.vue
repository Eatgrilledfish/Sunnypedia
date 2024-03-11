<script setup>
</script>

<template>
<div class="UVAware">
  <div class="column" v-for="(item, index) in items" :key="index">
    <div class="content-wrapper">
      <img :src="item.image" :alt="`Image ${index + 1}`" class="image">
      <h2>{{ item.heading1 }}</h2>
      <p1>{{ item.text1 }}</p1>
    </div>
    <div class="subheading" v-if="item.heading2">
      <h3>{{ item.heading2 }}</h3>
    </div>
    <p2 v-if="index === 0">
      {{ item.text2.split('warmest')[0] }}
      <a href="https://earthobservatory.nasa.gov/world-of-change/global-temperatures">warmest</a>
      {{ item.text2.split('warmest')[1] }}
    </p2>
    <p2 v-else-if="index === 1">
      {{ item.text2.split('Antartica')[0] }}
      <a href="https://www.dcceew.gov.au/environment/protection/ozone/ozone-science/ozone-layer">Antartica</a>
      {{ item.text2.split('Antartica')[1] }}
    </p2>
    <p2 v-else>
      {{ item.text2 }}
    </p2>
  </div>
    <div class="wrap-column">
      <div class="echart-container" ref="echartDom"></div>
      <div class="chart-description">
        <h2>{{ chartDescription.heading }}</h2>
        <p1>{{  chartDescription.text.split('uncontrollably')[0] }}<a href="https://www.aihw.gov.au/reports/cancer/cancer-data-in-australia/contents/overview-of-cancer-in-australia-2023">uncontrollably</a>{{  chartDescription.text.split('uncontrollably')[1] }}</p1>
        <h3>{{ chartDescription.heading2 }}</h3>
        <p2>{{  chartDescription.text2.split('ASR')[0] }}<a href="https://www.cancercouncil.com.au/cancer-prevention/sun-protection/understanding-uv-radiation/how-uv-radiation-increases-skin-cancer-risk/">ASR</a>{{  chartDescription.text2.split('ASR')[1] }}</p2>
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
        text2: "The Australian (ASR) rates of meanoma of skin (cancer) increased by 2020-22."
      }
    }
  },
  mounted() {
    // 初始化图表
    this.fetchDataAndInitChart();
  },
  methods: {
    fetchDataAndInitChart() {
      fetch('http://13.237.185.73:8000/data/graph')
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
  margin-left: 30px;
 
}
.content-wrapper {
  width: 100%; /* 确保包裹元素占满列的宽度 */
  
  font-size: 15px; 
   
  font-variant: normal; 
  font-weight: 400; 
  line-height: 21.4286px;
}

.column h2 {
  text-align: center;
  
   font-size: 24px; font-style: normal; font-variant: small-caps; font-weight: 700; line-height: 26.4px;color: #c09c84; font-family: Rockwell;
}
.column p1{
  
  font-family: Rockwell;font-size: 15px; font-style: light; font-style: italic;  font-weight: 500; line-height: 26.4px;
}
.column p2{
  
  font-family: Rockwell;font-size: 15px; font-style: light; font-weight: 500; line-height: 26.4px;
}


.image {
  max-width: 450px;
  height: 300px; /* 或你希望的固定高度 */
 

}
.column h3 {
  align-items: flex-start;
   font-size: 20px; font-style: normal; font-weight: 700; line-height: 26.4px;text-decoration: underline;
  
}

.chart-description h2 {
  text-align: center;
  font-size: 24px; font-style: normal; font-variant: small-caps; font-weight: 700; line-height: 26.4px;color: #c09c84; font-family: Rockwell;
  
}

.wrap-column {
  display: flex;
  flex-direction: column;
  align-items: center; /* 这会使图表和文本居中对齐 */
  margin: 20px;
  text-align: left;
}
.wrap-column p1{
  font-family: Rockwell;font-size: 15px; font-style: light; font-style: italic;  font-weight: 500; line-height: 24px;
}

.wrap-column p2{
  font-family: Rockwell;font-size: 15px; font-style: light; font-weight: 500; line-height: 26.4px;
}

.wrap-column h3{
  
   font-size: 20px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 26.4px;text-decoration: underline;

}
.echart-container {
  width: 450px;
  height:300px;

}
</style>