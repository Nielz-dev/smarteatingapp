<template>
  <div class="bg-green-500 min-h-screen ">
    <Navbar />
    <div class="px-4 sm:px-6 lg:px-8 mt-12">

      <div class="px-4 sm:px-6 lg:px-8">
        <div class="sm:flex sm:items-center">
          <div class="sm:flex-auto">
            <h1 class="text-3xl font-extrabold text-green-900">Eventos</h1>
            <p class="mt-2 text-sm font-semibold text-green-900">En esta tabla podrás filtrar por año para ver todos los
              platos
              disponibles agrupados por meses.</p>
          </div>
          <div class="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
            <router-link :to="`/addEvento`">
              <button type="button"
                class="flex items-center justify-center mb-5 rounded-md border border-transparent bg-green-800 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2 sm:w-auto">Añadir
                evento
              </button>
            </router-link>

            <select v-model="selectedYear" @change="fetchPlatosPorMes" id="mobile-currency" name="currency"
              class="bg-none border-transparent rounded-md py-0.5 pl-2 pr-5 flex items-center text-sm font-medium text-gray-700 group-hover:text-gray-800 focus:outline-none focus:ring-0 focus:border-transparent">
              <option v-for="y in this.fechas" :key="y" :value="y.year">{{ y.year }}</option>
            </select>
          </div>
        </div>
        <div class="mt-8 flex flex-col">
          <div class="-my-2 -mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
              <div class="overflow-hidden shadow ring-1 ring-black ring-opacity-5 md:rounded-lg">
                <table class="min-w-full">
                  <thead class="bg-green-900">
                    <tr>
                      <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-white sm:pl-6">Nombre
                        del plato
                      </th>
                      <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-white">Fecha</th>
                      <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-white">Foto</th>
                      <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-white">ID</th>
                      <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-6">
                        <span class="sr-only">Edit</span>
                      </th>
                    </tr>
                  </thead>
                  <tbody class="bg-green-100">
                    <template v-for="(item, index) in platosPorMes">
                      <tr class="border-t border-green-200">
                        <th colspan="5" scope="colgroup"
                          class="bg-green-900 px-4 py-2 text-left text-sm font-semibold text-white sm:px-6">{{ item.month
                          }}</th>
                      </tr>
                      <tr v-for="(plato, platoIndex) in item.platos" :key="platoIndex"
                        :class="[platoIndex === 0 ? 'border-gray-300' : 'border-gray-200', 'border-t']">
                        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm  font-semibold text-green-600 sm:pl-6">{{
                          plato.nombre }}</td>
                        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm  font-semibold text-green-600 sm:pl-6">{{
                          plato.fecha }}</td>
                        <div class="flex-shrink-0 pt-2">
                          <img class="h-8 pt-2 w-8 rounded-full" :src="plato.foto_perfil" alt="Imagen del plato" />
                        </div>
                        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm  font-semibold text-green-600 sm:pl-6">{{
                          plato.id
                        }}</td>

                        <td class="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6">
                          <div class="flex flex-row gap-1 items-center justify-end">
                            <router-link :to="`/misplatos/${plato.id}/update`">

                              <button class="p-1 mr-2 text-white bg-green-600  rounded-xl shadow-lg">Editar</button>

                            </router-link>
                            <div @click="addModal"
                              class="cursor-pointer flex justify-center py-1 px-1 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-red-600  focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
                              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-5 h-5">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                  d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                              </svg>
                            </div>


                          </div>
                          <!-- Modal -->
                          <TransitionRoot as="template" :show="open">
                            <Dialog as="div" class="fixed z-10 inset-0 overflow-y-auto" @close="open = false">
                              <div
                                class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
                                <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0"
                                  enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100"
                                  leave-to="opacity-0">
                                  <DialogOverlay class="fixed inset-0 bg-green-700 bg-opacity-75 transition-opacity" />
                                </TransitionChild>


                                <span class="hidden sm:inline-block sm:align-middle sm:h-screen"
                                  aria-hidden="true">&#8203;</span>
                                <TransitionChild as="template" enter="ease-out duration-300"
                                  enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                                  enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
                                  leave-from="opacity-100 translate-y-0 sm:scale-100"
                                  leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
                                  <div
                                    class="relative inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
                                    <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                                      <div class="sm:flex sm:items-start">
                                        <div
                                          class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                                          <ExclamationIcon class="h-6 w-6 text-red-600" aria-hidden="true" />
                                        </div>
                                        <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                                          <DialogTitle as="h3" class="text-lg leading-6 font-medium text-gray-900">
                                            Eliminando plato </DialogTitle>
                                          <div class="mt-2">
                                            <p class="text-sm text-gray-500">Está seguro de eliminar el plato?</p>
                                          </div>
                                        </div>
                                      </div>
                                    </div>
                                    <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                                      <button type="button"
                                        class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-red-600 text-base font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:ml-3 sm:w-auto sm:text-sm"
                                        @click="deleteModal(plato.id)">Eliminar</button>
                                      <button type="button"
                                        class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm"
                                        @click="open = false" ref="cancelButtonRef">Cancelar</button>
                                    </div>
                                  </div>
                                </TransitionChild>
                              </div>
                            </Dialog>
                          </TransitionRoot>





                        </td>
                      </tr>
                    </template>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
  <Footer></Footer>
</template>

<script>
import { months } from '../../data/test';
import Navbar from '../components/Navbar.vue'
import Footer from '../components/Footer.vue'
import axios from 'axios';
import { ref } from 'vue'
import { Dialog, DialogOverlay, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { ExclamationIcon } from '@heroicons/vue/outline'

export default {
  data() {
    return {
      x: months,
      selectedYear: 2023,
      fechas: [],
      platosPorMes: {}, // Objeto con los platos por mes
    }
  },
  async mounted() {
    try {
      // Obtener las fechas desde el backend
      const response1 = await axios.get('api/dates/');
      this.fechas = response1.data;

      // Obtener los platos por mes para el año seleccionado desde el backend
      const response2 = await axios.get(`api/platos/${this.selectedYear}/`);
      this.platosPorMes = response2.data;

    } catch (error) {
      console.log(error);
    }
  },
  methods: {
    // Obtener los platos por mes para el año seleccionado desde el backend
    async fetchPlatosPorMes() {
      try {
        const response = await axios.get(`api/platos/${this.selectedYear}/`);
        this.platosPorMes = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    // Abrir el modal
    addModal() {
      this.open = true;
    },
    // Eliminar un plato mediante el ID
    async deleteModal(platoID) {
      this.open = false;
      try {
        // Realizar la petición de eliminación del plato al backend
        const response = await axios.delete(`api/deleteplato/${platoID}/`);
        this.platosPorMes = response.data;
      } catch (error) {
        console.error(error);
      }

      try {
        // Actualizar los platos por mes después de eliminar el plato
        this.fetchPlatosPorMes();
      } catch (error) {
        console.error(error);
      }
    },
  },
  components: {
    Navbar,
    Footer,
    Dialog,
    DialogOverlay,
    DialogTitle,
    TransitionChild,
    TransitionRoot,
    ExclamationIcon,
  },
  setup() {
    // Estado para controlar la apertura/cierre del modal
    const open = ref(false);
    return {
      open,
    }
  },
}
</script>


