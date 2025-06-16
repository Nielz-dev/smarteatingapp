import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import Login from "../components/Login.vue";
import Misplatos from "../views/Misplatos.vue";
import AddEvent from "../views/PlatoForm.vue";
import Signup from "../components/Signup.vue";
import Activate from "../components/Activate.vue";
import ForgotPassword from "../components/ForgotPassword.vue";
import ResetPasswordConfirm from "../components/ResetPasswordConfirm.vue";
import PlatoForm from "../views/PlatoForm.vue";
import Eventos from "../views/Eventos.vue";
import UserDetail from "../components/UserDetail.vue";
import GenerarLista from "../views/GenerarLista.vue";



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", component: Home },
    { path: "/login", component: Login },
    { path: "/misplatos", component: Misplatos },
    { path: "/add", component: AddEvent },
    { path: "/signup", component: Signup },
    { path: "/addEvento", component: PlatoForm },
    { path: "/eventos", component: Eventos },
    { path: "/userdetail", component: UserDetail },
    { path: "/misplatos/:id/update", component: PlatoForm }, 
    { path: "/generarlista", component: GenerarLista },
    { path: "/reset-password", component: ForgotPassword },
    { path: '/password/reset/confirm/:uid/:token', component: ResetPasswordConfirm },
    { path: "/activate/:uid/:token", component: Activate },
  ],
});

export default router;
