<template>
  <div class="container">
    <!-- 居中的标题 -->
    <h1 class="heading">IF YOU CAN SEE SKIN, SO CAN <a href="https://www.sunsmart.com.au/downloads/resources/info-sheets/sun-protective-clothing-info-sheet.pdf" class="fancy-link">UV</a></h1>
    <!-- 下面的一行文本 -->
    <p class="text"><a href="https://www.skincancer.org/skin-cancer-prevention/sun-protection/sun-protective-clothing/" class="fancy-link">UPF (Ultraviolet Protection Factor)</a> measures the amount of UV radiation a fabric permits to reach your skin. UPF 50 blocks 98% of the sun's rays, significantly reducing your exposure risk.</p>
    <!-- 正下方居中的图片 -->
    <div class="image-and-text">
      <div class="left-content">
        <img class="side-image-left" :src="UPF7" alt="Low Protection">
        <h2 class="heading2-left">WHITE T-SHIRT</h2>
        <h3 class="subheading-left">LOW PROTECTION</h3>
        <ul class="dot-points-left">
          <li>Exposed skin</li>
          <li>Light colours</li>
          <li>Worn clothing</li>
          <li>Synthetic material</li>
          <li>Wet or too tight</li>
          <li>No Accessories</li>
        </ul>
      </div>
      <img class="centered-image" :src="clothingImage" alt="Clothing">
      <div class="right-content">
        <img class="side-image-right" :src="UPF1700" alt="High Protection">
        <h2 class="heading2-right">DARK DENIM SHIRT</h2>
        <h3 class="subheading-right">HIGH PROTECTION</h3>
        <ul class="dot-points-right">
          <li>Fully covered</li>
          <li>Dark colours</li>
          <li>Good condition</li>
          <li>Natural fibres like cotton</li>
          <li>Dry and fitting</li>
          <li>Hat and sunglasses</li>
        </ul>
      </div>
    </div>
  </div>
</template>


<script>
// 引入图片资源
import clothingImage from '@/assets/clothing.jpg';
import UPF7 from '@/assets/UPF7.png';
import UPF1700 from '@/assets/UPF1700.png';

export default {
  data() {
    return {
      clothingImage,
      UPF7, 
      UPF1700, 
    };
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.heading {
  color: #c09c84; /* 设置文本颜色 */
  font-size: 28px;
  font-family: Cambria;
}

.text {
  margin: 0 250px; /* 简化了左右外边距的设置 */
  color: #c09c84; /* 设置文本颜色 */
  font-style: italic; /* 使文本倾斜 */
  margin-top: 25px;
}
.side-image-left {
  max-width: 80px; /* 根据需要调整图片大小 */
  height: auto;
  margin-left: 200px; /* 设置图片和标题之间的间距 */
  float: left; /* 使图片浮动，标题和副标题紧随其后 */
}
.side-image-right {
  max-width: 80px; /* 根据需要调整图片大小 */
  height: auto;
  float: left; /* 使图片浮动，标题和副标题紧随其后 */
}

.image-and-text {
  display: flex;
  align-items: center;
  justify-content: space-around; /* 根据需要调整 */
  width: 100%;
  margin-top: 40px;
}

.centered-image {
  max-width: 100%; /* 确保图片不会超过其容器的宽度 */
  height: auto; /* 保持图片的原始宽高比 */
  margin-top: 0px;
  margin-left: 60px;
}

.left-content, .right-content {
  flex: 1;
}
.heading2-left {
  margin-left: 200px;
  margin-bottom: 40px;
  font-weight: 500;
  font-family: Cambria;
}

.heading2-right{
  margin-bottom: 40px;
  margin-right: 150px;
  font-weight: 500;
  font-family: Cambria;
  
}

.subheading-left {
  padding-left: 270px;
  margin-bottom: 30px;
  text-decoration: underline;
  font-style: italic;
  font-weight: 800;
}

.subheading-right {
  margin-bottom: 30px;
  margin-right: 120px;
  text-decoration: underline;
  font-style: italic;
  font-weight: 800;
}

.dot-points-left {
  text-align: left; /* 确保点状列表左对齐 */
  margin-left: 280px;
  color: #ff00ff;
  font-family: Rockwell;
}

.dot-points-right {
  text-align: left; /* 确保点状列表左对齐 */
  margin-left: 80px;
  color: #ff00ff;
  font-family: Rockwell;
  
}

.fancy-link {
  color: #c09c84; /* 链接的颜色 */
  /* text-decoration: none; 去掉下划线 */
}
</style>
