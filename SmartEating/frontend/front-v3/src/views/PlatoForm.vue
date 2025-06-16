


<template>
  <div class="min-h-full flex flex-col pt-6 py-12 px-6 lg:px-8 bg-green-500 ">
   <Navbar/>
    <div class="sm:mx-auto sm:w-full sm:max-w-md">

      <h1 class="font-sans mt-8 text-xl font-bold text-white pl-1">Añadir evento</h1>
      <p class="mt-2 text-center text-sm text-gray-600">
      </p>
    </div>

    <div class="mt-2 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="bg-white py-8 shadow rounded-lg px-6">
        <form class="space-y-6" @submit.prevent="submit">
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700"> Fecha </label>
            <div class="mt-1">
              <input v-model="form.date" id="date" name="date" type="date" autocomplete="form.date" required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
            </div>
          </div>

          <div>
            <label for="email" class="block text-sm font-medium text-gray-700"> Nombre del plato </label>
            <div class="mt-1">
              <input v-model="form.name" id="name" name="name" type="text" autocomplete="name" required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
            </div>
          </div>

          <div>
            <label for="email" class="block text-sm font-medium text-gray-700"> Imagen (url) </label>
            <div class="mt-1">
              <input v-model="form.image" id="image" name="image" type="text" autocomplete="image" 
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
            </div>
          </div>


          <div class="flex flex-row gap-2 items-center">
            <h2 class="font-sans text-sm font-bold ">Ingredientes ({{ ingredients_number }})</h2>
            <div @click="removeIngredient"
              class="cursor-pointer flex justify-center py-2 px-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-minus" width="16" height="16"
                viewBox="0 0 24 24" stroke-width="3.5" stroke="white" fill="none" stroke-linecap="round"
                stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                <path d="M5 12l14 0" />
              </svg>
            </div>
            <div @click="addIngredient"
              class="cursor-pointer flex justify-center py-2 px-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-plus" width="16" height="16"
                viewBox="0 0 24 24" stroke-width="3.5" stroke="white" fill="none" stroke-linecap="round"
                stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                <path d="M12 5l0 14" />
                <path d="M5 12l14 0" />
              </svg>
            </div>

          </div>



          <div class="flex flex-row gap-2" v-for="(item, index) in ingredients_number">
            <div class="w-1/2">
              <label for="email" class="block text-sm font-medium text-gray-700"> Ingrediente </label>
              <div class="mt-1">
                <input v-model="form.ingredients[index].name" id="name" name="name" type="text" autocomplete="name"
                  required
                  class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
              </div>
            </div>
            <div class="w-1/2 flex flex-row gap-2">
              <div class="w-1/2 "> <label for="quantity" class="block text-sm font-medium text-gray-700"> Cantidad
                </label>
                <div class="mt-1">
                  <input v-model="form.ingredients[index].quantity" id="quantity" name="quantity" type="number" min="0.1"
                    step="0.1" autocomplete="quantity" required
                    class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
                </div>
              </div>
              <div class="w-1/2 ">
                <label for="email" class="block text-sm font-medium text-gray-700"> Medida </label>
                <div class="mt-1">

                  <select name="ingredients" id="ingredients" v-model="form.ingredients[index].measure"
                    class=" block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm">
                    <option value="gramos">Gramos</option>
                    <option value="kilogramos">Kilogramos</option>
                    <option value="litros">Litros</option>

                  </select>
                </div>
              </div>

            </div>
          </div>


          <div>
            <button @click="crearPlato"
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
              Añadir plato</button>
          </div>
        </form>


      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue'
import axios from 'axios';

export default {
  data() {
    return {
      isUpdating: false, // Variable para indicar si estás en el proceso de actualización
      
      form: {
        date: "",
        name: "",
        image: "",
        ingredients: [
          {
            name: "",
            quantity: "",
            measure: ""
          }
        ],
      },
      ingredients_number: 1,
    };
  },
  async created() {
  // Obtener el ID del plato desde la URL
  const platoId = this.$route.params.id;
  
  if (platoId) {
    try {
    // Realizar una solicitud al servidor para obtener los datos del plato
    const response = await axios.get(`api/getplato/${platoId}/`);
    const plato = response.data;
    
    // Asignar los datos del plato al formulario
    this.form.name = plato.nombre;
    this.form.date = plato.fecha;
    this.form.image = plato.foto_perfil;
    this.form.ingredients = plato.ingredientes.map((ingrediente) => ({
      name: ingrediente.nombre,
      quantity: ingrediente.cantidad,
      measure: ingrediente.tipo_peso,
    }));
    if (this.form.ingredients.length > 0) {
      this.ingredients_number = 0;
    // Recorrer cada ingrediente existente y llamar a addIngredient()
    this.form.ingredients.forEach(() => {
      this.addIngredient();
    });
  }
  } catch (error) {
    console.error(error);
  }
  }
  
},
  mounted() {
    // Verificar la URL actual al cargar el componente
    const currentPath = this.$route.path;
    this.isUpdating = currentPath.includes("/update"); 
  },
  methods: {
    submit() {
      
    },
    addIngredient() {
      this.ingredients_number++;
      this.form.ingredients.push({
        name: "",
        quantity: "",
        measure: ""
      });
    },
    removeIngredient() {
      if (this.ingredients_number > 1) {
        this.ingredients_number--;
        this.form.ingredients.pop();
      }
    },

    async crearPlato() {
  let plato = '';
  // Construir el objeto JSON a partir de los datos del formulario
  plato = {
    nombre: this.form.name,
    fecha: this.form.date,
    foto_perfil: this.form.image,
    ingredientes: this.form.ingredients.map(item => {
      return {
        nombre: item.name,
        cantidad: item.quantity,
        tipo_peso: item.measure
      };
    })
  };

  try {
    if (this.isUpdating) {
      // Realizar una petición para eliminar el plato y sus ingredientes existentes
      await axios.delete(`api/deleteplato/${this.$route.params.id}/`);
      
    }

    // Enviar los datos al servidor para crear el plato
    const response = await axios.post('api/user/crear-receta/', plato);
    
    this.$router.push('/misplatos');
  } catch (error) {
    // Manejar el error
    console.error(error);
  }
}

  },
  components: { Navbar }
}


</script>