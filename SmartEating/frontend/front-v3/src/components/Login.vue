
<template>

    <div class="min-h-full flex flex-col justify-center py-12 sm:px-6 lg:px-8 bg-green-500">
      <div class="sm:mx-auto sm:w-full sm:max-w-md">
        <img class="mx-auto h-12 w-auto" src="../static/img/2.png" alt="Logo de SmartEating" />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-green-900">Inicio de sesión</h2>
        <p class="mt-2 text-center text-sm text-gray-600">
        </p>
      </div>
  
      <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
          <form class="space-y-6" @submit.prevent="submitForm">
            <div>
              <label for="email" class="block text-sm font-medium text-gray-700"> Correo electrónico </label>
              <div class="mt-1">
                <input v-model="email" id="email" name="email" type="email" placeholder="Email"  required class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
              </div>
            </div>
  
            <div>
              <label for="password" class="block text-sm font-medium text-gray-700">Contraseña</label>
              <div class="mt-1">
                <input id="password" v-model="password" name="password" type="password" placeholder="Contraseña"  required class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
                <div class="text-sm">
                  <router-link to="/reset-password" class="font-medium text-green-600 hover:text-green-500">Olvidaste tu contraseña?</router-link>
                </div>
              </div>
            </div>
  
            <div class="flex items-center justify-between">
              <div class="flex items-center">
                <input id="remember-me" name="remember-me" type="checkbox" class="h-4 w-4 text-green-600 focus:ring-green-500 border-gray-300 rounded" />
                <label for="remember-me" class="ml-2 block text-sm text-gray-900"> Remember me </label>
              </div>
  
              
              <div class="text-sm">
                <router-link to="/signup" class="font-medium text-green-600 hover:text-green-500">Regístrate</router-link>
              </div>
            </div>
  
            <div>
              <button type="submit" class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Iniciar sesión</button>
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
        password: ''
      };
    },
    setup() {
      // Inicializar la biblioteca de notificaciones Toast
      const toast = useToast();
      // Estas opciones anularán las opciones definidas en el registro del complemento "app.use" para esta notificación específica.
      // Se hace disponible dentro de los métodos
      return { toast };
    },
    methods: {
      // Método para enviar el formulario
      submitForm(e) {
        // Crear objeto FormData con los valores del formulario
        const formData = {
          email: this.email,
          password: this.password
        };
        axios.defaults.headers.common['Authorization'] = '';
        
        // Llamar a la API para iniciar sesión
        axios.post('api/token/login/', formData)
          .then(response => {
            // Redirigir al usuario a la página de inicio después de iniciar sesión
            this.$router.push('/');
            // Obtener el token de autenticación de la respuesta
            const token = response.data.auth_token;
            // Almacenar el token en el store o en localStorage según tus necesidades
            this.$store.commit('setToken', token);
            // Establecer el token en los headers de Axios para futuras solicitudes
            axios.defaults.headers.common['Authorization'] = "Token " + token;
            // Almacenar el token en localStorage para persistencia
            localStorage.setItem("token", token);
          })
          .catch(error => {
            if (error.response.data.detail == 'Token inválido.') {

              localStorage.removeItem("token", token);
              
            }
            console.log(error);
            if (error.response && error.response.status !== 200) {
              // Mostrar mensaje de error en caso de email o contraseña incorrectos
              this.toast.error("Email o contraseña incorrectos", {
                position: "top-right",
                timeout: 5000,
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
            }
          });
      }
    }
  };
  </script>
  