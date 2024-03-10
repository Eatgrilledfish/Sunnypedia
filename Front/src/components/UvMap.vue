<template>
  <div ref="chartContainer" class="uv-chart-container"></div>
</template>

<script>
import * as echarts from 'echarts';
import { ref, onMounted } from 'vue';

export default {
  setup() {
    const chartContainer = ref(null);
    const currentUvIndex = 3; // 假设这是实时获取的当前UV指数

    onMounted(() => {
      const myChart = echarts.init(chartContainer.value);

      // 自定义图表配置
      const option = {
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          type: 'time',
          boundaryGap: false
        },
        yAxis: {
          type: 'value',
          min: 0,
          max: 16,
          splitLine: {
            show: true
          }
        },
        visualMap: {
          top: 50,
          right: 10,
          pieces: [
            {gte: 11, color: '#7e0023'},
            {gte: 8, lt: 11, color: '#ff4500'},
            {gte: 6, lt: 8, color: '#ff8c00'},
            {gte: 3, lt: 6, color: '#fabed4'},
            {lt: 3, color: '#2894ff'}
          ],
          outOfRange: {
            color: '#999'
          }
        },
        series: [{
          data: [
            // 使用Unix时间戳（UTC）表示时间点
            [1618317040 * 1000, 2], // 2021-04-13 03:04:00 UTC
            [1618320640 * 1000, 1],
            [1618324240 * 1000, 3],
            [1618327840 * 1000, 4],
            [1618331440 * 1000, 8],
            [1618335040 * 1000, 6],
            [1618338640 * 1000, 4],
            [1618342240 * 1000, 2],
            [1618345840 * 1000, 1],
            // 可以继续添加更多数据点...
          ],
          type: 'line',
          areaStyle: {},
          smooth: true, // 曲线平滑
          lineStyle: {
            width: 2
          },
          itemStyle: {
            normal: {
              color: '#FF4500'
            }
          }
        }],
        graphic: [
          {
            type: 'group',
            bounding: 'raw',
            right: 80,
            bottom: 80,
            z: 100,
            children: [
              {
                type: 'rect',
                z: 100,
                left: 'center',
                top: 'middle',
                shape: {
                  width: 200,
                  height: 50
                },
                style: {
                  fill: '#fff',
                  stroke: '#555',
                  lineWidth: 2,
                  shadowBlur: 8,
                  shadowOffsetX: 3,
                  shadowOffsetY: 3,
                  shadowColor: 'rgba(0,0,0,0.3)'
                }
              },
              {
                type: 'text',
                z: 100,
                left: 'center',
                top: 'middle',
                style: {
                  fill: '#333',
                  text: [
                    'CURRENT',
                    `UV INDEX ${currentUvIndex}`
                  ].join('\n'),
                  font: '14px Microsoft YaHei'
                }
              }
            ]
          }
        ]
      };

      myChart.setOption(option);
    });

    return {
      chartContainer
    };
  }
};
</script>

<style scoped>
.uv-chart-container {
  width: 100%;
  height: 500px;
}
</style>
