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
            // 示例数据，实际应用中应从后端获取
            [new Date('2024-03-09T06:00Z').getTime(), 1],
            [new Date('2024-03-09T09:00Z').getTime(), 4],
            [new Date('2024-03-09T12:00Z').getTime(), 8],
            // 更多数据...
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
