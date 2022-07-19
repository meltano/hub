<template>
  <div @click="toggle" v-on-clickaway="away" class="relative">
    <slot name="toggler">
      <button>Toggle</button>
    </slot>
    <slot />
  </div>
</template>

<script>
import { mixin as clickaway } from "vue-clickaway";

export default {
  name: "SearchDropdown",
  mixins: [clickaway],
  provide() {
    return {
      sharedState: this.sharedState,
    };
  },
  data() {
    return {
      sharedState: {
        active: false,
      },
    };
  },
  methods: {
    toggle() {
      this.sharedState.active = !this.sharedState.active;
    },
    away() {
      this.sharedState.active = false;
    },
  },
};
</script>

<style></style>
