<template>
  <transition name="dropdown-content">
    <div
      v-if="active"
      class="origin-top-right absolute right-0 mt-2 w-48 bg-white rounded-lg border py-2"
    >
      <slot />
    </div>
  </transition>
</template>

<script>
export default {
  name: "DropdownContent",
  inject: ["sharedState"],
  computed: {
    active() {
      return this.sharedState.active;
    },
  },
};
</script>

<style>
.dropdown-content-enter-active,
.dropdown-content-leave-active {
  transition: all 0.2s;
}
.dropdown-content-enter,
.dropdown-content-leave-to {
  opacity: 0;
  transform: translateY(-5px);
}
</style>
