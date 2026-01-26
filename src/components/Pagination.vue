<script setup lang="ts">
import { computed } from 'vue';

interface Props {
  currentPage: number;
  totalPages: number;
  basePath: string;
}

const props = defineProps<Props>();

const pages = computed(() => {
  const result: (number | string)[] = [];
  const total = props.totalPages;
  const current = props.currentPage;

  if (total <= 7) {
    for (let i = 1; i <= total; i++) {
      result.push(i);
    }
  } else {
    result.push(1);

    if (current > 3) {
      result.push('...');
    }

    const start = Math.max(2, current - 1);
    const end = Math.min(total - 1, current + 1);

    for (let i = start; i <= end; i++) {
      result.push(i);
    }

    if (current < total - 2) {
      result.push('...');
    }

    result.push(total);
  }

  return result;
});

function getPageUrl(page: number): string {
  if (page === 1) {
    return props.basePath;
  }
  return `${props.basePath}/${page}`;
}
</script>

<template>
  <nav class="pager-container col-span-2 m-4 mx-auto text-black md:col-span-4" aria-label="Pagination">
    <a
      v-if="currentPage > 1"
      :href="getPageUrl(currentPage - 1)"
      class="pager-container__link px-2.5 py-1 hover:text-sky-300"
      aria-label="Previous page"
    >
      &laquo;
    </a>

    <template v-for="page in pages" :key="page">
      <span v-if="page === '...'" class="px-2.5 py-1">...</span>
      <a
        v-else-if="page !== currentPage"
        :href="getPageUrl(page as number)"
        class="pager-container__link px-2.5 py-1 hover:text-sky-300"
      >
        {{ page }}
      </a>
      <span
        v-else
        class="pager-container__link px-2.5 py-1 bg-blue text-white rounded-full"
        aria-current="page"
      >
        {{ page }}
      </span>
    </template>

    <a
      v-if="currentPage < totalPages"
      :href="getPageUrl(currentPage + 1)"
      class="pager-container__link px-2.5 py-1 hover:text-sky-300"
      aria-label="Next page"
    >
      &raquo;
    </a>
  </nav>
</template>
