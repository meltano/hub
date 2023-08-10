<script setup>
import HeroCard from './HeroCard.vue'
</script>

<template>
  <header>
    <div class="max-w-5xl w-full mx-auto pt-16 md:pt-16 lg:pt-32 px-4">
      <div
        class="flex flex-wrap-reverse md:flex-wrap items-center justify-center md:justify-between -mx-4"
      >
        <div class="w-full md:w-1/2 lg:w-2/5 xl:w-7/12 px-4 md:text-left text-center">
          <h1
            class="xl:text-7xl md:text-6xl text-5xl leading-tight font-pjs text-purple font-bold lg:max-w-lg"
          >
            The <span class="brackets brackets-pink">joy</span> of creating
          </h1>
          <p
            class="font-grotesk mt-6 max-w-sm leading-relaxed text-base lg:text-xl md:ml-0 mx-auto text-black/75"
          >
            Everything you need and more to move, transform, and explore your data
          </p>
        </div>

        <div class="w-10/12 md:w-1/2 lg:w-2/5 xl:5/12 px-4 mb-8 md:mb-0">
          <img src="@/assets/images/hero-image.svg" alt="hero image" class="hero-image w-full" />
        </div>
      </div>

      <div
        class="flex flex-wrap items-center justify-center mt-12 md:mt-16 lg:mt-20 -mx-3"
      >
        <div
          v-for="item in items"
          :key="item.name"
          class="w-full max-w-sm md:w-1/3 px-3 lg:my-0 my-4"
        >
          <HeroCard :item="item" />
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import IconArrowFrom from '../icons/IconArrowFrom.vue'
import IconArrowTo from '../icons/IconArrowTo.vue'
import IconWrench from '../icons/IconWrench.vue'

import cyl from '@/assets/images/cyl.svg'
import cube from '@/assets/images/cube.svg'
import cone from '@/assets/images/cone.svg'

const items = [
  { name: 'Browse Extractors', url: '/extractors', icon: IconArrowFrom, svg: cyl },
  { name: 'Browse Loaders', url: '/loaders', icon: IconArrowTo, svg: cube },
  { name: 'Browse Tools', url: '/utilities', icon: IconWrench, svg: cone }
]
export default {
  metaInfo: {
    title: 'Home'
  },
  name: 'HomePage',
  data() {
    return {
      items
    }
  }
}
</script>
