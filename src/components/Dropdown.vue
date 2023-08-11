<template>
  <div
    @mouseleave="() => (isOpen = false)"
    class="relative md:w-auto w-full md:py-3 rounded-md px-4 md:px-1.5 md:px-4 w-full backdrop-blur-md md:backdrop-blur-none bg-purple/5 md:bg-transparent md:w-auto md:border-transparent py-3 md:py-3 border md:border-2 border-black/15 md:border-transparent text-[15px] font-ibm rounded"
  >
    <button
      @mouseenter="handleHover"
      class="whitespace-nowrap text-left md:text-center block w-full"
    >
      {{ item }}
    </button>
    <div
      v-show="isOpen"
      :class="[
        alignment === 'left' ? 'left' : '',
        alignment === 'center' ? 'left-1/2 -ml-2' : '',
        alignment === 'right' ? 'right' : '',
        'hidden md:block md:absolute w-3 left-1/2 -ml-2 h-3 top-12 translate-y-1 bg-black border-t border-l border-black transform origin-center rotate-45 '
      ]"
    ></div>
    <div
      v-show="isOpen"
      :class="[
        alignment === 'left' ? 'left-0' : '',
        alignment === 'center' ? 'left-1/2 -ml-2' : '',
        alignment === 'right' ? 'right-0' : '',
        'hidden md:block md:absolute w-full -ml-2 h-10 top-12  transform origin-center '
      ]"
    ></div>
    <ul
      v-show="isOpen"
      :class="[
        alignment === 'left' ? 'left-0' : '',
        alignment === 'center' ? 'left-1/2 -mx-28' : '',
        alignment === 'right' ? 'right-0' : '',
        ,
        'md:absolute w-56 top-14 md:bg-black md:border md:border-black px-1 py-1.5 rounded-lg'
      ]"
    >
      <li v-for="(i, idx) in items" :key="`${item.replace(' ', '_')}-sub-${idx}`">
        <RouterLink
          :to="i.path"
          class="text-sm px-4 py-2.5 block text-black/80 md:text-white/80 hover:text-blue-light duration-200 font-ibm"
          >{{ i.name }}
        </RouterLink>
      </li>
    </ul>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router';

export default {
    name: "DropdownComponent",
    props: ["item", "items", "alignment"],
    data() {
        return {
            isOpen: false
        };
    },
    methods: {
        handleHover() {
            this.isOpen = !this.isOpen;
        }
    },
    components: { RouterLink }
}
</script>
