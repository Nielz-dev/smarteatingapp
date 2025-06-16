<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  
  <Disclosure as="nav" class="bg-green-500 " v-slot="{ open }">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 ">
      <div class="flex justify-between h-16">
        <div class="flex">
          <div class="-ml-2 mr-2 flex items-center md:hidden">
            <!-- Mobile menu button -->
            <DisclosureButton
              class="inline-flex items-center justify-center p-2 rounded-md text-white hover:text-white hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white">
              <span class="sr-only">Open main menu</span>
              <MenuIcon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
              <XIcon v-else class="block h-6 w-6" aria-hidden="true" />
            </DisclosureButton>
          </div>
          <div class="flex-shrink-0 flex items-center">
            <img class="block lg:hidden h-8 w-auto rounded-md" src="../static/img/2.png" alt="Logo de SmartEating" />
            <img class="hidden lg:block h-8 w-auto rounded-md" src="../static/img/2.png" alt="Logo de SmartEating" />
          </div>
          <div class="hidden md:ml-6 md:flex md:items-center md:space-x-4">
            <a v-for="item in navigation" :key="item.name" :href="item.href"
              :class="[item.current ? 'bg-green-900 text-white' : 'text-white hover:bg-green-700 hover:text-white', 'px-3 py-2 rounded-md text-md font-medium']"
              :aria-current="item.current ? 'page' : undefined">{{ item.name }}</a>
          </div>
        </div>
        <div class="flex items-center">
          <div class="hidden md:ml-4 md:flex-shrink-0 md:flex md:items-center">

            <!-- Profile dropdown -->
            <Menu as="div" class="ml-3 relative">
              <div>
                <MenuButton
                  class="bg-green-800 flex text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white">
                  <span class="sr-only">Open user menu</span>
                  <div v-if="isAuthenticated">
                    <img class="h-8 w-8 rounded-full" :src="user.imageUrl" alt="Imágen de perfil de usuario" />
                  </div>
                  <div v-else>
                    <img class="h-8 w-8 rounded-full" src="../static/img/logo.jpeg" alt="Imágen de perfil de usuario" />
                  </div>
                </MenuButton>
              </div>
              <transition enter-active-class="transition ease-out duration-200"
                enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100"
                leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100"
                leave-to-class="transform opacity-0 scale-95">
                <MenuItems
                  class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5 focus:outline-none"
                  style="z-index: 9999;">
                  <div v-if="isAuthenticated">
                    <MenuItem v-for="item in userNavigationLogged" :key="item.name" v-slot="{ active }">
                      <a :href="item.href" :class="[active ? 'bg-green-100' : '', 'block px-4 py-2 text-md font-medium text-green-500']" @click="item.onClick">{{ item.name }}</a>
                    </MenuItem>
                  </div>
                  <div v-else>
                    <MenuItem v-for="item in userNavigation" :key="item.name" v-slot="{ active }">
                      <a :href="item.href" :class="[active ? 'bg-green-100' : '', 'block px-4 py-2 text-md font-medium text-green-500']" @click="item.onClick">{{ item.name }}</a>
                    </MenuItem>
                  </div>
                  
                </MenuItems>
              </transition>
            </Menu>

          </div>
        </div>
      </div>
    </div>

    <DisclosurePanel class="md:hidden">
      <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
        <DisclosureButton v-for="item in navigation" :key="item.name" as="a" :href="item.href"
          :class="[item.current ? 'bg-green-900 text-white' : 'text-white hover:bg-green-700 hover:text-white', 'block px-3 py-2 rounded-md text-base font-medium']"
          :aria-current="item.current ? 'page' : undefined">{{ item.name }}</DisclosureButton>
      </div>
      <div class="pt-4 pb-3 border-t border-gray-700">
        <div class="flex items-center px-5 sm:px-6">

                  <div v-if="isAuthenticated">
                    <div class="flex-shrink-0">
                      <img class="h-10 w-10 rounded-full" :src="user.imageUrl" alt="" />
                    </div>
                    <div class="ml-3">
                      <div class="text-base font-medium text-white">{{ user.name }}</div>
                      <div class="text-sm font-medium text-white">{{ user.email }}</div>
                    </div>
                  </div>

                  <div v-else>
                    <div class="flex-shrink-0">
                      <img class="h-10 w-10 rounded-full" src='../static/img/logo.jpeg' alt="Logo de SmartEating" />
                    </div>
                    <div class="ml-3">
                      <div class="text-base font-medium text-white">{{ userUnlogged.name }}</div>
                      
                    </div>
                  </div>
          
          

        </div>
        <div class="mt-3 px-2 space-y-1 sm:px-3">
          <div v-if="isAuthenticated">
            <DisclosureButton v-for="item in userNavigationLogged" :key="item.name" as="a" :href="item.href" @click="item.onClick"
            class="block px-3 py-2 rounded-md text-base font-medium text-white hover:text-white hover:bg-green-700">{{
              item.name }}</DisclosureButton>
                  </div>
                  <div v-else>
                    <DisclosureButton v-for="item in userNavigation" :key="item.name" as="a" :href="item.href" @click="item.onClick"
            class="block px-3 py-2 rounded-md text-base font-medium text-white hover:text-white hover:bg-green-700">{{
              item.name }}</DisclosureButton>
                  </div>
          
        </div>
      </div>
    </DisclosurePanel>
  </Disclosure>
</template>
  
<script>
import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import { BellIcon, MenuIcon, XIcon } from '@heroicons/vue/outline'
import { PlusSmIcon } from '@heroicons/vue/solid'
import { mapState } from 'vuex';
import axios from 'axios';

export default {
  data() {
    return {
      // Elementos de navegación para usuarios no autenticados
      userNavigation: [
        { name: 'Inicio', href: '/', },
        { name: 'Perfil', href: '/login', },
        { name: 'Iniciar sesión', onClick: this.goLogin },
        // Otros elementos de navegación del usuario con funciones onClick personalizadas
      ],
      // Elementos de navegación para usuarios autenticados
      userNavigationLogged: [
        { name: 'Inicio', href: '/', },
        { name: 'Perfil', href: '/userdetail', },
        { name: 'Cerrar sesión', onClick: this.logout },
        // Otros elementos de navegación del usuario con funciones onClick personalizadas
      ],
      // Información del usuario autenticado
      user: {
        name: '',
        lastname: '',
        email: '',
        imageUrl: '../static/img/2.png',
        pk: '',
      },
      // Información del usuario no autenticado
      userUnlogged: {
        name: 'Inicie sesión por favor',
        imageUrl: '../static/img/2.png',
      },
      // Elementos de navegación general
      navigation: [
        { name: 'Inicio', href: '/', current: true },
        { name: 'Mis platos', href: '/misplatos', current: false },
        { name: 'Eventos', href: '/eventos', current: false },
        { name: 'Generar lista', href: '/generarlista', },
      ],
    };
  },
  components: {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
    Menu,
    MenuButton,
    MenuItem,
    MenuItems,
    BellIcon,
    MenuIcon,
    PlusSmIcon,
    XIcon,
  },
  methods: {
    // Función para cerrar sesión
    logout() {
      axios.post('api/token/logout/')
        .then(response => {
          // Eliminar el token del almacenamiento local (localStorage)
          localStorage.removeItem("token");
          
        })
        .catch(error => {
          // Manejar el error en caso de que ocurra
          console.log(error);
        });
      // Redirigir al usuario a la página de inicio de sesión
      this.$router.push('/login');
    },
    // Función para redirigir al usuario a la página de inicio de sesión
    goLogin() {
      this.$router.push('/login');
    },
    // Función para obtener los datos del usuario autenticado desde la API
    async fetchUserData() {
      await axios.get('api/user/')
        .then(response => {
          // Asignar los datos del usuario a las propiedades correspondientes
          this.user.email = response.data.email;
          this.user.name = response.data.first_name;
          this.user.lastname = response.data.last_name;
          this.user.imageUrl = response.data.url;
          this.user.pk = response.data.pk;
          // Emitir el evento "user-data" con los datos del usuario
          this.$emit('user-data', this.user);
        })
        .catch(error => {
          // Manejar el error en caso de que ocurra
          console.log(error);
        });
    },
  },
  mounted() {
    // Obtener los datos del usuario si está autenticado
    if (this.isAuthenticated) {
      this.fetchUserData();
    }
  },
  computed: {
    ...mapState({
      token: state => state.token,
      isAuthenticated: state => state.isAuthenticated,
    }),
  },
};
</script>




