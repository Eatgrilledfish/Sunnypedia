<template>
  <el-container>
    <el-header>
      <!-- 导航栏 -->
      <img src="./assets/logo.png" alt="logo" style="width: 180px; height: auto;" />
      <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
      >
        <el-menu-item index="1" @click="goToPage('/')">Home</el-menu-item>
        <el-menu-item index="2" @click="goToPage('/uva-aware')">UV Aware</el-menu-item>
        <el-menu-item index="3">UV Map</el-menu-item>
        <el-menu-item index="4">Clothing</el-menu-item>
        <el-menu-item index="5" @click="goToPage('/sunscreen-calculator')">Sunscreen Calculator</el-menu-item>
      </el-menu>
    </el-header>
    <router-view></router-view>
  </el-container>
</template>

<script>
import femaleImage from '@/assets/female.png';
export default {
  data() {
    return {
      activeIndex:'1',
      // 添加走马灯的数据
      items: [
        { id: 1, imageSrc: femaleImage, text_name: 'TESTOMONIALS' , text_content : "Discovering this website revolutionized my skincare routine. From UV index insights to personalized sunscreen calculations, it's become my go-to for staying protected and informed. Highly recommend!"},
        { id: 2, imageSrc: femaleImage, text_name: '第二张图片的描述' ,text_content : 'sssss'},
      ]
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log("select key:",key, keyPath);
    },
    goToPage(path) {
    this.$router.push(path);
    },
  },
};

</script>

<style scoped>

.el-menu {
  background-color: #f8f7f5;
  justify-content: center;
  height: 40px;
  line-height: 60px;
  padding-left: 100px;
  padding-top: 2px;
  border-bottom: none !important; /* 移除下划线 */
  --active-color: #fff;
  flex-grow: 1;
}


.el-menu-item {
  font-size: 18px; 
  padding-right: 80px;
}

.pediabg {
  width: 100%; /* 或者指定宽度 */
  min-height: 300px; /* 根据需要调整高度 */
  background-image: url('./assets/Pedia_new2.jpg');
  background-size: contain; /* 或者使用 'contain' 根据需求 */
  background-repeat: no-repeat; /* 防止图片重复 */
  background-position:  right;
  background-color: #fff; /* 设置背景颜色为白色，用于图片未覆盖的部分 */
}

.text-overlay {
  position: absolute; /* 绝对定位允许你指定元素相对于最近的定位祖先元素的确切位置 */
  top:40%; /* 垂直居中 */
  left:10%; /* 水平居中 */
  transform: translate(-50%, -50%); /* 使用 transform 来精确定位文本居中 */
  width: 10%;
  color: black; /* 根据背景图的颜色，你可能需要调整文本的颜色 */
  /* 添加其他需要的样式，比如字体大小、字体样式等 */
}

.el-carousel {
  max-height: 400px; 
  height: auto;
  width: 100%;
}


/* .el-carousel__item h3 {
  display: flex;
  color: #f8f7f5;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
} */

/* .el-carousel__item:nth-child(2n) {
  background-color: #f8f7f5;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #f8f7f5;
} */
</style>