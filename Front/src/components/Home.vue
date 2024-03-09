<template>
    <el-main>

        <!-- 主要内容区域 -->
        <div class="main-content">
        <div class="pediabg">
            <p class="text-overlay">Get your sources stright before laying sunny side up</p>
        </div>
        </div>
        
        <!-- 走马灯 -->
        <div class="testimonial-section">
        <el-carousel indicator-position="none" :autoplay="false" >
            <el-carousel-item v-for="item in items" :key="item.id">
                <!-- 图片 -->
                <img :src="item.imageSrc" alt="图片描述" style="max-width: 100%; max-height: 320px;  display: block; position: middle; margin-left: auto; margin-right: auto;" />
                <!-- 文字描述
                <div style="position: absolute; bottom: 70%; left: 50%; transform: translateX(-50%); color: #a69b93; background-color: #f8f7f5; padding: 10px; font-weight: bold; font-family: 'Arial', sans-serif; ">
                {{ item.text_name }}
                </div>
                <div style="position: absolute; bottom: 40%; left: 40%; transform: translateX(-50%); color: balck; background-color: #f8f7f5; padding: 10px; font-weight: bold; font-family: 'Arial', sans-serif; ">
                {{ item.text_content }}
                </div> -->
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


.pediabg {
  width: 100%; /* 或者指定宽度 */
  min-height: 300px; /* 根据需要调整高度 */
  background-image: url('../assets/Pedia_new2.jpg');
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
</style>