<template>

    <div class="min-h-full flex flex-col justify-center py-12 sm:px-6 lg:px-8 bg-green-500">
      <div class="sm:mx-auto sm:w-full sm:max-w-md">
        <img class="mx-auto h-12 w-auto" src="../static/img/2.png" alt="Logo de SmartEating" />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-green-900">Reestablecer contraseña</h2>
        <p class="mt-2 text-center text-sm text-gray-600">
        </p>
      </div>
  
      <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
          <form class="space-y-6" @submit.prevent="submitForm">
            <div>
              <label for="email" class="block text-sm font-medium text-green-700"> Correo electrónico </label>
              <div class="mt-1">
                <input  v-model="email" id="email" name="email" type="email" placeholder="Email" autocomplete="email" required class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
              </div>
            </div>
  
            <div>
              <button @click.prevent="resetPass" type="submit" class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Enviar</button>
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
      submitForm(event) {
        this.resetPass(event);
      },
    
      // Método para restablecer la contraseña
      resetPass(event) {
        event.preventDefault(); // Prevenir comportamiento predeterminado del formulario
  
        console.log("HA ENTRADO");
        // Llamar a la API para restablecer la contraseña
        axios.post('api/users/reset_password/', { email: this.email })
          .then(response => {
            // Notificación de éxito
            this.toast.success("Se ha enviado un email de confirmación para resetear la contraseña.", {
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
          })
          .catch(error => {
            console.log(error);
            if (error.response && error.response.status !== 200) {
              // Mostrar mensaje de error en caso de respuesta con error
              this.toast.error("Ha ocurrido un error", {
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
  