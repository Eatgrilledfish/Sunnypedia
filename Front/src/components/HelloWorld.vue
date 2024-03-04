<template>
  <div id="app">
    <el-button type="primary" @click="fetchMessage">Fetch Message</el-button>
    <div v-if="message">
      Message from Flask: {{ message }}
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { ElButton } from 'element-plus'
import 'element-plus/dist/index.css'

export default {
  name: 'App',
  components: {
    ElButton,
  },
  data() {
    return {
      message: null,
    }
  },
  methods: {
    fetchMessage() {
      axios.get('http://127.0.0.1:5000/hello/')
        .then(response => {
          this.message = response.data.message;
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    }
  }
}
</script>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
