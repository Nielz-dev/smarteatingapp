<template>
  <Navbar></Navbar>
  <div class="relative bg-green-500 overflow-hidden min-h-screen">
    <div class="hidden sm:block sm:absolute sm:inset-y-0 sm:h-full sm:w-full" aria-hidden="true">
      <div class="relative h-full max-w-7xl mx-auto">

      </div>
    </div>

    <div class="relative pt-6 pb-16 sm:pb-24">

      <div class="max-w-7xl mx-auto px-4 sm:px-6">
        <nav class="relative flex items-center justify-between sm:h-10 md:justify-center" aria-label="Global">
          <div class="flex items-center flex-1 md:absolute md:inset-y-0 md:left-0">
            <div class="flex items-center justify-between w-full md:w-auto">


            </div>
          </div>

        </nav>
      </div>

      <main class="mt-16 mx-auto max-w-7xl px-4 sm:mt-24">
        <div class="text-center">
          <h1 class="text-4xl tracking-tight font-extrabold text-white sm:text-5xl md:text-6xl">
            <span class="block xl:inline">Bienvenido a SmartEating App</span>
            {{ ' ' }}
            <span class="block text-green-900 xl:inline">la aplicación para organizar tu cocina</span>
          </h1>

          <div class="mt-5 max-w-md mx-auto sm:flex sm:justify-center md:mt-8">
            <div class="rounded-md shadow">
              <a href="#"
                class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-green-900 hover:bg-green-700 md:py-4 md:text-lg md:px-10">
                Get started </a>
            </div>

          </div>
          <div class="mt-5 max-w-4xl mx-auto sm:flex sm:justify-center md:mt-8">
            <div class=" shadow">
              <img src="../static/img/portada.jpg" alt="Imagen de la página principal" class="rounded-lg">
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
  <Footer></Footer>
</template>

<script>

import Navbar from './Navbar.vue';
import Footer from './Footer.vue';


export default {
  components: {
    Navbar,
    Footer,
  },
  setup() {
    return {

    }
  },
}
</script>