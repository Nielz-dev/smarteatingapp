
<template>

    <div class="min-h-full flex flex-col justify-start py-12 sm:px-6 lg:px-8 bg-green-500">
      <div class="sm:mx-auto sm:w-full sm:max-w-md">
        <img class="mx-auto h-12 w-auto" src="../static/img/2.png" alt="Logo de SmartEating" />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-green-900">Activación de cuenta</h2>
        <p class="mt-2 text-center text-sm text-gray-600">
        </p>
      </div>
      <div class=" rounded-md bg-green-50 p-4 justify-center">
      <div class="flex ">
        <div class="flex-shrink-0 ">
          <CheckCircleIcon class="h-5 w-5 text-green-400" aria-hidden="true" />
        </div>
        <div class="ml-3">
          <p class="text-sm font-medium text-green-800">Su cuenta ha sido activada con éxito</p>
        </div>
        <div class="ml-auto pl-3 ">
          <div class="-mx-1.5 -my-1.5">
            <button type="button" class="inline-flex bg-green-50 rounded-md p-1.5 text-green-500 hover:bg-green-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-green-50 focus:ring-green-600">
              <span class="sr-only">Dismiss</span>
              
            </button>
          </div>
        </div>
      </div>
    </div> 

    </div>
    
  </template>


 
<script>
import { CheckCircleIcon, XIcon } from '@heroicons/vue/solid'
import axios from 'axios';

export default {
  // Componentes utilizados en este componente
  components: {
    CheckCircleIcon,
    XIcon,
  },
  data() {
    return {
      uid: '',
      token: ''
    };
  },
  created() {
    // Recuperar los parámetros uid y token de la ruta
    this.uid = this.$route.params.uid;
    this.token = this.$route.params.token;

    // Activar la cuenta al cargar el componente
    this.activateAccount();
  },
  methods: {
    // Método para activar la cuenta
    activateAccount() {
      // Construir la URL de la API de activación
      const url = axios.defaults.baseURL + `/api/users/activation/`;

      // Llamar a la API de activación
      axios({
        method: 'post',
        url: url,
        headers: { 'Content-Type': 'application/json' },
        data: { uid: this.uid, token: this.token }
      })
        .then(response => {
          // Redirigir al usuario a la página de inicio de sesión después de activar la cuenta
          this.$router.push('/login');
        })
        .catch(error => {
          // Manejar errores en caso de fallo de activación
          console.error(error);
        });
    }
  }
};
</script>
