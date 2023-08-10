<template>
  <a
    :href="item.url"
    class="block text-white hover:bg-white/70 bg-purple/5 border border-purple/20 rounded group"
  >
    <img :src="item.svg" :alt="item.name" class="lg:w-40 w-40 md:w-28 lg:h-40 h-40 md:h-28 mx-auto mt-12 md:mt-6 lg:mt-12 mb-8 md:mb-4 lg:mb-8 " />
    <span class="flex flex-row justify-center mb-12 md:mb-6 lg:mb-12">
      <span
        class="bg-blue flex flex-row justify-center font-ibm items-center w-auto rounded-md px-4 py-2.5 border border-blue leading-tight group-hover:bg-purple group-hover:border-purple"
      >
        <component class="bg-white/20 rounded-full text-white mr-2.5" :is="item.icon" />
        {{ item.name }}
      </span>
    </span>
  </a>
</template>

<script>
export default {
  name: 'HeroCard',
  props: {
    item: Object
  }
}
</script>
