<template>
  <el-main>
    <!-- 主要内容区域 -->
    <div class="main-content">
  <div class="pediabg">
    <div class="text-background">
      <div class="text-overlay">
        <h2 class="overlay-heading">Introducing Sunny Pedia</h2>
        <p>Verified resources to stay sun smart while lying sunny side up</p>
      </div>
    </div>
  </div>
</div>


    <!-- 走马灯 -->
    <div class="testimonial-section">
      <el-carousel indicator-position="none" :autoplay="false">
        <el-carousel-item v-for="item in items" :key="item.id">
          <div class="carousel-content">
            <!-- 图片 -->
            <img class="carousel-image" :src="item.imageSrc" alt="图片描述" />
            <!-- 文字描述 -->
            <div class="carousel-text">
              <p>{{ item.text_content }}</p>
              <h3>{{ item.text_name }}</h3>
              
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
    </div>
  </el-main>
</template>


<script>
import femaleImage1 from '@/assets/female1.avif';
import femaleImage2 from '@/assets/female2.jpg';
import femaleImage3 from '@/assets/female3.jpg';
export default {
  data() {
    return {
      // 添加走马灯的数据
      items: [
        { id: 1, imageSrc: femaleImage1, text_name: 'SARAH D', text_content: "\"Discovering this website revolutionized my skincare routine. From UV index insights to personalized sunscreen calculations, it's become my go-to for staying protected and informed. Highly recommend!\""},
        { id: 2, imageSrc: femaleImage2, text_name: 'Anne Zimmer' ,text_content : "\"Sunnypedia is my go-to for sun protection. With its intuitive interface, I easily find UPF clothing and accessories tailored to the day's UV index. The clickable UV index scale simplifies selection. From hats to goggles, Sunnypedia offers comprehensive options. Now, I confidently enjoy outdoor activities knowing I'm shielded from harmful UV rays. For effortless sun protection, Sunnypedia is unmatched.\""},
        { id: 3, imageSrc: femaleImage3, text_name: 'Jamie H' ,text_content : "\"SunnyPedia is a lifesaver for parents like me, prioritizing our children's health. Their website spreads crucial awareness about sun exposure, backed by eye-opening trendline charts of skin cancer in Australia. SunnyPedia empowers informed decisions, equipping us with essential knowledge and tools to safeguard our kids. With SunnyPedia, I feel confident in protecting my children from harmful UV exposure. Highly recommended for all parents concerned about sun safety.\""},
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
.pediabg {
  display: flex; /* 使用flex布局 */
  justify-content: space-between; /* 保持元素分开 */
  min-height: 300px;
  padding: 20px; /* 添加一些内边距 */
}

.pediabg::before {
  content: '';
  order: 2; /* 将图片放在右边 */
  flex-basis: 50%; /* 占据一半的宽度 */
  background-image: url('../assets/Pedia_new2.jpg');
  background-size: cover; /* 覆盖整个区域 */
  background-repeat: no-repeat;
}

.text-background {
  order: 1; /* 将白色背景放在左边 */
  flex-basis: 50%; /* 另一半的宽度用于文本和白色背景 */
  background-color: #fff; /* 白色背景 */
  display: flex;
  align-items: center; /* 垂直居中文本 */
  justify-content: center; /* 水平居中文本 */
  position: relative; /* 为了绝对定位文本覆盖层 */
  margin-left: 70px;
}

.text-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80%; /* 根据需要调整宽度 */
  color: black;
  padding-left: 400px;
  font-family: "Papyrus"; 
  font-weight: 700;
  line-height: 40px;
  font-size: 20px;
  
}


.overlay-heading {
  margin-bottom: 40px; /* 标题和段落之间的间距 */
  margin-top: -20px; /* 向上移动标题 */
  font-family: "Papyrus"; 
  font-size: 40px; 
  font-style: normal; 
  font-variant: normal; 
  font-weight: 700; 
  line-height: 45px;
}

.carousel-content {
  display: flex;
  align-items: center;
  justify-content: flex-start; /* 使内容靠左对齐 */
  padding-left: 100px; /* 图片左侧的间距 */
  padding-right: 100px; /* 文本右侧的间距 */
  
}

.carousel-image {
  flex: 1 0 auto; /* 修改为 auto 或具体的宽度值，根据需要调整 */
  max-width: 450px; /* 允许图片宽度自动调整 */
  height: auto; /* 保持图片高度自动，以维持比例 */
  object-fit: contain; /* 保证图片按比例缩放，完整显示 */
  margin-right: 40px; /* 保留原有的间距 */
}

.el-carousel {
  max-height: 400px; /* 如果需要，可以调整或移除最大高度限制 */
  height: auto; /* 保持自动高度，适应图片大小 */
  width: 100%; /* 保持原有的宽度设置 */
}


.carousel-text {
  display: flex; /* 启用 flex 布局 */
  flex-direction: column; /* 设置项目垂直排列 */
  align-items: center; /* 水平方向上居中对齐项目 */
  justify-content: center; /* 垂直方向上居中对齐项目 */
  text-align: center; /* 确保文本在其容器中居中 */
  flex: 1 0 40%; /* 根据需要调整宽度和基础设置 */
  padding: 20px; /* 添加一些内边距，根据需要调整 */
  color: #c09c84; /* 设置文本颜色 */
  font-style: italic; /* 使文本倾斜 */

}



</style>
