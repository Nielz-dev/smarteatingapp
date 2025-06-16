<template>

    <div class="min-h-full flex flex-col justify-center py-12 sm:px-6 lg:px-8 bg-green-500">
      <div class="sm:mx-auto sm:w-full sm:max-w-md">
        <img class="mx-auto h-12 w-auto" src="../static/img/2.png" alt="Logo SmartEating App" />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-green-900">Registro</h2>
        <p class="mt-2 text-center text-sm text-gray-600">
        </p>
      </div>
  
      <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
          <form class="space-y-6" @submit.prevent="submitFormSignup">
            <div>
              <label for="email" class="block text-sm font-medium text-gray-700"> Correo electrónico </label>
              <div class="mt-1">
                <input v-model="email" id="email" name="email" type="email" placeholder="Email" autocomplete="email" required class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
              </div>
            </div>

            <div>
              <label for="first_name" class="block text-sm font-medium text-gray-700"> Nombre </label>
              <div class="mt-1">
                <input v-model="first_name" id="first_name" name="first_name" type="text" placeholder="Nombre" autocomplete="first_name" required class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
                
              </div>
            </div>

            <div>
              <label for="last_name" class="block text-sm font-medium text-gray-700"> Apellidos </label>
              <div class="mt-1">
                <input v-model="last_name" id="last_name" name="last_name" type="text" placeholder="Apellidos" autocomplete="last_name" required class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
                
              </div>
            </div>
  
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
      first_name: '',
      last_name: '',
      re_password: '',
    };
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
        email: this.email,
        password: this.password,
        re_password: this.re_password,
        last_name: this.last_name,
        first_name: this.first_name,
      };

      const login = {
        email: this.email,
        password: this.password,
      };

      // Verificar si las contraseñas coinciden
      if (this.password == this.re_password) {
        axios
          .post('api/users/', formData)
          .then(response => {
            // Cuenta creada con éxito
            this.toast("Cuenta creada con éxito. Se ha enviado el link de activación a su correo.", {
              position: "top-right",
              timeout: 10000,
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
            // Verificar si ya existe un usuario con el correo electrónico proporcionado
            if (error.response.data.email == 'Ya existe user account con este email.') {
              this.toast.warning("Ya existe un usuario con este email.", {
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
            }
          });
      } else {
        // Las contraseñas no coinciden
        this.toast.error("La contraseña no coincide", {
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
    }
  }
};
</script>
