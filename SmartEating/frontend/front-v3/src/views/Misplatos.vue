
<template>
  <Navbar/>

  <div class="bg-green-500 ">
    <div class="flex flex-col max-w-[1280px] mx-auto py-10 gap-10 px-10 lg:px-20">
      <div class="w-full text-3xl font-extrabold text-green-900">Mis platos</div>
      <router-link :to="`/addEvento`">
              <button type="button"
                class="flex items-center justify-center mb-5 rounded-md border border-transparent bg-green-800 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2 sm:w-auto">Añadir
                plato
              </button>
        </router-link>
    </div>
  </div>
  
  
   
<div class="min-h-screen bg-green-500 flex justify-center items-top py-10">
  <div class="md:px-4 md:grid md:grid-cols-2 lg:grid-cols-4 gap-5 space-y-4 md:space-y-0">  
    <div v-for="item in x">
      <div class="w-80 bg-green-200 px-6 pt-6 pb-2 rounded-xl shadow-lg transform hover:scale-105 transition duration-500">
      <div class="relative ">
        <img class="w-full rounded-xl object-cover h-52 " :src="item.foto_perfil" alt="Imagen de perfil del usuario" />
      </div>
      <h1 class="mt-4 text-green-800 text-2xl font-bold cursor-pointer">{{ item.nombre }}</h1>
      <div class="my-4">
        <div class="flex space-x-1 items-center" v-for="ingrediente in item.ingredientes" :key="ingrediente.nombre">
          
          <p class="text-green-800 font-semibold">
           - {{ ingrediente.nombre }} 
            ( {{ ingrediente.cantidad }}
             {{ ingrediente.tipo_peso }} )
          </p>
        </div>
        <router-link :to="`/misplatos/${item.id}/update`">
          <button class="mt-4 text-xl w-full text-white bg-green-600 py-2 rounded-xl shadow-lg">Editar plato</button>
        </router-link>
       
      </div>
    </div>
    </div>
  
  </div>
</div>
<Footer></Footer> 
</template>

<script>
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';
import axios from 'axios';

export default {
  data() {
    return {
      x: [] // Array vacío para almacenar los datos recibidos
    }
  },
  methods: {
    test() {
      console.log('test');
    }
  },
  components: {
    Navbar,
    Footer
  },
  mounted() {
    // Realizar una solicitud GET a la ruta 'api/listplatos/'
    axios.get('api/listplatos/')
      .then(response => {
        // Cuando se reciba la respuesta, asignar los datos a la variable 'x'
        this.x = response.data;
      })
      .catch(error => {
        console.log(error);
      });
  }
}
</script>
