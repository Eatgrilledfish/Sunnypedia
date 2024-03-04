<template>
  <el-container class="home-container">
    <el-header>
      <h1>SunnyPedia</h1>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
        <el-menu-item index="1">UV Index</el-menu-item>
        <el-menu-item index="2">Clothing</el-menu-item>
        <el-menu-item index="3">Sunscreen Calculator</el-menu-item>
        <el-menu-item index="4">UVAware</el-menu-item>
        <el-menu-item index="5">Notifications</el-menu-item>
      </el-menu>
    </el-header>
    <el-main>
      <div class="content">
        <h2>Empowering Families, Protecting Futures:</h2>
        <p>Your Guide to Sun Safety</p>
      </div>
      <!-- 忽略图片的部分 -->
      <div>
        <p>Content or placeholders can go here.</p>
      </div>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      activeIndex: '1'
    };
  }
};
</script>

<style scoped>
.home-container {
  text-align: center;
}

.el-header {
  background-color: #333;
  color: white;
  padding: 20px;
}

.el-menu-demo {
  background-color: transparent;
  border: none;
}

.content h2,
.content p {
  color: #333;
}

.el-main {
  background-color: #f5f5f5; /* Changed to a plain color for background */
  padding: 60px;
}

/* ...additional styles... */
</style>
