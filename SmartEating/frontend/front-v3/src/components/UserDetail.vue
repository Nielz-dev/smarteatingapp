
<template>
    <Navbar @user-data="handleUserData"></Navbar>
    <div>

        <div class="md:pl-64 bg-green-500 min-h-screen">
            <div class="max-w-4xl mx-auto flex flex-col md:px-8 xl:px-0">
                <main class="flex-1">
                    <div class="relative max-w-4xl mx-auto md:px-8 xl:px-0">
                        <div class="pt-10 pb-16">
                            <div class="px-4 sm:px-6 md:px-0">
                                <h1 class="text-3xl font-extrabold text-green-900 xl:inline">Detalles de la cuenta</h1>
                            </div>
                            <div class="px-4 sm:px-6 md:px-0 ">
                                <div class="p-6 mt-5 border-2 border-green-800 rounded">




                                    <div class="mt-10 divide-y divide-gray-200">
                                        <div class="space-y-1">
                                            <h3 class="text-lg leading-6 font-extrabold text-green-900 xl:inline">Perfil
                                            </h3>

                                        </div>
                                        <div class="mt-6">
                                            <dl class="divide-y divide-gray-200">


                                                <div class="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4">
                                                    <dt class="text-sm font-extrabold text-green-900 xl:inline">Email</dt>
                                                    <dd class="mt-1 flex text-sm text-white sm:mt-0 sm:col-span-2">

                                                        <span
                                                            class="flex-grow text-white font-bold">{{ userData.email }}</span>
                                                        <span class="ml-4 flex-shrink-0">
                                                            <button type="button" @click="addEmailInput"
                                                                class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-700 hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Modificar</button>
                                                        </span>
                                                    </dd>
                                                    <div class="flex mt-1" v-show="showEmailInput">
                                                        <form class="space-y-6">
                                                            <div>
                                                                <label for="new_email"
                                                                    class="block text-sm font-extrabold text-green-900 xl:inline"> Escribe
                                                                    el nuevo correo electrónico</label>
                                                                <div class="mt-1">
                                                                    <input v-model="new_email" id="new_email"
                                                                        name="new_email" type="email"
                                                                        placeholder="Escribe el nuevo email"
                                                                        autocomplete="email" required
                                                                        class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
                                                                </div>
                                                            </div>



                                                            <div>
                                                                <label for="re_new_email"
                                                                    class="block text-sm font-extrabold text-green-900 xl:inline"> Repite
                                                                    el nuevo correo electrónico </label>
                                                                <div class="mt-1">
                                                                    <input v-model="re_new_email" id="re_new_email"
                                                                        name="re_new_email" type="email"
                                                                        placeholder="Repite el correo electrónico"
                                                                        autocomplete="email" required
                                                                        class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
                                                                </div>
                                                            </div>

                                                            <div>
                                                                <label for="current_password"
                                                                    class="block text-sm font-extrabold text-green-900 xl:inline">
                                                                    Contraseña </label>
                                                                <div class="mt-1">
                                                                    
                                                                    <input v-model="current_password" id="current_password"
                                                                        name="current_password" type="password"
                                                                        placeholder="Contraseña" required
                                                                        class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
                                                                </div>
                                                            </div>



                                                            <div>
                                                                <button @click="updateEmail" type="submit"
                                                                    class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-700 hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Modificar
                                                                    email</button>
                                                            </div>
                                                        </form>

                                                    </div>
                                                </div>


                                                <div class="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4">
                                                    <dt class="text-sm font-extrabold text-green-900 xl:inline">Nombre</dt>
                                                    <dd class="mt-1 flex text-sm text-white sm:mt-0 sm:col-span-2">
                                                        <span class="flex-grow text-white font-bold">{{ userData.name }}</span>
                                                        
                                                        <span class="ml-4 flex-shrink-0">
                                                            <button type="button" @click="addUserInput"
                                                                class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-700 hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Modificar</button>
                                                        </span>
                                                    </dd>
                                                    <div class="flex mt-1" v-show="showNameInput">
                                                        <form class="space-y-6">
                                                            <div>
                                                                <label for="first_name"
                                                                    class="block text-sm font-bold text-green-900 xl:inline"> Escribe el nuevo nombre</label>
                                                                <div class="mt-1">
                                                                    <input v-model="first_name" id="first_name"
                                                                        name="first_name" type="text"
                                                                        placeholder="Escribe el nuevo nombre"
                                                                         required
                                                                        class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
                                                                </div>
                                                            </div>

                                                            <div>
                                                                <button @click="updateUser" type="submit"
                                                                    class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-700 hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Modificar
                                                                    nombre</button>
                                                            </div>
                                                        </form>

                                                    </div>
                                                </div>


                                                <div class="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4">
                                                    <dt class="text-sm font-extrabold text-green-900 xl:inline">Apellido
                                                    </dt>
                                                    <dd class="mt-1 flex text-sm text-white sm:mt-0 sm:col-span-2">
                                                        <span class="flex-grow text-white font-bold">{{ userData.lastname }}</span>
                                                        <span class="ml-4 flex-shrink-0">
                                                            <button type="button" @click="addLastNameInput"
                                                                class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-700 hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Modificar</button>
                                                        </span>
                                                    </dd>
                                                    <div class="flex mt-1" v-show="showLastNameInput">
                                                        <form class="space-y-6">
                                                            <div>
                                                                <label for="last_name"
                                                                    class="block text-sm font-bold text-green-900 xl:inline"> Escribe el nuevo apellido</label>
                                                                <div class="mt-1">
                                                                    <input v-model="last_name" id="last_name"
                                                                        name="last_name" type="text"
                                                                        placeholder="Apellido"
                                                                         required
                                                                        class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
                                                                </div>
                                                            </div>

                                                            <div>
                                                                <button @click="updateLastName" type="submit"
                                                                    class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-700 hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Modificar
                                                                    nombre</button>
                                                            </div>
                                                        </form>

                                                    </div>
                                                </div>


                                                <div class="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:pt-5">
                                                    <dt class="text-md font-extrabold text-green-900 xl:inline">Foto de
                                                        perfil</dt>
                                                    <dd class="mt-1 flex text-sm text-white sm:mt-0 sm:col-span-2">
                                                        <span class="flex-grow">
                                                            <img class="h-8 w-8 rounded-full"
                                                                :src="userData.imageUrl"
                                                                alt="Foto de perfil del usuario" />
                                                        </span>
                                                        <span class="ml-4 flex-shrink-0 flex items-start space-x-4">
                                                            <button type="button" @click="addUrlInput"
                                                                class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-700 hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Modificar</button>

                                                        </span>
                                                    </dd>
                                                    <div class="flex mt-1" v-show="showUrlInput">
                                                        <form class="space-y-6">
                                                            <div>
                                                                <label for="url"
                                                                    class="block text-sm font-bold text-green-900 xl:inline"> Url de tu foto de perfil</label>
                                                                <div class="mt-1">
                                                                    <input v-model="url" id="url"
                                                                        name="url" type="text"
                                                                        placeholder=""
                                                                         required
                                                                        class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm" />
                                                                </div>
                                                            </div>

                                                            <div>
                                                                <button @click="updateUrl" type="submit"
                                                                    class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-700 hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Modificar
                                                                    Url</button>
                                                            </div>
                                                        </form>

                                                    </div>
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
    <Footer></Footer>
</template>
  
<script>
import axios from 'axios';
import Navbar from './Navbar.vue';
import Footer from './Footer.vue'
import { useToast } from "vue-toastification";

export default {
    data() {
        return {
            new_email: '',
            re_new_email: '',
            current_password: '',
            first_name: '',
            last_name: '',
            url: '',
            showEmailInput: false,
            showNameInput: false,
            showLastNameInput: false,
            showUrlInput: false,
            userData: {},
        };
    },
    components: {
        Navbar,
        Footer,
    },
    setup() {
        const toast = useToast();
        return { toast };
    },
    methods: {
        // Mostrar campo de entrada de correo electrónico
        addEmailInput() {
            this.showEmailInput = true;
        },
        // Mostrar campo de entrada de nombre
        addUserInput() {
            this.showNameInput = true;
        },
        // Mostrar campo de entrada de apellido
        addLastNameInput() {
            this.showLastNameInput = true;
        },
        // Mostrar campo de entrada de URL
        addUrlInput() {
            this.showUrlInput = true;
        },
        // Actualizar el correo electrónico
        updateEmail() {
            const datosEmail = {
                new_email: this.new_email,
                re_new_email: this.re_new_email,
                current_password: this.current_password
            };
            axios.post('api/users/set_email/', datosEmail)
                .then(response => {
                    // Email cambiado con éxito
                    this.toast.success("Email cambiado con éxito.", {
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
                    // Código para el caso de respuesta con error
                    console.log(error);
                    if (error.response && error.response.status !== 200) {
                        // Aquí puedes manejar errores específicos en caso de respuesta con error
                    }
                });
            this.showEmailInput = false;
        },
        // Manejar los datos del usuario
        handleUserData(userData) {
            if (this.userData !== null) {
                this.userData = userData;
            }
        },
        // Actualizar el nombre de usuario
        updateUser() {
            axios.put(`api/user/update/${this.userData.pk}/`, { first_name: this.first_name })
                .then(response => {
                    // Nombre cambiado con éxito
                    this.toast.success("Nombre cambiado con éxito.", {
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
                    // Código para el caso de respuesta con error
                    console.log(error);
                    if (error.response && error.response.status !== 200) {
                        // Aquí puedes manejar errores específicos en caso de respuesta con error
                    }
                });
            this.showNameInput = false;
        },
        // Actualizar el apellido del usuario
        updateLastName() {
            axios.put(`api/user/update/${this.userData.pk}/`, { last_name: this.last_name })
                .then(response => {
                    // Apellido cambiado con éxito
                    this.toast.success("Apellido cambiado con éxito.", {
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
                    // Código para el caso de respuesta con error
                    console.log(error);
                    if (error.response && error.response.status !== 200) {
                        // Aquí puedes manejar errores específicos en caso de respuesta con error
                    }
                });
            this.showLastNameInput = false;
        },
        // Actualizar la URL del usuario
        updateUrl() {
            axios.put(`api/user/update/${this.userData.pk}/`, { url: this.url })
                .then(response => {
                    // URL cambiada con éxito
                    this.toast.success("URL cambiada con éxito.", {
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
                    // Código para el caso de respuesta con error
                    console.log(error);
                    if (error.response && error.response.status !== 200) {
                        // Aquí puedes manejar errores específicos en caso de respuesta con error
                    }
                });
        },
    },
};
</script>
