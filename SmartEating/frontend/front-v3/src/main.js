import './assets/main.css';
import { createApp } from 'vue';
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
import App from './App.vue';
import router from './router';
import store from './store/store';
import axios from 'axios';


axios.defaults.baseURL = process.env.VITE_API_ENDPOINT;

const app = createApp(App);
app.use(store);
app.use(router, axios);
app.use(Toast);
app.mount('#app');

