<template>
    <Navbar @user-data="handleUserData"></Navbar>
    <div class="min-h-full flex flex-col pt-8 py-12 px-6 lg:px-8 bg-green-500  ">
        <div v-show="mostrarForm">
            <div class="sm:mx-auto sm:w-full sm:max-w-md">

                <h1 class="text-3xl font-extrabold text-green-900 xl:inline">Generar lista de ingredientes</h1>
                <p class="mt-2 text-center text-sm text-gray-600">
                </p>
                <div class="mt-2 sm:mx-auto sm:w-full sm:max-w-md">
                    <div class="bg-white py-8 shadow rounded-lg px-6">
                        <form class="space-y-6" @submit.prevent="submit">
                            <div>

                                <div class="mt-1 flex items-center gap-2 justify-center ">
                                    <label for="date1" class="block text-sm font-medium text-green-600">Desde:</label>
                                    <input v-model="form.date1" id="date1" name="date1" type="date" autocomplete="form.date"
                                        required
                                        class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
                                    <label for="date2" class="block text-sm font-medium text-green-600">Hasta:</label>
                                    <input v-model="form.date2" id="date2" name="date2" type="date" autocomplete="form.date"
                                        required
                                        class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
                                </div>
                            </div>




                            <div class="flex items-center gap-2">
                                <label for="quantity" class="w-4/5 text-sm font-medium text-green-600">Cantidad de
                                    comensales
                                    (aproximada):</label>
                                <input v-model="form.quantity" id="quantity" name="quantity" type="number" min="1" step="1"
                                    autocomplete="quantity" required
                                    class="w-1/5 appearance-none block px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
                            </div>


                            <div>
                                <button @click="generarLista"
                                    class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
                                    Generar</button>
                            </div>



                        </form>


                    </div>
                </div>
            </div>
        </div>


        <div v-show="mostrarLista">
            <div class="md:pl-64 bg-green-500 min-h-screen">
                <div class="max-w-4xl mx-auto flex flex-col md:px-8 xl:px-0 justify-center">
                    <main class="flex-1">
                        <div class="relative max-w-4xl mx-auto md:px-8 xl:px-0">
                            <div class="pt-10 pb-16">
                                <div class="px-4 sm:px-6 md:px-0">
                                    <h1 class="text-3xl font-extrabold text-green-900 xl:inline">Lista de ingredientes</h1>
                                </div>
                                <div class="px-4 sm:px-6 md:px-0 ">
                                    <div class="p-3 mt-5 border-2 border-green-800 rounded">




                                        <div class="mt-10  divide-gray-200">

                                            <div class="mt-6">
                                                <dl class="divide-gray-200">


                                                    <div class="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4">
                                                        <dt class="text-sm font-extrabold text-green-900 xl:inline">Nombre y
                                                            apellido</dt>
                                                        <dd class="mt-1 flex text-sm text-white sm:mt-0 sm:col-span-2">

                                                            <span class="flex-grow text-white font-bold">{{ userData.name }}
                                                                {{
                                                                    userData.lastname }}</span>

                                                        </dd>
                                                        <dt class="text-sm font-extrabold text-green-900 xl:inline">Email
                                                        </dt>
                                                        <dd class="mt-1 flex text-sm text-white sm:mt-0 sm:col-span-2">

                                                            <span class="flex-grow text-white font-bold">{{ userData.email
                                                            }}</span>

                                                        </dd>
                                                        <dt class="text-sm font-extrabold text-green-900 xl:inline">Foto de
                                                            perfil</dt>
                                                        <dd class="mt-1 flex text-sm text-white sm:mt-0 sm:col-span-2">
                                                            <span class="flex-grow">
                                                                <img class="h-8 w-8 rounded-full" :src="userData.imageUrl"
                                                                    alt="Imagen de perfil del usuario" />
                                                            </span>

                                                        </dd>
                                                        <dt class="text-sm font-extrabold text-green-900 xl:inline">Fechas
                                                            de la lista de ingredientes </dt>
                                                        <dd class="mt-1 flex text-sm text-white sm:mt-0 sm:col-span-2">

                                                            <span class="flex-grow text-white font-bold">{{ date1Formateada
                                                            }} hasta
                                                                {{
                                                                    date2Formateada }}</span>

                                                        </dd>
                                                    </div>
                                                    

                                                    <div  v-for="ingrediente in respuesta.ingredientes"
                                                        class="flex justify-center p-1 mt-5">
                                                        <div class="w-64 text-sm font-extrabold text-green-900 xl:inline ">
                                                            <p>- {{ ingrediente.nombre }}</p>
                                                        </div>
                                                        <div class="w-32 text-sm font-extrabold text-green-900 xl:inline">
                                                            <p>({{ ingrediente.cantidad }} {{ ingrediente.tipo_peso }})</p>
                                                        </div>
                                                    </div>
                                                    <div class="flex justify-center mt-5">
                                                        <button @click="generarPDF"
                                                    class="w-50 flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-800 hover:bg-green-900 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
                                                    Generar pdf
                                                    </button>
                                                    </div>
                                                    






                                                </dl>
                                            </div>


                                        </div>


                                    </div>
                                </div>
                            </div>
                        </div>
                    </main>
                </div>
            </div>
        </div>

    </div>


    <Footer></Footer>
</template>





<script>
import axios from 'axios';
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue'
import { jsPDF } from "jspdf";

export default {
    data() {
        return {
            isUpdating: false, // Variable para indicar si estás en el proceso de actualización
            respuesta: [],
            userData: {},
            parts: '',
            date1Formateada: '',
            date2Formateada: '',
            mostrarForm: true,
            mostrarLista: false,
            form: {
                date1: "",
                date2: "",
                quantity: "",
            },
        };
    },
    setup() {
        return {
            
        }
    },
    components: {
        Navbar,
        Footer,
    },
    methods: {
        // Generar la lista de ingredientes
        async generarLista() {
            if (this.form.date2 > this.form.date1) {
                let datos = '';
                // Construir el objeto JSON a partir de los datos del formulario
                datos = {
                    fecha1: this.form.date1,
                    fecha2: this.form.date2,
                    cantidad: this.form.quantity,
                };
                this.parts = this.form.date1.split('-');
                this.date1Formateada = `${this.parts[2]}/${this.parts[1]}/${this.parts[0]}`; // Cambia el formato de la fecha aquí
                this.parts = this.form.date2.split('-');
                this.date2Formateada = `${this.parts[2]}/${this.parts[1]}/${this.parts[0]}`; // Cambia el formato de la fecha aquí

                try {
                    const response = await axios.post(`api/listaingredientes/`, datos);
                    this.respuesta = response.data;
                    this.mostrarForm = false;
                    this.mostrarLista = true;
                } catch (error) {
                    console.error(error);
                }
            } else {
                // Código para el caso de fechas inválidas
            }
        },
        // Manejar los datos del usuario
        handleUserData(userData) {
            if (this.userData !== null) {
                this.userData = userData;
            }
        },
        // Generar el PDF de la lista de ingredientes
        generarPDF() {
            const doc = new jsPDF();
            // Define las coordenadas iniciales para el contenido
            let x = 10;
            let y = 70;
            // Obtiene el ancho del PDF
            const pdfWidth = doc.internal.pageSize.getWidth();
            // Calcula la posición horizontal para centrar el título
            const titleX = (pdfWidth - doc.getStringUnitWidth('Lista de ingredientes') * 18 * 0.352) / 2; // 0.352 = factor de conversión de unidades
            doc.text('Lista de ingredientes', titleX, 10);    
            doc.text('- Usuario: ', 10, 30);
            doc.text(this.userData.name, 35, 30);
            doc.text(this.userData.lastname, 70, 30);
            doc.text('- Email: ', 10, 40);
            doc.text(this.userData.email, 35, 40);   
            doc.text('- Ingredientes necesarios desde:', 10, 50);
            doc.text(this.date1Formateada, 95, 50);
            doc.text('hasta ', 125, 50);
            doc.text(this.date2Formateada, 145, 50);     
            // Itera sobre la lista de ingredientes y agrega cada uno al PDF
            this.respuesta.ingredientes.forEach((ingrediente) => {
                const texto = `- ${ingrediente.nombre}: ${ingrediente.cantidad} ${ingrediente.tipo_peso}`;
                // Agrega el texto al documento en las coordenadas actuales
                doc.text(texto, x, y);
                // Incrementa la coordenada Y para pasar a la siguiente línea
                y += 10;
            });
            // Guarda el PDF
            doc.save('lista_ingredientes.pdf');
        },
    }
}
</script>
