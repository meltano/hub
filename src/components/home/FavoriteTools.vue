<template>
  <div
    class="relative max-w-6xl pt-32 pb-20 mx-auto border rounded bg-purple/5 border-purple/15 backdrop-blur-md"
  >
    <div class="w-full max-w-4xl px-4 mx-auto">
      <div class="absolute w-48 -ml-24 left-1/2 -top-24">
        <img src="../../assets/images/island.svg" alt="Island" class="" />
      </div>
      <div class="text-center">
        <h2 class="mb-4 text-3xl font-bold text-black md:text-4xl lg:text-5xl">
          Do <span class="brackets brackets-blue">even more</span> with your data
        </h2>
        <p class="font-normal opacity-75 text-black/75 text-md font-grotesk">
          Meltano works with many of your favorite tools
        </p>
        <p class="mt-6 text-center">
          <!-- TODO: Add URL -->
          <a
            href="#"
            class="items-center inline-block w-auto py-3 leading-snug text-white border rounded-md bg-blue font-ibm px-7 border-blue hover:bg-purple hover:border-purple"
            >Browse All</a
          >
        </p>
      </div>
      <div
        class="grid max-w-lg grid-cols-2 gap-3 mx-auto my-10 md:grid-cols-3 lg:grid-cols-3 md:gap-4 md:max-w-full"
      >
        <div v-for="(item, index) in extractors" :key="index + 'item'">
          <a
            :href="item.url"
            class="block text-white border rounded group hover:bg-white/70 bg-purple/5 border-purple/20"
          >
            <div
              class="flex items-center w-20 h-20 mx-auto mt-10 mb-6 bg-white rounded-full lg:w-24 lg:h-24 md lg:mt-12 lg:mb-8"
            >
              <img :src="item.svg" :alt="item.name" class="w-10 h-10 mx-auto" />
            </div>
            <span
              class="flex flex-row items-center justify-center mb-10 lg:mb-12 font-ibm text-black/75 text-[15px] font-semibold"
            >
              {{ item.name }}
              <span
                class="hidden mt-px ml-2 text-xl leading-none duration-200 lg:block group-hover:translate-x-2"
                ><IconRightArrow
              /></span>
            </span>
          </a>
        </div>
      </div>

      <div class="flex flex-row justify-around -mx-1.5">
        <div class="px-1.5 py-2" v-for="(item, idx) in btns" :key="item.name + '-' + idx">
          <a
            :href="item.url"
            class="flex flex-col md:flex-row text-center md:text-left justify-center font-ibm text-blue items-center w-auto rounded-md px-4 py-2.5 border border-transparent leading-tight hover:underline"
          >
            <component class="mb-2 rounded-full md:mr-4 md:mb-0" :is="item.icon" />
            {{ item.name }}
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import IconRightArrow from "../icons/IconRightArrow.vue";
import IconPublish from "../gradient-icons/IconPublish.vue";
import IconBuild from "../gradient-icons/IconBuild.vue";
import IconExplore from "../gradient-icons/IconExplore.vue";

import bigquery from "../../assets/images/extractors/bigquery.svg";
import airflow from "../../assets/images/extractors/airflow.svg";
import dagster from "../../assets/images/extractors/dagster.svg";
import ge from "../../assets/images/extractors/ge.svg";
import superset from "../../assets/images/extractors/superset.svg";
import postgres from "../../assets/images/extractors/postgres.svg";

const extractors = [
  { name: "dbt BiqQuery (EDK)", url: "utilities/dbt-bigquery", svg: bigquery },
  { name: "Airflow (EDK)", url: "utilities/airflow#", svg: airflow },
  { name: "Dagster", url: "extractors/tap-dagster", svg: dagster },
  { name: "Great Expectations", url: "utilities/great-expectations", svg: ge },
  { name: "Superset", url: "utilities/superset", svg: superset },
  { name: "Postgres", url: "extractors/tap-postgres", svg: postgres },
];

// TODO: Add URLs
const btns = [
  { name: "Explore Tools", url: "#", icon: IconExplore },
  { name: "Build a Tool", url: "#", icon: IconBuild },
  { name: "Publish a Tool", url: "#", icon: IconPublish },
];

export default {
  components: {
    IconRightArrow,
    IconPublish,
    IconBuild,
    IconExplore,
  },
  name: "FavoriteTools",
  data() {
    return {
      extractors,
      btns,
    };
  },
};
</script>
