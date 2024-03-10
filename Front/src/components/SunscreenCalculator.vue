
<template>
  <div style="flex-grow: 1;">
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
      <!-- 调整了内部布局的边距 -->
      <div style="flex: 1; margin-left: 300px;"> <!-- 根据需要调整边距 -->
        <img :src="sunOutlineImageUrl" alt="Description Image" style="width: 100%; max-width: 200px; height: auto;">
      </div>
      <div style="flex: 3;margin-right: 200px;">
        <p>Worrying if you've been applying enough sunscreen? Sit back and leave the heavy math to us.</p>
        <p>SunnyPedia's new Sunscreen Calculator highly customised formula can tell you exactly how much YOU need! Give it a spin!</p>
      </div>
    </div>
    
    <h1 style="margin-left: 330px;">User Profile</h1>


    <div style="display: flex; align-items: flex-start;">
      <!-- 图片部分 -->
      <div style="margin-left: 500px;"> <!-- 根据需要调整右边距 -->
        <img :src="outlineImageUrl" alt="Outline Image" style="width: auto; max-width: 200px; max-height: 100%;">
      </div>

      <div style="flex-grow: 1; margin-left: 100px;">
        <form @submit.prevent="submitForm">
          <div style="margin-bottom: 25px;margin-top: 50px;">
            <label for="gender">Gender:</label>
              <select v-model="gender">
                <option value="male">Male</option>
                <option value="female">Female</option>
              </select>
          </div>
          <div style="margin-bottom: 25px;">
            <label for="height">Height (cm):</label>
            <input type="number" v-model.number="height" />
          </div>
          <div style="margin-bottom: 25px;">
            <label for="weight">Weight (kg):</label>
            <input type="number" v-model.number="weight" />
          </div>

          <!-- 衣物选择 -->
          <div style="margin-bottom: 25px;">
            <label for="head">Headwear:</label>
            <select v-model="head">
              <option value="">None</option>
              <option value="hat">Hat</option>
              <!-- 添加更多头饰选项 -->
            </select>
          </div>
          <div style="margin-bottom: 25px;">
            <label for="top">Topwear:</label>
            <select v-model="top">
              <option value="">None</option>
              <option value="long_sleeved">Long-sleeved top</option>
              <option value="short_sleeved">Short-sleeved top</option>
              <option value="vest">Short-sleeved top</option>
              <option v-if="gender === 'female'" value="full_body_swimsuit">full-body swimsuit</option>
              <option v-if="gender === 'female'" value="swimsuit">swimsuit</option>
              <!-- 添加更多上衣选项 -->
            </select>
          </div>
          <div style="margin-bottom: 25px;">
            <label for="bottom">Bottomwear:</label>
            <select v-model="bottom">
              <option value="">None</option>
              <option value="trousers">Trousers</option>
              <option v-if="gender === 'female'" value="long_shorts">Long shorts</option>
              <option v-if="gender === 'female'" value="long_skirt">long skirts</option>
              <option v-if="gender === 'female'" value="middle_skirt">middle skirt</option>
              <option v-if="gender === 'female'" value="short_shorts">short shorts</option>
              <option v-if="gender === 'female'" value="short_skirt">short skirt</option>
              <option v-if="gender === 'male'" value="skateboard_shorts">skateboard shorts</option>
              <option v-if="gender === 'male'" value="swimming_trunks">swimming trunks</option>
              <!-- 添加更多下身衣物选项 -->
            </select>
          </div>
          <div style="margin-bottom: 25px;">
            <label for="shoes">Shoes:</label>
            <select v-model="shoes">
              <option value="">None</option>
              <option value="shoes">Shoes</option>
              <option value="flip_flops">Flip-flops</option>
              <!-- 添加更多鞋子选项 -->
            </select>
          </div>

        <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  </div>
    
  
</template>
<script>
import axios from 'axios';

import sunOutlineImage from '@/assets/SunOutline.jpg';

import outlineImage from '@/assets/outline.png';

export default {
  
  data() {
    return {
      gender: 'male',
      height: 0,
      weight: 0,
      head: '',
      top: '',
      bottom: '',
      shoes: '',
      sunOutlineImageUrl: sunOutlineImage,
      outlineImageUrl: outlineImage,
    };
  },
  methods: {
    submitForm() {
      const userProfile = {
        gender: this.gender,
        height: this.height,
        weight: this.weight,
        head: this.head,
        top: this.top,
        bottom: this.bottom,
        shoes: this.shoes,
      };

      // 直接发送到后端，使用axios
      axios.post('http://127.0.0.1:5000/data/sunscreen', userProfile)
        .then(response => {
          // 这里处理后端返回的响应
          console.log(response.data);
          alert("Sunscreen calculation result: " + JSON.stringify(response.data));
        })
        .catch(error => {
          // 处理错误
          console.error(error);
          alert("Failed to calculate sunscreen amount.");
        });
    },
  },
};
</script>
