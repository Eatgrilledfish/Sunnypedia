
<template>
  <div style="flex-grow: 1;">
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
      <!-- 调整了内部布局的边距 -->
      <div style="flex: 1; margin-left: 300px;"> 
        <img :src="sunOutlineImageUrl" alt="Description Image" style="width: 100%; max-width: 200px; height: auto;">
      </div>
      <div style="flex: 3;margin-right: 200px; font-family: Rockwell; font-size: 20px;color: #c09c84; /* 设置文本颜色 */ font-style: italic; /* 使文本倾斜 */">
        <p>Worrying if you've been applying enough sunscreen? Sit back and leave the heavy math to us.</p>
        <p>SunnyPedia's new Sunscreen Calculator highly customised formula can tell you exactly how much YOU need! Give it a spin!</p>
      </div>
    </div>
    
    <h1 style="margin-left: 330px; color: #c09c84; text-decoration: underline;">User Profile</h1>


    <div style="display: flex; align-items: flex-start;">
      <!-- 图片部分 -->
      <div style="margin-left: 500px;"> 
        <img :src="outlineImageUrl" alt="Outline Image" style="width: auto; max-width: 200px; max-height: 100%;">
      </div>

      <div style="flex-grow: 1; margin-left: 100px;">
        <form @submit.prevent="submitForm">
          <div style="margin-bottom: 25px;margin-top: 10px;">
            <label for="gender">Gender:</label>
              <select v-model="gender">
                <option value="male">Male</option>
                <option value="female">Female</option>
              </select>
          </div>
          <div style="margin-bottom: 20px;">
            <label for="height">Height (cm):</label>
            <input type="number" v-model.number="height" step="0.01"/>
          </div>
          <div style="margin-bottom: 20px;">
            <label for="weight">Weight (kg):</label>
            <input type="number" v-model.number="weight" step="0.01" />
          </div>
          <!-- 衣物选择 -->
          <div style="margin-bottom: 20px;">
            <label for="head">Headwear:</label>
            <select v-model="head">
              <option value="">None</option>
              <option value="hat">Hat</option>      
            </select>
          </div>
          <div style="margin-bottom: 20px;">
            <label for="top">Topwear:</label>
            <select v-model="top">
              <option value="">None</option>
              <option value="long_sleeved">Long-sleeved top</option>
              <option value="short_sleeved">Short-sleeved top</option>
              <option value="vest">vest</option>
              <option v-if="gender === 'female'" value="full_body_swimsuit">full-body swimsuit</option>
              <option v-if="gender === 'female'" value="swimsuit">swimsuit</option>
            </select>
          </div>
          <div style="margin-bottom: 20px;">
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
            </select>
          </div>
          <div style="margin-bottom: 20px;">
            <label for="shoes">Shoes:</label>
            <select v-model="shoes">
              <option value="">None</option>
              <option value="shoes">Shoes</option>
              <option value="flip_flops">Flip-flops</option>
            </select>
          </div>

        <button type="submit">Submit</button>
        </form>
        <div class="results-container" v-if="calculationResult" style="margin-top: 20px; text-align: center;">
          <h2>Sunscreen Calculation Result</h2>
          <p>{{ calculationResult }}</p>
        </div>
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
      calculationResult: null,
    };
  },
  methods: {
    submitForm() {
      if (this.height <= 0 || this.weight <= 0) {
        alert("Please enter valid values for Height and Weight.");
        return; 
      }
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
      axios.post('https://aokodaisuki.com/api/sunscreen', userProfile)
        .then(response => {
          // 这里处理后端返回的响应
          console.log(response.data);
          this.calculationResult = `You need to apply approximately ${response.data.teaspoons} teaspoons (${response.data.milliliters}ml) of sunscreen every 2 hours when outside.\n\nNo sunscreen provides 100% protection so always use with a broad brimmed hat, sunglasses, covering clothing, and shade.`;
        })
        .catch(error => {
          // 处理错误
          console.error(error);this.calculationResult = "Failed to calculate sunscreen amount.";
          alert("Failed to calculate sunscreen amount.");
        });
    },
  },
};
</script>


<style>
.results-container {

  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
  max-width: 350px; 
}
</style>