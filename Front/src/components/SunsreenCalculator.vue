<template>
  <div>
    <h1>User Profile</h1>
    <form @submit.prevent="submitForm">
      <div>
        <label for="gender">Gender:</label>
        <select v-model="gender">
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>
      </div>
      <div>
        <label for="height">Height (cm):</label>
        <input type="number" v-model.number="height" />
      </div>
      <div>
        <label for="weight">Weight (kg):</label>
        <input type="number" v-model.number="weight" />
      </div>

      <!-- 衣物选择 -->
      <div>
        <label for="head">Headwear:</label>
        <select v-model="head">
          <option value="">None</option>
          <option value="hat">Hat</option>
          <!-- 添加更多头饰选项 -->
        </select>
      </div>
      <div>
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
      <div>
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
      <div>
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
</template>
<script>
import axios from 'axios';

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
      axios.post('http://127.0.0.1:8000/data/sunscreen', userProfile)
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
