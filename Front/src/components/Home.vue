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
              <h3>{{ item.text_name }}</h3>
              <p>{{ item.text_content }}</p>
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
    </div>
  </el-main>
</template>


<script>
import femaleImage from '@/assets/female.png';
export default {
  data() {
    return {
      // 添加走马灯的数据
      items: [
        { id: 1, imageSrc: femaleImage, text_name: 'TESTOMONIALS' , text_content : "Discovering this website revolutionized my skincare routine. From UV index insights to personalized sunscreen calculations, it's become my go-to for staying protected and informed. Highly recommend!"},
        { id: 2, imageSrc: femaleImage, text_name: 'Title of second persona' ,text_content : 'sssssssssssssssssssssssssssssssssssssssssssssssssssssss'},
        { id: 3, imageSrc: femaleImage, text_name: 'Title of Third persona' ,text_content : 'sssssssssssssssssssssssssssssssssssssssssssssssssssssss'},
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
}

.text-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80%; /* 根据需要调整宽度 */
  color: black;
  padding-left: 500px;
}


.overlay-heading {
  font-size: 24px; /* 标题大小 */
  margin-bottom: 10px; /* 标题和段落之间的间距 */
  margin-top: -40px; /* 向上移动标题 */
}

.carousel-content {
  display: flex;
  align-items: center;
  justify-content: flex-start; /* 使内容靠左对齐 */
  padding-left: 100px; /* 图片左侧的间距 */
  padding-right: 20px; /* 文本右侧的间距 */
}

.carousel-image {
  flex: 1 0 50%; /* 允许图片占据更多空间，基础宽度设置为50% */
  max-width: 50%; /* 增加图片的最大宽度，让图片变大 */
  height: auto;
  margin-right: 20px; /* 图片和文本之间的间距 */
}

.carousel-text {
  flex: 1 0 40%; /* 减少文本框的基础宽度，限制其成长 */
  padding-right: 20px; /* 文本的右侧添加间距 */
}



.el-carousel {
  max-height: 400px;
  height: auto;
  width: 100%;
}
</style>
