<template>
  <div>
    <div class="filter-box">
      <!-- 假设这里有一个下拉框供用户选择地区 -->
      <el-select v-model="selectedSuburb"  filterable placeholder="Please enter or select suburb" @change="fetchWeatherData">
        <el-option
          v-for="suburb in suburbs"
          :key="suburb"
          :label="suburb"
          :value="suburb">
        </el-option>
      </el-select>
      <div class="choose-button">
        <el-button @click="toggleDay">Switch to {{ isToday ? 'Tomorrow' : 'Today' }}</el-button>
      </div>
    </div>
    <div ref="chartContainer" class="uv-chart-container"></div>
    <div v-if="alerts.length" class="alerts">
      <div v-for="alert in alerts" :key="alert.event" class="alert">
        <h3>{{ alert.event }}</h3>
        <p>{{ alert.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import { ref, onMounted } from 'vue';

export default {
  setup() {
    const chartContainer = ref(null);
    const selectedSuburb = ref('');
    const alerts = ref([]);
    const suburbs = ref([]); // 动态加载地图
    const isToday = ref(true); // 今天还是明天的标志
    const uvData = ref([]); // 存储UV数据

    // Fetch suburbs from the backend
    const fetchSuburbs = async () => {
      // 先从本地存储中尝试获取地区列表
      const cachedSuburbs = localStorage.getItem('suburbs');
      if (cachedSuburbs) {
        suburbs.value = JSON.parse(cachedSuburbs);
      } else {
        try {
          const response = await fetch('http://127.0.0.1:5000/data/suburbs');
          if (response.ok) {
            const data = await response.json();
            suburbs.value = data;
            // 将地区列表保存到本地存储
            localStorage.setItem('suburbs', JSON.stringify(data));
          } else {
            console.error('Failed to fetch suburbs');
          }
        } catch (error) {
          console.error('Error fetching suburbs:', error);
        }
      }
    };

    // 切换当前显示的UV指数数据（今天/明天）
    const toggleDay = () => {
      isToday.value = !isToday.value;
      fetchWeatherData();
    };

    // 从后端获取数据
    const fetchWeatherData = async () => {
      try {
        const response = await fetch('http://13.237.185.73:8000/api/data/weather', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'accept': 'application/json',
          },
          body: JSON.stringify({ suburb: selectedSuburb.value }),
        });
        if (response.ok) {
          const data = await response.json();
          // 根据isToday更新数据，展示今天或明天的UV指数
          uvData.value = isToday.value ? data.today_hourly_uvi.map(item => [item.time, item.uvi]) : data.tomorrow_hourly_uvi.map(item => [item.time, item.uvi]);
          alerts.value = data.current_alerts;
          // console.log("UV Data:", uvData.value); // 打印原始数据
          // const mappedData = uvData.value.map(item => [item[0], item[1]]);
          // console.log("Mapped UV Data:", mappedData); // 打印映射后的数据
          updateChart();
        } else {
          console.error('Failed to fetch weather data');
        }
      } catch (error) {
        console.error('Error fetching weather data:', error);
      }
    };

    // 更新图表
    const updateChart = () => {
      const myChart = echarts.init(chartContainer.value);

      const option = {
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          type: 'category',
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
          data: uvData.value.map(item => [item[0], item[1]]),
          type: 'line',
          areaStyle: {},
          smooth: true,
          lineStyle: {
            width: 2
          },
          itemStyle: {
              color: '#FF4500'
          }
        }]
      };

      myChart.setOption(option);
    };

    onMounted(() => {
      fetchSuburbs(); // 获取地区列表
      fetchWeatherData(); // 加载组件时立即加载天气数据
    });

    return {
      chartContainer,
      selectedSuburb,
      alerts,
      suburbs,
      fetchWeatherData,
      toggleDay,
      isToday
    };
  }
};
</script>

<style scoped>
.uv-chart-container {
  width: 100%;
  height: 500px;
}
.alerts {
  margin-top: 20px;
}
.alert {
  border: 1px solid #ff4500;
  padding: 10px;
  margin-bottom: 10px;
}
.filter-box {
  display: flex;
  margin: 0 auto;
  width:50%;
  margin-bottom: 20px;
}
.choose-button {
  margin-left: 50px;
}
</style>
