<template>

    <div class="min-h-full flex flex-col justify-center py-12 sm:px-6 lg:px-8 bg-green-500">
      <div class="sm:mx-auto sm:w-full sm:max-w-md">
        <img class="mx-auto h-12 w-auto" src="../static/img/2.png" alt="Logo SmartEating App" />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-green-900">Reestablecer contraseña</h2>
        <p class="mt-2 text-center text-sm text-gray-600">
        </p>
      </div>
  
      <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
          <form class="space-y-6" @submit.prevent="submitFormSignup">
            
  
            <div>
              <label for="password" class="block text-sm font-medium text-gray-700"> Contraseña </label>
              <div class="mt-1">
                <input  v-model="password" id="password" name="password" type="password" placeholder="Contraseña" autocomplete="current-password" required class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
                
              </div>
            </div>

            <div>
              <label for="re_password" class="block text-sm font-medium text-gray-700"> Repetir contraseña </label>
              <div class="mt-1">
                <input  v-model="re_password" id="re_password" name="re_password" type="password" placeholder="Contraseña"  required class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
              </div>
            </div>

            
 
            <div>
              <button type="submit" class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Registrarse</button>
            </div>
          </form>
  
        
        </div>
      </div>
    </div>
  </template>

<script>
import axios from 'axios';
import { useToast } from "vue-toastification";

export default {
  data() {
    return {
      email: '',
      password: '',
      re_password: '',
      uid: '',
      token: '',
    };
  },
  created() {
    // Obtener los parámetros de la ruta
    this.uid = this.$route.params.uid;
    this.token = this.$route.params.token;
  },
  setup() {
    const toast = useToast();
    // Estas opciones reemplazarán las opciones definidas en el registro del complemento "app.use" para esta tostada específica
    // Hacerlo disponible dentro de los métodos
    return { toast };
  },
  methods: {
    // Función para enviar el formulario de registro
    submitFormSignup(e) {
      const formData = {
        uid: this.uid,
        token: this.token,
        new_password: this.password,
        re_new_password: this.re_password,
      };

      // Verificar si las contraseñas coinciden
      if (this.password == this.re_password) {
        axios
          .post('api/users/reset_password_confirm/', formData)
          .then(response => {
            // Contraseña restablecida con éxito
            this.toast.success("Contraseña restablecida con éxito.", {
              position: "top-right",
              timeout: 7010,
              closeOnClick: true,
              pauseOnFocusLoss: true,
              pauseOnHover: true,
              draggable: true,
              draggablePercent: 0.6,
              showCloseButtonOnHover: false,
              hideProgressBar: true,
              closeButton: "button",
              icon: true,
              rtl: false
            });

            // Redirigir al usuario a la página de inicio de sesión
            this.$router.push('/login');
          })
          .catch(error => {
            // Error al restablecer la contraseña
            this.toast.warning("Ha ocurrido un error, por favor vuelva a intentarlo.", {
              position: "top-right",
              timeout: 4990,
              closeOnClick: true,
              pauseOnFocusLoss: true,
              pauseOnHover: true,
              draggable: true,
              draggablePercent: 0.6,
              showCloseButtonOnHover: false,
              hideProgressBar: true,
              closeButton: "button",
              icon: true,
              rtl: false
            });
          });
      }
    }
  }
};
</script>
